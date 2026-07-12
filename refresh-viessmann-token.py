#!/usr/bin/env python3
"""Auto-refresh Viessmann IoT token via developer portal (Playwright)."""
import asyncio, json, os, sys, re
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
            # 1. Login — step 1: email
            await page.goto(PORTAL, timeout=20000)
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(2000)

            # Fill email and click Next
            await page.fill('input[type="text"]', USERNAME)
            await page.click('button:has-text("Next")')
            await page.wait_for_timeout(3000)

            # 2. Login — step 2: password
            pw_sel = 'input[type="password"]:not([tabindex="-1"])'
            await page.wait_for_selector(pw_sel, timeout=10000)
            await page.fill(pw_sel, PASSWORD)
            await page.click('button:has-text("Login")')
            
            # Wait for redirect to portal
            await page.wait_for_url("**/app.developer.viessmann**", timeout=20000)
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(3000)
            print(f"1. Logged in: {page.url}")

            # 3. Navigate to the client "HomeAssistant"
            # Try to find and click the client
            try:
                await page.click('text="HomeAssistant"', timeout=5000)
                print("2. Clicked HomeAssistant")
            except:
                # Maybe on dashboard — find the clients link
                await page.click('a[href*="client"]', timeout=5000)
                await page.wait_for_load_state("networkidle")
                await page.click('text="HomeAssistant"', timeout=5000)
                print("2. Found HomeAssistant via nav")

            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(2000)

            # 4. Generate token
            # Look for "Access Tokens" tab or "Generate" button
            try:
                await page.click('text="Access Tokens"', timeout=3000)
                await page.wait_for_timeout(1500)
            except:
                pass

            try:
                await page.click('button:has-text("Generate")', timeout=5000)
                print("3. Clicked Generate")
            except:
                print("3. Generate button not found, trying alternatives...")

            await page.wait_for_timeout(3000)
            content = await page.content()

            # 5. Extract JWT token
            jwts = re.findall(r'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+', content)
            if jwts:
                token = max(jwts, key=len)
                print(f"✅ Token trouvé: {token[:30]}... ({len(token)} chars)")

                # Save to .env
                with open(ENV_FILE, "r") as f:
                    lines = f.readlines()
                with open(ENV_FILE, "w") as f:
                    for line in lines:
                        if line.startswith("VIESSMANN_TOKEN="):
                            f.write(f"VIESSMANN_TOKEN={token}\n")
                        else:
                            f.write(line)
                
                # Run collection immediately
                import subprocess
                env = os.environ.copy()
                env["VIESSMANN_TOKEN"] = token
                subprocess.run(
                    [sys.executable, os.path.join(os.path.dirname(__file__), "collect-viessmann.py")],
                    env=env, timeout=30
                )
                
                return token
            else:
                print(f"❌ No JWT found. Page: {page.url}")
                # Screenshot for debugging
                await page.screenshot(path="/tmp/viessmann_debug.png")
                return None

        except Exception as e:
            print(f"❌ Error: {e}")
            await page.screenshot(path="/tmp/viessmann_error.png")
            return None
        finally:
            await browser.close()

if __name__ == "__main__":
    result = asyncio.run(refresh_token())
    if result:
        print("✅ Token refreshed")
        sys.exit(0)
    else:
        print("❌ Failed")
        sys.exit(1)
