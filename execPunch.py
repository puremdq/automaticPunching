import healthPunch.autoPunch as autoPunch
import asst.asstPunch as asstPunch
import time
import sys
key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgZmNj7QvhbpgdqxN7ZCR+r874KZb/qRvlHRieJJREH+i5/hPbpPH5KheEFxoo7nyAkPIcQYPshHvC4UJBe1HrHjdhjFnMA967aebBtioXBOB0qR4ql0DtWA0PrJWtDABeTpPXedqmzMcYIxr1Wq/viIPsjCHRiyRx6mhYqT5P6wIDAQAB"


def start(account):
    account = account.split(" ")
    if '2'.endswith(account[2]):
        print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) +
              " 执行用户:" + account[0]+" 小帮手打卡 "+str(asstPunch.startPunch(account[0], account[1], key)))
        print("")
    if '1'.endswith(account[2]):
        print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) +
              " 执行用户:" + account[0] + " 健康打卡 "+str(autoPunch.startPunch(account[0], account[1])))
        print("")


def startFromFile(filename):
    accounts = open(filename, 'r', encoding='utf-8').read().split('\n')
    for account in accounts:
        if account.startswith('#') or len(account) < 1:
            continue
        start(account)


startFromFile(sys.path[0] + '/accounts')
