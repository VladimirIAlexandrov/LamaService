import psycopg2
from Models import Message, User

class DatabaseManager:
    def __init__(self, db_config):
        # db_config должен быть словарем с ключами host, database, user, password
        self.connection = psycopg2.connect(**db_config)
        self.create_tables()

    def create_tables(self):
        with self.connection.cursor() as cursor:
            # Создание таблицы сообщений
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id TEXT PRIMARY KEY,
                    message TEXT,
                    messageType TEXT,
                    AiRepliedId TEXT,
                    created INTEGER
                )
            """)
            # Создание таблицы пользователей
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    avatar TEXT
                )
            """)
            # Создание таблицы групп, связывающей сообщения и пользователей
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS groups (
                    group_entry_id SERIAL PRIMARY KEY,
                    id TEXT NOT NULL,                
                    MessageId TEXT REFERENCES messages(id) ON DELETE CASCADE,
                    UserId TEXT REFERENCES users(id) ON DELETE CASCADE
                );
            """)
        self.connection.commit()

    def insert_message(self, message: Message):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO messages (id, message, messageType, AiRepliedId, created)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (message.id, message.message, message.messageType, message.AiRepliedId, message.created))
        self.connection.commit()

    def insert_user(self, user: User):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (id, name, avatar)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (user.id, user.name, user.avatar))
        self.connection.commit()

    def insert_group(self, group_id: str, message_id: str, user_id: str):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO groups (id, MessageId, UserId)
                VALUES (%s, %s, %s)
            """, (group_id, message_id, user_id))
        self.connection.commit()

    def get_last_five_messages_for_group(self, group_id: str):
        with self.connection.cursor() as cursor:
            cursor.execute("""SELECT m.message
                                FROM messages m
                                JOIN groups g ON m.id = g.messageid
                                WHERE g.id = '"""+group_id+"""'
                                ORDER BY m.created DESC
                                LIMIT 5;""")

            rows = cursor.fetchall()

        # Объединяем только текст сообщений в одну строку, добавляя каждый через новую строку
        if rows:
            messages_str = "\n".join(row[0] for row in reversed(rows))
        else:
            messages_str = "No messages found."
        return messages_str

    def create_user(self, user_id: str, name: str, avatar: str):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (id, name, avatar)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (user_id, name, avatar))
        self.connection.commit()

    def close(self):
        self.connection.close()
