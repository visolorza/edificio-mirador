from models.PagoModel import Pago
from app import db
from datetime import datetime

class PagoService:
    @staticmethod
    def create_pago(gasto, fecha_pago):
        gasto.estado = "Pagado"
        pago = Pago(monto=gasto.monto, fecha_pago=fecha_pago, gasto_id=gasto.id)
        db.session.add(pago)
        db.session.commit()
        return pago
