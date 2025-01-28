import requests

cookies = {
# Your cookies
}

params = {
# Your params
}
while True:
    resp = requests.get(
    'https://szsupport.weixin.qq.com/cgi-bin/mmcover-bin/checkreceiveuri',
    params=params,
    cookies=cookies,
    )
    print(resp.text)

