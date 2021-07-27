from aiogram import types

import const
import filters
from init import dp
from keyboards.filters_keyboards import get_filters_keyboard
from states.states import States
from utils import try_parse_int

state = States.Filters.set_filters


@dp.callback_query_handler(text="time_2_from", state=state)
async def time_2_from(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("От:")
    await call.message.delete()
    await States.Filters.time_2_from.set()


@dp.callback_query_handler(text="time_2_to", state=state)
async def time_2_to(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("До:")
    await call.message.delete()
    await States.Filters.time_2_to.set()


@dp.message_handler(state=States.Filters.time_2_from)
async def time_2_from(message: types.Message):
    value = message.text
    if try_parse_int(value) and int(value) >= const.TIME2['min'] and int(value) < filters.time_2['to']:
        filters.time_2['from'] = int(value)
        await message.delete()
        await States.Filters.set_filters.set()
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    else:
        await message.answer(f"Значение должно быть >= {const.TIME2['min']} и < {filters.time_2['to']}")

@dp.message_handler(state=States.Filters.time_2_to)
async def time_2_to(message: types.Message):
    value = message.text
    if try_parse_int(value) and int(value) > filters.time_2['from']  and int(value) <= const.TIME2['max']:
        filters.time_2['to'] = int(value)
        await message.delete()
        await States.Filters.set_filters.set()
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    else:
        await message.answer(f"Значение должно быть > {filters.time_2['from'] } и <= {const.TIME2['max']}")