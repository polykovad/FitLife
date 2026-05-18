# Проект FitLife - MVP версия 1.0

def acquaintance():
    """Знакомимся с пользователем и узнаем возраст"""
    ERROR_AGE = "Ошибка: некорректное значение возраста!"
    age = None  # заранее объявляю переменную

    # Получаем от пользователя имя
    name = input("Здравствуйте! Я FitLife MVP - ваш личный фитнес-трекер.\n"
                 "Познакомимся?\n"
                 "Введите Ваше имя: ")
    if not name.strip():
        print("Ошибка: имя не может быть пустым!")
    # Получаем от пользователя возраст
    try:
        age = int(input("Введите Ваш возраст (полных лет): "))
        if (age < 0) or (age > 122):
            print(ERROR_AGE)
    except (ValueError, TypeError):
        print(ERROR_AGE)
    return name, age


def get_data():
    """Спрашиваем вес и рост"""
    ERROR_WEIGHT = "Ошибка: некорректное значение веса!"
    ERROR_HEIGHT = "Ошибка: некорректное значение роста!"
    weight = None  # заранее объявляю переменную
    height = None  # заранее объявляю переменную

    # Получаем от пользователя вес
    try:
        weight = float(input("Укажите ваш вес в кг (например, 65.5): "))
        if (weight < 0) or (weight > 700):
            print(ERROR_WEIGHT)
    except (ValueError, TypeError):
        print(ERROR_WEIGHT)
    # Получаем от пользователя рост
    try:
        height = float(input("Укажите ваш рост в метрах (например, 1.75): "))
        if (height < 0) or (height > 3):
            print(ERROR_HEIGHT)
    except (ValueError, TypeError):
        print(ERROR_HEIGHT)
    return weight, height


def calculation_bmi(user_weight, user_height):
    """Рассчитываем ИМТ"""
    bmi = round(user_weight / (user_height ** 2), 1)
    return bmi


def calculation_water(user_weight):
    """Рассчитываем объем воды в литрах"""
    WATER_PER_KG = 30
    VOLUME_WATER = 1000

    water_l = round(user_weight * WATER_PER_KG / VOLUME_WATER, 1)
    return water_l


def get_age_string(user_age):
    """Правильный вывод пометки возраста лет/года"""
    # Находим две последние цифры для проверки исключений
    last_two_digits = user_age % 100
    # Находим последнюю цифру для базовых правил
    last_digit = user_age % 10
    # Исключения: от 11 до 14 всегда "лет"
    if 11 <= last_two_digits <= 14:
        return f"{user_age} лет"
    # Если заканчивается на 1 будет "год"
    if last_digit == 1:
        return f"{user_age} год"
    # Если заканчивается на 2, 3, 4 будет "года"
    if 2 <= last_digit <= 4:
        return f"{user_age} года"
    # Для всех остальных цифр 0, 5, 6, 7, 8, 9 бует "лет"
    return f"{user_age} лет"


def main():
    """Основная программа фитнес-трекера FitLife"""
    # 1. Знакомство
    user_name, user_age = acquaintance()
    # 2. Сбор данных
    user_weight, user_height = get_data()
    # 3. Считаем ИМТ и норму воды
    bmi = calculation_bmi(user_weight, user_height)
    water_needed = calculation_water(user_weight)
    # 4. Вывод красивого результата
    age_string = get_age_string(user_age)
    print("=================================================================")
    print(f"Отчет для пользователя: {user_name} ({age_string})", end="\n\n")
    print(f"Ваш Индекс Массы Тела:: {bmi}", end="\n\n")
    print(f"Рекомендуемая норма воды: {water_needed} л. в день", end="\n\n")
    print("Расчет окончен. Будьте здоровы!")
    print("=================================================================")


if __name__ == "__main__":
    main()
