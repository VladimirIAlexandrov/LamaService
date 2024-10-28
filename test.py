import socketio
import time

# Создание клиента Socket.IO
sio = socketio.Client()

@sio.event
def connect():
    print('Подключен к серверу')
    sio.start_background_task(ping_server)

@sio.event
def disconnect():
    print('Отключен от сервера')

@sio.on('pong_event')
def on_pong(data):
    print('Получен pong от сервера:', data)

def ping_server():
    while True:
        sio.emit('ping_event')
        print('Отправлен ping на сервер')
        time.sleep(10)  # Ждём 10 секунд перед отправкой следующего ping

@sio.event
def connect_error(data):
    print("Не удалось подключиться к серверу:", data)

@sio.on('connection_response')
def on_connection_response(data):
    print("Ответ от сервера при подключении:", data)

@sio.on('new_answer')
def on_new_answer(data):
    print("Получен ответ от сервера:", data)

def start_client():
    try:
        sio.connect('http://192.168.1.120:8300')
        #sio.connect('http://127.0.0.1:8300')
        sio.wait()
    except Exception as e:
        print("Ошибка при подключении или во время работы:", e)

if __name__ == '__main__':
    start_client()
