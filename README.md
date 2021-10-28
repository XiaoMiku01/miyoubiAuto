# miyoubiAuto 
米游社每日米游币自动化Python脚本(务必使用Python3)  
10.8更新：更换cookie的获取地址
## 注意：禁止在B站、贴吧、或各大论坛大肆传播！
#### 小引一波 
推荐关注几个非常可爱有趣的女孩！ 
欢迎B站搜索:  
[@嘉然今天吃什么](https://space.bilibili.com/672328094/)&emsp;[@向晚大魔王](https://space.bilibili.com/672346917/)&emsp;&emsp;[@乃琳Queen](https://space.bilibili.com/672342685/)&emsp;&emsp;&emsp;[@贝拉kira](https://space.bilibili.com/672353429/)&emsp;&emsp;&emsp;[@珈乐Carol](https://space.bilibili.com/351609538/)</br>
<img src="https://i2.hdslb.com/bfs/face/d399d6f5cf7943a996ae96999ba3e6ae2a2988de.jpg@128w_128h_1o.webp" /><img src="https://i0.hdslb.com/bfs/face/566078c52b408571d8ae5e3bcdf57b2283024c27.jpg@128w_128h_1o.webp" /><img src="https://i1.hdslb.com/bfs/face/8895c87082beba1355ea4bc7f91f2786ef49e354.jpg@128w_128h_1o.webp" /><img src="https://i2.hdslb.com/bfs/face/668af440f8a8065743d3fa79cfa8f017905d0065.jpg@128w_128h_1o.webp" /><img src="https://i1.hdslb.com/bfs/face/a7fea00016a8d3ffb015b6ed8647cc3ed89cbc63.jpg@128w_128h_1o.webp" />
### 第三方库

```shell
pip install requests
或
pip3 install requests
```
### 食用方法
 1.下载源码  
 2.在Global.py中设置米游社Cookie  
 3.运行myb.py  
 本地第一次运行时会自动生产一个文件储存cookie，请勿删除
 ```shell
 python3 myb.py
 或
 python myb.py
 ```
#### 当前仅支持单个账号！  

###  获取Cookie方法


1. 浏览器**无痕模式**打开 [http://user.mihoyo.com/](http://user.mihoyo.com/) ，登录账号
2. 按`F12`，打开`开发者工具`，找到并点击`Network`
3. 按`F5`刷新页面，按下图复制 Cookie：

![How to get mys cookie](http://i0.hdslb.com/bfs/album/95cbe5bc1886df3886045c92f5a3583ab733d8ab.png)

当触发`Debugger`时，可尝试按`Ctrl + F8`关闭，然后再次刷新页面，最后复制 Cookie。也可以使用另一种方法：

1. 复制代码 `var cookie=document.cookie;var ask=confirm('Cookie:'+cookie+'\n\nDo you want to copy the cookie to the clipboard?');if(ask==true){copy(cookie);msg=cookie}else{msg='Cancel'}`
2. 浏览器**无痕模式**打开 [http://user.mihoyo.com/](http://user.mihoyo.com/) ，登录账号
3. 按`F12`，打开`开发者工具`，找到并点击`Console`
4. 控制台粘贴代码并运行，获得类似`Cookie:xxxxxx`的输出信息
5. `xxxxxx`部分即为所需复制的 Cookie，点击确定复制

### 部署方法--腾讯云函数版（推荐！）

1. 下载项目源码和[压缩包](https://github.com/XiaoMiku01/miyoubiAuto/releases/tag/1.1)

2. 进入项目文件夹打开命令行执行以下命令
   ```shell
   python index.py "xxxxxxx"
   或
   python3 index.py "xxxxxxx"
   ```
   xxxxxxx为通过上面方式或取得米游社cookie  
   一定要用**双引号**包裹!!  
   例如:
   ![1.png](https://i.loli.net/2021/05/05/uEw7CYA4SZv3Tks.png)
3. 复制返回内容(包括括号)  
例如:
![QQ截图20210505031552.png](https://i.loli.net/2021/05/05/r6yiA4QwZSRcXOg.png)  
4. 登录[腾讯云函数官网](https://cloud.tencent.com/product/scf)  
5. 选择函数服务-新建-自定义创建
6. 函数名称随意-地区随意-运行环境Python3.6
7. 提交方法:上次本地zip包-执行方法不要改-函数代码上传刚刚下载的压缩包
8. 高级配置-环境配置-执行超时时间300秒
9. 环境变量key填**mysCookie**(注意大小写),value填刚刚第3步复制的内容(注意括号也要复制)
      ![QQ截图20210505033548.png](https://i.loli.net/2021/05/05/HjrMEuYvqCVxgJb.png)
10. 触发器配置-自己定义时间([Cron表达式文档](https://cloud.tencent.com/document/product/583/9708#cron-.E8.A1.A8.E8.BE.BE.E5.BC.8F))
11. 完成-立即转跳-函数管理-函数代码
12. 点击部署-部署成功后点击测试-耐心等待返回结果-观看返回日志是否成功(中文可能出现编码问题，不过无伤大雅)
  ![___C9_@CUSV_3`82A95I9PV.png](https://i.loli.net/2021/05/05/vHtBGqXRLfQ2r6o.png)
    ![QQ截图20210505034758.png](https://i.loli.net/2021/05/05/xbKjnrm5g2qJEMN.png)


### 部署方法-docker运行
1. 下载源码
2. 
```shell
docker build -t miyoubi-auto <源码的路径>
docker run -it -d --name miyoubi-auto -e MYS_COOKIE="填米游社Cookie" miyoubi-auto
docker logs -f miyoubi-auto
```
