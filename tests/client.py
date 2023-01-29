import socketio

class ClientMethod(socketio.ClientNamespace):

    def on_connect(self, ):
        print('establish connect')

    def on_test_string(self, data):
        print(data)


sio = socketio.Client()
sio.register_namespace(ClientMethod('/test'))
sio.connect('http://localhost:5000')
sio.emit('test_string', 'hello', namespace='/test')