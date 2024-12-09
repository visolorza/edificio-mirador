from flask import Blueprint, request, render_template, flash, redirect, url_for
from controllers.GastoComunController import GastoComunController
from services.ResidenteService import ResidenteService

gasto_bp = Blueprint('gasto', __name__)

@gasto_bp.route('/generar', methods=['GET', 'POST'])
def generar_gastos():
    if request.method == 'POST':
        mes, anio, monto = request.form['mes'], request.form['anio'], float(request.form['monto'])
        for residente_id in ResidenteService.get_all_residente_ids():
            GastoComunController.create_gasto_controller(f'Gasto común {mes}/{anio}', monto, mes, anio, residente_id)
        flash('Gastos generados con éxito', 'success')
        return redirect(url_for('gasto.listar_pendientes'))
    return render_template('generar_gasto.html')

@gasto_bp.route('/pendientes', methods=['GET'])
def listar_pendientes():
    pendientes = GastoComunController.get_pendientes_controller()
    return render_template('pendientes.html', pendientes=pendientes)
