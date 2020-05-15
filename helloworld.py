

import os

s1 = """
<img changedsize="true" class="BDE_Image" height="365" size="391900" src="http://tiebapic.baidu.com/forum/w%3D580/sign=c533a1495e540923aa696376a259d1dc/170148a7d933c89599c1c711c61373f0830200c5.jpg" width="560"/><img changedsize="true" class="BDE_Image" height="633" size="147623" src="http://tiebapic.baidu.com/forum/w%3D580/sign=a35ac864319759ee4a5060c382fa434e/64fc871001e939018a9f21576cec54e737d196db.jpg" width="560"/><img changedsize="true" class="BDE_Image" height="560" size="466718" src="http://tiebapic.baidu.com/forum/w%3D580/sign=0d41136b1d55b3199cf9827d73a88286/cfef71cb0a46f21f1c8b0139e1246b600d33aec6.jpg" width="560"/>

"""

import re
print(re.findall(r"<img.*?class=\"BDE_Image\".*?src=\"(.*?/([a-z0-9]+?.jpg))\".*?/>", s1))
