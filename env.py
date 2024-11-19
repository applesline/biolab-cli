import json
from config import check
from request import post

def create_env(workflowcode, step, type, key, feature):
    if check():
        data = {
            "workflowCode" : workflowcode,
            "step" : step,
            "type" : type,
            "key" : key,
            "feature" : feature
        };
        count = post("env", "create", json.dumps(data))
        if count == 0:
            print("[Biolab] The env ["+workflowcode+"_"+ step+"_"+type+"]#["+key+"] already registered")
        else:
            print("[Biolab] The env ["+workflowcode+"_"+ step+"_"+type+"]#["+key+"]  registered successful !")


def list_env(workflowcode, step):
    if check():
        data = {
            "workflowCode" : workflowcode,
            "step" : step
        };
        envs = post("env", "list", json.dumps(data))
        for env in envs:
            print(env)