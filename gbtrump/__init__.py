import click

from gbtrump.gbtrump import GBTrump
from gbtrump.config import Config

from gbtrump.__main__ import __version__


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, default=False)
def cmd(version):
    click.echo("GBTrump version: " + __version__)

@cmd.command(help="run command")
def run():
    print("running....")
    GBTrump().run()
    print("stoped")

@cmd.command(help="config reset")
def reset():
    config = Config()
    config.all_reset()
    click.echo("OK!")

@cmd.command(help="once check followers and timeline")
def once():
    GBTrump().once()

@cmd.command(help="once check followers")
def once_followers():
    GBTrump().once_followers()

@cmd.command(help="once check timeline")
def once_timeline():
    GBTrump().once_timeline()


def main():
    cmd()


