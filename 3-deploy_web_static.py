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
    """ THis instance shall dist the arch to web_servers"""
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


def deploy():
    """ THis shall deplay the files of the web_static"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
