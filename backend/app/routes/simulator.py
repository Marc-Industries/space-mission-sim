EOF
from fastapi import APIRouter

router = APIRouter()

@router.get("/simulate_mission")
def simulate_mission():
    return {"message": "Missione simulata con successo!"}
EOF

# Aggiungi il nuovo router nel main.py
sed -i "/from fastapi import FastAPI/c\from fastapi import FastAPI\nfrom app.routes.simulator import router as simulator_router" app/main.py
sed -i "/app.include_router/c\app.include_router(simulator_router)" app/main.py

# Testa il nuovo endpoint (verifica che sia stato correttamente aggiunto)
uvicorn app.main:app --reload