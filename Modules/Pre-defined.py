import math
from math import sqrt
# from modulepackage import call
from modulepackage.call import module_call

class root():

    def square(self, a):
        print(math.sqrt(a))
        print(sqrt(5))

    def check(self):
        check = 66
        recheck = 33
        # call.module_call(check, recheck)

        module_call(check, recheck)

s = root()
s.square(10)
s.check()