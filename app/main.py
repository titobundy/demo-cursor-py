from fastapi import FastAPI, HTTPException, Depends, status
from app.settings import settings
from app.schemas import Plato
from typing import List
import uuid

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

# In-memory simulated database
platos_db = {
    1: Plato(id=1, name="Paella Valenciana", precio=25.50),
    2: Plato(id=2, name="Tacos al Pastor", precio=15.00),
    3: Plato(id=3, name="Sushi Roll Especial", precio=18.75)
}

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"mensaje": "¡Bienvenido a la API de demostración!"}

# CRUD endpoints for Plato

@app.post("/platos/", response_model=Plato, status_code=status.HTTP_201_CREATED)
def create_plato(plato: Plato):
    """
    Create a new dish.
    """
    if plato.id in platos_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El plato con id {plato.id} ya existe"
        )
    platos_db[plato.id] = plato
    return plato

@app.get("/platos/", response_model=List[Plato])
def read_platos():
    """
    Get all available dishes.
    """
    return list(platos_db.values())

@app.get("/platos/{plato_id}", response_model=Plato)
def read_plato(plato_id: int):
    """
    Get a specific dish by its ID.
    """
    if plato_id not in platos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plato con id {plato_id} no encontrado"
        )
    return platos_db[plato_id]

@app.put("/platos/{plato_id}", response_model=Plato)
def update_plato(plato_id: int, plato: Plato):
    """
    Update an existing dish.
    """
    if plato_id not in platos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plato con id {plato_id} no encontrado"
        )
    
    # Make sure the ID in the route matches the ID in the body
    if plato_id != plato.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El ID del plato en la ruta no coincide con el ID en el cuerpo"
        )
    
    platos_db[plato_id] = plato
    return plato

@app.delete("/platos/{plato_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_plato(plato_id: int):
    """
    Delete a dish.
    """
    if plato_id not in platos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plato con id {plato_id} no encontrado"
        )
    
    del platos_db[plato_id]
    return None 