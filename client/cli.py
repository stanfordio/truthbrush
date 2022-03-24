"""Defines the CLI for TruthSeeker."""

import json
import os
import click
import pkg_resources
from dotenv import load_dotenv

from .api import Api

load_dotenv()  # take environment variables from .env.
api = Api(os.getenv("TRUTHSOCIAL_TOKEN"))


@click.group()
def cli():
    """This is an API client for Truth Social."""


@cli.command()
def trends():
    """Pull a user's metadata."""

    print(json.dumps(api.trending()))


@cli.command()
@click.argument("handle")
def user(handle: str):
    """Pull a user's metadata."""

    print(json.dumps(api.lookup(handle)))


@cli.command()
@click.argument("handle")
@click.option("--maximum", help="the maximum number of followers to pull", type=int)
def followers(handle: str, maximum: int = None):
    """Pull a user's followers."""

    for follower in api.user_followers(handle, maximum=maximum):
        print(json.dumps(follower))
