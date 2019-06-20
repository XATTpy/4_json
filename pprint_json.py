import json
import sys
from sys import argv


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return json.loads(json_file.read())


def pretty_print_json(decoded_json):
    return json.dumps(decoded_json, sort_keys=True, indent=4, ensure_ascii=False)


def main():
    try:
        filepath = argv[1]
        decoded_json = load_data(filepath)
        print(pretty_print_json(decoded_json))
    except (IndexError, IsADirectoryError):
        sys.exit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        sys.exit("Такого файла не существует")
    except ValueError:
        sys.exit("Файл имеет неверный формат.")



if __name__ == "__main__":
    main()
