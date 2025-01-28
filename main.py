# -*- coding: utf-8 -*-
# @Time    : 2025/1/28 15:53
# @Author  : 之落花--falling_flowers
# @File    : main.py
# @Software: PyCharm
import asyncio
from datetime import *

from red_packet import RedPacket

headers = {
    # your headers
}

cookies = {
    # your cookies
}

feSessionid = ""  # your feSessionid

start = datetime.now()  # start time
duration = timedelta(seconds=3)  # duration


def main():
    asyncio.run(
        RedPacket(cookies, feSessionid, headers).start(1, start, duration)
    )


if __name__ == '__main__':
    main()
