import json

__file = open("config.json", "r")
config = json.loads(__file.read())
__file.close()
