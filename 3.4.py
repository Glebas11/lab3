import json
# Имя файла с данными о фирмах
file_name = "фирмы.txt"
# Инициализация списков
firm_data_list = []
profit_dict = {}
# Открываем файл для чтения
with open(file_name, "r", encoding="utf-8") as file:    # Читаем файл построчно
    for line in file:        # Разделяем строку на данные о фирме
        parts = line.strip().split()
        # Проверяем, что в строке есть четыре части
        if len(parts) == 4:
            firm_name, form_of_ownership, revenue, expenses = parts
            revenue = int(revenue)
            expenses = int(expenses)
            # Вычисляем прибыль фирмы
            profit = revenue - expenses
                        # Добавляем фирму и её прибыль в список
            firm_data_list.append({firm_name: profit})
            # Если фирма получила прибыль (не убыток), учитываем её прибыль
            if profit > 0:
                profit_dict[firm_name] = profit
# Вычисляем среднюю прибыль
average_profit = sum(profit_dict.values()) / len(profit_dict) if len(profit_dict) > 0 else 0
# Добавляем среднюю прибыль в список
firm_data_list.append({"average_profit": average_profit})
# Сохраняем список в виде JSON-объекта
json_file_name = "фирмы.json"
with open(json_file_name, "w") as json_file:
    json.dump(firm_data_list, json_file)
print(f"Данные о фирмах и средняя прибыль сохранены в файл {json_file_name}")