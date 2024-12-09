from models.GastoComunModel import GastoComun
from app import db

class GastoComunService:
    @staticmethod
    def create_gasto(descripcion, monto, mes, anio, residente_id):
        gasto = GastoComun(descripcion=descripcion, monto=monto, mes=mes, anio=anio, residente_id=residente_id)
        db.session.add(gasto)
        db.session.commit()
        return gasto

    @staticmethod
    def get_pendientes():
        return GastoComun.query.filter_by(estado='Pendiente').all()
