

class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def fout(self):
        print(self.x)


b = B(100)
b.fout()

import pandas
import numpy

def get_x():
    pass