import request
from flask import Blueprint, render_template
from werkzeug.utils import redirect

from app.controllers.purchase_order_controller import PurchaseOrderController

app_approval = Blueprint('app.approval', __name__)


@app_approval.route('/approval')
def approval():
    return render_template('aprovar_compra.html')


@app_approval.route('/salvar_compra', methods=['POST'])
def salvar_compra():
    purchase_controller = PurchaseOrderController()
    try:
        if not purchase_controller.verify_approval(request.form):
            raise Exception('Purchase denied')

        return redirect('/home')
    except:
        return redirect('/approval')
