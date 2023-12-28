from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    balance = db.Column(db.String)
    address = db.Column(db.String)
    rate = db.Column(db.Integer)

    def get(self):
        pass

    def get_all(self):
        pass

    def save(self):
        pass


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    balance = db.Column(db.String)
    address = db.Column(db.String)
    rate = db.Column(db.Integer)

    def get(self):
        pass

    def get_all(self):
        pass

    def save(self):
        pass


class Lot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    start_amount = db.Column(db.Float)
    min_step = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))  # Исправлено

    def get(self):
        pass

    def get_all(self):
        pass

    def save(self):
        pass


class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    lot_id = db.Column(db.Integer, db.ForeignKey('lot.id'))  # Исправлено
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'))  # Исправлено

    def get(self):
        pass

    def get_all(self):
        pass

    def save(self):
        pass


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))  # Исправлено
    amount = db.Column(db.Float)
    description = db.Column(db.String)
