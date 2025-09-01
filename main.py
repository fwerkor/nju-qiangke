import requests
import time
import json

def send_post_request(url, headers, data, max_retries=10):
    print("开始发包！")
    retries = 0
    while max_retries is None or retries <= max_retries:
        try:
            response = requests.post(url, headers=headers, data=data)
            
            # 检查状态码是否为200
            if response.status_code == 200:
                # 尝试解析JSON响应
                try:
                    response_json = response.json()
                    # 检查JSON中是否包含"已满"关键字
                    if "已满" in json.dumps(response_json, ensure_ascii=False):
                        time.sleep(duration)
                        print(".", end="")
                        continue
                    else:
                        print("成功！")
                        return response_json
                except json.JSONDecodeError:
                    print("响应不是有效的JSON格式")
                    retries += 1
                    return None
            else:
                print(f"状态码异常: {response.status_code}，10秒后重试...")
                time.sleep(10)
                retries += 1
                
        except requests.exceptions.RequestException as e:
            print(f"请求异常: {e}，10秒后重试...")
            time.sleep(10)
            retries += 1
    
    print("达到最大重试次数，请求失败")
    return None

# 用户输入
token = input("请输入token: ")
cookie = input("请输入cookie: ")
student_code = input("请输入studentCode: ")
add_param = input("请输入addParam: ")
duration = int(input("请输入发包延时（单位：秒）: "))

if duration<=2:
    print("发包延时不得低于2秒！已修改为2")
    duration = 2                               #做个人吧，别删掉这段代码

# 构建请求URL
url = "https://xk.nju.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do"

# 构建请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": cookie,
    "Host": "xk.nju.edu.cn",
    "Origin": "https://xk.nju.edu.cn",
    "Referer": f"https://xk.nju.edu.cn/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={token}",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "language": "zh_cn",
    "sec-ch-ua": '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "token": token
}

# 构建请求体
data = {
    "addParam": add_param,
    "studentCode": student_code
}

# 发送请求
result = send_post_request(url, headers, data)

print("")

# 处理结果
if result:
    print("最终响应结果:", json.dumps(result, ensure_ascii=False, indent=2))
