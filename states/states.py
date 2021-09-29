from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    class Filters(StatesGroup):
        set_filters = State()
        category = State()
        money_from = State()
        money_to = State()
        percent_from = State()
        percent_to = State()
        percent_change_from = State()
        percent_change_to = State()
        coeff_to = State()
        coeff_from = State()
        coeff_diff = State()
        time_1_to = State()
        time_1_from = State()
        time_2_to = State()
        time_2_from = State()
        first_half = State()