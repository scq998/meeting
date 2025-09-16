from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.String(50))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    user_id = db.Column(db.String(100))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime)