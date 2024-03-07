#!/usr/bin/python3
""" THis script shall create and dist archives using func deploy"""
from fabric.api import local, env, put, run
import os
import os.path
from os.path import exists
import datetime
from datetime import datetime

env.hosts = ['54.174.72.190', '100.26.218.108']


def do_pack():
    """This instance shall pack web_static into tgz with ymdhr format"""
    date = datetime.utcnow()
    fiche = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                          date.month,
                                                          date.day,
                                                          date.hour,
                                                          date.minute,
                                                          date.second)
    res = local("mkdir -p versions")
    res = local("tar -cvzf " + fiche + " web_static")
    if res.failed:
        return None
    return fiche


def do_deploy(archive_path):
    """THis instance shall dist the archive of web_stat to the web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    fiche = archive_path.split("/")[-1]
    nom = fiche.split(".")[0]

    if put(archive_path, "/tmp/{}".format(fiche)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(nom)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(nom)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(fiche, nom)).failed is True:
        return False
    if run("rm /tmp/{}".format(fiche)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(nom, nom)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(nom)).failed is True:
        return False
    return True


def deploy():
    """This instance shall deploy the web_static """
    fiche = do_pack()
    if fiche is None:
        return False
    return do_deploy(fiche)
