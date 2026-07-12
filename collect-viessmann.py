#!/usr/bin/env python3
"""Collecte des données Viessmann vers JSON pour le dashboard LEO."""
import json, os, sys
import urllib.request as ur
import urllib.error

TOKEN = os.environ.get("VIESSMANN_TOKEN", "")
INSTALL = "2226395"
GW = "7637415004647217"
DEV = "0"
BASE = "https://api.viessmann-climatesolutions.com/iot/v2"
OUT = os.path.expanduser("~/.hermes/metrics/viessmann.json")

if not TOKEN:
    print("❌ VIESSMANN_TOKEN not set", file=sys.stderr)
    sys.exit(1)

features = {}

try:
    url = f"{BASE}/features/installations/{INSTALL}/gateways/{GW}/devices/{DEV}/features"
    req = ur.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    with ur.urlopen(req, timeout=20) as r:
        data = json.loads(r.read())
        for f in data.get("data", []):
            props = f.get("properties", {})
            for k, v in props.items():
                if isinstance(v, dict) and "value" in v:
                    features[f"{f['feature']}.{k}"] = {
                        "value": v["value"],
                        "unit": v.get("unit", ""),
                    }
except Exception as e:
    print(f"❌ API error: {e}", file=sys.stderr)
    sys.exit(1)

# Extraire les valeurs utiles
result = {
    "timestamp": __import__("datetime").datetime.now().isoformat(),
    "boiler_temp": features.get("heating.boiler.sensors.temperature.main.value", {}).get("value"),
    "outside_temp": features.get("heating.sensors.temperature.outside.value", {}).get("value"),
    "dhw_temp": features.get("heating.dhw.sensors.temperature.hotWaterStorage.value", {}).get("value"),
    "dhw_target": features.get("heating.dhw.temperature.main.value", {}).get("value"),
    "burner_modulation": features.get("heating.burners.0.modulation.value", {}).get("value"),
    "circuit0_supply": features.get("heating.circuits.0.sensors.temperature.supply.value", {}).get("value"),
    "circuit0_mode": features.get("heating.circuits.0.operating.modes.active.value", {}).get("value"),
    "circuit0_program": features.get("heating.circuits.0.operating.programs.active.value", {}).get("value"),
    "solar_production": features.get("heating.solar.power.production.value", {}).get("value"),
    "solar_cumulative": features.get("heating.solar.power.cumulativeProduced.value", {}).get("value"),
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(result, f, indent=2)

print(f"✅ Viessmann data → {OUT}")
print(f"   Boiler: {result['boiler_temp']}°C | Outside: {result['outside_temp']}°C | DHW: {result['dhw_temp']}°C | Burner: {result['burner_modulation']}%")
