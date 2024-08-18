def genGameBoard():
    size = int(input("What game board size (n*n) do you want to draw? Input n: "))
    ho = " --- " * size
    ve = "|    " * (size+1)

    for i in range(size):
        print(ho)
        print(ve)
    print(ho)

    
genGameBoard()
    
