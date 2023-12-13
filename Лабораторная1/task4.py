visitors = ["Пользователь1", "Пользователь2", "Пользователь3", "Пользователь1", "Пользователь4", "Пользователь2"]

statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

statistics["Общее количество"] = len(visitors)

unique_visitors = set(visitors)
statistics["Уникальные посещения"] = len(unique_visitors)

print("Статистика посещений сайта:")
print(statistics)
