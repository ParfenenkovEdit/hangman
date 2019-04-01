def hangman(word):
    for i in range (0,10):
        print("\n")
    wrong = 0
    stages = ["",
              "______     ",
              "|          ",
              "|    |     ",
              "|    0     ",
              "|   /|\    ",
              "|   / \    ",
              "|          ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь")

    while wrong < len(stages)-1:
        print("\n")
        msg = input("Введите букву: \n")
        if msg in rletters:
            cind = rletters.index(msg)
            board[cind] = msg
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you WON!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("Вы проиграли\n"
                "Было загадано слово {}".format(word))
