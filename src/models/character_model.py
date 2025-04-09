from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class CharacterModel:
    id : Optional[int]
    first_name: str
    last_name: str
    age: int
    lineage : str
    job : str
    image : Optional[str] = None
    created_at : Optional[str] = None
    updated_at : Optional[str] = None
    
    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        if self.created_at is None:
            self.created_at = "2023-10-01T00:00:00Z"
        if self.updated_at is None:
            self.updated_at = "2023-10-01T00:00:00Z"
        self.lineage = self.lineage or "Unknown"
        self.job = self.job or "Unknown"
        self.image = self.image or "default_image.png"
    
    def __str__(self):
        return self.full_name
        