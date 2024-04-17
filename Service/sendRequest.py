import requests


def send_request(baseUrl, method, path, request_json):
    # 设置请求头，指定内容类型为JSON

    headers = {'Content-Type': 'application/json'}
    if method == 'GET':
        response = requests.get(baseUrl + path, json=request_json, headers=headers)
    else:
        response = requests.post(baseUrl + path, json=request_json, headers=headers)

    if response.status_code != 200:
        # 如果请求失败，打印错误信息
        print(f"请求失败: {response.status_code}")
        return None
    # 检查请求是否成功
    else:
        # 处理响应
        return response.json()

# 请求数据
# request_json = {
#     "device_name": "string",
#     "another_info": "string",
#     "address_mac": "string",
#     "address_ip": "string"
# }
#
# # 发送请求并打印响应
# print(send_request('http://127.0.0.1:8080', '/device/report', request_json))
