#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives using the function do_clean.
"""

from fabric.colors import red
from fabric.api import local, run, env, cd, lcd

env.hosts = ['34.204.81.91', '35.168.7.64']


def do_clean(number=0):
    """Delete unnecessary archives on web servers."""
    number = int(number)
    if number < 0:
        print(red("Number must be non-negative."))
        return

    if number == 0:
        return

    with lcd("versions"):
        local_archives = local("ls -1t", capture=True).splitlines()
        local_archives_to_keep = local_archives[:number]
        local_archives_to_remove = local_archives[number:]
        for archive in local_archives_to_remove:
            local(f"rm -f {archive}")

    with cd("/data/web_static/releases"):
        remote_archives = run("ls -1t").splitlines()
        remote_archives_to_keep = remote_archives[:number]
        remote_archives_to_remove = remote_archives[number:]
        for archive in remote_archives_to_remove:
            run(f"rm -rf {archive}")
