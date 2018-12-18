#!/usr/bin/python
import click
from github import Github, GithubException


@click.group("repo")
@click.pass_context
def repo_cli(ctx):
    ctx.obj = Github(ctx.obj["token"])
    pass


@repo_cli.command("list")
@click.argument("organization_name", required=True)
@click.pass_obj
def list_repos(repo, organization_name):
    for current_repo in repo.get_organization(organization_name).get_repos():
        print(current_repo)


@repo_cli.command("list_empty")
@click.argument("organization_name", required=True)
@click.pass_obj
def list_empty_repos(repo, organization_name):
    for current_repo in repo.get_organization(organization_name).get_repos():
        try:
            contents = current_repo.get_contents("")
            if len(contents) == 0:
                print(current_repo)
        except GithubException:
            print(current_repo)
