from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional

# Crea l'applicazione FastAPI
app = FastAPI()

# Configurazione del middleware CORS per permettere il frontend da React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permette solo il frontend React in localhost
    allow_credentials=True,
    allow_methods=["*"],  # Permette tutti i metodi HTTP (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permette tutte le intestazioni
)

# Modello per una missione (Richiesta e risposta)
class Mission(BaseModel):
    name: str = Field(..., example="Missione di Test")
    description: str = Field(..., example="Descrizione dettagliata della missione.")
    date: str = Field(..., example="2025-05-01")
    status: Optional[str] = Field(default="pending", example="pending")

# Simulazione di un database in memoria (lista di missioni)
missions_db = []

# Rotta per ottenere tutte le missioni
@app.get("/api/missions", response_model=List[Mission])
async def get_missions():
    """
    Restituisce tutte le missioni nel database simulato.
    """
    return missions_db

# Rotta per ottenere una missione per ID
@app.get("/api/missions/{mission_id}", response_model=Mission)
async def get_mission(mission_id: int = Path(..., gt=0, example=1)):
    """
    Restituisce una missione specifica in base all'ID.
    """
    if mission_id < 1 or mission_id > len(missions_db):
        raise HTTPException(status_code=404, detail="Mission not found")
    return missions_db[mission_id - 1]

# Rotta per creare una nuova missione
@app.post("/api/missions", response_model=Mission)
async def create_mission(mission: Mission):
    """
    Crea una nuova missione e la salva nel database simulato.
    """
    missions_db.append(mission)
    return mission

# Rotta per aggiornare una missione esistente
@app.put("/api/missions/{mission_id}", response_model=Mission)
async def update_mission(mission_id: int, mission: Mission):
    """
    Aggiorna una missione esistente con nuovi dati.
    """
    if mission_id < 1 or mission_id > len(missions_db):
        raise HTTPException(status_code=404, detail="Mission not found")
    
    missions_db[mission_id - 1] = mission
    return mission

# Rotta per eliminare una missione
@app.delete("/api/missions/{mission_id}")
async def delete_mission(mission_id: int):
    """
    Elimina una missione dal database simulato.
    """
    if mission_id < 1 or mission_id > len(missions_db):
        raise HTTPException(status_code=404, detail="Mission not found")
    
    deleted_mission = missions_db.pop(mission_id - 1)
    return {"message": "Mission deleted successfully", "mission": deleted_mission}

# Rotta per ottenere missioni filtrate per status (opzionale)
@app.get("/api/missions/status/{status}", response_model=List[Mission])
async def get_missions_by_status(status: str):
    """
    Ottieni tutte le missioni che corrispondono a uno specifico stato.
    """
    filtered_missions = [mission for mission in missions_db if mission.status == status]
    return filtered_missions

# Rotta di benvenuto per test
@app.get("/")
async def root():
    """
    Pagina principale dell'API per assicurarsi che il server stia funzionando.
    """
    return {"message": "Welcome to the Mission API!"}
