from services.GastoComunService import GastoComunService

class GastoComunController:
    @staticmethod
    def create_gasto_controller(descripcion, monto, mes, anio, residente_id):
        return GastoComunService.create_gasto(descripcion, monto, mes, anio, residente_id)

    @staticmethod
    def get_pendientes_controller():
        return GastoComunService.get_pendientes()
