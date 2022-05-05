#Домашнее задание
#Счастливые билеты.
#Цель:
#Решить задачу «Счастливые билеты» и проверить решение по тестам.
#Создать систему тестирования на основе файлов.
#УРОВЕНЬ MIDDLE
#Скачать и распаковать архив A01_Счастливые_билеты.zip
#Прочитать условие задачи \1.Tickets\problem.txt
#Решить задачу в общем случае и протестировать вручную на тестах, которые находятся в архиве.#
from datetime import datetime
from ticket_lucky import getCntLuckyTicketsRandomLen
start_time = datetime.now()
for i in range(1,11):
    res = getCntLuckyTicketsRandomLen(i)
    print(res)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds()*1000)



