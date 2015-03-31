# Package: dmcb
from flask import abort, send_file;

from dmcb import app, cache, generator;

# The views:

@app.route('/<name>/<address>/banner.png')
@app.route('/1.7/<name>/<address>/banner.png')
def name_address(name, address):
    return send_file(wrapper(name, adress),
                     mimetype="image/png", as_attachment=False)

@app.route('/<name>/<address>/<int:port>/banner.png')
@app.route('/1.7/<name>/<address>/<int:port>/banner.png')
def name_address_port(name, address, port):
    return send_file(wrapper(name, address, port=port),
                     mimetype="image/png", as_attachment=False)

@cache.memoize(timeout=app.config['TIMEOUT'])
def wrapper(name, address, port=25565):
    return generator.banner(name, address, port=port)
