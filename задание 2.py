# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delim=','):
    # Разделяем строки на списки фамилий
    participants1 = group1.split(delim)
    participants2 = group2.split(delim)

    # С помощью множеств находим пересечение общих участников
    common_participants = set(participants1) & set(participants2)

    # Преобразуем множество в отсортированный список
    return sorted(list(common_participants))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, delim='|') # Вызываем функцию с разделителем
print("Общие участники:", result)

# TODO Провеьте работу функции с разделителем отличным от запятой
