#!/usr/bin/env python
# encoding: utf-8

def get_cars(brand_name, start_url):
    start_url = 'http://car.autohome.com.cn/price/brand-15-80.html'
    print start_url
    from setting import headers, wait_sec, domain
    from bs4 import BeautifulSoup
    import requests
    import time
    cars = []
    # 设置referer
    headers['referer'] = start_url

    # 设置起始抓取页面
    now_url = start_url
    next_url = now_url
    while True:
        result = requests.get(now_url, headers=headers)
        print result.request.headers
        html_content = result.content
        html_content = result.content.decode('gbk').encode('utf-8')
        html_content_soup = BeautifulSoup(html_content, 'html.parser')
        cars_tag = html_content_soup.find_all(class_='list-cont-bg')
        #print ' 输出链接',  html_content_soup.find(class_='tab-content fn-visible').find(class_='page-item-next')
        # 结束逻辑
        # 1. 一开始就没有翻页
        # 2. 准确判断 page-item-next
        # 3. 循环

        # 判断是否只有一页
        #print 'next url len: ', len(html_content_soup.find_all(class_='page-item-next'))
        # 这里搜索id， 必须指定节点（比如这里的div）
        #next_url_tag  = html_content_soup.find("div", {"id":"brandtab-1"}).find(class_='page-item-next')
        print 'next len is ', len(html_content_soup.find_all(class_="page-item-next"))
        next_url_tag = html_content_soup.select("#brandtab-1")
        #next_url_tag  = html_content_soup.find("div", id="brandtab-1")
        print next_url_tag
        exit()
        next_url = domain + next_url_tag['href']
        print 'next_url is ', next_url
        print 'find 结果',next_url.find('###')
        if next_url.find('javascript') == -1:
            return cars
        print 'next_url is ', next_url
        # 提取下一页
        for car_tag in cars_tag:
            car = {}
            car['brand'] = brand_name
            car['url'] = now_url
            car['name'] = car_tag.find(class_='main-title').get_text(strip=True)
            car['price'] = car_tag.find(class_='font-arial').get_text(strip=True)
            # @TODO 颜色还有问题
            for car_attr_tag  in car_tag.find('ul', class_='lever-ul').find_all('li'):
                #print car_attr_tag
                car_attr = car_attr_tag.get_text(',',strip=True)
                if len(car_attr.split(u'：')) < 2 :
                    continue
                car_attr_key = car_attr.split(u'：')[0]
                car_attr_value = car_attr.split(u'：')[1]
                car[car_attr_key] = car_attr_value.strip(',')
            cars.append(car)
        time.sleep(wait_sec)
        # 更换页面
        now_url = next_url
