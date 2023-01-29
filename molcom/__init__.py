# author: Roy Kid
# contact: lijichen365@126.com
# date: 2023-01-29
# version: 0.0.1

import socketio
import eventlet
import multiprocessing as mp
MethodsCollection = socketio.Namespace

class Molcom:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sio = socketio.Server(cors_allowed_origins="*")
        self.app = socketio.WSGIApp(self.sio)

        self.server = None

    def send(self, event, data=None, namespace=None, callback=None):
        
        self.sio.emit(event, data, namespace, callback)

    def register_methods(self, methods:MethodsCollection):
        
        self.sio.register_namespace(methods)

    def run(self):

        def _run():
            eventlet.wsgi.server(eventlet.listen((self.host, self.port)), self.app)

        self.server = mp.Process(target=_run)
        self.server.start()
        # _run()

    def stop(self):
            
        self.server.terminate()
