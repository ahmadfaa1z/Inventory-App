from db import db
from app import app, db_filename
import os

if __name__ == '__main__':
    if os.path.exists(f'./instance/{db_filename}'):
        os.remove(f'./instance/{db_filename}')
    with app.app_context():
        db.create_all()