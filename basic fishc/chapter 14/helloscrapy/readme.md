scrapy是专门的写爬虫的框架, 一般分为四个步骤:
1. 创建项目
2. 定义Item容器
3. 编写爬虫
4. 存储内容

scrapy框架主要分为这么几个部分
1. scrapy engine, 引擎, 负责控制数据流在所有组件间流动, 并在相应动作时触发事件
2. scheduler, 调度器, 为引擎服务, 提供请求调度服务, 引擎把待处理的请求压入调度器, 可以处理时再调出来
3. downloader, 下载器, 引擎把请求从调度器里拿出来, 给下载器, 下载器获取页面数据给引擎
4. downloader middlewares, 下载器中间件, 在下载器下载完页面数据后, 进行初步处理后再给引擎
5. spiders, 爬, 引擎拿到response后交给spider进行正式处理的地方, 提取item和进一步爬取地址
6. spider middlewares, spider中间件, 引擎在把response给spider时先在spider中间件里预处理一下,
以及spider把提取出的item和进一步爬取地址给到引擎的时候, 也在spider中间件里预处理一下
7. item pipeline, spider提取出来item给到引擎后, 引擎会给item pipeline进行专门的数据处理, 比如清理, 
验证, 持久化(存储到数据库等)

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
- response.selector.extract(), 将.xpath, .css找到的selector对象内容提取出来
- response.selector.re()  基于正则

知识点补充: BeautifulSoup是一个库，而XPath是一种技术，python中最常用的XPath库是lxml; 
速度上, re>bs>lxml, 易用性上bs>lxml>re; 另外, 讲一下Response对象: urllib里的response对象
实际是http.client.HTTPResponse, 包含.status .version .getcode() .getheaders() .getheader()
.geturl() .info() .read() .readline(); 而scrapy里的response对象是自己实现的scrapy.http.Response,
有属性url, status, headers(字典形式), body, request(Request对象), meta, urljoin(url), 其下设
三个子类TextResponse, HtmlResponse, XmlResponse, 而最常用的TextResponse新增了这么几个属性和方法:
text(等价于response.body.decode(response.encoding)), encoding, selector(选择器对象, 复杂写法
response.selector.xpath(query)或response.selector.css(query), 也可简写response.xpath('//p), 
response.css('p'))

#####4. 爬, 进到项目根目录, scrapy crawl dmoz (spider里的name)


