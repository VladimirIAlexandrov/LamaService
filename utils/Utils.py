import string
import random  # Исправленный импорт модуля random


class Utils:
    @staticmethod
    def generateId(length=10):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(length))

