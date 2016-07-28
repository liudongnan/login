# coding: utf-8
import os
import sys
import random
import urllib
import urllib2
from bs4 import BeautifulSoup


def get_html_soup(url, headers, params=None):
    """
    获取、解析页面
    :param url: 请求 url
    :param params: 请求 params
    :param headers: 主要更新headers = {'Referer': ''}
    :return:
    """

    if params:
        params = urllib.urlencode(params)
        req = urllib2.Request(url, params, headers=headers)
    else:
        req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    return BeautifulSoup(response, 'html.parser')


def get_params(soup, key_dict):
    """

    :param soup:
    :param key_dict:
    :return:
    """
    params = {}
    value = lambda key, soup: soup.find('input', {'name': key})
    [params.update({key:  value(key, soup).get('value') if value(key, soup) else ''}) for key in key_dict]
    return params


def save_img(base_url, headers, soup):
    """

    :param base_url:
    :param relative_url:
    :param headers:
    :param soup:
    :return:
    """

    imgurl = base_url + soup.find("img", id="imgrc")["src"]
    img_req = urllib2.Request(imgurl, headers=headers)
    img_content = urllib2.urlopen(img_req).read()
    img_path = cur_file_dir() + '\\' + repr(random.random()) + '.jpg'

    with open(img_path, "wb") as f:
        f.write(img_content)
    return img_path


def parser(soup, key_list):
    """

    :param soup:
    :param key_list:
    :return:
    """
    params = {}
    fun = lambda key, soup: soup.find('input', {'name': key})
    [params.update({key:  fun(key, soup).get('value') if fun(key, soup) else ''}) for key in key_list]
    return params


def cur_file_dir():
    """

    :return:
    """
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)