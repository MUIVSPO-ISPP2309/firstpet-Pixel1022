def celsius_to_other(temp):
    return {
        "Фаренгейт": (temp * 9/5) + 32,
        "Кельвин": temp + 273.15,
        "Реомюр": temp * 4/5,
        "Ранкин": (temp + 273.15) * 9/5,
        "Ньютон": temp * 33/100
    }

def fahrenheit_to_other(temp):
    return {
        "Цельсий": (temp - 32) * 5/9,
        "Кельвин": (temp - 32) * 5/9 + 273.15,
        "Реомюр": (temp - 32) * 4/9,
        "Ранкин": temp + 459.67,
        "Ньютон": (temp - 32) * 11/60
    }

def kelvin_to_other(temp):
    return {
        "Цельсий": temp - 273.15,
        "Фаренгейт": (temp - 273.15) * 9/5 + 32,
        "Реомюр": (temp - 273.15) * 4/5,
        "Ранкин": temp * 9/5,
        "Ньютон": (temp - 273.15) * 33/100
    }

def reaumur_to_other(temp):
    return {
        "Цельсий": temp * 5/4,
        "Фаренгейт": (temp * 9/4) + 32,
        "Кельвин": (temp * 5/4) + 273.15,
        "Ранкин": (temp * 9/4) + 491.67,
        "Ньютон": temp * 33/80
    }

def rankine_to_other(temp):
    return {
        "Цельсий": (temp - 491.67) * 5/9,
        "Фаренгейт": temp - 459.67,
        "Кельвин": temp * 5/9,
        "Реомюр": (temp - 491.67) * 4/9,
        "Ньютон": (temp - 491.67) * 11/60
    }

def newton_to_other(temp):
    return {
        "Цельсий": temp * 100/33,
        "Фаренгейт": (temp * 60/11) + 32,
        "Кельвин": (temp * 100/33) + 273.15,
        "Реомюр": temp * 80/33,
        "Ранкин": (temp * 60/11) + 491.67
    }

def convert_temperature(value, from_unit):
    if from_unit == "Цельсий":
        return celsius_to_other(value)
    elif from_unit == "Фаренгейт":
        return fahrenheit_to_other(value)
    elif from_unit == "Кельвин":
        return kelvin_to_other(value)
    elif from_unit == "Реомюр":
        return reaumur_to_other(value)
    elif from_unit == "Ранкин":
        return rankine_to_other(value)
    elif from_unit == "Ньютон":
        return newton_to_other(value)
    else:
        return None

def main():
    print("Конвертер температур (By Blinov)")
    
    # Ввод температуры
    temperature = float(input("Введите температуру: "))
    
    # Выбор единицы измерения
    units = ["Цельсий", "Фаренгейт", "Кельвин", "Реомюр", "Ранкин", "Ньютон"]
    print("Выберите единицу измерения:")
    for i, unit in enumerate(units):
        print(f"{i + 1}. {unit}")
    
    unit_choice = int(input("Введите номер единицы измерения: ")) - 1
    from_unit = units[unit_choice]
    
    # Конвертация и вывод результата
    converted_temps = convert_temperature(temperature, from_unit)
    
    print(f"Результаты конвертации из {from_unit}:")
    for unit, value in converted_temps.items():
        print(f"{value:.2f} {unit}")

if __name__ == "__main__":
    main()