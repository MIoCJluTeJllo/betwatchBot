from aiogram import types

import const
import filters
from init import dp
from keyboards.filters_keyboards import get_filters_keyboard
from states.states import States
from utils import try_parse_int

state = States.Filters.set_filters


@dp.callback_query_handler(text="percent_change_from", state=state)
async def percent_change_from(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("↑ % От:")
    await States.Filters.percent_change_from.set()


@dp.callback_query_handler(text="percent_change_to", state=state)
async def percent_change_to(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("↑ % До:")
    await States.Filters.percent_change_to.set()


@dp.message_handler(state=States.Filters.percent_change_from)
async def percent_change_from(message: types.Message):
    value = message.text
    if try_parse_int(value) and const.PERCENT['min'] <= int(value) <= filters.percent_change['to']:
        filters.percent_change['from'] = int(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {const.PERCENT['min']} и <= {filters.percent_change['to']}")


@dp.message_handler(state=States.Filters.percent_change_to)
async def percent_change_to(message: types.Message):
    value = message.text
    if try_parse_int(value) and filters.percent_change['from'] <= int(value) <= const.PERCENT['max']:
        filters.percent_change['to'] = int(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {filters.percent_change['from']} и <= {const.PERCENT['max']}")