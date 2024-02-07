import logging

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    handlers=[logging.FileHandler("legend.log"), logging.StreamHandler()],
    level=logging.INFO,
    datefmt="%H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("oldpyro").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)

LOGS = logging.getLogger("StringBot")
