#!/usr/bin/python3
"""This fabric script shall dist archive to web_servers"""
from fabric.api import local, env, put, run
import os
from os.path import exists
env.hosts = ['54.174.72.190', '100.26.218.108']


def do_deploy(archive_path):
    """This shall dist archives to server"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        nom = archive_path.split("/")[1].split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(nom))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(nom, nom))
        run("rm /tmp/{}.tgz".format(nom))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/
        releases/{}/".format(nom, nom))
        run("rm -rf /data/web_static/releases/{}/web_static".format(nom))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(nom))
        return True
    except:
        return False
