import json
from sys import argv


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return json.loads(json_file.read())


def pretty_print_json(decoded_json):
    return json.dumps(decoded_json, sort_keys=True, indent=4, ensure_ascii=False)


def show_json():
    try:
        filepath = argv[1]
        decoded_json = load_data(filepath)
        print(pretty_print_json(decoded_json))
    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")
    except ValueError:
        quit("Файл имеет неверный формат.")



if __name__ == "__main__":
    show_json()
