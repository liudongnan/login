# coding: utf-8

import urllib2
import cookielib

from conf import *
from common import *

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

reload(sys)
sys.setdefaultencoding('utf8')


class Login(object):
    """
    模拟登陆获取验证报告

    :param object:
    :return:
    """

    def __init__(self):
        self.user_name = ''
        self.pass_word = ''
        self.date = ''
        self.token = ''
        self.method = ''
        self.img_code = ''      # 图片验证码
        self.img_path = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def getLoginInfo(self):

        urllib2.urlopen(ZX_URL['init_url'])
        soup = get_html_soup(ZX_URL['get_params_url'], ZX_HEADERS['get_params'])
        params = get_params(soup, GET_LOGIN_PARAMS)
        img_path = save_img(ZX_URL['init_url'], ZX_HEADERS['img_code'], soup)
        params.update({'img_path': img_path})
        return params

    def setLoginInfo(self, **kw):
        """
        kw
        在视图中获取 用户提交的 user_name, pass_word, img_code,
        然后合并getLoginInfo中获取的params字典
        :param kw:
        :return:
        """
        self.user_name = kw['user_name']
        self.pass_word = kw['pass_word']
        self.date = kw['date']
        self.method = kw['method']
        self.img_code = kw['img_code']
        self.img_path = kw['img_path']

    def login(self):

        login_params = {
            'loginname': self.user_name,
            'password': self.pass_word,
            'date': self.date,
            'method': self.method,
            '_@IMGRC@_': self.img_code,
            'org.apache.struts.taglib.html.TOKEN': self.token
        }
        return get_html_soup(ZX_URL['login_url'], ZX_HEADERS['login'], login_params)

    def getVerifyQuestion(self):

        soup = get_html_soup(ZX_URL['get_verify_params_url'], ZX_HEADERS['get_verify_params'])
        params = {'authtype': "2", 'ApplicationOption': "21"}
        token = soup.find('input', {'name': 'org.apache.struts.taglib.html.TOKEN'}).get('value')
        params.update({"org.apache.struts.taglib.html.TOKEN": token})
        soup = get_html_soup(ZX_URL['get_verify_question_url'], ZX_HEADERS['get_verify_question'], params)
        return parser(soup, GET_QUESTION)

    def verifyByQuestion(self, **options):

        get_html_soup(ZX_URL['verify_by_question_url'], ZX_HEADERS['verify_by_question'], options)


class Register(object):
    """
    注册新用户
    输入用户名后验证是否已经存在问题
    """
    def __init__(self):
        # auth relation params
        self.name = ''
        self.method_auth = ''
        self.cert_type = ''
        self.cert_num = ''
        self.img_code = ''
        self.img_path = ''

        # register account params
        self.user_name = ''
        self.pass_word = ''
        self.confirm_pw = ''
        self.email = ''
        self.telephone = ''
        self.tel_code = ''
        self.token = ''
        self.count = ''
        self.mehtod_register = ''
        self.tc_id = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def getAuthInfo(self):

        params = {}
        urllib2.urlopen(ZX_URL['init_url'])
        soup = get_html_soup(ZX_URL['auth_user_url'], ZX_HEADERS['auth_user'])
        img_path = save_img(ZX_URL['init_url'], ZX_HEADERS['get_params'], soup)
        token = soup.find('input', {'name': 'org.apache.struts.taglib.html.TOKEN'}).get('value')
        params.update({'org.apache.struts.taglib.html.TOKEN': token, 'img_path': img_path})
        return params

    def setAuthInfo(self, **kw):
        self.name = kw['name']
        self.method_auth = kw['method']
        self.cert_type = kw['cert_type']
        self.cert_num = kw['cert_num']
        self.img_code = kw['img_code']
        self.img_path = kw['img_path']

    def authUser(self):
        """
        TODO 判断用户是否已经注册， 或者信息不存在

        :return:
        """
        soup = get_html_soup(ZX_URL['get_register_params_url'], ZX_HEADERS['get_register_params'], kw)
        print parser(soup, GET_USERINFO)

    def setRegisterInfo(self, **kw):

        self.user_name = kw['userInfoVO.loginName']
        self.pass_word = kw['userInfoVO.password']
        self.confirm_pw = kw['userInfoVO.confirmpassword']
        self.email = kw['userInfoVO.email']
        self.telephone = kw['userInfoVO.mobileTel']
        self.token = kw['org.apache.struts.taglib.html.TOKEN']
        self.mehtod_register = kw['method']

    def getTelCode(self):
        params = {'method': "getAcvitaveCode", 'mobileTel': self.telephone}
        self.tc_id = get_html_soup(ZX_URL['get_register_params_url'], ZX_HEADERS['get_register_tel_code'], params)

    def getAccount(self):

        register_params = {
            'tcId': self.tc_id,
            'userInfoVO.loginName': self.user_name,
            'userInfoVO.password': self.pass_word,
            'userInfoVO.confirmpassword': self.confirm_pw,
            'userInfoVO.email': self.email,
            'userInfoVO.mobileTel': self.telephone,
            'userInfoVO.verifyCode': self.tel_code,
            'counttime': self.count and self.count or '1',
            'org.apache.struts.taglib.html.TOKEN': self.token

        }

        soup = get_html_soup(ZX_URL['get_register_params_url'], ZX_HEADERS['get_register_tel_code'], register_params)
        print soup
