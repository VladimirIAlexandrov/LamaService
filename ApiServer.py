import asyncio

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from pydantic import BaseModel, ValidationError
import LamaService
import Models
from utils.Сonst import *
from LamaService import *

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading', ping_interval=Const.Host.SocketIOConf.PING_INTERVAL, ping_timeout=Const.Host.SocketIOConf.PING_TIMEOUT)
#socketio = SocketIO(app, async_mode='threading', ping_interval=Const.Host.SocketIOConf.PING_INTERVAL, ping_timeout=Const.Host.SocketIOConf.PING_TIMEOUT, cors_allowed_origins="*")


@socketio.on(Const.SocketMessageName.connect)
def handle_connect():
    print('Клиент подключился по WebSocket')
    emit('connection_response', {'status': Const.SocketMessageName.connect})


@socketio.on(Const.SocketMessageName.disconnect)
def handle_disconnect():
    print('Клиент отключился от WebSocket')
    emit(Const.SocketMessageName.disconnect_response, {Const.ConstText.STATUS: Const.SocketMessageName.disconnect})


@socketio.on(Const.SocketMessageName.ping_event)
def handle_ping(data):
    print('Получен ping от клиента')
    emit(Const.SocketMessageName.pong_event, {Const.ConstText.STATUS: 'pong'})


@app.route(Const.RestEndPoint.POST_MESSAGES, methods=['POST'])
def receive_message():
    try:
        data = request.json
        message = Models.Message.parse_obj(data['message'])
        print(f"Получено сообщение с ID: {message}")
        socketio.start_background_task(sync_process_message, message)

        return jsonify({Const.ConstText.STATUS: Const.JsonIFyText.TYPE_200}), 200

    except ValidationError as e:
        return jsonify({Const.ConstText.STATUS: Const.ConstText.ERROR, "message": Const.JsonIFyText.TYPE_400, Const.ConstText.DETAILS: e.errors()}), 400
    except Exception as e:
        return jsonify({Const.ConstText.STATUS: Const.ConstText.ERROR, "message": Const.JsonIFyText.TYPE_500, Const.ConstText.DETAILS: str(e)}), 500


def sync_process_message(message):
    asyncio.run(process_message_async(message))


async def process_message_async(message):
    try:
        print('Модель получила сообщение')
        answer = await LamaService.generateMessage(message)
        await send_answer_via_socket(answer)
    except Exception as e:
        print("")


async def send_answer_via_socket(answer: Answer):
    print(f"Отправка ответа по WebSocket: {answer}")
    await socketio.emit(Const.SocketMessageName.new_answer, answer.dict())


if __name__ == '__main__':
    socketio.run(app, host=Const.Host.MY_HOST, port=8300, allow_unsafe_werkzeug=True)
