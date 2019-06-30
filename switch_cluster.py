import click
import os
from kubernetes import client, config

@click.group()
def cli():
    pass


@cli.command()
@click.option('--kubeconfig', type=click.Path(), default=os.environ['HOME'] + '/.kube/config', help='Path of the admin Kubeconfig file')
def add_user(**kwargs):
    click.echo("Kubeconfig path is: {}".format(kwargs['kubeconfig']))