import json
from config import check
from request import post

def create_workflow(workflowname, workflowcode, step, preStep):
    if check():
        data = {
            "workflowName" : workflowname,
            "workflowCode" : workflowcode,
            "step" : step,
            "preStep" : json.dumps(preStep)
        };
        count = post("workflow", "create", json.dumps(data))
        if count == 0:
            print("[Biolab] Workflow ["+workflowname+"]["+workflowcode+"_"+ step+"] already registered")
        else:
            print("[Biolab] Workflow [" + workflowname + "][" + workflowcode + "_" + step + "] registered successful !")


def list_workflow(workflowcode):
    if check():
        data = [workflowcode];
        if not workflowcode:
            data = []
        # print(list(unique_no))
        workflows = post("workflow", "list", json.dumps(data))
        for workflow in workflows:
            print(workflow)