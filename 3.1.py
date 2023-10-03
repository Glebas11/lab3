# Шаг 1: Записываем данные пользователя в файл F1
with open("F1.txt", "w") as f1:
    while True:
        user_input = input("Введите данные для записи в F1 (пустая строка для завершения): ")
        if not user_input:            break
        f1.write(user_input + '\n')
# Шаг 2: Копируем строки из F1 в F2, начиная с строки K до K+5
K = int(input("Введите номер строки K: "))  # Пользователь вводит K
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    if K < len(lines):
        for i in range(K, min(K + 5, len(lines))):
            f2.write(lines[i])
# Шаг 3: Подсчитываем количество гласных букв в F2
def count_vowels(text):
    vowels = "AEIOUaeiou"
    return sum(1 for char in text if char in vowels)
with open("F2.txt", "r") as f2:
    content = f2.read()
    vowel_count = count_vowels(content)
print(f"Количество гласных букв в строках F2: {vowel_count}")