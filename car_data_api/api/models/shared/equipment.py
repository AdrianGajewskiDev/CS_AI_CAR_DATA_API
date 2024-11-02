from pydantic import BaseModel
from typing import List, Dict

class AudioAndMultimedia(BaseModel):
    checks: List[str]

class ComfortNested(BaseModel):
    air_conditioning: List[str]
    cabriolet: List[str]
    sun_shield: List[str]
    roof: List[str]
    upholstery: List[str]

class Comfort(BaseModel):
    nested: ComfortNested
    checks: List[str]

class ElectricVehicles(BaseModel):
    checks: List[str]

class DriverAssistNested(BaseModel):
    crusie_control: List[str]
    lamp_type: List[str]

class DriverAssist(BaseModel):
    nested: DriverAssistNested
    checks: List[str]

class TuningNested(BaseModel):
    rims: List[str]
    tyres: List[str]

class Tuning(BaseModel):
    nested: TuningNested
    checks: List[str]

class Safety(BaseModel):
    checks: List[str]

class Equipment(BaseModel):
    audio_and_multimedia: AudioAndMultimedia
    compfort: Comfort
    electric_vehicles: ElectricVehicles
    driver_assist: DriverAssist
    tuning: Tuning
    safety: Safety