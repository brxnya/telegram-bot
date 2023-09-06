def bmi_calc(height: int, weight: float):
    if weight == 0.0 or height == 0:
        return
    bmi = round(weight / (height / 100) ** 2, 1)
    return bmi


def rec_mass_calc(height: int):
    if height == 0:
        return
    rec_mass1 = round(18.5 * (height / 100) ** 2, 1)
    rec_mass2 = round(25.0 * (height / 100) ** 2, 1)
    return rec_mass1, rec_mass2


def calorie_calc(gender: str, age: int, weight: float, height: int, psy_activity: str):
    result = 0.0
    if gender == 'Мужской':
        result += (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 'Женский':
        result += (10 * weight) + (6.25 * height) - (5 * age) - 161
    match psy_activity:
        case 'Низкий':
            result *= 1.2
        case 'Ниже среднего':
            result *= 1.375
        case 'Средний':
            result *= 1.55
        case 'Выше среднего':
            result *= 1.725
        case 'Высокий':
            result *= 1.9
    return round(result, 1)
