import itertools
from pyramid.view import view_config

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    s = '----.----.---------.----.---------.----.-----------------....-----...------...-----------------.----..--------.---.--------..----.-----------------...------...-----....-----------------.----.---------.----.---------.----.----'
    lines = []
    LINE_SIZE = 15
    for i in itertools.count(0, LINE_SIZE):
        if i >= len(s):
            break
        lines.append(s[i:i+LINE_SIZE])
    return {'project': 'xw', 'lines': lines}
