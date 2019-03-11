from __future__ import print_function
from setuptools import setup
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import get_pkg_version
import shutil          # move and delete files/folders
import os
import sys

if sys.version_info.major != 3 and sys.version_info.minor >= 5:
    raise Exception("Python 3.5 or higher is supported")


def mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        # folder was already created ... it's ok
        pass


def rmdir(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        # folder was already deleted or doesn't exist ... it's ok
        pass


# setup c
print('Building C ---------------------------')
# rmdir("src/build")
mkdir("src/build")
os.chdir("src/build")
os.system('cmake .. && make')
os.chdir("../..")

BinaryDistribution.binary = True

PACKAGE_NAME = 'hello'
BuildCommand.pkg = PACKAGE_NAME
BuildCommand.py2 = False
BuildCommand.test = False
PublishCommand.pkg = PACKAGE_NAME

VERSION = get_pkg_version('hello/__init__.py')
PublishCommand.version = VERSION

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description='test ext modules',
    packages=['hello'],
    package_data={
        'hello': ['src/lib/libhello.dylib'],
    },
    install_requires=['build_utils'],
    distclass=BinaryDistribution,
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand
    }
)
