import click
from config import set_config, load_config, check
from file import create_file,list_file
from workflow import create_workflow, list_workflow

@click.group()
def cli():
    pass

@cli.group()
def workflow():
    pass

@cli.group()
def file():
    pass


@cli.command()
@click.option('--server', default='http://localhost', help='server http address, eg: http://biolab.com')
@click.option('--port', default='8080', help='server port, eg 8080')
def config(server,port):
    set_config(server, port)


@workflow.command()
@click.option('--workflowname', required=True, help='eg: Strain Analysis workflow')
@click.option('--workflowcode', required=True, help='eg: StrainAnalysis')
@click.option('--step', required=True, help='eg: assembly')
@click.option('--prestep', multiple=True, required=True, help='qcstat')
def create(workflowname,workflowcode,step, prestep):
    print("workflow==>", workflowname, workflowcode, step, prestep)
    create_workflow(workflowname, workflowcode, step, list(prestep))

@workflow.command()
@click.option('--workflowcode', required=False, help='-')
def listworkflow(workflowcode):
    list_workflow(workflowcode);


@file.command()
@click.option('--basedir', required=True, help='eg: /baseDir/sampleNo/uniqueNo/sampleNo.R1.fq.gz')
def create(basedir):
    create_file(basedir)


@file.command()
@click.option('--uniqueno', multiple=True, required=True, help='-')
def listfile(uniqueno):
    list_file(uniqueno);

if __name__ == '__main__':
    cli()
