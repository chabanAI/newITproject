def calculate_months_to_debt(money_capital, salary, spend, increase):
    months = 0

    while money_capital >= 0:
        budget_this_month = salary + money_capital
        if spend > budget_this_month:
            break  # Выход из цикла, если траты превышают бюджет текущего месяца

        money_capital -= spend  # Уменьшаем финансовую подушку безопасности
        spend *= (1 + increase / 100)  # Увеличиваем расходы на следующий месяц
        months += 1

    return months

# Заданные значения
money_capital = 10000  # Финансовая подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Расходы на проживание
increase = 5  # Увеличение расходов ежемесячно на 5%

# Расчет
months_to_debt = calculate_months_to_debt(money_capital, salary, spend, increase)

# Вывод результата
print(f"Можно протянуть без долгов {months_to_debt} месяцев.")
