from app import db
from datetime import *

class BaseModel:

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, coffee):
        db.session.add(coffee)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
