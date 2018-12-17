#!/usr/bin/python
import click
from github import Github


@click.group("team")
@click.pass_context
def team_cli(ctx):
    ctx.obj = Github(ctx.obj["token"])
    pass


@team_cli.command("list")
@click.argument("organization_name", required=True)
@click.pass_obj
def list_teams(team, organization_name):
    teams = []
    for current_team in team.get_organization(organization_name).get_teams():
        teams.append(current_team.name)
    teams.sort()
    for current_team in teams:
        print(f"- {current_team}")


@team_cli.command("members")
@click.argument("organization_name", required=True)
@click.argument("team_name", required=True)
@click.pass_obj
def get_team_members(team, organization_name, team_name):
    for current_team in team.get_organization(organization_name).get_teams():
        if current_team.name == team_name:
            members = []
            for member in current_team.get_members():
                members.append(member.login)
            members.sort()
            for member in members:
                print(f"- {member}")
