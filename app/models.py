from sqlalchemy import  Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
import enum
from .database import Base, engine

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)

class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str]

class Status(enum.Enum):
    awaiting = "awaiting"
    confirmed = "confirmed"
    unconfirmed = "unconfirmed"

class Weather(enum.Enum):
    sunny = "sunny"
    rain = "rain"
    cloudy = "cloudy"

class Prediction(BaseModel):
    __tablename__ = "predictions"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    city: Mapped[str]
    country: Mapped[str]
    prediction: Mapped[Weather]
    date = Column(DateTime)
    status: Mapped[Status]

class Result(BaseModel):
    __tablename__ = "results"
    city: Mapped[str]
    country: Mapped[str]
    actual_weather: Mapped[Weather]
    date = Column(DateTime)

if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)