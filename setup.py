#!/usr/bin/python3

import sys

if sys.version_info < (3, 5):
    sys.exit("Sorry, we need at least Python 3.5.")

from setuptools import setup

setup(
    name="mkosi",
    version="1",
    description="Create legacy-free OS images",
    url="https://github.com/systemd/mkosi",
    maintainer="mkosi contributors",
    maintainer_email="systemd-devel@lists.freedesktop.org",
    license="LGPLv2+",
    scripts=["mkosi"],
)
