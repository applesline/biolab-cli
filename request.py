import requests
import json
import os

route_dict = {
  "fileIndex": {
    "create": "/index/create",
    "createAll": "/index/createAll",
    "list": "/cmd/index/list"
  },
  "workflow": {
    "create": "/cmd/workflow/create",
    "list": "/cmd/workflow/list"
  }
}

def post(module, method, data):
    config_dict = load_config();
    url = config_dict["server"] + ":" + config_dict["port"];
    headers = {
        'Content-Type': 'application/json'
    }
    url += route_dict[module][method]
    print("[Biolab] ", url)
    response = requests.request("POST", url, data=data, headers=headers)
    print(response.json())


def load_config():
    home_dir = os.path.expanduser('~')
    config_path = os.path.join(home_dir, '.biolab_config');
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config_string = f.read()
            return json.loads(config_string)
    else:
        print("[Biolab] Use config command to set 'server' and 'port' first");
        return {}