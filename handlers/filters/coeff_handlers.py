from aiogram import types

import const
import filters
from init import dp
from keyboards.filters_keyboards import get_filters_keyboard
from states.states import States
from utils import try_parse_float

state = States.Filters.set_filters


@dp.callback_query_handler(text="coeff_from", state=state)
async def coeff_from(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("% От:")
    await States.Filters.coeff_from.set()


@dp.callback_query_handler(text="coeff_to", state=state)
async def coeff_to(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("% До:")
    await States.Filters.coeff_to.set()


@dp.message_handler(state=States.Filters.coeff_to)
async def coeff_to(message: types.Message):
    value = message.text
    if try_parse_float(value) and filters.coeff['from'] <= float(value) <= const.COEFF['max']:
        filters.coeff['to'] = float(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {filters.coeff['from']} и <= {const.COEFF['max']}")


@dp.message_handler(state=States.Filters.coeff_from)
async def coeff_from(message: types.Message):
    value = message.text
    if try_parse_float(value) and const.COEFF['min'] <= float(value) <= filters.coeff['to']:
        filters.coeff['from'] = float(value)
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
        await States.Filters.set_filters.set()
    else:
        await message.answer(f"Значение должно быть >= {const.COEFF['min']} и <= {filters.coeff['to']}")