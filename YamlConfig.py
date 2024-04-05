import yaml


class Step1YamlData:
    sql_filepath: str

    def __init__(self, data: dict):
        self.sql_filepath = data["step1"]["sql_filepath"]


class Step2YamlData:
    csv_filepaths: [str]
    columns_map: dict
    table_name: str
    database_name: str

    def __init__(self, data: dict):
        self.csv_filepaths = data["step2"]["csv_filepaths"]
        self.columns_map = data["step2"]["columns_map"]
        self.table_name = data["step2"]["table_name"]
        self.database_name = data["step2"]["database_name"]


class Step3YamlData:
    sql_query_filepath: str
    sql_result_filepath: str

    def __init__(self, data: dict):
        self.sql_query_filepath = data["step3"]["sql_query_filepath"]
        self.sql_result_filepath = data["step3"]["sql_result_filepath"]


class YamlData:
    step1: Step1YamlData
    step2: Step2YamlData
    step3: Step3YamlData

    def __init__(self):
        data = self.__load_yaml()
        self.step1 = Step1YamlData(data)
        self.step2 = Step2YamlData(data)
        self.step3 = Step3YamlData(data)

    def __load_yaml(self):
        with open("config.yaml", 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                exit(1)


if __name__ == '__main__':
    config = YamlData()
