from aiogram import Bot, Dispatcher, executor, types
import db
import kb

API_TOKEN = ''

dp = Dispatcher(Bot(API_TOKEN))


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    new_user = db.check_user(user_id)
    if new_user:
        db.add_new_user(user_id, user_name, 72.1, 165)
    await message.answer(
        f"В разработке..."
    )

# await message.answer(
#         f"Привет, <b>{user_name}</b>!\n\n"
#         "Вижу что ты у нас впервые, давай укажем твои параметры:\n\n"
#         f"<i>Рост</i>:    <b>{height}</b> <i>см</i>\n"
#         f"<i>Вес</i>:      <b>{weight}</b> <i>кг</i>\n",
#         parse_mode='HTML',
#         reply_markup=kb.new_user_menu
#     )


@dp.callback_query_handler(lambda c: c.data == "set_height")
async def edit_msg(query: types.CallbackQuery):
    await query.message.edit_text("Укажите рост:")


if __name__ == '__main__':
    db.init()
    executor.start_polling(dp, skip_updates=True)
