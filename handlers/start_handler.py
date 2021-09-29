from aiogram.dispatcher.filters import CommandStart

import const
import filters
from database import commands
from init import dp
from aiogram import types

from keyboards.filters_keyboards import get_filters_keyboard, get_set_filters_keyboard
from states.states import States


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    const.START = True
    id_user = message.from_user.id
    username = message.from_user.username
    await commands.add_user(id_user, username)
    await States.Filters.set_filters.set()
    await message.answer("Бот запущен", reply_markup=get_set_filters_keyboard(const.START))


@dp.message_handler(text="Изменить фильтры", state=States.Filters.set_filters)
async def spam_subscription(message: types.Message):
    const.PAUSE = True
    await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    await message.delete()



@dp.message_handler(text="Приостановить", state=States.Filters.set_filters)
async def spam_subscription(message: types.Message):
    const.START = False
    await message.answer("Бот приостановлен", reply_markup=get_set_filters_keyboard(const.START))
    await message.delete()


@dp.message_handler(text="Возобновить", state=States.Filters.set_filters)
async def spam_subscription(message: types.Message):
    const.START = True
    await message.answer("Бот запущен", reply_markup=get_set_filters_keyboard(const.START))
    await message.delete()


@dp.callback_query_handler(text="save_filters", state=States.Filters.set_filters)
async def category(call: types.CallbackQuery):
    await call.message.delete()
    const.PAUSE = False