from app import db
from models.base import BaseModel

class GenreModel(db.Model, BaseModel):

    __tablename__ = "genres"

    genre = db.Column(db.Text, nullable=False, unique=True)