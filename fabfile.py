# coding: utf-8
import os
import subprocess

from fabric.api import env, cd, run


def shell(command):
    run(command.format(**{'git_url': env.git_url,
                          'project_dir': env.project_dir}))


def git_url():
    process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.strip()


def setup_env():
    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa.pub')]
    env.user = 'root'
    env.project_root = '/opt'
    env.shell = '/bin/bash -c'
    env.git_url = git_url()
    env.project_dir = 'django_project'
    shell('apt -y update && apt -y upgrade && apt -y install git docker docker-compose')


def deploy():
    setup_env()
    with cd(env.project_root):
        shell('rm -rf {project_dir}')
        shell('git clone {git_url} {project_dir}')
        shell('docker ps -a -q | xargs docker stop')
        shell('cd {project_dir} && docker-compose stop')
        shell('cd {project_dir} && docker-compose build')
        shell('cd {project_dir} && docker-compose up -d')