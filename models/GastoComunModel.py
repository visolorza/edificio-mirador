from app import db

class GastoComun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    mes = db.Column(db.Integer, nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), default='Pendiente')
    residente_id = db.Column(db.Integer, db.ForeignKey('residente.id'), nullable=False)
