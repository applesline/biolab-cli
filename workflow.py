import json
from config import check
from request import post

def create_workflow(workflowname, workflowcode, step, preStep):
    if check():
        data = {
            "workflowName" : workflowname,
            "workflowCode" : workflowcode,
            "step" : step,
            "preStep" : json.dumps(list(preStep))
        };
        response = post("workflow", "create", json.dumps(data))
        if not response:
            return
        if response["code"] == 0:
            print("[Biolab] Workflow " + workflowname + "#" + workflowcode + "_" + step + " registered successful !")
        else:
            print("[Biolab] Workflow " + workflowname + "#" + workflowcode + "_" + step + " already registered")



def list_workflow(workflowcode):
    if check():
        data = [workflowcode]
        if not workflowcode:
            data = []
        # print(list(unique_no))
        response = post("workflow", "list", json.dumps(data))
        if not response:
            return
        if not response['data']:
            print("No workflow configured")
            return
        for workflow in response["data"]:
            print(workflow)