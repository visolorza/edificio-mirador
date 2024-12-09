from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.IndexView import index_bp
import os

# Singleton Database Instance
db = SQLAlchemy()

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)

# Application Factory
def create_app():
    # Specify template folder if not in default location
    app = Flask(
        __name__, 
        template_folder=os.path.join(os.path.dirname(__file__), '../templates')
    )

    # Load Configuration
    app.config.from_object('config.Config')

    # Initialize Singleton Database Instance
    SingletonDB(app)

    # Create Database Tables if Not Exists
    with app.app_context():
        from models.ResidenteModel import Residente
        from models.GastoComunModel import GastoComun
        from models.PagoModel import Pago
        db.create_all()  # Ensure all tables are created

    # Register blueprints
    from views.GastoComunView import gasto_bp
    from views.PagoView import pago_bp

    app.register_blueprint(gasto_bp, url_prefix='/gastos')
    app.register_blueprint(pago_bp, url_prefix='/pagos')
    app.register_blueprint(index_bp)

    return app
