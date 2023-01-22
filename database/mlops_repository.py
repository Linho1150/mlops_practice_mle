import os

import psycopg2


class MlopsRepository:
    def __init__(self) -> None:
        try:
            self.db_connect= psycopg2.connect(
                user=os.environ.get('USER'),
                password=os.environ.get('PASSWORD'),
                host=os.environ.get('HOST'),
                port=int(os.environ.get('PORT')),
                database=os.environ.get('DATABASE')
            )
        except:
            raise "Can't connect to DB"

    def findAll(self):
        cursor = self.db_connect.cursor()
        result = cursor.fetchall()
        cursor.close()
        return result

    def save(self, sql:str):
        cursor = self.db_connect.cursor()
        cursor.execute(sql)
        self.db_connect.commit()
        cursor.close()




