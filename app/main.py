from fastapi import FastAPI
from .models import User, Result, Prediction, Status
from .schemas import CreatePrediction, GetPrediction, CreateUser, GetUser
from .database import Session
from .utilities import get_city
from .keys import ow_key
from datetime import datetime

app = FastAPI()


@app.post("/api/v1/prediction")
def create_prediction(prediction : CreatePrediction):
    cities = get_city(prediction.city, prediction.country, ow_key, 1)
    if cities is not None:
        city = cities[0]
        with Session() as db:
            db.add(Prediction(
                user_id=prediction.user_id,
                city=city['local_names']['en'],
                country=prediction.country,
                prediction=prediction.prediction,
                date=datetime.utcnow(),
                status=Status("awaiting")
                ))
            db.commit()
        
    return {"message": "Предсказание создано"}

@app.get("/api/v1/prediction/{prediction_id}")
def get_prediction(prediction_id) -> GetPrediction:
    with Session() as db:
        prediction = None
        prediction = db.query(Prediction).filter(Prediction.id==prediction_id).one()
    return GetPrediction(
        id=prediction.id,
        user_id=prediction.user_id,
        city=prediction.city,            
        country=prediction.country,
        prediction=prediction.prediction
        )

@app.post("/api/v1/user")
def create_user(user : CreateUser):
        User()
        with Session() as db:
             db.add(User(name=user.name))
             db.commit()
        return {"message": "Пользователь создан"}


