#!/usr/bin/python3
from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists


def do_pack():

    file_name = f"web_static_{datetime.now():%Y%m%d%H%M%S}.tgz"
    print(file_name)

    local("mkdir -p versions")

    name = local(f"tar -czvf {file_name} {'web_static'}")

    return f"versions/{file_name}"


env.hosts = ['35.174.207.232', '34.204.81.91']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    tmp_path = "/tmp/"

    put(archive_path, tmp_path)

    file_name = archive_path.split('/')[-1]
    folder_name = file_name.split('.')[0]
    relea_path = f"/data/web_static/releases/{folder_name}"
    run(f"mkdir -p {relea_path}")
    run(f"tar -xzf /tmp/{file_name}.tgz -C {relea_path} --strip-components=1")
    if result.failed:
        return False
    run(f"rm {tmp_path}{file_name}")
    run(f"rm -rf /data/web_static/current")
    run(f"ln -s {relea_path} /data/web_static/current")

    return not result.failed
