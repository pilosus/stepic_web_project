#/usr/bin/env python3
#from cgi import parse_qs, escape
from urllib.parse import parse_qs

def app(environ, start_response):
    """wsgi minimal app.
    $ gunicorn hello:app
    """
    parameters = parse_qs(environ.get('QUERY_STRING', ''))

    output = ''
    for p in parameters:
        for r in parameters[p]:
            output += p + '=' + r + '\n'
    start_response('200 OK', [('Content-Type', 'text/plain')])

    return iter([str.encode(output)])
