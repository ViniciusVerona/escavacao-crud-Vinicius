import json
from database import SessionLocal, init_db
from schemas import ExcavationPointCreate
from crud import create_point

init_db()
db = SessionLocal()

with open("sample_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    point = ExcavationPointCreate(**item)
    create_point(db, point)

print("✅ Dados inseridos com sucesso.")
