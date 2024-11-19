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
        };
        count = post("script", "create", json.dumps(data))
        if count == 0:
            print("[Biolab] Script ["+script+"]["+workflowcode+"_"+ step+"] already registered")
        else:
            print("[Biolab] Script [" + script + "][" + workflowcode + "_" + step + "] registered successful !")


def list_script(workflowcode):
    if check():
        data = [workflowcode];
        if not workflowcode:
            data = []
        scripts = post("script", "list", json.dumps(data))
        for script in scripts:
            print(script)