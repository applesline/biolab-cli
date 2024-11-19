import click

from config import set_config, load_config, check
from file import create_file,list_file
from workflow import create_workflow, list_workflow
from script import create_script,list_script
from env import create_env, list_env
from sysconfig import create_config, list_config

@click.group()
def cli():
    pass

@cli.group()
def workflow():
    pass

@cli.group()
def script():
    pass

@cli.group()
def env():
    pass

@cli.group()
def file():
    pass

@cli.group()
def config():
    pass


@cli.command()
@click.option('--server', required=True, default='http://localhost', help='server http address, eg: http://biolab.com')
@click.option('--port', required=True, default='8080', help='server port, eg 8080')
def local(server,port):
    set_config(server, port)


@workflow.command()
@click.option('--workflowname', required=True, help='eg: Strain Analysis workflow')
@click.option('--workflowcode', required=True, help='eg: StrainAnalysis')
@click.option('--step', required=True, help='eg: assembly')
@click.option('--prestep', multiple=True, required=True, help='qcstat')
def create(workflowname,workflowcode,step, prestep):
    create_workflow(workflowname, workflowcode, step, list(prestep))

@workflow.command()
@click.option('--workflowcode', required=False, help='-')
def listworkflow(workflowcode):
    list_workflow(workflowcode)

@script.command()
@click.option('--workflowcode', required=True, help='eg: StrainAnalysis')
@click.option('--step', required=True, help='eg: assembly')
@click.option('--type', required=False, default="Docker", help='-')
@click.option('--script', required=True, help='qcstat:v1.0.0')
def create(workflowcode,step,type, script):
    create_script(workflowcode,step, type, script)

@script.command()
@click.option('--workflowcode', required=False, help='-')
def listscript(workflowcode):
    list_script(workflowcode)


@env.command()
@click.option('--workflowcode', required=True, help='eg: StrainAnalysis')
@click.option('--step', required=True, help='eg: assembly')
@click.option('--type', required=True, default="Docker", help='Input,Output,Mount')
@click.option('--key', required=True, help='qcstat:v1.0.0')
@click.option('--feature', required=True, help='qcstat:v1.0.0')
def create(workflowcode,step,type, key, feature):
    create_env(workflowcode,step, type, key, feature)

@env.command()
@click.option('--workflowcode', required=True, help='-')
@click.option('--step', required=True, help='-')
def listenv(workflowcode, step):
    list_env(workflowcode, step)

@file.command()
@click.option('--basedir', required=True, help='eg: /baseDir/sampleNo/uniqueNo/sampleNo.R1.fq.gz')
def create(basedir):
    create_file(basedir)


@file.command()
@click.option('--uniqueno', multiple=True, required=True, help='-')
def listfile(uniqueno):
    list_file(uniqueno)

@config.command()
@click.option('--type', required=True, help='-')
@click.option('--key', required=True, help='-')
@click.option('--value', required=True, help='-')
def create(basedir):
    create_config(basedir)


@config.command()
def listconfig():
    list_config();

if __name__ == '__main__':
    cli()
