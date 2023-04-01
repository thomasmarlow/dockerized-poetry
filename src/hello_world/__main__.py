import socketio
import logging
from aiohttp import web

logging.basicConfig(level=logging.DEBUG)

routes = web.RouteTableDef()

# sio = socketio.AsyncServer(async_mode='aiohttp')
sio = socketio.AsyncServer(async_mode='aiohttp')

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
async def message(sid, data):
    print("Received message from client:", data)
    await sio.emit('message', data)

@routes.get('/')
async def hello(request):
    return web.Response(text="Dónde está la casa de Pepe?")

@routes.options('/')
async def hello_options(request):
    response = web.Response()
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    return response

@routes.post('/emit')
async def emit(request):
    message = await request.text()
    await sio.emit('message', message)
    return web.Response()

@web.middleware
async def cors(request, handler):
    response = await handler(request)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

app = web.Application(middlewares=[cors])
app.add_routes(routes)

sio.attach(app)

if __name__ == '__main__':
    web.run_app(app)
