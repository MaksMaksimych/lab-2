# Вариант 3. Написать программу, которая, читая текст из файла, выводит на экран только предложения,
# не содержащие запятых. Выполнил Иванов.М.А ИСТбд-11


import os
import time

max_buffer_len = 1000  # максимальный размер рабочего буфера
buffer_len = 1  # размер буфера чтения

w_buffer = ""  # рабочий буфер
cflag = False  # флаг наличия запятой
c = 0  # флаг наличия предложений, удовлетворяющих условию

try:
    start = time.time()
    with open("1111.txt", "r", encoding = 'utf-8') as file:  # открываем файл
        print("\n-----Результат работы программы-----\n\nПредложения, не содержащие запятых:\n")
        buffer = file.read(buffer_len)  # чтение первого блока

        if not buffer:  # если файл пустой
            print(
                "\nДанный файл в директории проекта пустой.\nДобавьте не пустой файл в директорию либо переименуйте существующий")

        while buffer:  # пока файл не пустой
            w_buffer += buffer  # обработка данного блока

            if buffer.find(",") >= 0:
                cflag = True

            if buffer.find(".") >= 0 or buffer.find("!") >= 0 or buffer.find(
                    "?") >= 0:  # Если символ - окончание предложения
                if cflag == False:  # Если в предложении не было запятой
                    print(w_buffer)  # Печатаем предложение и готовим новый цикл
                    c += 1
                cflag = False
                w_buffer = ""

            buffer = file.read(buffer_len)

            if len(w_buffer) >= max_buffer_len and buffer.find(".") < 0 and buffer.find("!") < 0 and buffer.find(
                    "?") < 0:
                print(
                    "Файл  не содержит знаков окончания предложения и максимальный размер буфера превышен. \nОткорректируйте существующий файл *.txt или переименуйте существующий *txt файл.")
                w_buffer = ""
                break

                # если в тексте не найдено ни одного предложения, удовлетворяющего условию:
                if c == 0:
                    print("Предложений, содержащих запятой, не найдено\n")

        # если файл не содержит знаков окончания предложения и буффер переполнен:
        if len(w_buffer) > 0:
            print(
                "\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")

        # если в тексте не найдено ни одного предложения, удовлетворяющего условию:
        if c == 0:
            print("Таких предложений в тексте нет\n")

        finish = time.time()
        result = finish - start
        print("\nВремя работы программы:" + str(result) + " секунд.")


except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")