from flask_sqlalchemy import SQLAlchemy
from extensions import db

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String)
    ship_id = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    speed = db.Column(db.String)
    weather = db.Column(db.String)
    voice_log = db.Column(db.Text)

    def serialize(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'ship_id': self.ship_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'speed': self.speed,
            'weather': self.weather,
            'voice_log': self.voice_log
        }
