
team1_num = 5
print("В команде Мастера кода участников:%s! " % (team1_num))
team2_num = 6
print("Итого сегодня в командах участников: %s и %d!" % (team1_num, team2_num))
score_2 = 42
print("Команда Волшебники данных решила задач: {}!".format(score_2))
team1_time = 18015.2
print("Волшебники данных решили задачи за {} с !".format(team1_time))
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач.")
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"
challenge_result = f"Результат битвы: {result}"
print(challenge_result)
tasks_total = score1 + score2
time_avg = ((team1_time + team2_time) / tasks_total)
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
