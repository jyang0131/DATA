from typing import final

import requests
from moviepy.editor import VideoFileClip, AudioFileClip

#从moviepy 导入all功能

url='https://upos-hz-mirrorakam.akamaized.net/upgcxcode/19/25/124672519/124672519-1-30011.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1734788977&gen=playurlv2&os=akam&oi=3024806792&trid=f205ff78304e441ea2b3cd404c680e7au&mid=3546811037911781&platform=pc&og=cos&upsig=ff43ec3941959d041a7865631f89a1e1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&hdnts=exp=1734788977~hmac=74bb5f9d48685eceff4fbaa969b495bf4e3fa783bbc5a316fae634e7eb9d82b8&bvc=vod&nettype=0&orderid=0,2&buvid=838E1C93-F019-CE4D-72B0-B07D6A784AF255083infoc&build=0&f=u_0_0&agrr=0&bw=29812&logo=80000000'
# 伪装爬虫 应付网站检查  user agent :浏览器标识 //用户标识（cookie） // referer // host
dic = {
    "user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
#获取数据 resp 是全部东西  如果resp.content 要的是resp 里面的content

resp = requests.get(url, headers=dic)

#打开一个文件
#wb 是什么 wb 是打开的目的 告诉电脑想干什么 write-binary 二进制文件
file=open('面具人舞蹈.mp4', 'wb') #打开一个文件
file.write(resp.content) #写如获取到的二进制内容

#======================================================================
#获取音频 mp3 因为视频没有音乐
url='https://upos-hz-mirrorakam.akamaized.net/upgcxcode/19/25/124672519/124672519-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1734788977&gen=playurlv2&os=akam&oi=3024806792&trid=f205ff78304e441ea2b3cd404c680e7au&mid=3546811037911781&platform=pc&og=hw&upsig=7b68efdbe8e16e1aac031f8745ad5760&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&hdnts=exp=1734788977~hmac=1db24d1e2ccb58b16d96bf569e4b55873c932c67cd1a8be45b8652ce4582831e&bvc=vod&nettype=0&orderid=0,2&buvid=838E1C93-F019-CE4D-72B0-B07D6A784AF255083infoc&build=0&f=u_0_0&agrr=0&bw=8399&logo=80000000'

dic = {
    "user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
resp = requests.get(url, headers=dic)
open('面具人舞蹈.mp3', 'wb').write(resp.content)
