# coding: utf-8
import os
from os import path

from fabric.api import env, cd, run


HOME = os.environ['HOME']
REPO = 'https://github.com/mermoldy/dockerized-django.git'


def shell(command):
    run(command.format(**{'repo': env.repo,
                          'project_dir': env.project_dir}))


def setup_env():
    env.key_filename = [path.join(HOME, '.ssh', 'id_rsa.pub')]
    env.user = 'root'
    env.project_root = '/opt'
    env.shell = '/bin/bash -c'
    env.repo = REPO
    env.project_dir = 'django_project'
    shell('apt -y update && apt -y upgrade && apt -y install git docker docker-compose')


def deploy():
    setup_env()
    with cd(env.project_root):
        shell('rm -rf {project_dir}')
        shell('git clone {repo} {project_dir}')
        shell('docker ps -a -q | xargs docker stop')
        shell('cd {project_dir} && docker-compose stop')
        shell('cd {project_dir} && docker-compose build')
        shell('cd {project_dir} && docker-compose up -d')
        shell('cd {project_dir} && docker-compose run web /usr/local/bin/python manage.py migrate')