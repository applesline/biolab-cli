import json
from config import check
from request import post

def create_config(type, key, value):
    if check():
        data = {
            "type" : type,
            "key" : key,
            "value" : value
        };
        count = post("config", "create", json.dumps(data))
        if count == 0:
            print("[Biolab] The config ["+type+"_"+ key+"] already registered")
        else:
            print("[Biolab] The config ["+type+"_"+ key+"] registered successful !")


def list_config():
    if check():
        data = {};
        configs = post("config", "list", json.dumps(data))
        for config in configs:
            print(config)