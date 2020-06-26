# import rsaEncrypt
import sys
import rsaEncrypt
import requests
import json


def getToken(username, password, publickey):
    encryptedPass = rsaEncrypt.encrypt(password, publickey)
    url = "https://asst.cetccloud.com/ncov/login"
    payload = "------WebKitFormBoundaryZmQBeyzFucxQ0qjs\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n"+username+"\r\n------WebKitFormBoundaryZmQBeyzFucxQ0qjs\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n" + \
        encryptedPass+"\r\n------WebKitFormBoundaryZmQBeyzFucxQ0qjs\r\nContent-Disposition: form-data; name=\"client\"\r\n\r\nh5\r\n------WebKitFormBoundaryZmQBeyzFucxQ0qjs--"
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'requestType': 'zuul',
        'accessToken': 'null',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'applyID': 'df626fdc9ad84d3a95633c10124df358',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryZmQBeyzFucxQ0qjs',
        'Accept': 'application/json',
        'secretKey': 'D8FE427008F065C1B781917E82E1EC1E',
        'Origin': 'https://asst.cetccloud.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://asst.cetccloud.com/',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cookie': 'SESSION=YTQyZjFiYjQtMDA0My00NjYwLTllMzUtM2IzN2I2YjFhZGM3; OUTFOX_SEARCH_USER_ID_NCOO=1812329457.9782567; ___rl__test__cookies=1593173411102'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text.encode('utf8')).get('data').get('userInfo')


def execPunch(res):
    url = "https://asst.cetccloud.com/oort/oortcloud-2019-ncov-report/2019-nCov/report/edit_everyday_report"
    payload = "{\"phone\":\""+res.get('oort_phone')+"\",\"Traffic_data\":{\"bike\":0,\"bike_way\":\"\",\"bus\":0,\"bus_number\":\"\",\"car\":0,\"car_way\":\"\",\"metro\":0,\"metro_number\":\"\",\"other\":0,\"other_way\":\"\",\"walk\":0,\"walk_way\":\"\",\"phone\":\""+res.get('oort_phone')+"\"},\"physical_data\":{\"type1\":0,\"type1_state\":\"0\",\"type2\":0,\"type3\":0,\"type4\":0,\"type5\":0,\"type6\":0,\"type7\":0,\"type7_state\":\"\",\"phone\":\""+res.get('oort_phone')+"\"},\"track_data\":{\"tracks\":\"[]\",\"phone\":\""+res.get('oort_phone')+"\"},\"work_way\":0,\"touch\":0,\"accessToken\":\""+res.get("accessToken")+"\",\"uid\":\""+res.get("oort_uuid")+"\"}"
    headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'requestType': 'zuul',
    'accessToken': res.get("accessToken"),
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'applyID': 'df626fdc9ad84d3a95633c10124df358',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'secretKey': 'D8FE427008F065C1B781917E82E1EC1E',
    'Origin': 'https://asst.cetccloud.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://asst.cetccloud.com/',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1812329457.9782567; ___rl__test__cookies=1593173411102'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    return json.loads(response.text)

key="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgZmNj7QvhbpgdqxN7ZCR+r874KZb/qRvlHRieJJREH+i5/hPbpPH5KheEFxoo7nyAkPIcQYPshHvC4UJBe1HrHjdhjFnMA967aebBtioXBOB0qR4ql0DtWA0PrJWtDABeTpPXedqmzMcYIxr1Wq/viIPsjCHRiyRx6mhYqT5P6wIDAQAB"
print(execPunch(getToken('18580935926','991458902', key)))
 