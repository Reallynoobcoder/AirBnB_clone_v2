#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    file_name = f"web_static_{datetime.now():%Y%m%d%H%M%S}.tgz"
    print(file_name)

    local("mkdir -p versions")

    name = local(f"tar -czvf {file_name} {'web_static'}")

    return f"versions/{file_name}"
