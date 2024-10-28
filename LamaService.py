from datetime import datetime

import torch
from ctransformers import AutoModelForCausalLM
import time
from Models import *
from utils.Сonst import Const

model_path = Const.ModelLlamaPath.LLAMA_2_7B

# model = AutoModelForCausalLM.from_pretrained(model_path, model_type="llama")               # Запуск на CPU.

model = AutoModelForCausalLM.from_pretrained(model_path, model_type="llama", gpu_layers=60)  # Запуск всех слоёв на GPU.  В среднем работает в 4 раза быстрее на NVIDIA GeForce RTX 3060 Laptop GPU


async def lamaStart(message_text: str) -> str:
    try:
        if torch.cuda.is_available():
            print(f"Модель ипользует GPU: {torch.cuda.get_device_name(0)} \n")
        else:
            print("GPU не доступен, ипользуется CPU \n")

        print('Модель получила сообщение, идёт генерация \n')
        start_time = time.time()

        response = model(message_text)

        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.4f} секунд \n")
        return response
    except Exception as e:
        return f"Ошибка: {e}"


async def generateMessage(message: Message) -> Answer:
    answer = await lamaStart(message.message)
    response_timestamp = int(datetime.utcnow().timestamp())
    print('Генерация завершена - Ответ: ' + answer)
    answerModel = Answer(
        answer=answer,
        messageId=message.id,
        created=response_timestamp
    )
    return answerModel
