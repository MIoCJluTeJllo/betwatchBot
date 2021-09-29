from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def get_set_filters_keyboard(start):
    return ReplyKeyboardMarkup([
        [
            KeyboardButton(text="Изменить фильтры"),
        ],
        [
            KeyboardButton(text=f"{'Приостановить' if start else 'Возобновить'}"),
        ]
    ], resize_keyboard=True)


def get_choice_keyboadrs(dict):
    buttons = []
    for key in dict.keys():
        buttons.append(InlineKeyboardButton(text=dict[key], callback_data=key))
    return InlineKeyboardMarkup(inline_keyboard=[buttons], resize_keyboard=True)


def get_percent_buttons(filters):
    if filters.percent_switch:
        return [
            InlineKeyboardButton(text=f"От {filters.percent['from']} %", callback_data="percent_from"),
            InlineKeyboardButton(text=f"До {filters.percent['to']} %", callback_data="percent_to"),
            InlineKeyboardButton(text=f"OFF", callback_data="percent_switch")
        ]
    else:
        return [
            InlineKeyboardButton(text=f"ON", callback_data="percent_switch")
        ]


def get_filters_keyboard(filters):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"{filters.category}", callback_data="category")],
            [
                InlineKeyboardButton(text=f"От {filters.money['from']} €", callback_data="money_from"),
                InlineKeyboardButton(text=f"До {filters.money['to']} €", callback_data="money_to")
            ],
            get_percent_buttons(filters),
            [
                InlineKeyboardButton(text=f"От {filters.coeff['from']} кф", callback_data="coeff_from"),
                InlineKeyboardButton(text=f"До {filters.coeff['to']} кф", callback_data="coeff_to")
            ],
            [
                InlineKeyboardButton(text=f"От {filters.time_1['from']} мин I", callback_data="time_1_from"),
                InlineKeyboardButton(text=f"До {filters.time_1['to']} мин I", callback_data="time_1_to")
            ],
            [
                InlineKeyboardButton(text=f"От {filters.time_2['from']} мин II", callback_data="time_2_from"),
                InlineKeyboardButton(text=f"До {filters.time_2['to']} мин II", callback_data="time_2_to")
            ],
            [
                InlineKeyboardButton(text=f"От ↑ {filters.percent_change['from']} %", callback_data="percent_change_from"),
                InlineKeyboardButton(text=f"До ↑ {filters.percent_change['to']} %", callback_data="percent_change_to")
            ],
            [
                InlineKeyboardButton(text="Сохранить", callback_data="save_filters"),
            ]
        ], resize_keyboard=True
    )
