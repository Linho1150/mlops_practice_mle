from database.mlops_insert_iris_data import SettingIrisDataset
from database.mlops_query_manager import MlopsQueryManager
from database.mlops_repository import MlopsRepository


def iris_table_setting():
    print("Create Table start")
    create_table_query = MlopsQueryManager().create_iris_data_query()
    MlopsRepository().save(create_table_query)

def insert_iris_data():
    print("Create Dataset start")
    SettingIrisDataset().set_iris_dataset()

if __name__ == "__main__":
    iris_table_setting()
    insert_iris_data()
    