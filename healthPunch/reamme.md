# 用Python实现自动打卡，妈妈再也不用担心我缺卡了
疫情期间公司需要每日上报健康状况，如果到了固定时间点没打卡就会在群里公开处刑，作为一个安静的程序员这点面子挂不住啊，奈何我有老是忘记打卡，于是我就有了做一个自动打卡的脚本来帮助我每日自动打卡想法。

## part1.语言选择
***为什么是python？***
刚开始的想法是用shell脚本，但是我通过抓包发现自动打卡的逻辑较为复杂，需要先获取token公钥子类的东西，然后再把密码加密后提交，用shell估计不好实现，后来打算用java 但是考虑到java部署过程比较麻烦，可能还要应用很多第三方jar包最终的文件就会比较大，再加上python本身校本化的特点，类库多部署方便于是我就选择了它。

## part2. 抓包分析
打卡系统有两套，一套叫健康打卡上报每日体温，一套是小帮手上报每日身体状况。

### 2.1 健康打卡

####2.1.1获取登录接口

![登录接口网络请求](https://upload-images.jianshu.io/upload_images/5131093-cbf1d4d214786688.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
通过分析这个请求我得知他就是把密码做了一个md5加密这个比较好实现。

####2.1.2先通过postman模拟这个请求
chrome浏览器有一个很好用的功能**copy as curl** 先把这个请求copy成curl命令的形式 然后通过postman的import导入就可以直接把这个请求导入postman了

**1.copy as curl**
![copy as curl](https://upload-images.jianshu.io/upload_images/5131093-07576a89d152cb1c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**2.把curl命令导入到postman**
![把curl命令导入到postman](https://upload-images.jianshu.io/upload_images/5131093-495445f1194ac038.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**3.转化登录请求为python代码**
现在这个请求已经在我的postman里面了我如何把它转化为python代码呢
不得不说postman很强大，人家已经为你想好了，按照如下操作就可以轻松实现

![转化登录请求为python代码](https://upload-images.jianshu.io/upload_images/5131093-66ff1a4134a8d8f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


####2.1.2获取打卡接口

在健康打卡页面点击打卡然后提交然后看网络请求
![提交健康打卡](https://upload-images.jianshu.io/upload_images/5131093-7a90a1089eb6a176.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![健康打卡提交](https://upload-images.jianshu.io/upload_images/5131093-581be985da5d0c6f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
可以看到在header里面有一个token这个token就是上一步登录接口返回的
我们还是按照上一步中的方法先把这个请求导入到postman然后通过postman把他转化为python代码

###2.2 小帮手抓包分析
小帮手抓包分析的过程和健康打卡的大体一致不过小帮手的密码加密更加复杂一些，我分析这个分析了很久

**小帮手登录的网络请求**
![image.png](https://upload-images.jianshu.io/upload_images/5131093-b96f4d876c264ed3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
可以看到登录后的密码是很长一串乱码很明显是被加密了的，我得拿到他的加密算法但是他整个项目是通过vue写的然后部署过后全是编译混淆以后的代码很不好排查。但是这也难不倒我我把他用到的js全部下载下来，虽然全是混淆后的代码但是也可以格式化以后一行一行慢慢看

![下载的编译后的js文件](https://upload-images.jianshu.io/upload_images/5131093-70330856cfcba78d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通过全局查找password关键字发现了一个getsign方法让我眼前一亮我仔细研究发现他就是通过的JSEncrypt进行的加密并且公钥写死在代码中，那这就简单多了。
![关键代码](https://upload-images.jianshu.io/upload_images/5131093-a1fdb3080fa870f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## part3. 代码书写

有了前面的准备工作 就开始写代码了，代码相对来说比较简单，毕竟postman可以直接把请求生成代码，我要做的只是把它整合起来，先获取token然后在打卡的时候把token换成刚获取的
![代码概览](https://upload-images.jianshu.io/upload_images/5131093-97988b215f769fe1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

值得一提的是考虑到可能有多个人的情况，我把账户单独拿出来放到配置文件这样如果需要添加一个用户来打卡只需要添加一行配置文件就可以了
![账户配置文件](https://upload-images.jianshu.io/upload_images/5131093-cf3beffb91f6b7c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

关于详细的代码有兴趣的可以访问[https://github.com/puremdq/automaticPunching](https://github.com/puremdq/automaticPunching)


## part4. 自动化打卡
直接把这段代码传到linux主机上然后把它加入到crontab任务中
以下是我加入crontab任务中的命令仅供参考
```shell
cd /root
mkdir crontab
crontab -l >/root/crontab/crontab.bak
echo "/srv/Python-3.6.4/bin/python3 /srv/workSpace/automaticPunching/tangyh/execPunch.py > /tmp/daka.txt" >> /root/crontab/crontab.bak
crontab /root/crontab/crontab.bak
```
## part5.总结
这个自动打卡的小demo就介绍完了，大家如果有需要可以到这个链接自取[https://github.com/puremdq/automaticPunching](https://github.com/puremdq/automaticPunching)
感谢各位耐心读完，要是给个关注就更好了
![扫我吧](https://upload-images.jianshu.io/upload_images/5131093-2bd0fe10e0ba7bc8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)














 



