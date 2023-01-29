# author: Roy Kid
# contact: lijichen365@126.com
# date: 2023-01-29
# version: 0.0.1

import pytest
import socketio
from molcom import Molcom, MethodsCollection
import multiprocessing as mp

class ServerMethods(socketio.Namespace):

    def on_test_string(self, sid, data):

        assert data == 'hello'
        self.emit('test_string', 'Hi')

class ClientMethods(socketio.ClientNamespace):

    def on_test_string(self, data):

        assert data == 'Hi'


class TestHello:

    @pytest.fixture(scope='class', name='client')
    def client(self):
        
        mc = Molcom('localhost', 5000)
        mc.register_methods(ServerMethods('/test'))
        server = mp.Process(target=mc.run)
        client = socketio.Client()
        client.register_namespace(ClientMethods('/test'))
        server.start()
        yield client
        server.terminate()

    def test_connect(self, client):
     
        client.connect('http://localhost:5000')
        client.disconnect()

    def test_string(self, client):
            
        client.connect('http://localhost:5000')
        client.emit('test_string', 'hello', namespace='/test')
        client.disconnect()