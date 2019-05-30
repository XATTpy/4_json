import json
import sys
from sys import argv


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return (json.loads(json_file.read()))["features"]


def pretty_print_json(shops):
    return json.dumps(shops, sort_keys=True, indent=4, ensure_ascii=False)


file_path = argv[1]
try:
    shops = load_data(file_path)
except FileNotFoundError:
    print("Файл не найден.")
    sys.exit()
except ValueError:
    print("Файл имеет неверный формат.")
    sys.exit()

print(pretty_print_json(shops))
