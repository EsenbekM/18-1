from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [5367214519, ]
URL = "https://python18-1.herokuapp.com/"
URI = "postgres://grpmuwncfntulp:6f402700286241042361d7b3d8bf70669acbba0df74474be943a75662ee6c04d@ec2-54-246-185-161.eu-west-1.compute.amazonaws.com:5432/d4kh44f4v8gkgl"
