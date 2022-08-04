from app import db
from models.base import BaseModel

class TypeModel(db.Model, BaseModel):

    __tablename__ = "types"

    type = db.Column(db.Text, nullable=False, unique=True)