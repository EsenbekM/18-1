from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello my master {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Чему равно число пи?'
    answers = [
        '3.15', '4.35', '3.14', '3.13'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'By whom invented Python?'
    answers = [
        "Harry Potter",
        "Putin",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
        "Guido Van Rossum",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    question = 'ОТВЕЧАЙ!!!!'
    answers = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]
    photo = open('media/problem1.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
