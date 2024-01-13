#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from datetime import datetime
from os import path
from fabric.api import local, put, run, env

env.hosts = ['35.168.7.64', '34.204.81.91']


def do_pack():
    """Create a .tgz archive from the contents of web_static folder."""
    archive_filename = f"web_static_{datetime.now():%Y%m%d%H%M%S}.tgz"
    archive_path = f"versions/{archive_filename}"

    local("mkdir -p versions")
    local(f"tar -cvzf {archive_path} web_static")
    return archive_path

def do_deploy(archive_path):
    """ deploy """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_comp, new_folder))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False
