import requests
import json
import hashlib


def getToken(username,password):
  url = "http://yiqing.minzheng.net:8110/nCoV/user/login?cuUserName="+username+"&cuPassWord="+hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
  payload = {}
  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'DNT': '1',
    'Origin': 'http://yiqing.minzheng.net:8080',
    'Referer': 'http://yiqing.minzheng.net:8080/nCov/pages/login-page/login-page.html',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
  }
  
  return json.loads(requests.request("GET", url, headers=headers, data = payload).text.encode('utf8'))


def execPunch(res):
  url = "http://yiqing.minzheng.net:8110/nCoV/temperature/add"

  payload = "{\"ceNo\":\""+res.get('userId')+"\",\"cetDate\":\"20200626\",\"cetTemperature\":\"36.5\"}"
  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'token': res.get("token"),
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'http://yiqing.minzheng.net:8080',
    'Referer': 'http://yiqing.minzheng.net:8080/nCov/pages/body-temp-report/body-temp-report.html',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=928010709.1547182'
  }

  code=json.loads(requests.request("POST", url, headers=headers, data = payload).text).get('code')
  return code==0




print(execPunch(getToken('BT7604','BT7604')))
