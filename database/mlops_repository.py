import os

import psycopg2


class MlopsRepository:
    def __init__(self) -> None:
        try:
            self.db_connect= psycopg2.connect(
                user=os.environ.get('MLOPS_USER'),
                password=os.environ.get('MLOPS_PASSWORD'),
                host="postgres-server",
                port=int(os.environ.get('MLOPS_PORT')),
                database=os.environ.get('MLOPS_DATABASE')
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




