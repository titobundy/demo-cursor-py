from pydantic import BaseModel, Field
from typing import Optional

class Plato(BaseModel):
    """
    Model representing a dish in the menu.
    """
    id: int = Field(..., description="Unique identifier for the dish")
    name: str = Field(..., description="Name of the dish")
    precio: float = Field(..., description="Price of the dish in currency units")
    
    class Config:
        """
        Configuration class for the Plato model.
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Pasta Carbonara",
                "precio": 12.50
            }
        } 