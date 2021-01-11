import click

from app.main import Main
from app.config import Config


@click.group()
def cmd():
    pass

@cmd.command()
def run():
    print("running....")
    Main().run()
    print("stoped")

@cmd.command()
def reset():
    config = Config()
    config.all_reset()
    click.echo("OK!")

@cmd.command()
def once():
    Main().once()


def main():
    cmd()


