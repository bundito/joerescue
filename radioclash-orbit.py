#!/usr/bin/local/python3.6


import datetime
#from ws4py.client.threadedclient import WebSocketClient
from decimal import *
getcontext().prec = 3

import sys
import time

import cherrypy
cherrypy.config.update({'server.socket_host': '10.0.0.53' } ) # Pub IP
cherrypy.config.update({'server.socket_port': 9999})
cherrypy.config.update({'tools.caching.on' :False})
cherrypy.config.update({'environment': 'embedded'})


#cherrypy.engine.autoreload.files.add("/home/bundito/Downloads")
#cherrypy.engine.autoreload.frequency = 1

#global TIMEOUT
#TIMEOUT = 0.00
#cherrypy.log("%f seconds" % (TIMEOUT))

""" 
from cherrypy.process.plugins import Monitor

class Clockwork(object):
    idle_timeout = TIMEOUT
    last_served = time.time()
    curr_time = time.time()
    diff = curr_time - last_served

    def __init__(self, seconds):

        cherrypy.log("%f seconds" % (seconds))
        Clockwork.idle_timeout = seconds
        curr_time = 0.00
        diff = 0.00

    staticmethod
    def ticktock():
        curr_time = time.time()
        diff = curr_time - Clockwork.last_served

        if diff > 60.00 and diff < 50.00:
            cherrypy.log("One minute to go.")

        if diff > Clockwork.idle_timeout:
            cherrypy.log("Time's up. Exiting.")
            cherrypy.server.stop()
            cherrypy.engine.exit()

    def is_valid(self):
        Clockwork.last_served = time.time()
        cherrypy.log("Monitor", "Timer reset by valid server call.")

    def timeremaining(self):
        self.curr_time = time.time()
        self.diff = self.curr_time - Clockwork.last_served
        self.delta = Clockwork.idle_timeout - self.diff
        td = datetime.timedelta(seconds=self.delta)
        seconds = td.seconds
        minutes = (seconds % 3600) // 60
        secs = (seconds % 60)
        timeserved = time.localtime(Clockwork.last_served)
        return 
       # Last served: {}<P>
       # Time until shutdown: {} min(s) {} seconds
        #format (time.strftime("%X", timeserved), minutes, secs)
        

Monitor(cherrypy.engine, Clockwork.ticktock, frequency=1).subscribe()

def timeout_reset():
    Clockwork.last_served = time.time()

def report():
    return str(Clockwork.diff)
"""
#----------- String Generator below -------------#


class StringGenerator(object):

    @cherrypy.expose
    def stream_move(self):
        import stream_mover
        content = stream_mover.move()
        return content("Ok")

    @cherrypy.expose
    def hello(self):
        return "Hello world!"

    @cherrypy.expose
    def alive(self):
        return("OK")

   # @cherrypy.expose
   # def timeremaining(self):
   #     val = Clockwork.timeremaining(self)
   #     return val

    @cherrypy.expose
    def dir(self):
        #cl.is_valid()
        import DownloadListing
        return DownloadListing.jaysun

    @cherrypy.expose
    def item(self, item):
    #    cl.is_valid()
        print(type(item))
        import analyzetitle
        jayson = analyzetitle.sendquery("-rename", item)
        return jayson

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def move(app_data):
    #    cl.is_valid()
        jayson = cherrypy.request.json
        import filecopy
        j = filecopy.move(jayson)
        return j

    @cherrypy.expose
    def delete(self, file, path):
    #    cl.is_valid()
        import deleter
        jayson = deleter.delete(file, path)
        return jayson

    @cherrypy.expose
    def read_config(self):
     #   cl.is_valid()
        import config_app
        jayson = config_app.read_config()
        #jayson = jayson.encode('utf-8')
        return jayson

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def write_config(self):
     #   cl.is_valid()
        #data = data.decode('utf-8')
        #jayson = pickle.loads(data)
        jayson = cherrypy.request.json
        import config_app
        j = config_app.write_complete_config(jayson)
        return j

    @cherrypy.expose
    def rsync(self):
        return("Done")


if __name__ == '__main__':

    #mins = sys.argv[2]

    #mins = float(mins)
    #seconds = mins * float(60.0)
    #TIMEOUT = float(60.00)
    #cl = Clockwork(seconds)



   # cherrypy.tree.mount(Sockets('ws://localhost:9998/index'), '/index')
    #cherrypy.tree.mount(StringGenerator())

    #ws = Sockets('ws://localhost:9998/index', protocols=['http-only', 'chat'])
    #ws.daemon = False
    #ws.connect()

    #cherrypy.engine.start()
    #cherrypy.engine.block()

    cherrypy.quickstart(StringGenerator())