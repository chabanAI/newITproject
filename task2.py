def find_common_participants(group1, group2, separator=','):

    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Преобразуем списки в множества для удобства поиска общих участников
    number_of_participants1 = set(participants1)
    number_of_participants2 = set(participants2)

    # Находим общих участников
    common_participants = number_of_participants1.intersection(number_of_participants2)

    # Преобразуем результат в отсортированный список
    smth_new= sorted(list(common_participants))

    return smth_new
# Пример использования функции:
group1 = "Анна,Иван,Мария,Петр"
group2 = "Иван,Мария,Сергей,Елена"

result = find_common_participants(group1, group2)

print(f"Общие участники: {result}")


