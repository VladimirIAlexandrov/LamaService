from utils.database.DatabaseManager import DatabaseManager
from Models import Message


class InitDataBase:
    def __init__(self):
        # Конфигурация базы данных
        self.db_config = {
            'host': 'localhost',
            'database': 'aichat',
            'user': 'aiuser',
            'password': '12345678'
        }
        # Инициализация менеджера базы данных
        self.database_manager = DatabaseManager(self.db_config)
        self.database_manager.create_user(user_id="AI-cyborg_killer_Т800", name="Cyborg Killer", avatar="nuclear")

    def insertMessageModelData(self, message: Message):
        print(message)
        self.database_manager.insert_message(message)
        self.database_manager.insert_user(message.user)
        self.database_manager.insert_group(group_id=message.groupId, message_id=message.id, user_id=message.user.id)
    def insertMessage(self, message: Message):
        print(message)
        self.database_manager.insert_message(message)


    def getHistoryMessage(self, groupId: str):
        lastMessages = self.database_manager.get_last_five_messages_for_group(groupId)
        return lastMessages

