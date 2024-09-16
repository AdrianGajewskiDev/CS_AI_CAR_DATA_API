from typing import List, Optional
from pydantic import BaseModel

class ModelGeneration(BaseModel):
    generation: str
    years: str
    start_year: Optional[int] = None
    end_year: Optional[int] = None

    def _map_years(self):
        split = self.years.split('-')
        self.start_year = int(split[0])
        self.end_year = int(split[1]) if len(split) > 1 and split[1] != "present" else None

class Model(BaseModel):
    model: str