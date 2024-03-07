#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers,
using the function do_deploy.
"""
from fabric.api import local, env, put, run
import os
from os.path import exists
import datetime

env.hosts = ['54.174.72.190', '100.26.218.108']


def do_deploy(archive_path):
    """THis shall dist the archive to the web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        arch = archive_path.split("/")[-1]
        pth = "/data/web_static/releases/"
        put("{}".format(archive_path), "/tmp/{}".format(arch))
        run("sudo mkdir -p {}{}/".format(pth, arch[:-4]))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(arch, pth, arch[:-4]))
        run("sudo rm /tmp/{}".format(arch))
        run("sudo mv {0}{1}/web_static/* {0}{1}/"
            .format(pth, arch[:-4]))
        run("sudo rm -rf {}{}/web_static".format(pth, arch[:-4]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(pth, arch[:-4]))
        return True
    except:
        return False
