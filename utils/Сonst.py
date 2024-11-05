from Models import User


class Const:
    class SocketMessageName:
        connect = 'connect'
        disconnect = "disconnect"
        disconnect_response = "disconnect_response"
        ping_event = "ping_event"
        pong_event = "pong_event"
        new_answer = "new_answer"

    class RestEndPoint:
        POST_MESSAGES = '/api/generate'

    class JsonIFyText:
        TYPE_200 = 'Success!'
        TYPE_400 = 'Ошибка валидации данных'
        TYPE_500 = 'Произошла ошибка при обработке запроса'

    class ConstText:
        DETAILS = 'details'
        ERROR = 'error'
        STATUS = 'status'

    class Host:
        LOCAL_HOST = '127.0.0.1'
        MY_HOST = '192.168.1.120'

        class SocketIOConf:
            PING_INTERVAL = 10
            PING_TIMEOUT = 5

    class ModelLlamaPath:
        LLAMA_2_7B = 'C:\\maga\\Zinkin\\llama-2-7b-chat.Q3_K_M.gguf'
    class AiUserModel:
        AI_LLAMA = User(
            id='AI-cyborg_killer_Т800',
            name='Cyborg Killer',
            avatar='nuclear'
        )
