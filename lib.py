#!/usr/bin/env python
# encoding: utf-8
from setting import headers
from bs4 import BeautifulSoup
import requests

def get_cars(brand_name, start_url):
    """TODO: Docstring for get_cars.

    :brand_name: TODO
    :start_url: TODO
    :returns: TODO

    """
    #cars_dict = []
    # 设置referer
    headers['referer'] = start_url
    print  brand_name, start_url, headers
    result = requests.get(start_url, headers=headers)
    html_content_soup = BeautifulSoup(result.content, 'html.parser')
    cars_tag = html_content_soup.find_all(class_='list-cont-bg')
    # 提取下一页
    cars = []
    for car_tag in cars_tag:
        car = {}
        car['brand'] = brand_name
        car['name'] = car_tag.find(class_='main-title').get_text(strip=True)
        car['price'] = car_tag.find(class_='font-arial').get_text(strip=True)
        print ' 颜色', car_tag.find(class_='carcolor fn-left')
        # @TODO 颜色还有问题
        for car_attr_tag  in car_tag.find('ul', class_='lever-ul').find_all('li'):
            print car_attr_tag
            car_attr = car_attr_tag.get_text(',',strip=True)
            car_attr_key = car_attr.split(u'：')[0]
            car_attr_value = car_attr.split(u'：')[1]
            #car[car_attr_key] = car_attr_value.strip(',')
            car[car_attr_key] = car_attr_value
        cars.append(car)
    return cars
