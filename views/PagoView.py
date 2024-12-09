from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.GastoComunModel import GastoComun
from controllers.PagoController import PagoController
from datetime import datetime

pago_bp = Blueprint('pago', __name__)

@pago_bp.route('/registrar', methods=['GET', 'POST'])
def pagar_gasto():
    if request.method == 'POST':
        gasto_id = int(request.form['gasto_id'])
        fecha_pago = datetime.strptime(request.form['fecha_pago'], "%Y-%m-%d")
        gasto = GastoComun.query.get_or_404(gasto_id)
        PagoController.create_pago_controller(gasto, fecha_pago)
        flash('Pago registrado con éxito', 'success')
        return redirect(url_for('gasto.listar_pendientes'))
    return render_template('pagar_gasto.html')
