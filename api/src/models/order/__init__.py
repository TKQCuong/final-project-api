from src import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    servicetype = db.Column(db.String)
    dateandtime = db.Column(db.String)
    address = 
    



db.create_all()