from pydantic import BaseModel
from .models import Weather

class CreatePrediction(BaseModel):
    user_id: int
    city: str
    country: str
    prediction: Weather  # "rain", "sunny", "cloudy"

class GetPrediction(CreatePrediction):
    id: int

class CreateUser(BaseModel):
    username: str

class GetUser(CreateUser):
    id: int