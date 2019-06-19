import json
import sys
from sys import argv


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return json.loads(json_file.read())


def pretty_print_json(decoded_json):
    return json.dumps(decoded_json, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    try:
        filepath = argv[1]
        decoded_json = load_data(filepath)
    except IndexError:
        sys.exit("Введите путь к файлу в качестве аргумента при запуске.")
    except IsADirectoryError:
        sys.exit("Вы ввели путь к файлу, не указав самого файла.")
    except FileNotFoundError:
        sys.exit("Такого файла не существует")
    except ValueError:
        sys.exit("Файл имеет неверный формат.")


    print(pretty_print_json(decoded_json))
