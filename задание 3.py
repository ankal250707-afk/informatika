list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_ = len(list_players) // 2 #считаем количество и делим его на два

first_team = list_players[:middle_] #первая команда это первая поливина людей
second_team = list_players[middle_:] #вторая команда это вторая половина людей
#выводим переменные
print(first_team)
print(second_team)
