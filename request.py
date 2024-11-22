import requests
import sys
from config import load_config

route_dict = {
  "fileIndex": {
    "create": "/index/create",
    "createAll": "/index/createAll",
    "list": "/index/list"
  },
  "workflow": {
    "create": "/workflow/create",
    "list": "/workflow/list"
  },
  "script": {
    "create": "/script/create",
    "list": "/script/list"
  },
  "env": {
    "create": "/env/create",
    "list": "/env/list"
  },
  "task": {
    "create": "/task/create",
    "list": "/task/list"
  },
  "config": {
    "create": "/config/create",
    "list": "/config/list"
  }
}

sys.tracebacklimit = 0
def post(module, method, data):
    config_dict = load_config()
    url = config_dict["server"] + ":" + config_dict["port"];
    headers = {
        'Content-Type': 'application/json',
        'biolab-token': config_dict["token"]
    }
    url += route_dict[module][method]
    # print("[Biolab] ", url, data)
    try:
        response = requests.request("POST", url, data=data, headers=headers)
        # print(response.json())
        resp = response.json()
        if(resp['code']) == 500:
            print("Sorry, server has an unknown exception in currently")
            resp['data'] = [""]
        return resp
    except Exception as e:
        print("Can't communicate with server, maybe token is invalid, please check your local config and the url " + url)

