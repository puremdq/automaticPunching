from cv2 import cv2
import json
import requests
import time


# 获取图片
def readImg(url, name):
    # 把下载地址发送给requests模块
    f = requests.get(url)
    # 下载文件
    with open(name, "wb") as code:
        code.write(f.content)
    return name


# 查找一个图片再另一个图片的位置
def FindPic(target, template):
    target_rgb = cv2.imread(target)
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread(template, 0)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    return value[2]
    # return value[3]


# 获取验证码Id
def getSlideid():
    url = "https://asst.cetccloud.com/oort/oortcloud-sso/sso/v1/getCaptcha"

    payload = "{\"model\":\"login\"}"
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'requestType': 'zuul',
        'accessToken': 'null',
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
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1812329457.9782567; ___rl__test__cookies=1596887438136'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text.encode('utf8')).get('data').get('slideID')


def getPicXpos(slideid):
    timestamp = str(int(round(time.time() * 1000)))
    point = FindPic(readImg("https://asst.cetccloud.com/oort/oortcloud-sso/slide/v1/"+slideid+"/big.png?"+timestamp, "big.png"),
                    readImg("https://asst.cetccloud.com/oort/oortcloud-sso/slide/v1/"+slideid+"/slice.png?"+timestamp, "slice.png"))
    return point[0]


def slideverify(slideid, xpos):
    url = "https://asst.cetccloud.com/oort/oortcloud-sso/sso/v1/slideverify"
    payload = "{\"slideid\":\""+slideid+"\",\"xpos\":"+xpos+"}"
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'requestType': 'zuul',
        'accessToken': 'null',
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
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1812329457.9782567; ___rl__test__cookies=1596887578384'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def execSlideverify():
    slideid = getSlideid()
    xpos = getPicXpos(slideid)
    slideverify(slideid, str(xpos))

# execSlideverify()
