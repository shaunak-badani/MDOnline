from flask import (
    Blueprint, request, render_template
)

bp = Blueprint('systems', __name__, url_prefix='/systems')

@bp.route('', methods = ['GET', 'POST'])
def systems_home():
    if request.method == 'GET':
        return render_template('systems/home.html')