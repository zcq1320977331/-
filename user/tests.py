#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,requests

requests
# ----------------------------------
# 天气预报调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/73
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.根据城市查询天气
    request1(appkey, "GET")


# 根据城市查询天气
def request1(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/weather/query"
    params = {
        "cityname": "",  # 要查询的城市，如：温州、上海、北京
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


if __name__ == '__main__':
    main()