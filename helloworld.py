

from urllib import response

from urllib import request

x = request.urlopen("http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/")

print(x.read().decode("utf-8"))