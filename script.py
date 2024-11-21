import json
from config import check
from request import post

def create_script(workflowcode, step, type, script):
    if check():
        data = {
            "workflowCode" : workflowcode,
            "step" : step,
            "type" : type,
            "script" : script
        }
        response = post("script", "create", json.dumps(data))
        if not response:
            return
        if response["code"] == 0:
            print("[Biolab] Script " + workflowcode + "_" + step + "#"  + script  + " registered successful")
        else:
            print("[Biolab] Script " + workflowcode + "_" + step + "#"  + script  + " already registered")


def list_script(workflowcode):
    if check():
        data = [workflowcode];
        if not workflowcode:
            data = []
        response = post("script", "list", json.dumps(data))
        if not response:
            return
        if not response['data']:
            print("No scripts configured")
            return
        for script in response['data']:
            print(script)