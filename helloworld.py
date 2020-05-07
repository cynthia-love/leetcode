

import re

s = r'<a href="/wikicategory/view?categoryName=恐龙大全" target="_blank">恐龙百科</a>'

print(re.findall(r" ((.*)=\"(.*view.*)\") ", s))

for x in re.finditer(r"(href=\"(\S*view\S*)\")", s):
    print(x.group(0))


print("aaa" in "hewll ooo aaa")

x = {"aaa":1, "bbb":2}

x = "aaaa"
print("".join([x]))