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
        response = post("config", "create", json.dumps(data))
        if not response:
            return
        if response['code'] == 0:
            print("[Biolab] The config " + type + "_" + key + " registered successful")
        else:
            print("[Biolab] The config " + type + "_" + key + " already registered")


def list_config():
    if check():
        data = {};
        response = post("config", "list", json.dumps(data))
        if not response:
            return
        if not response['data']:
            print("No system configs configured")
            return
        for config in response['data']:
            print(config)