from aiogram import Dispatcher, types
from Main.create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_kb_start = InlineKeyboardMarkup(row_width=2)
inline_btn1 = InlineKeyboardButton('Тайна', callback_data='btn_usl')
inline_btn2 = InlineKeyboardButton('Секрет', callback_data='btn_struct')
inline_btn_location = InlineKeyboardButton('Местоположение', callback_data='btn_struct', request_location=True)
inline_kb_start.add(inline_btn1, inline_btn2, inline_btn_location)

keyboard = types.ReplyKeyboardMarkup()
button = types.KeyboardButton("Поделиться геолокацией и оставить предзказ", request_location=True)
keyboard.add(button)

from Main import db


@dp.message_handler(commands=['start'])
async def start_greetings(message: types.Message):
    uid = message.from_user.id

    if not db.check_user(uid):
        await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать, это бетаверсия нашего будущего'
                                                                  ' сервиса в котором вы можете заказать снимок себя '
                                                                  'из космоса, пока что вы можете оставить предзаказ',
                               reply_markup=keyboard, parse_mode="HTML")

        db.add_user(uid)
    else:
        await bot.send_message(chat_id=message.from_user.id, text='С возращением вас, вы уже оставили предзаказ, как только появиться новая информация мы вас тут же оповестим',
                               reply_markup=keyboard, parse_mode="HTML")

    print(message)
    await bot.send_message(chat_id=message.from_user.id, text='Hello, world!',
                             reply_markup=keyboard, parse_mode="HTML")


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    uid = message.from_user.id
    lat = message.location.latitude
    lon = message.location.longitude
    db.add_user_presale(uid, lat, lon)
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_greetings, commands=['start'])
    dp.register_message_handler(handle_location, content_types=['location'])