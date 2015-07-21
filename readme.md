###项目简介

本项目主要用于介绍使用 requests 和 BeautifulSoup 进行爬虫开发


* requests 文档:[http://docs.python-requests.org/en/latest/](http://docs.python-requests.org/en/latest/)
* BeautifulSoup 文档:[http://www.crummy.com/software/BeautifulSoup/bs4/doc/](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


### 使用须知
1. clone 本项目

    ```
# git clone git@github.com:William-Sang/autohome_crawler.git
```
2. 配置依赖

    ```
	# cd autohome_crawler
	# pip install -r requirements
	```
	
3. 修改配置


    ```
	# vim setting.py
	```
	
4. 执行爬取任务，默认结果会下载到 requests 目录下


    ```
	# python app.py
	```

### 需要加强功能
1.  下载重试功能 http://www.coglib.com/~icordasc/blog/2014/12/retries-in-requests.html

### 可能出现的问题
1. 抓取具体车型信息的时候，会出现颜色无法抓取成功的情况。（有时）
