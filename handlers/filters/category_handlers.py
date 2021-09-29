import const
import filters
from init import dp
from aiogram import types

from keyboards.filters_keyboards import get_choice_keyboadrs, get_filters_keyboard
from states.states import States

state = States.Filters.category


@dp.callback_query_handler(text="category", state=States.Filters.set_filters)
async def category(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Выберите категорию:", reply_markup=get_choice_keyboadrs(const.CATEGORY))
    await States.Filters.category.set()


@dp.callback_query_handler(text="all", state=state)
async def all(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    filters.category = const.CATEGORY['all']
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    await States.Filters.set_filters.set()


@dp.callback_query_handler(text="live", state=state)
async def live(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    filters.category = const.CATEGORY['live']
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    await States.Filters.set_filters.set()


@dp.callback_query_handler(text="prematch", state=state)
async def prematch(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    filters.category = const.CATEGORY['prematch']
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    await States.Filters.set_filters.set()
