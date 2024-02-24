from flask import (
    Blueprint, request, render_template
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('', methods = ['GET'])
def systems_home():
    return render_template('home.html')