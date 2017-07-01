import click

from jinja2 import Environment, PackageLoader


ENV = Environment(loader=PackageLoader('quickrun', 'templates'),
                  keep_trailing_newline=True)


def template_command(command):
    template = ENV.get_template("slurm_script.j2")

    command_string = ' '.join(command)

    params = {
        "job": command_string,
        "partition": 'rg-mh',
        "jobmem": "2000"
    }

    submission_script = template.render(params)

    print(submission_script)


@click.command()
@click.argument('command', nargs=-1)
def cli(command):
    template_command(command)
