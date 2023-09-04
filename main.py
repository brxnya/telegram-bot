from aiogram import Bot, Dispatcher, executor, types
from magic_filter import F
import db
import kb

API_TOKEN = ''

dp = Dispatcher(Bot(API_TOKEN))

user_data = {}


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    new_user = db.check_user(message.chat.id)
    if new_user:
        db.add_new_user(message.chat.id, message.chat.full_name, 0, 0)
    user_params = db.get_user_params(message.chat.id)
    await message.answer(
            f"Привет, <b>{user_params[1]}</b>, рад видеть тебя!\n\n"
            "Твои параметры:\n\n"
            f"<i>Рост</i>:    <b>{'не указано' if user_params[3] == 0.0 else user_params[3]}</b> <i>см</i>\n"
            f"<i>Вес</i>:      <b>{'не указано' if user_params[2] == 0.0 else user_params[2]}</b> <i>кг</i>\n",
            parse_mode='HTML',
            reply_markup=kb.menu
    )


async def update_height(message: types.Message, new_value: float):
    await message.edit_text(
        f"Укажите рост: {round(new_value, 1)} см",
        reply_markup=kb.get_keyboard()
    )


@dp.callback_query_handler(lambda c: c.data == "set_param_height")
async def cmd_height(callback: types.CallbackQuery):
    user_data[callback.message.chat.id] = db.get_user_params(callback.from_user.id)[3]
    await callback.message.edit_text(
        f"Укажите рост: {user_data.get(callback.message.chat.id)} см",
        reply_markup=kb.get_keyboard()
    )


@dp.callback_query_handler(F.data.startswith("num_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.message.chat.id)
    action = callback.data.split("_")[1]

    if action == "incr01":
        user_data[callback.message.chat.id] = user_value+0.1
        await update_height(callback.message, user_value + 0.1)
    elif action == "incr1":
        user_data[callback.message.chat.id] = user_value+1
        await update_height(callback.message, user_value + 1)
    elif action == "incr5":
        user_data[callback.message.chat.id] = user_value+5
        await update_height(callback.message, user_value + 5)
    elif action == "incr10":
        user_data[callback.message.chat.id] = user_value+10
        await update_height(callback.message, user_value + 10)
    elif action == "decr01":
        user_data[callback.message.chat.id] = user_value-0.1
        await update_height(callback.message, user_value - 0.1)
    elif action == "decr1":
        user_data[callback.message.chat.id] = user_value-1
        await update_height(callback.message, user_value - 1)
    elif action == "decr5":
        user_data[callback.message.chat.id] = user_value-5
        await update_height(callback.message, user_value - 5)
    elif action == "decr10":
        user_data[callback.message.chat.id] = user_value-10
        await update_height(callback.message, user_value - 10)
    elif action == "finish":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, height=user_data.pop(callback.message.chat.id))
        await send_welcome(callback.message)

    await callback.answer()


if __name__ == '__main__':
    db.init()
    executor.start_polling(dp, skip_updates=True)
