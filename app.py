#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup
from lib import get_cars
from setting import headers, domain, start_url, file_output
import json

output_file = open(file_output, 'a')

# 第一步提取 品牌列表
# 第二部通过品牌列表提取 车辆详细列表(下一页)


#print url
# 设置隐藏爬虫痕迹
result = requests.get(start_url, headers=headers)
#result.encoding = 'gbk'  ## @TODO 这一行干嘛用的
# @TODO 验证是否下载成功
html_content = result.content
html_content = html_content.decode('gbk').encode('utf-8')
# @TODO 保存原始文档
# @TODO beautifulsoup 设置解析器（不然迁移可能出错）
html_content_soup = BeautifulSoup(html_content,'html.parser')
print type(html_content_soup)
# 提取品牌链接
# 品牌名称和链接
# ? 这里也不知道为什么 class 不用加 class_ = "cartree"
brands_tag =  html_content_soup.find_all('li')


for brand_tag in brands_tag:
    cars = []
    brand_name  = brand_tag.get_text(',').split(',')[0]
    brand_href = domain + brand_tag.a['href']
    print '品牌名称为:', brand_name
    print ' 品牌链接为:', brand_href
    cars =  get_cars(brand_name, brand_href)
    print json.dumps(cars)
    for car in cars:
        output_file.write(json.dumps(car))
        output_file.write('\n')

    exit()
