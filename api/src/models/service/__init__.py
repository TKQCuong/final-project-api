from src import db

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    Service_name = db.Column(db.String)

db.create_all()