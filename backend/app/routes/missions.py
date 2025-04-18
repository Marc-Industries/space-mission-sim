from fastapi import APIRouter
from app.schemas.mission import Mission
import json
from pathlib import Path

router = APIRouter()
DB_FILE = Path(__file__).resolve().parent.parent / "missions.json"

def read_missions():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_missions(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@router.get("/missions")
def get_missions():
    return read_missions()

@router.post("/missions")
def create_mission(mission: Mission):
    missions = read_missions()
    missions.append(mission.dict())
    write_missions(missions)
    return {"message": "Mission created", "data": mission}

@router.put("/missions/{mission_id}")
def update_mission(mission_id: int, updated_mission: Mission):
    missions = read_missions()
    for i, m in enumerate(missions):
        if m["id"] == mission_id:
            missions[i] = updated_mission.dict()
            write_missions(missions)
            return {"message": "Mission updated", "data": updated_mission}
    return {"error": "Mission not found"}

@router.delete("/missions/{mission_id}")
def delete_mission(mission_id: int):
    missions = read_missions()
    updated_missions = [m for m in missions if m["id"] != mission_id]
    if len(updated_missions) == len(missions):
        return {"error": "Mission not found"}
    write_missions(updated_missions)
    return {"message": "Mission deleted"}
