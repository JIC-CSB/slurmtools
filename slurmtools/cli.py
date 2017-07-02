import click

from fluent import sender

from jinja2 import Environment, PackageLoader


ENV = Environment(loader=PackageLoader('slurmtools', 'templates'),
                  keep_trailing_newline=True)


def template_command(command, params):
    template = ENV.get_template("slurm_script.j2")

    command_string = ' '.join(command)

    submission_script = template.render(params, job=command_string)

    return submission_script


@click.command()
@click.argument('command', nargs=-1)
def cli(command):

    params = {
        "partition": "rg-mh",
        "jobmem": "2000"
    }

    logger = sender.FluentSender('mongo')

    submit_script = template_command(command, params)

    message = {
        'command': ' '.join(command),
        'slurm_params': params,
        'submit_script': submit_script
    }

    logger.emit('quickrun', message)

    print(submit_script)
