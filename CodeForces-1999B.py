t = int(input())
answers = []

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    suneet_wins = 0
    possible_games = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    for game in possible_games:
        suneet_rounds = 0
        slavic_rounds = 0
        if game[0] > game[1]:
            suneet_rounds += 1
        elif game[0] < game[1]:
            slavic_rounds += 1
        if game[2] > game[3]:
            suneet_rounds += 1
        elif game[2] < game[3]:
            slavic_rounds += 1
        if suneet_rounds > slavic_rounds:
            suneet_wins += 1

    answers.append(suneet_wins)
for result in answers:
    print(result)
