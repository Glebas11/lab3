# Открываем файл для чтения
with open("цветы.txt", "r", encoding="utf-8") as file:
    total_cost = 0
    count = 0
    # Читаем файл построчно
    for line in file:
        # Разделяем строку на название цвета и стоимость
        parts = line.strip().split()
                # Проверяем, что в строке есть две части (название и стоимость)
        if len(parts) == 2:
            flower_name, cost = parts
            cost = int(cost)  # Преобразуем стоимость в целое число
            # Выводим цветы дороже 10 рублей
            if cost > 10:
                print(f"{flower_name}: {cost} руб.")
            # Обновляем сумму и количество цветов
            total_cost += cost
            count += 1
    # Вычисляем среднюю стоимость всех цветов
    if count > 0:
         average_cost = total_cost / count
         print(f"Средняя стоимость всех цветов: {average_cost:.2f} руб.")
    else:
         print("В файле нет данных о цветах.")