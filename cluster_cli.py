import click
import os
from kubernetes import client, config
import yaml
import io

class Config(object):
    def __init__(self):
        self.kubeconfig = ''

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--kubeconfig', type=click.Path(), default=os.environ['HOME'] + '/.kube/config', help='Path of the admin Kubeconfig file')
@pass_config
def cli(config, **kwargs):
    config.kubeconfig = kwargs['kubeconfig']


@cli.command()
@click.argument('user-name', type=str)
@pass_config
def add_user(config, **kwargs):
    namespace = 'swan-' + kwargs['user_name']
    username = kwargs['user_name']
    rolebinding_name = 'edit-cluster-' + namespace

    with io.open('role-binding-template.yaml', 'r', encoding='utf8') as stream:
        load = yaml.safe_load(stream)

    load['metadata']['name'] = rolebinding_name
    load['metadata']['namespace'] = namespace
    load['subjects'][0]['name'] = username

    with io.open('role-binding-template.yaml', 'w', encoding='utf8') as out:
        yaml.safe_dump(load, out, default_flow_style=False, allow_unicode=True)

    click.echo("User successfully added!")
