def bingo(ticket,win):
    mini_wins = 0
    for each_lottery in ticket:
        for letter in each_lottery[0]:
            if ord(letter) == each_lottery[1]:
                mini_wins += 1
                break
    if mini_wins >= win:
        return('Winner!')
    else:
        return('Loser!')
