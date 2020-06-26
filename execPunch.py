import healthPunch.autoPunch as autoPunch
import asst.asstPunch as asstPunch
import time
 
key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgZmNj7QvhbpgdqxN7ZCR+r874KZb/qRvlHRieJJREH+i5/hPbpPH5KheEFxoo7nyAkPIcQYPshHvC4UJBe1HrHjdhjFnMA967aebBtioXBOB0qR4ql0DtWA0PrJWtDABeTpPXedqmzMcYIxr1Wq/viIPsjCHRiyRx6mhYqT5P6wIDAQAB"
print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+" 执行健康打卡 "+str(autoPunch.startPunch('BT7604', 'BT7604')))
print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+" 执行小帮手打卡 "+str(asstPunch.startPunch('18580935926', '991458902', key)))