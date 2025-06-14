import json
import os

path_db = ""
server_config = {}


def load_config():
    global path_db
    global server_config
    path_db = os.path.join("..", "server", "config.json")

    with open(path_db, "r") as config_data:
        config = json.load(config_data)

    database = config["database"]
    path_db = os.path.join(*database["path"])

    server_config = config["server"]
