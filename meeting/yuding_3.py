import threading
import requests
import os
from requests.exceptions import RequestException
from datetime import datetime
import time


# 定义目标HTTP接口的URL

def yuding():
    url = 'http://new-meeting.ke.com/api/creatCalendatEvent'
    # 定义请求头部，这里只是示例，你可以根据需要修改
    headers = {
        'pcpopclub': "f5eb24af05dd4f12a6fc010f5519172c",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Safari/537.36 Language/zh wxwork/4.1.10 (MicroMessenger/6.2) WindowsWechat  MailPlugin_Electron WeMail embeddisk',
        'Referer': 'http://new-meeting.ke.com/roomBoard',
        'Origin': 'http://new-meeting.ke.com',
        'Host': 'new-meeting.ke.com',
        'Content-Type': 'application/json',
        'Cookie': "lianjia_uuid=da07e1bd-d3db-41c9-b0e9-342aa63426c8; wx_device_id=KVHV-rO1gyR3WRvL3CPI9DbCk4SXnZsAVVhUf53Kwzs=; fast_wechat_token=2.0012b837b4873156e50311890607f9972c; fast_wechat_token_corpid=ww85a00b875a33e60b; session_id=12187ef4-761a-37d6-aa0a-b42a9ad4cf73; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22191737681ca398-0b2ff926ae90de-b024828-1024000-191737681cb13a4%22%2C%22%24device_id%22%3A%22191737681ca398-0b2ff926ae90de-b024828-1024000-191737681cb13a4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; c3po_ke_com=2.00131f51ac869630fd02b6ef1e2269f0fa; c3po_ke_com_corpid=ww85a00b875a33e60b; vision-1.3.18-lang=zh-chs; Hm_lvt_0339fbce6f875abd4da9b4448a636ac4=1724034727,1724035359,1724119462,1724222808; HMACCOUNT=E4C2B5782254CBB4; vision-1.3.18-token=f5eb24af05dd4f12a6fc010f5519172c; lianjia_token=2.0012018ed58788ef8403a830675a81c835; lianjia_token_corpid=ww85a00b875a33e60b; lianjia_ssid=b1ae4bca-f169-4e40-b616-b3f9e2febece; Hm_lpvt_0339fbce6f875abd4da9b4448a636ac4=1724291478"
        # 添加其他需要的头部...
    }

    # 定义要发送的请求体，这里只是示例，你可以根据需要修改
    # 丽江：941  海南岛：2090  东极岛：2091 钓鱼岛：2099 台湾岛：2092
    chengdu = [941, 2090, 2091, 2099, 2092]
    # 甜水园：258 鸟巢： 259 水立方：260  五根松：15979  颐和园：262   奥森：263  1402：264
    beijing = [262, 263, 15979, 260]
    # 会议室预定时间：北京提前4天，成都提前5天

    # 唐宇航：2486181 俊安：2483899
    userid = [2486181, 2483899]

    # 时间戳转换
    startTime = "2024-08-27 14:00:00"
    endTime = "2024-08-27 15:00:00"
    # 将日期时间转换回时间戳

    s_starttime = time.strptime(startTime, "%Y-%m-%d %H:%M:%S")  # 返回元祖
    startTime = int(time.mktime(s_starttime) * 1000)
    s_endtime = time.strptime(endTime, "%Y-%m-%d %H:%M:%S")  # 返回元祖
    endTime = int(time.mktime(s_endtime) * 1000)

    # 1724295600000
    # 1724295600

    for beijing in beijing:
        chengdu_payload = {
            "roomId": chengdu,
            "startTime": startTime,
            "endTime": endTime,
            "subject": "面试",
            "timeZone": "UTC+8",
            "addTcentMeet": 0,
            "userId": 2486181
        }
        beijing_payload = {
            "roomId": beijing,
            "startTime": startTime,
            "endTime": endTime,
            "subject": "周会",
            "timeZone": "UTC+8",
            "addTcentMeet": 0,
            "userId": 2486181
        }

        # 定义线程工作函数
        def worker():
            try:
                # 发送POST请求
                response = requests.post(url, json=beijing_payload, headers=headers)
                # 打印响应内容

                print("预定会议室%s,%s" % (beijing_payload, response.text))
            except RequestException as e:
                # 打印异常信息
                print(f'An error occurred: {e}')

        # 创建线程列表
        threads = []

        # 创建并启动5个线程
        for i in range(5):
            thread = threading.Thread(target=worker)
            threads.append(thread)
            thread.start()
        # 等待所有线程完成
        for thread in threads:
            thread.join()

        print('All threads finished execution.')
