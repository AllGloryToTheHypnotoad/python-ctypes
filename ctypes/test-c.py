#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# this file just tests the ctype extension
from math import cos as pycos
from hello import test
from hello import cos
from hello import testarray, ClassTest

print("Test cos(5)", cos(5), pycos(5) == cos(5))
print("Test test(5)", test(5), test(5) == 25)

# a = [1,2,3,4,5]
a = testarray()
for v in a:
    print(v)

c = ClassTest()
a = c.read()
print(a)
