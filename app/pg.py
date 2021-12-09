from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort
from .functions import pass_gen

bp = Blueprint('passgen',__name__, url_prefix='/')

@bp.route('/')
def home():
    password = pass_gen()
    print(f'{password}')
    return render_template('pg/home.html', password = password)