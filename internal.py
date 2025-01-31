import json


database: dict


def get_data(identification: int, data_list: list, id_type: str) -> dict | None:
    for i in data_list:
        if i[id_type] == identification:
            return i
    return None


def load_data(file_path: str) -> dict:
    with open(file_path) as file:
        raw_data = file.read()
    return json.loads(raw_data)


def save_data(data: dict, file_path: str) -> None:
    raw_data = json.dumps(data, indent=4)
    with open(file_path, "w") as file:
        file.write(raw_data)
