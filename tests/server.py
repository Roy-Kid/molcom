import socketio
import eventlet
import numpy as np

from molcom import Molcom

class ServerMethod(socketio.Namespace):

    def on_connect(self, sid, env, data):
        print('incoming connect')
        # print(sid, env, data)

    def on_test_string(self, sid, data):
        self.emit('test_string', 'World')

    def on_test_number(self, sid, data):
        self.emit('test_number', 42)

    def on_test_data(self, sid, data):
        self.emit('test_data', {'data': [[1,2,3, 2,3,4]], 'shape': [2, 3], 'dtype':'int'})

    def on_test_array(self, sid, data):
        self.emit('test_array', np.array([[[1,2,3], [2,3,4]], [[1,2,3], [2,3,4]]]))

# sio = socketio.Server()
# sio.register_namespace(ServerMethod('/test'))
# app = socketio.WSGIApp(sio)
# eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

com = Molcom('localhost', 5000)
com.register_methods(ServerMethod('/test'))
com.run()