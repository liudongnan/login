# coding: utf-8

ZX_HEADERS = {
     # login relation
     'img_code':
          {'Referer': 'https://ipcrs.pbccrc.org.cn'},
     'get_params':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/top1.do'},
     'login':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp'},

     # get verify relation
     'get_verify_params':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/menu.do'},
     'get_verify_question':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/reportAction.do?method=applicationReport'},
     'verify_by_question':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/reportAction.do?method=checkishasreport'},

     # register relation
     'auth_user':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/top1.do'},
     'get_register_params':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/userReg.do?method=initReg'},
     'get_register_tel_code':
          {'Referer': 'https://ipcrs.pbccrc.org.cn/userReg.do'}

             }



ZX_URL = {
     # login relation
     'init_url': "https://ipcrs.pbccrc.org.cn",
     'get_params_url': "https://ipcrs.pbccrc.org.cn/login.do?method=initLogin",
     'login_url': "https://ipcrs.pbccrc.org.cn/login.do",

     # get verify relation
     'get_verify_params_url': 'https://ipcrs.pbccrc.org.cn/reportAction.do?method=applicationReport',
     'get_verify_question_url': 'https://ipcrs.pbccrc.org.cn/reportAction.do?method=checkishasreport',
     'verify_by_question_url': 'https://ipcrs.pbccrc.org.cn//reportAction.do?method=submitKBA',

     # register relation
     'auth_user_url': 'https://ipcrs.pbccrc.org.cn/userReg.do?method=initReg',
     'get_register_params_url': 'https://ipcrs.pbccrc.org.cn/userReg.do'
     }

PARAMS_LIST = [
     'org.apache.struts.taglib.html.TOKEN',
     'method',



]

# 获取 登陆征信中心 的post params
GET_LOGIN_PARAMS = [
     'org.apache.struts.taglib.html.TOKEN',
     'date',
     'method'

]

# 获取 申请征信报告时 做验证的 问题
GET_QUESTION = [
     'org.apache.struts.taglib.html.TOKEN',
     'method',
     'authtype',
     'ApplicationOption',
     'kbaList[0].derivativecode',
     'kbaList[0].businesstype',
     'kbaList[0].questionno',
     'kbaList[0].kbanum',
     'kbaList[0].question',
     'kbaList[0].options1',
     'kbaList[0].options2',
     'kbaList[0].options3',
     'kbaList[0].options4',
     'kbaList[0].options5',
     'kbaList[0].answerresult',
     'kbaList[0].options',
     'kbaList[1].derivativecode',
     'kbaList[1].businesstype',
     'kbaList[1].questionno',
     'kbaList[1].kbanum',
     'kbaList[1].question',
     'kbaList[1].options1',
     'kbaList[1].options2',
     'kbaList[1].options3',
     'kbaList[1].options4',
     'kbaList[1].options5',
     'kbaList[1].answerresult',
     'kbaList[1].options',
     'kbaList[2].derivativecode',
     'kbaList[2].businesstype',
     'kbaList[2].questionno',
     'kbaList[2].kbanum',
     'kbaList[2].question',
     'kbaList[2].options1',
     'kbaList[2].options2',
     'kbaList[2].options3',
     'kbaList[2].options4',
     'kbaList[2].options5',
     'kbaList[2].answerresult',
     'kbaList[2].options',
     'kbaList[3].derivativecode',
     'kbaList[3].businesstype',
     'kbaList[3].questionno',
     'kbaList[3].kbanum',
     'kbaList[3].question',
     'kbaList[3].options1',
     'kbaList[3].options2',
     'kbaList[3].options3',
     'kbaList[3].options4',
     'kbaList[3].options5',
     'kbaList[3].answerresult',
     'kbaList[3].options',
     'kbaList[4].derivativecode',
     'kbaList[4].businesstype',
     'kbaList[4].questionno',
     'kbaList[4].kbanum',
     'kbaList[4].question',
     'kbaList[4].options1',
     'kbaList[4].options2',
     'kbaList[4].options3',
     'kbaList[4].options4',
     'kbaList[4].options5',
     'kbaList[4].answerresult',
     'kbaList[4].options'

]


# post_data = {
#             "counttime": counttime,
#             "userInfoVO.confirmpassword": password,
#             "userInfoVO.email": email,
#             "userInfoVO.loginName": loginname,
#             "userInfoVO.mobile_tel": tel,
#             "userInfoVO.password": password,
#             "userInfoVO.verifyCode": verify_code
#         }

GET_USERINFO = [
     'org.apache.struts.taglib.html.TOKEN',
     'method',
     'counttime',
     'userInfoVO.confirmpassword',
     'userInfoVO.email',
     'userInfoVO.loginName',
     'userInfoVO.mobileTel',
     'userInfoVO.password'
     ]