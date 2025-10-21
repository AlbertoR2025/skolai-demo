import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def load_data(filename):
    path = DATA_DIR / filename
    if not path.exists():
        path.write_text("[]")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(filename, data):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
