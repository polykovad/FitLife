# Проект FitLife - MVP версия 1.0

# Объявляю константы
ERROR_AGE = "Ошибка: некорректное значение возраста!"
ERROR_WEIGHT = "Ошибка: некорректное значение веса!"
ERROR_HEIGHT = "Ошибка: некорректное значение роста!"
WATER_PER_KG = 30
VOLUME_WATER = 1000
MIN_AGE = 0  # минимальный возраст
MAX_AGE = 122  # максимальный возраст
MIN_WEIGHT = 0  # минимальный вес в кг
MAX_WEIGHT = 700  # максимальный вес в кг
MIN_HEIGHT = 0  # минимальный рост в метрах
MAX_HEIGHT = 3  # максимальный рост в метрах


def acquaintance():
    """Знакомимся с пользователем и узнаем возраст"""
    print("Здравствуйте! Я FitLife MVP - ваш личный фитнес-трекер.\n"
          "Познакомимся?")
    # Получаем от пользователя имя
    while True:
        name = input("Введите Ваше имя: ")
        if not name.strip():
            print("Ошибка: имя не может быть пустым!")
            continue
        break
    # Получаем от пользователя возраст
    while True:
        try:
            age = int(input("Введите Ваш возраст (полных лет): "))
            if (age <= MIN_AGE) or (age > MAX_AGE):
                print(ERROR_AGE)
                continue
            break
        except (ValueError, TypeError):
            print(ERROR_AGE)
    return name, age


def get_data():
    """Спрашиваем вес и рост"""
    # Получаем от пользователя вес
    while True:
        try:
            weight = float(input("Укажите ваш вес в кг (например, 65.5): "))
            if (weight <= MIN_WEIGHT) or (weight > MAX_WEIGHT):
                print(ERROR_WEIGHT)
                continue
            break
        except (ValueError, TypeError):
            print(ERROR_WEIGHT)
    # Получаем от пользователя рост
    while True:
        try:
            height = float(input("Укажите ваш рост в метрах "
                                 "(например, 1.75): "))
            if (height <= MIN_HEIGHT) or (height > MAX_HEIGHT):
                print(ERROR_HEIGHT)
                continue
            break
        except (ValueError, TypeError):
            print(ERROR_HEIGHT)
    return weight, height


def calculation_bmi(user_weight, user_height):
    """Рассчитываем ИМТ"""
    return round(user_weight / (user_height ** 2), 1)


def calculation_water(user_weight):
    """Рассчитываем объем воды в литрах"""
    return round(user_weight * WATER_PER_KG / VOLUME_WATER, 1)


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
    # Для всех остальных цифр 0, 5, 6, 7, 8, 9 будет "лет"
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
