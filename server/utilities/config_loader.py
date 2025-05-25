import json
import os

config = {}

path_db = ""


def load_config():
    global config
    global path_db
    path_db = os.path.join("..", "server", "config.json")

    with open(path_db, "r") as config_data:
        config = json.load(config_data)

    database = config["database"]
    path_db = os.path.join(*database["path"])
