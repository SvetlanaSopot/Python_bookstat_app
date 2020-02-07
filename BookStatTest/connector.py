import sqlite3


class Connector:  # отвечает за соединение с базой
    def __init__(self, get_database_url):  # функция принимает на вход урл для соединения с базой
        conn = sqlite3.connect(get_database_url)    # соединение с базой
        self.cursor = conn.cursor()

    def execute(self, query):     # возвращение курсора для манипуляций
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]