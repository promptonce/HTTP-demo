import requests  # 导入 requests 库

# 定义目标 URL
url = "https://server.itopmap.com/api/extract-targets"

# 发送 GET 请求
response = requests.get(url)

# 打印状态码（比如 200 表示成功）
print("状态码:", response.status_code)

# 打印响应头信息（服务器返回的一些元数据）
print("响应头:", response.headers)

# 打印响应内容（通常是 JSON 或 HTML）
print("响应内容:", response.text)

# 如果返回的是 JSON 格式，可以用 .json() 方法转换为字典
try:
    data = response.json()
    print("解析后的 JSON 数据:", data)
except ValueError:
    print("响应内容不是 JSON 格式")