from __future__ import print_function
from __future__ import division
import os
from hello.hello import hellofunc
# from .meta import *

__version__ = '0.1.0'
__author__ = 'bob'
__license__ = 'MIT'

lib_path = os.path.join(os.path.dirname(__file__), 'libhello.dylib')
# lib = CDLL(lib_path)
print(lib_path)
