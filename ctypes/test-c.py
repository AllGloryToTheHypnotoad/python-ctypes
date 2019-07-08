#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# this file just tests the ctype extension
from math import cos as pycos
from hello import test
from hello import cos
from hello import testarray, ClassTest

cos5 = cos(5)
test5 = test(5)
print("Test cos(5)", cos5, pycos(5) == cos5)
print("Test test(5)", test5, test5 == 25)

# a = [1,2,3,4,5]
# a = testarray()
# for v in a:
#     print(v)

c = ClassTest()
a = c.read()
a = c.read()
a = c.read()
# print(a)
a = c.readprotected()
# aa = [0]*10
# for i in range(10):
#     aa[i] = a[i]
# print(aa)
