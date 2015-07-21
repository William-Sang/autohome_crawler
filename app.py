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
# beautifulsoup 设置解析器（不然迁移可能出错）
html_content_soup = BeautifulSoup(html_content,'html.parser')
brands_tag =  html_content_soup.find_all('li')


for brand_tag in brands_tag:
    cars = []
    brand_name  = brand_tag.get_text(',').split(',')[0]
    brand_href = domain + brand_tag.a['href']
    cars =  get_cars(brand_name, brand_href)
    # 输出中文问题
    for car in cars:
        line = json.dumps(car, encoding="UTF-8", ensure_ascii=False)
        print type(line)
        # 输出 Unicode 到文件
        line = line.encode('UTF-8')
        output_file.write(line)
        output_file.write('\n')
