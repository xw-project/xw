from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'project': 'xw'}
