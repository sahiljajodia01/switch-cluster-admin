import click
import os
from kubernetes import client, config

@click.command()
@click.option('--kubeconfig', type=click.Path(), default=os.environ['HOME'] + '/.kube/config', help='Path of the administrator Kubeconfig file')
def cli(**kwargs):
    click.echo("Kubeconfig path is: {}".format(kwargs['kubeconfig']))