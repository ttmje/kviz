import psycopg2
from psycopg2 import Error
import config


class Database:
    def __init__(self):
        try:
            self.con = psycopg2.connect(user=config.USER,
                                        password=config.PASSWORD,
                                        host=config.HOST,
                                        port=config.PORT,
                                        database=config.DATABASE)
            self.cursor = self.con.cursor()
            print("Информация о сервере PostgreSQL")
            print(self.con.get_dsn_parameters(), "\n")
        except (Exception, Error) as error:
            print('Ошибка...', error)

    def add_word(self, word, translate):
        with self.con:
            return self.cursor.execute(f"""INSERT INTO rus_words (word, translate) VALUES ('{word}', '{translate}')""")


    def word_exists(self, word, translate):
        with self.con:
            self.cursor.execute(f"""SELECT * FROM rus_words WHERE word = '{word}' OR translate = '{translate}' """)
            result = self.cursor.fetchall()
            return bool(len(result))

    def get_word(self, get_word):
        with self.con:
            self.cursor.execute(f"""SELECT word, translate FROM rus_words WHERE word = '{get_word}'""")
            return self.cursor.fetchone()

    def show_all(self):
        with self.con:
            self.cursor.execute("SELECT * FROM rus_words")
            result = self.cursor.fetchall()
            return result

    def get_last_words(self, limit):
        with self.con:
            self.cursor.execute(f"""SELECT * FROM rus_words ORDER BY word DESC LIMIT {limit}""")
            result = self.cursor.fetchall()
            return result

    def get_count(self):
        with self.con:
            self.cursor.execute(f"""SELECT COUNT (*) FROM rus_words""")
            result = self.cursor.fetchone()
            return result

    def close(self):
        """Закрываем соединение с БД """
        self.con.close()