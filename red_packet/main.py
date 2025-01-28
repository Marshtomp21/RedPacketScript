import asyncio
from datetime import *

import aiohttp


class RedPacket:
    def __init__(self, cookies: dict, fsessionid: str, headers=None):
        if headers is None:
            headers = {}
        self.__cookies = cookies
        self.__params = cookies.copy()
        self.__params["feSessionid"] = fsessionid
        self.__headers = headers

        self.__url = "https://szsupport.weixin.qq.com/cgi-bin/mmcover-bin/checkreceiveuri"

    async def __grab(self, start, duration):
        while datetime.now() < start:
            await asyncio.sleep(0.1)
        while datetime.now() < start + duration:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        url=self.__url,
                        cookies=self.__cookies,
                        params=self.__params,
                        headers=self.__headers
                ) as resp:
                    print(await resp.text())

    async def start(self, num: int = 1, start=datetime.now(), duration=timedelta.max):
        """
        Start grabbing red packets.
        :param num: the number of async tasks
        :param start: the start time to grab red packets
        :param duration: the duration to grab red packets
        :return:
        """
        tasks = [self.__grab(start, duration) for _ in range(num)]
        await asyncio.gather(*tasks)
