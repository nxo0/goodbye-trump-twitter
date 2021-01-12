import click

from gbtrump.main import Main
from gbtrump.config import Config


@click.group()
def cmd():
    pass

@cmd.command(help="run command")
def run():
    print("running....")
    Main().run()
    print("stoped")

@cmd.command(help="config reset")
def reset():
    config = Config()
    config.all_reset()
    click.echo("OK!")

@cmd.command(help="once check followers and timeline")
def once():
    Main().once()

@cmd.command(help="once check followers")
def once_followers():
    Main().once_followers()

@cmd.command(help="once check timeline")
def once_timeline():
    Main().once_timeline()


def main():
    cmd()


