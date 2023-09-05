from aiogram import Bot, Dispatcher, executor, types
from magic_filter import F
import db
import kb

API_TOKEN = ''

dp = Dispatcher(Bot(API_TOKEN))

user_data = {}


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    new_user = db.check_new_user(message.chat.id)
    if new_user:
        db.add_new_user(message.chat.id, message.chat.full_name, 'not specified', 0, 0.0, 0, 'not specified')
    user_params = db.get_user_params(message.chat.id)
    await message.answer(
        f"Привет <b>{user_params[1]}</b>! 👋\n"
        "Рад тебя видеть!\nЯ — твой личный помощник для контроля веса 🍽️✨\n"
        "Давай коротко расскажу как все тут устроено, этакая «внутренняя кухня» 👨‍🍳🔥:\n\n"
        "Мы будем использовать принцип <i>порционного питания</i>.\n"
        "Порционное питание — это подход к питанию, при котором ежедневное питание разбивается на 5-6 небольших и "
        "сбалансированных приемов пищи, основанный на контроле размеров порций. Он поможет тебе "
        "сбалансировать рацион, контролировать калорийность приемов пищи и достигать своих целей в области здоровья и "
        "фитнеса. 🥦🍎\n\n"
        "\"Контролировать калорийность приемов пищи\" — звучит сложно и страшно, правда ведь?\n"
        "Збагойствие, только збагойствие 🐨. Я тебе в этом помогу 😉\n\n"
        "📝 Для расчета калорий по формуле Миффлина-Сан-Жеора, мне понадобятся следующие параметры от тебя:\n"
        "1️⃣ Пол (мужской/женский)\n"
        "2️⃣ Возраст (в годах)\n"
        "3️⃣ Вес (в килограммах)\n"
        "4️⃣ Рост (в сантиметрах)\n"
        "5️⃣ Уровень физической активности (от сидячего образа жизни до высокой активности)\n\n"
        "Собрав эти данные, я смогу рассчитать приблизительное количество калорий, которое тебе следует потреблять "
        "ежедневно. Это будет полезным основанием для планирования твоего рациона и достижения твоих целей. 💪💡\n\n"
        "Готов начать этот путь вместе? Делись своими параметрами, и мы приступим к делу! 🌟😊\n\n"
        f"<i>Пол</i>:    <b>{'не указано' if user_params[2] == 'not specified' else user_params[2]}</b>\n"
        f"<i>Возраст</i>:    <b>{'не указано' if user_params[3] == 0 else user_params[3]}</b>\n"
        f"<i>Вес</i>:    <b>{'не указано' if user_params[4] == 0.0 else user_params[4]}</b>\n"
        f"<i>Рост</i>:    <b>{'не указано' if user_params[5] == 0 else user_params[5]}</b>\n"
        f"<i>Физическая активность</i>: "
        f"<b>{'не указано' if user_params[6] == 'not specified' else user_params[6]}</b>\n",
        parse_mode='HTML',
        reply_markup=kb.get_kb_menu()
    )


async def update_params(message: types.Message, new_value):
    if user_data.get(message.chat.id)[1] == "set_param_age":
        await message.edit_text(
            f"Укажи возраст: {new_value[0]}",
            reply_markup=kb.get_kb_height()
        )
    elif user_data.get(message.chat.id)[1] == "set_param_weight":
        await message.edit_text(
            f"Укажи вес: {round(new_value[0], 1)} кг",
            reply_markup=kb.get_kb_weight()
        )
    elif user_data.get(message.chat.id)[1] == "set_param_height":
        await message.edit_text(
            f"Укажи рост: {new_value[0]} см",
            reply_markup=kb.get_kb_height()
        )


@dp.callback_query_handler(
    lambda c: c.data == "set_param_gender" or c.data == "set_param_age" or c.data == "set_param_weight" or
    c.data == "set_param_height" or c.data == "set_param_activity" or c.data == "male" or c.data == "female" or
    c.data == "low_act" or c.data == "below_average_act" or c.data == "average_act" or c.data == "above_average_act" or
    c.data == "high_act")
async def cmd_params(callback: types.CallbackQuery):
    if callback.data == "set_param_gender":
        await callback.message.edit_text(
            f"Выбери пол:",
            reply_markup=kb.get_kb_gender()
        )
    elif callback.data == "set_param_age":
        value = db.get_user_params(callback.from_user.id)[3]
        if value == 0:
            value += 20
        user_data[callback.message.chat.id] = [value, callback.data]
        await callback.message.edit_text(
            f"Укажи возраст: {user_data.get(callback.message.chat.id)[0]}",
            reply_markup=kb.get_kb_height()
        )
    elif callback.data == "set_param_weight":
        value = db.get_user_params(callback.from_user.id)[4]
        if value == 0.0:
            value += 68
        user_data[callback.message.chat.id] = [value, callback.data]
        await callback.message.edit_text(
            f"Укажи вес: {user_data.get(callback.message.chat.id)[0]} кг",
            reply_markup=kb.get_kb_weight()
        )
    elif callback.data == "set_param_height":
        value = db.get_user_params(callback.from_user.id)[5]
        if value == 0:
            value += 165
        user_data[callback.message.chat.id] = [value, callback.data]
        await callback.message.edit_text(
            f"Укажи рост: {user_data.get(callback.message.chat.id)[0]} см",
            reply_markup=kb.get_kb_height()
        )
    elif callback.data == "set_param_activity":
        await callback.message.edit_text(
            "Выбери уровень физической активности:\n\n"
            "Низкий — если у тебя нет физических нагрузок и сидячая работа\n"
            "Ниже среднего — если ты совершаешь небольшие пробежки или делаешь легкую гимнастику 1–3 раза в неделю\n"
            "Средний — если ты занимаешься спортом со средними нагрузками 3–5 раз в неделю\n"
            "Выше среднего — если ты полноценно тренируешься 6–7 раз в неделю\n"
            "Высокий — если твоя работа связана с физическим трудом, ты тренируешься 2 раза в день и "
            "включаешь в программу тренировок силовые упражнения",
            reply_markup=kb.get_kb_activity()
        )
    elif callback.data == "male":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, gender='Мужской')
        await send_welcome(callback.message)
    elif callback.data == "female":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, gender='Женский')
        await send_welcome(callback.message)
    elif callback.data == "low_act":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, activity='Низкий')
        await send_welcome(callback.message)
    elif callback.data == "below_average_act":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, activity='Ниже среднего')
        await send_welcome(callback.message)
    elif callback.data == "average_act":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, activity='Средний')
        await send_welcome(callback.message)
    elif callback.data == "above_average_act":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, activity='Выше среднего')
        await send_welcome(callback.message)
    elif callback.data == "high_act":
        await callback.message.delete()
        db.change_user_params(callback.message.chat.id, activity='Высокий')
        await send_welcome(callback.message)


@dp.callback_query_handler(F.data.startswith("num_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.message.chat.id)
    action = callback.data.split("_")[1]

    if action == "incr01":
        user_data[callback.message.chat.id] = [user_value[0] + 0.1, user_value[1]]
        await update_params(callback.message, [user_value[0] + 0.1, user_value[1]])
    elif action == "incr1":
        user_data[callback.message.chat.id] = [user_value[0] + 1, user_value[1]]
        await update_params(callback.message, [user_value[0] + 1, user_value[1]])
    elif action == "incr5":
        user_data[callback.message.chat.id] = [user_value[0] + 5, user_value[1]]
        await update_params(callback.message, [user_value[0] + 5, user_value[1]])
    elif action == "incr10":
        user_data[callback.message.chat.id] = [user_value[0] + 10, user_value[1]]
        await update_params(callback.message, [user_value[0] + 10, user_value[1]])
    elif action == "decr01":
        user_data[callback.message.chat.id] = [user_value[0] - 0.1, user_value[1]]
        await update_params(callback.message, [user_value[0] - 0.1, user_value[1]])
    elif action == "decr1":
        user_data[callback.message.chat.id] = [user_value[0] - 1, user_value[1]]
        await update_params(callback.message, [user_value[0] - 1, user_value[1]])
    elif action == "decr5":
        user_data[callback.message.chat.id] = [user_value[0] - 5, user_value[1]]
        await update_params(callback.message, [user_value[0] - 5, user_value[1]])
    elif action == "decr10":
        user_data[callback.message.chat.id] = [user_value[0] - 10, user_value[1]]
        await update_params(callback.message, [user_value[0] - 10, user_value[1]])
    elif action == "finish":
        await callback.message.delete()
        if user_data.get(callback.message.chat.id)[1] == "set_param_age":
            age = user_data.get(callback.message.chat.id)[0]
            db.change_user_params(callback.message.chat.id, age=age)
            del user_data[callback.message.chat.id]
        elif user_data.get(callback.message.chat.id)[1] == "set_param_height":
            height = user_data.get(callback.message.chat.id)[0]
            db.change_user_params(callback.message.chat.id, height=height)
            del user_data[callback.message.chat.id]
        elif user_data.get(callback.message.chat.id)[1] == "set_param_weight":
            weight = round(user_data.get(callback.message.chat.id)[0], 1)
            db.change_user_params(callback.message.chat.id, weight=weight)
            del user_data[callback.message.chat.id]
        await send_welcome(callback.message)

    await callback.answer()


@dp.callback_query_handler(lambda c: c.data == "params_complete")
async def alert(callback: types.CallbackQuery):
    user_params = db.get_user_params(callback.message.chat.id)
    bmi = round(user_params[4] / (user_params[5] / 100) ** 2, 1)
    rec_mass1 = round(18.5 * (user_params[5] / 100) ** 2, 1)
    rec_mass2 = round(25.0 * (user_params[5] / 100) ** 2, 1)
    await callback.message.edit_text(
        f"<i>Пол</i>:    <b>{'не указано' if user_params[2] == 'not specified' else user_params[2]}</b>\n"
        f"<i>Возраст</i>:    <b>{'не указано' if user_params[3] == 0 else user_params[3]}</b>\n"
        f"<i>Вес</i>:    <b>{'не указано' if user_params[4] == 0.0 else user_params[4]}</b>\n"
        f"<i>Рост</i>:    <b>{'не указано' if user_params[5] == 0 else user_params[5]}</b>\n"
        f"<i>Физическая активность</i>: "
        f"<b>{'не указано' if user_params[6] == 'not specified' else user_params[6]}</b>\n"
        f"Твой ИМТ:  <b>{bmi}</b> <i>кг/м²</i>, норма: от 18.5 до 25 <i>кг/м²</i>\n"
        f"Норма массы тела: <b>{rec_mass1}</b> - <b>{rec_mass2}</b> <i>кг</i>\n\n",
        parse_mode='HTML',
    )


if __name__ == '__main__':
    db.init()
    executor.start_polling(dp, skip_updates=True)
