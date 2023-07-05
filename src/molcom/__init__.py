import socketio
import asyncio

# create a Socket.IO server
sio = socketio.AsyncServer()

# wrap with ASGI application
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
async def message(sid, data):
    print("Received message:", data, "from", sid)
    await sio.emit("response", "Echo: " + data, room=sid)

async def start_server():
    server = await sio.start_background_task(app)
    return server

if __name__ == "__main__":
    asyncio.run(start_server())