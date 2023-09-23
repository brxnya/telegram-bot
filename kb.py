from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_kb_menu():
    buttons = [
        [
            InlineKeyboardButton(text="Выбрать пол", callback_data="set_param_gender"),
            InlineKeyboardButton(text="Указать возраст", callback_data="set_param_age")
        ],
        [
            InlineKeyboardButton(text="Указать вес", callback_data="set_param_weight"),
            InlineKeyboardButton(text="Указать рост", callback_data="set_param_height")
        ],
        [
            InlineKeyboardButton(text="Указать физическую активность", callback_data="set_param_activity")
        ],
        [
            InlineKeyboardButton(text="Готово", callback_data="params_complete")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_weight():
    buttons = [
        [
            InlineKeyboardButton(text="-10", callback_data="num_decr10"),
            InlineKeyboardButton(text="-5", callback_data="num_decr5"),
            InlineKeyboardButton(text="+5", callback_data="num_incr5"),
            InlineKeyboardButton(text="+10", callback_data="num_incr10")
        ],
        [
            InlineKeyboardButton(text="-1", callback_data="num_decr1"),
            InlineKeyboardButton(text="-0.1", callback_data="num_decr01"),
            InlineKeyboardButton(text="+0.1", callback_data="num_incr01"),
            InlineKeyboardButton(text="+1", callback_data="num_incr1")
        ],
        [InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_height():
    buttons = [
        [
            InlineKeyboardButton(text="-10", callback_data="num_decr10"),
            InlineKeyboardButton(text="-5", callback_data="num_decr5"),
            InlineKeyboardButton(text="+5", callback_data="num_incr5"),
            InlineKeyboardButton(text="+10", callback_data="num_incr10")
        ],
        [
            InlineKeyboardButton(text="-1", callback_data="num_decr1"),
            InlineKeyboardButton(text="+1", callback_data="num_incr1")
        ],
        [InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_gender():
    buttons = [
        [
            InlineKeyboardButton(text="Мужской", callback_data="male"),
            InlineKeyboardButton(text="Женский", callback_data="female")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_activity():
    buttons = [
        [InlineKeyboardButton(text="Низкий", callback_data="low_act")],
        [InlineKeyboardButton(text="Ниже среднего", callback_data="below_average_act")],
        [InlineKeyboardButton(text="Средний", callback_data="average_act")],
        [InlineKeyboardButton(text="Выше среднего", callback_data="above_average_act")],
        [InlineKeyboardButton(text="Высокий", callback_data="high_act")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_dietary_ration():
    buttons = [
        [InlineKeyboardButton(text="Составить план питания", callback_data="meal_plan")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_go_main():
    buttons = [
        [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
