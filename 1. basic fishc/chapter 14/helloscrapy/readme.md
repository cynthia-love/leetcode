scrapy是专门的写爬虫的框架, 一般分为四个步骤:
1. 创建项目
2. 定义Item容器(第一个要写的文件items.py)
3. 编写爬虫(第二个要写的文件, spiders/dmoz.py)
4. 存储内容(第三个要写的文件, pipelines.py)

一般情况下, 这三个就够了, 有时候还需要写middlewares, 包括引擎-下载器中间件, 引擎-spider中间件

scrapy框架主要分为这么几个部分
1. scrapy engine, 引擎, 负责控制数据流在不同组件间传递, 框架本身已实现
2. scheduler, 调度器, 一个队列, 暂存引擎发送过来的请求, 框架本身已实现
3. downloader, 下载器, 引擎把请求从调度器里拿出来, 给下载器, 下载器获取页面数据给引擎, 框架本身已实现
4. downloader middlewares, 位于引擎和下载器之间, 处理引擎给下载器的request和下载器回来的response, 比如修改请求头部, 视需要实现
5. spiders, 引擎拿到response后交给spider进行正式处理的地方, 提取item和进一步爬取地址, 要自己实现
6. spider middlewares, 位于引擎和spider之间, 处理spider的输出(item和request)以及引擎回来的response, 视需要实现
7. item pipeline, spider提取出来item给到引擎后, 引擎会给item pipeline进行专门的数据处理, 比如清理, 
验证, 持久化(存储到数据库等), 要自己实现

还是有点乱:
1. spider的yield将request发送给engine
2. engine对request不做任何处理发送给scheduler
3. scheduler，生成request交给engine
4. engine拿到request，通过middleware发送给downloader
5. downloader在获取到response之后，又经过middleware发送给engine
6. engine获取到response之后，返回给spider，spider的parse()方法对获取到的response进行处理，解析出items或者requests
7. 将解析出来的items或者requests发送给engine
8. engine获取到items或者requests，将items发送给ItemPipeline，将requests发送给scheduler
（ps，只有调度器中不存在request时，程序才停止，及时请求失败scrapy也会重新进行请求）

练手:
http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/
http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/

构建步骤:
#####1. 创建项目`scrapy startproject helloscrapy`, 主要包含这么几个部分:
    - scrapy.conf, 项目配置文件
    - xxx/settings.py, 项目设置文件
    - xxx/spiders, spider代码(解析response)
    - xxx/items, item文件
    - xxx/pipelines, pipelines文件
    - middlewares, 中间件文件

#####2. 定义item主要是确定要爬取哪些字段, 先用浏览器分析html, 确定要: title, desc, link后修改items.py
```html
<div class="title-and-desc">
    <a target="_blank" href="xxxx">
        <div class="site-title">xxxx</div>
    </a>
    <div class="site-descr">
        dkjfkdjfkjdaljfkd
    </div>
</div>
```
```python
class HelloscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()
```

#####3. 编写spider, 用于提供初始url及从返回中提取item和二次爬取url; spiders下可以创建多个spider创建dmoz, 继承scrapy.Spider, 实现三个属性:

- name,唯一
- start_urls, 启动时爬取的页面列表
- parser(), 解析初始url返回的response, 提取item及生成二次爬取url对象

```python
class dmoz(scrapy.Spider):
    name = 'dmoz'
    start_urls = [
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
    ]
    allowed_domains = ["dmoztools.net"]   # 不在此域中的url不会访问

    # 注意这里的parser, 每个初始url返回response后都会调这个方法; 如果有多个url
    # 可以通过response.url区分是哪个url返回的, 以进行不同的处理逻辑
    def parse(self, response):
        print(response)
        source_url = response.url
        file_name = source_url.split("/")[-2]  # 一般url最后会带一个/
        with open("data/"+file_name, "wb") as f:
            f.write(response.body)
```
上面只是对response进行简单的处理, scrapy处理html主要基于四个方法:

- response.selector.xpath()  基于xpath
- response.selector.css()  基于css
- response.selector.extract(), 将.xpath, .css找到的selector对象内容提取出来; 注意extractor()是
对selector出来的每个都进行操作, 所以结果是个list, 如果确定就一个结果, 也可以extract_first()
- response.selector.re()  基于正则

知识点补充: BeautifulSoup是一个库，而XPath是一种技术，python中最常用的XPath库是lxml; 
速度上, re>bs>lxml, 易用性上bs>lxml>re; 另外, 讲一下Response对象: urllib里的response对象
实际是http.client.HTTPResponse, 包含.status .version .getcode() .getheaders() .getheader()
.geturl() .info() .read() .readline(); 而scrapy里的response对象是自己实现的scrapy.http.Response,
有属性url, status, headers(字典形式), body(这里的body属性获取的内容同urllib里response对象的read(), 
request(Request对象), meta, urljoin(url), 其下设三个子类TextResponse, HtmlResponse, XmlResponse, 
而最常用的TextResponse新增了这么几个属性和方法:text(等价于response.body.decode(response.encoding)), 
encoding, selector(选择器对象, 复杂写法response.selector.xpath(query)或response.selector.css(query), 
也可简写response.xpath('//p), response.css('p'))

#####4. 爬, 进到项目根目录, scrapy crawl dmoz (spider里的name), 会发现对应目录下多了俩文件; 这里由于没对response做什么处理, 直接存, 所以文件里存的是网页html原始内容

使用xpath提取数据:
- response.xpath("/div"), root节点的一级子节点, 注意是root, 类似于linux文件夹绝对路径
- response.xpath("a/div/div")  相对路径, 从当前节点的子节点开始算
- response.xpath("//div"), 查询所有子孙节点
- response.xpath("."), 当前节点
- response.xpath(".."), 父节点
- response.xpath("//div[@id]"), 所有带id属性的子孙节点
- response.xpath('//div[@id]/@id') 带id属性的子孙节点的id属性值
- response.xpath("//div[@id='xxx']"), 所有id属性等于xxx的子孙div节点
- response.xpath("//div/span[1]"), 所有div下第一个span元素
- response.xpath("//div/span/text()") 所有div-span的文字内容

根据上述语法, 补充spider里提取title, desc, link
```python
        items = response.xpath('//div[@class="title-and-desc"]')
        for item in items:
            title = item.xpath('a/div/text()').extract()[0].strip()
            link = item.xpath('a/@href').extract()[0].strip()
            desc = item.xpath('div/text()').extract_first().strip()
        # extarct()返回list, extract_first()返回第一个
```

#####5. 使用item
前面有定义item, 这里要修改parse返回List[HelloscrapyItem]格式数据
```python
        res, items = [], response.xpath('//div[@class="title-and-desc"]')
        for item in items:
            t = HelloscrapyItem()
            t['title'] = item.xpath('a/div/text()').extract()[0].strip()
            t['link'] = item.xpath('a/@href').extract()[0].strip()
            t['desc'] = item.xpath('div/text()').extract_first().strip()
            res.append(t)
        return res
```
之后可以用命令: scrapy crawl dmoz -o 文件名 -t 类型输出爬取的item数据, 格式有json, json lines, csv, xml
试试: scrapy crawl dmoz -o data/Items -t csv

#####6. pipeline, 负责处理被spider提取出来的item(当然, 也可以在spider里处理, 不过不建议, 那样spider太臃肿)
管道里主要实现process_item(), 每一个item管道组件都会调用该方法，并且必须返回一个item对象或dict或raise DropItem异常。
被丢掉的item将不会在管道组件进行执行。此方法有两个参数，一个是item,即要处理的Item对象，另一个参数是spider,即爬虫。
由于默认Item是无序的, 这里可以用OrderedDict做二次处理后return; 之后在setting里启用该管道
```python
from collections import OrderedDict
class HelloscrapyPipeline:
    def process_item(self, item, spider):
        od = OrderedDict()
        od["title"] = item["title"]
        od["link"] = item["link"]
        od["desc"] = item["desc"]
        return od
```
修改settings.py
```python
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'helloscrapy.pipelines.HelloscrapyPipeline': 300,
}
```
