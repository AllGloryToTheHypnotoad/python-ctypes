import numpy
import ctypes

try:
    # do the dll one from ctypes
    # _libhello = ctypes.cdll.LoadLibrary('./src/lib/libhello.dylib')
    _libhello = numpy.ctypeslib.load_library('libhello.dylib', './src/lib')
    # _libhello = numpy.ctypeslib.load_library('libhello.a', './src/build')
except OSError as e:
    print(e)
    exit(1)

print("_libhello", _libhello)

# input/output of cos function
_libhello.hcos.argtypes = [ctypes.c_double]
_libhello.hcos.restype = ctypes.c_double


def cos(n):
    return _libhello.hcos(float(n))


# input/output of test function
_libhello.test.argtypes = [ctypes.c_int]
_libhello.test.restype = ctypes.c_int


def test(n):
    return _libhello.test(int(n))


_testarray = _libhello.testarray
_testarray.argtypes = [ctypes.POINTER(ctypes.c_double)]
_testarray.restype = ctypes.c_void_p


def testarray():
    p = (ctypes.c_double*5)()
    print("p", p)
    _testarray(p)
    print(len(p))
    return tuple(p)

# c++ objects
# http://www.auctoris.co.uk/2017/04/29/calling-c-classes-from-python-with-ctypes/


class ClassTest(object):
    def __init__(self):
        _libhello.new_test.argtypes = [ctypes.c_void_p]
        _libhello.new_test.restypes = ctypes.c_void_p

        _libhello.read.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double)]
        _libhello.read.restypes = ctypes.c_void_p

        _libhello.readprotected.argtypes = [ctypes.c_void_p]
        _libhello.readprotected.restypes = ctypes.c_void_p  # ctypes.POINTER(ctypes.c_double)

        self.obj = _libhello.new_test(None)
        self.buffer = (ctypes.c_double*5)()

    def read(self):
        print("self.obj", self.obj)
        _libhello.read(self.obj, self.buffer)
        print("post read")
        return tuple(self.buffer)

    def readprotected(self):
        print("readprotected obj", self.obj)
        # a = _libhello.readprotected(self.obj)
        _libhello.readprotected(self.obj)
        # print(a)
        # aa = [0]*10
        # for i in range(10):
        #     aa[i] = a[i]
        # return tuple(aa)
