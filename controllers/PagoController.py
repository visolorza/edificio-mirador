from services.PagoService import PagoService

class PagoController:
    @staticmethod
    def create_pago_controller(gasto, fecha_pago):
        return PagoService.create_pago(gasto, fecha_pago)
