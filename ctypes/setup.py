from __future__ import print_function
from setuptools import setup
# from hello import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import get_pkg_version
from shutil import rmtree
import os

# read in like text file
# version = {}
# with open("hello/meta.py") as fp:
# 	exec(fp.read(), version)
# VERSION = version['__version__']

# VERSION = get_pkg_version('hello/__init__.py')

# setup c
print('Building C ---------------------------')
os.system('rm -fr src/build')
# rmtree()
os.system('mkdir -p src/build')
# try:
# 	os.mkdir('src/build')
# except OSError:
# 	pass

os.system('cd src/build && cmake .. && make')

BinaryDistribution.binary = True

PACKAGE_NAME = 'hello'
BuildCommand.pkg = PACKAGE_NAME
BuildCommand.py2 = False
BuildCommand.test = False
PublishCommand.pkg = PACKAGE_NAME

VERSION = get_pkg_version('hello/__init__.py')
# from hello import __version__ as VERSION
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
