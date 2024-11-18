import os
import json
from config import check
from request import post

def create_file(basedir):
    if check():
        if basedir.endswith('/'):
             basedir = basedir[:-1]
        batchNo = os.path.basename(basedir)
        data = [];
        file_address = [];
        for root, dirs, files in os.walk(basedir):
            for file in files:
                if file.endswith('.fq.gz'):
                    sample_no, unique_no = os.path.basename(os.path.dirname(root)), os.path.basename(root)
                    file_path = os.path.join(root, file)
                    found = False
                    for item in data:
                        if item['sampleNo'] == sample_no and item['uniqueNo'] == unique_no:
                            item['address'].append(file_path)
                            file_address = item['address']
                            item['address'] = json.dumps(file_address);
                            found = True
                            break
                    if not found:
                        data.append({'batchNo':batchNo,'sampleNo': sample_no, 'uniqueNo': unique_no,'type':'rawdata', 'address': [file_path]})

        # print(data)
        count = post("fileIndex", "createAll", json.dumps(data))
        if count == 0:
            print("[Biolab] Files ", file_address, "already registered")
        else:
            print("[Biolab] Files ", file_address, " register successful")


def list_file(uniqueno):
    if check():
        # print(list(unique_no))
        files = post("fileIndex", "list", json.dumps(uniqueno))
        for file in files:
            print(file)