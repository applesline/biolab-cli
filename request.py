import requests
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
  }
}

def post(module, method, data):
    config_dict = load_config();
    url = config_dict["server"] + ":" + config_dict["port"];
    headers = {
        'Content-Type': 'application/json'
    }
    url += route_dict[module][method]
    # print("[Biolab] ", url, data)
    response = requests.request("POST", url, data=data, headers=headers)
    # print(response)
    return response.json()['data'];