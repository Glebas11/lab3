# Имя файла с данными о предметах и занятиях
file_name = "предметы.txt"
# Инициализация пустого словаря
subjects_dict = {}
# Открываем файл для чтения
with open(file_name, "r", encoding="utf-8") as file:
    # Читаем файл построчно
    for line in file:
        # Разделяем строку на название предмета и данные о занятиях
        parts = line.strip().split(":")
                # Проверяем, что в строке есть две части (название и данные)
        if len(parts) == 2:
            subject_name, data = parts
            # Инициализируем счетчик общего количества занятий
            total_lessons = 0
            # Разделяем данные о занятиях на отдельные части
            lesson_parts = data.split()
            # Обходим все части данных о занятиях
            for lesson_part in lesson_parts:
                # Ищем числа в скобках и суммируем их
                if '(' in lesson_part and ')' in lesson_part:
                    lesson_count = int(''.join(filter(str.isdigit, lesson_part)))
                    total_lessons += lesson_count
            # Добавляем название предмета и общее количество занятий в словарь
            subjects_dict[subject_name] = total_lessons
# Выводим словарь на экран
print(subjects_dict)