#!/usr/bin/env python3
"""Auto-refresh Viessmann IoT token via developer portal (Playwright)."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

PORTAL = "https://app.developer.viessmann-climatesolutions.com/"
USERNAME = "Christophe.danhier@outlook.com"
PASSWORD = "TSec&6769"
ENV_FILE = os.path.expanduser("~/Projets_Dev/BAVI_LEO/.env")

async def refresh_token():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context()
        page = await ctx.new_page()

        try:
            # 1. Login
            await page.goto(PORTAL, timeout=20000)
            await page.wait_for_load_state("networkidle")

            # Fill email
            await page.fill('input[type="text"], input[name="email"], input[placeholder*="Email"]', USERNAME)
            await page.click('button:has-text("Next"), button[type="submit"]')

            # Wait for password field (avoid hidden-password)
            await page.wait_for_selector('input[type="password"]:not([tabindex="-1"])', timeout=10000)
            await page.fill('input[type="password"]:not([tabindex="-1"])', PASSWORD)
            await page.click('button:has-text("Login"), button[type="submit"]')
            await page.wait_for_load_state("networkidle", timeout=15000)

            # 2. Navigate to API Clients page
            # Try to find "Access Tokens" or "API Clients" in nav
            if 'clients' not in page.url:
                # Click on Clients/API menu
                try:
                    await page.click('a[href*="client"], a:has-text("Clients"), a:has-text("API")', timeout=5000)
                    await page.wait_for_load_state("networkidle", timeout=5000)
                except:
                    pass

            # 3. Generate new token
            # Look for "Generate Access Token" button
            await page.wait_for_timeout(2000)

            # Click the client "HomeAssistant"
            try:
                await page.click('text=HomeAssistant', timeout=5000)
                await page.wait_for_load_state("networkidle")
            except:
                pass

            # Click Generate Token
            try:
                await page.click('button:has-text("Generate"), button:has-text("Token"), a:has-text("Generate")', timeout=5000)
                await page.wait_for_load_state("networkidle")
            except:
                pass

            # 4. Extract token from page
            # The token might be in a code block or pre element
            content = await page.content()
            
            # Look for JWT pattern in the page
            import re
            jwts = re.findall(r'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+', content)
            
            if jwts:
                # Prefer the longest one (likely the access token)
                token = max(jwts, key=len)
                print(f"✅ Token: {token[:40]}... (len={len(token)})")

                # Save to .env
                with open(ENV_FILE, "r") as f:
                    lines = f.readlines()
                with open(ENV_FILE, "w") as f:
                    for line in lines:
                        if line.startswith("VIESSMANN_TOKEN="):
                            f.write(f"VIESSMANN_TOKEN={token}\n")
                        else:
                            f.write(line)
                return token
            else:
                print("❌ No JWT token found on page")
                print(f"Page URL: {page.url}")
                print(f"Page title: {await page.title()}")
                return None

        except Exception as e:
            print(f"❌ Error: {e}")
            return None
        finally:
            await browser.close()

if __name__ == "__main__":
    result = asyncio.run(refresh_token())
    if result:
        print("✅ Token refreshed successfully")
        sys.exit(0)
    else:
        print("❌ Token refresh failed")
        sys.exit(1)
