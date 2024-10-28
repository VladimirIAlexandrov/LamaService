# **LamaService**


## REST API
- POST `http://192.168.1.120:8000/api/generate` - запрос на генерацию ответа

body 
```
{
  "message": {
    "id": "001",
    "message": "Helloy",
    "userId": "user123",
    "groupId": "group123",
    "messageType": "user",
    "AiRepliedId": null,
    "created": 1698175200,
    "user": {
      "id": "user123",
      "name": "Имя",
      "avatar": "avatar1"
    }
  }
}
```

## SOCKET

Слушать

- `Name: new_answer`

Возвращает Json

 body
  ```
  {
      "answer": {
        "answer": "Thank you for your interest in the position of Data Scientist at [Company Name].",
        "messageId": "001",
        "created": "1730098147"
      }
  }
  ```

## Ping - Pong
При подключении клиент оправляет ***ping_event*** , далее при прослушавании ***pong_event***
  - `Name: pong_event`  - клиент слушает
  - `Name: ping_event`  - клиент отправляет
