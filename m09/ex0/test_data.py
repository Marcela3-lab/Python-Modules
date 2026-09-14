import json
from pathlib import Path
from pydantic import ValidationError
from space_station import SpaceStation

data_dir = Path(__file__).parent.parent / "tools" / "data_generator"

with open(data_dir / "space_stations.json", encoding="utf-8") as f:
    stations = json.load(f)

for item in stations:
    try:
        SpaceStation(**item)
        print(f"OK: {item['station_id']}")
    except ValidationError as e:
        print(f"FALHOU: {item['station_id']} -> {e.errors()[0]['msg']}")