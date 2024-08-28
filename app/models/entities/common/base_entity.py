from datetime import datetime
from app.application.settings.extensions import db


class BaseEntity(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now())