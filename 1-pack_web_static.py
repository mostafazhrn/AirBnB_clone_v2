#!/usr/bin/python3
""" THis script shall generate tgz for web_static"""
import fabric
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """This shall pack web_static files into .tgz file"""
    local("mkdir -p versions")
    dat = datetime.now().strftime("%Y%m%d%H%M%S")
    fiche = "versions/web_static_{}.tgz".format(dat)
    res = local("tar -cvzf " + fiche + " web_static")
    if res.failed:
        return None
    return fiche
