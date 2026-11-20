import json
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
print(project_root)
config_file = project_root / "config" / "config.json"

with open(config_file, "r") as f:
    config = json.load(f)

print("Application:", config["application"])
print("Environment:", config["environment"])
print("Timeout:", config["timeout"])