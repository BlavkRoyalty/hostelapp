from flask import Blueprint
siteobj = Blueprint('bpsite', __name__, url_prefix='/')

from . import siteroutes