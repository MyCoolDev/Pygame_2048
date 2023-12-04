import json
from Grid import Grid

__file = open("config.json", "r")
config = json.loads(__file.read())
__file.close()

def set_score(score):
    config["BestScore"] = score
    update_json()

def update_json():
    with open("config.json", "w") as write_file:
        json.dump(config, write_file)
