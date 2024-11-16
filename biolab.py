import os
import click
import json
from request import post,load_config;

@click.group()
def cli():
    pass

@cli.group()
def file():
    pass


@cli.command()
@click.option('--server', default='http://localhost', help='server http address, eg: http://biolab.com')
@click.option('--port', default='8080', help='server port, eg 8080')
def config(server,port):
    config = {
        "server": server,
        "port": port
    }
    home_dir = os.path.expanduser('~')
    config_path = os.path.join(home_dir, '.biolab_config');

    print("[Biolab] Config write in [", config_path, "] successful!")    # 配置服务端信息
    with open(config_path, 'w') as file:
        file.write(json.dumps(config,indent=4));


def check():
    config = load_config();
    if len(config) == 0:
        return False;
    if "server" not in config or "port" not in config:
        print("[Biolab] 'server' and 'port' must be configured, use config command first")
        return False;
    return True;

@file.command()
@click.option('--basedir', required=True, help='eg: /baseDir/sampleNo/uniqueNo/sampleNo.R1.fq.gz')
def create(basedir):
    if check():
        batchNo = os.path.basename(basedir)
        print("=====111111",batchNo)
        data = [];
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

        print(data)
        post("fileIndex", "createAll", json.dumps(data))


@file.command()
@click.option('--unique-no', required=True, help='-')
def list(unique_no):
    if check():
        print(unique_no)
        post("fileIndex", "list", {"uniqueNo",unique_no})

if __name__ == '__main__':
    cli()
