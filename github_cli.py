#!/usr/bin/env python
import click

from objects.team import team_cli


@click.group()
@click.option("--token", metavar="TOKEN", envvar="TOKEN", help="GitHub Token")
@click.pass_context
def cli(ctx, token):
    ctx.obj = {"token": token}


cli.add_command(team_cli)

if __name__ == '__main__':
    cli()
