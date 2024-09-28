for _ in range(int(input())):
    n = int(input())
    word_count = {}
    players_words = []
    
    for player in range(3):
        words = input().strip().split()
        players_words.append(words)
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    scores = [0, 0, 0]
    
    for player in range(3):
        for word in players_words[player]:
            count = word_count[word]
            if count == 1:
                scores[player] += 3 
            elif count == 2:
                scores[player] += 1  

    print(scores[0], scores[1], scores[2])
