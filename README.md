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
      "name": "Ебланчик",
      "avatar": "avatar1"
    }
  }
}
```

## SOCKET
- `Name: new_answer`
  
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
  - `pong_event`  - клиент слушает
  - `ping_event`  - клиент отправляет
