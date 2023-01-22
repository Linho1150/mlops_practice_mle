class MlopsQueryManager:
    def create_iris_data_query(self)->str:
        return """
            CREATE TABLE IF NOT EXISTS iris_data (
                id SERIAL PRIMARY KEY,
                timestamp timestamp,
                sepal_length float8,
                sepal_width float8,
                petal_length float8,
                petal_width float8,
                target int
            );"""

    def insert_iris_data_query(self,data)->str:
        return f"""
            INSERT INTO iris_data
                (timestamp, sepal_length, sepal_width, petal_length, petal_width, target)
                VALUES (
                    NOW(),
                    {data.sepal_length},
                    {data.sepal_width},
                    {data.petal_length},
                    {data.petal_width},
                    {data.target}
                );
            """