import numpy
import ctypes


# do the dll one from ctypes
_libhello = numpy.ctypeslib.load_library('libhello.dylib', './src/lib')

_libhello.hello.argtypes = [ctypes.c_int]
_libhello.hello.restype = ctypes.c_int


def hellofunc(n):
	return _libhello.hello(int(n))
