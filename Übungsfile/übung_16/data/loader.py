from config import JSON_FILE
import json
import sys

path = JSON_FILE


def open_json(path):
    try:
        with open(path,"r") as f:
            x = json.load(f)
            return x
    except FileNotFoundError:
        return print(f"file {path} wurde nicht gefunden"), sys.exit(1)
        
    


if __name__ == "__main__":
    print(open_json(path))