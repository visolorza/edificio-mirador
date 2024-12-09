from app import db

class Pago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    fecha_pago = db.Column(db.DateTime, nullable=False)
    gasto_id = db.Column(db.Integer, db.ForeignKey('gasto_comun.id'), nullable=False)
