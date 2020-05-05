# 打包库模块并发布到PyPI

>**区别pyinstaller的打包成可执行文件！！！**

Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。它允许人们使用易读易写的纯文本格式编写文档，然后转换成格式丰富的HTML页面，Markdown文件的后缀名便是“.md”， 你可以使用[MdEditor](http://www.mdeditor.com/)在线编辑Markdown文档。包使用过程中如有任何疑问请联系Cynthia（bbliu666@126.com）。

## 环境准备
1. conda install setuptools
2. conda install wheel
3. conda install twine
4. 新建twine配置文件.pypirc

``` html
[distutils]
index-servers=pypi
[pypi]
repository = https://upload.pypi.org/legacy/
username: PyPI用户名
password: PyPI密码
```
## 操作步骤
1. python setup.py check
2. python setup.py sdist bdist_wheel
3. twine upload dist/*
4. 指定版本: twine upload dist/\*1.0.5\*

## 使用说明
```
import hellopy.hello as hh
import hellopy.opts.const as hoc
import hellopy.utils.tool as hut
```

## 版本更新历史
###### V-1.0.1 版本
1. 基础版本
2. 支持打包和发布

###### V-1.0.2 版本
1. 细化配置文件
2. 增加自定义包层级
