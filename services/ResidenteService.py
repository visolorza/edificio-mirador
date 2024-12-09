from models.ResidenteModel import Residente

class ResidenteService:
    @staticmethod
    def get_all_residente_ids():
        return [residente.id for residente in Residente.query.all()]
