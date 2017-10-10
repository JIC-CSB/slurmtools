import os
import subprocess

import click

from fluent import sender

from pymongo import MongoClient

from jinja2 import Environment, PackageLoader


SLURMLOGS = os.path.expanduser("~/slurmlogs")

ENV = Environment(loader=PackageLoader('slurmtools', 'templates'),
                  keep_trailing_newline=True)


def template_command(command, params):
    template = ENV.get_template("slurm_script.j2")

    command_string = ' '.join(command)

    submission_script = template.render(params, job=command_string)

    return submission_script


@click.command()
def slurmhist():

    client = MongoClient('mongodb://localhost:27017/')

    db = client.fluentd

    collection = db.test

    result = collection.find()

    for n, doc in enumerate(result):
        print(n, doc['command'])


def setup():

    if not os.path.isdir(SLURMLOGS):
        os.mkdir(SLURMLOGS)


@click.command()
@click.option('--dryrun', '-d', is_flag=True)
@click.argument('command', nargs=-1)
def cli(command, dryrun):

    setup()

    params = {
        "partition": "rg-mh",
        "jobmem": "2000",
        "stdout": "{}/slurm.%N.%j.out".format(SLURMLOGS),
        "stderr": "{}/slurm.%N.%j.err".format(SLURMLOGS)
    }

    # logger = sender.FluentSender('mongo')

    submit_script = template_command(command, params)

    message = {
        'command': ' '.join(command),
        'slurm_params': params,
        'submit_script': submit_script
    }

    # logger.emit('quickrun', message)

    if dryrun:
        submit_command = 'cat'
    else:
        submit_command = 'sbatch'

    p = subprocess.Popen([submit_command], shell=False, stdin=subprocess.PIPE)
    out, err = p.communicate(submit_script.encode())
