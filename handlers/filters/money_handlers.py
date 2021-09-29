from aiogram import types

import const
import filters
from init import dp
from keyboards.filters_keyboards import get_filters_keyboard
from states.states import States
from utils import try_parse_int

state = States.Filters.set_filters


@dp.callback_query_handler(text="money_from", state=state)
async def money_from(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("€ От:")
    await States.Filters.money_from.set()


@dp.callback_query_handler(text="money_to", state=state)
async def money_to(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("€ До:")
    await States.Filters.money_to.set()


@dp.message_handler(state=States.Filters.money_from)
async def money_from(message: types.Message):
    value = message.text
    if try_parse_int(value) and const.MONEY['min'] <= int(value) <= filters.money['to']:
        filters.money['from'] = int(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {const.MONEY['min']} и <= {filters.money['to']}")


@dp.message_handler(state=States.Filters.money_to)
async def money_to(message: types.Message):
    value = message.text
    if try_parse_int(value) and filters.money['from'] <= int(value) <= const.MONEY['max']:
        filters.money['to'] = int(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {filters.money['from']} и <= {const.MONEY['max']}")