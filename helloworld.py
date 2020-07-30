
import os

for root, dirs, file in os.walk(".", topdown=False):
    print(root)