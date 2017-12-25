#!/usr/bin/python3

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.wsgi import wsgiapp

import radioclash as radioclash
import views


#if __name__ == '__main__':
config = Configurator()


config.add_route('hello', '/hello')
config.add_route('alive', '/alive')
config.add_route('dir', '/dir')
       #config.add_route('item', '/item')
config.add_route('get_config', '/get_config')
config.add_route('write_config', '/write_config')

config.scan('views')

app = config.make_wsgi_app()
server = make_server('0.0.0.0', 6543, app)
server.serve_forever()