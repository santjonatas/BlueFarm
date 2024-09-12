import os
from datetime import datetime
from dotenv import load_dotenv
from app.application.settings.extensions_setting import db

load_dotenv()


class BaseEntity(db.Model):
    __abstract__ = True
    __table_args__ = {'schema': os.getenv(key='SQLALCHEMY_DATABASE_SCHEMA', default='bluefarm')}

    id = db.Column(db.Integer, primary_key=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)
