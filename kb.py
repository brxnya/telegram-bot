from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

new_user_menu = [
    [InlineKeyboardButton(text="Рост", callback_data="set_param_height"),
     InlineKeyboardButton(text="Вес", callback_data="set_param_weight")],
    [InlineKeyboardButton(text="Готово", callback_data="params_complete")]
]

menu = [
    [InlineKeyboardButton(text="Изменить вес", callback_data="alter_weight"),
     InlineKeyboardButton(text="Изменить рост", callback_data="alter_height")],
    [InlineKeyboardButton(text="Рассчитать ИМТ", callback_data="bms_value")]
]


new_user_menu = InlineKeyboardMarkup(inline_keyboard=new_user_menu)
menu = InlineKeyboardMarkup(inline_keyboard=menu)
