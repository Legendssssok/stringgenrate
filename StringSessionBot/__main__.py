import asyncio

from StringSessionBot.core.clients import Start_Bot
from StringSessionBot.core.logger import LOGS

loop = asyncio.get_event_loop()


if __name__ == "__main__":
    loop.run_until_complete(Start_Bot())
    LOGS.info(" Good Bye ! ")
