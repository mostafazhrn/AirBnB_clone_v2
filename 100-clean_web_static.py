#!/usr/bin/python3
""" THis script shall delete out of date archives using do_clean"""
from fabric.api import local, env, put, run
import os
from os.path import exists
import datetime
from datetime import datetime

env.hosts = ['54.174.72.190', '100.26.218.108']


def do_clean(number=0):
    """This instance shall clean the outdated archives"""
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
    return True
