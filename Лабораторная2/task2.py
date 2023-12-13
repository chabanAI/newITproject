def calculate_required_money_capital(salary, spend, increase, months_to_survive):
    money_capital = 0  # Начальное значение финансовой подушки безопасности
    months = 0

    while months < months_to_survive:
        budget_this_month = salary + money_capital
        if spend > budget_this_month:
            money_capital += spend - budget_this_month  # Увеличиваем подушку безопасности
        spend *= (1 + increase / 100)  # Увеличиваем расходы на следующий месяц
        months += 1

    return round(money_capital, 2)

# Заданные значения
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Расходы на проживание
increase = 3  # Увеличение расходов ежемесячно на 3%
months_to_survive = 10  # Количество месяцев для протяжки без долгов

# Расчет
required_money_capital = calculate_required_money_capital(salary, spend, increase, months_to_survive)

# Вывод результата
print(f"Необходимая финансовая подушка безопасности: {required_money_capital} руб.")
