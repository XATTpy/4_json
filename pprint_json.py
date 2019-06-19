import json
import sys
from sys import argv

# Functions
def load_data(filepath):
    with open(filepath, "r") as json_file:
        return json.loads(json_file.read())


def pretty_print_json(info):
    return json.dumps(info, sort_keys=True, indent=4, ensure_ascii=False)


# Exeptions and variable initialization
try:
    filepath = argv[1]
    info = load_data(filepath)
except (IndexError, IsADirectoryError, FileNotFoundError):
    sys.exit("Введите путь к файлу в качестве аргумента при запуске. Прим.: python3 bars.py /path_to_file/file_name.json")
except ValueError:
    sys.exit("Файл имеет неверный формат.")


if __name__ == "__main__":
    print(pretty_print_json(info))
