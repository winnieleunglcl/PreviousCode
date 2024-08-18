def guess_by_bin():
    print("This program will guess the number in your mind!")
    print("Please think of a number between 0 and 100.")

    minimum = 0
    maximum = 100
    middle = 50
    count = 1

    condition = input(f"Is your guess {middle} ? (0 = it's too low, 1 = it's right, 2 = it's too high) ")
    while condition != "1":
        count += 1
        if condition == "0":
            minimum = middle + 1
        elif condition == "2":
            maximum = middle - 1
        middle = (minimum + maximum) // 2
        condition = input(f"Is your guess {middle} ? (0 = it's too low, 1 = it's right, 2 = it's too high) ")

    print(f"It took {count} times to guess your number")

guess_by_bin()
