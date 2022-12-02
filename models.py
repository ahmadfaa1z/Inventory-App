from db import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    received_date = db.Column(db.Date)
    is_defect = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(300))