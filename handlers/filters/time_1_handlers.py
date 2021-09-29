from aiogram import types

import const
import filters
from init import dp
from keyboards.filters_keyboards import get_filters_keyboard
from states.states import States
from utils import try_parse_int

state = States.Filters.set_filters


@dp.callback_query_handler(text="time_1_from", state=state)
async def time_1_from(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("мин I От:")
    await States.Filters.time_1_from.set()


@dp.callback_query_handler(text="time_1_to", state=state)
async def time_1_to(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("мин I До:")
    await States.Filters.time_1_to.set()


@dp.message_handler(state=States.Filters.time_1_from)
async def time_1_from(message: types.Message):
    value = message.text
    if try_parse_int(value) and const.TIME1['min'] <= int(value) <= filters.time_1['to']:
        filters.time_1['from'] = int(value)
        await States.Filters.set_filters.set()
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    else:
        await message.answer(f"Значение должно быть >= {const.TIME1['min']} и <= {filters.time_1['to']}")


@dp.message_handler(state=States.Filters.time_1_to)
async def time_1_to(message: types.Message):
    value = message.text
    if try_parse_int(value) and filters.time_1['from'] <= int(value) <= const.TIME1['max']:
        filters.time_1['to'] = int(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {filters.time_1['from']} и <= {const.TIME1['max']}")
