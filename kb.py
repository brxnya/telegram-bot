from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [
        InlineKeyboardButton(text="Изменить рост", callback_data="set_param_height"),
        InlineKeyboardButton(text="Изменить вес", callback_data="set_param_weight")
    ],
    [
        InlineKeyboardButton(text="Готово", callback_data="params_complete")
    ]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)


def get_keyboard():
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
