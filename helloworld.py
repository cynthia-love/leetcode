

import os

s = '<img changedsize="true" class="BDE_Image" height="1045" size="741728" src="http://tiebapic.baidu.com/forum/w%3D580/sign=1948519d883df8dca63d8f99fd1072bf/2137b91bb051f819ef9f5c20cdb44aed2f73e7c3.jpg" width="560"/>'
import re
print(re.findall(r"<img.*src=\"(.*/(.*\.jpg))\".*/>", s))