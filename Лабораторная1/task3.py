players = ["Игрок1", "Игрок2", "Игрок3", "Игрок4", "Игрок5", "Игрок6", "Игрок7", "Игрок8"]
total_players = len(players)

midpoint = total_players // 2
team1 = players[:midpoint]
team2 = players[midpoint:]

print("Общее количество игроков:", total_players)
print("Команда 1:", team1)
print("Команда 2:", team2)
