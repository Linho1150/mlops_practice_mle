import time

import pandas as pd
from sklearn.datasets import load_iris

from database.mlops_query_manager import MlopsQueryManager
from database.mlops_repository import MlopsRepository


class SettingIrisDataset:
    def get_iris_dataset(self):
        X, y = load_iris(return_X_y=True, as_frame=True)
        df = pd.concat([X, y], axis="columns")
        rename_rule = {
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        }
        return df.rename(columns=rename_rule)

    def set_iris_dataset(self):
        mlops_repository = MlopsRepository()
        mlops_query = MlopsQueryManager()
        while True:
            iris_sql = mlops_query.insert_iris_data_query(self.get_iris_dataset().sample(1).squeeze())
            mlops_repository.save(iris_sql)
            time.sleep(1)