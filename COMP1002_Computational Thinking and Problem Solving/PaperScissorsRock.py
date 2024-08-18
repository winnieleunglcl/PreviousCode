u1_win = False

user1 = input("What is your name, user 1? ")
user2 = input("What is your name, user 2? ")

while True:
    user1_choice = input("User 1's choice? ").lower()
    user2_choice = input("User 2's choice? ").lower()

    if user1_choice == user2_choice:
        print("This is a tie! Please continue.")
        continue
    
    elif user1_choice == "rock":
       if user2_choice == "scissors":
            u1_win = True


    elif user1_choice == "paper":
       if user2_choice == "rock":
           u1_win = True


    elif user1_choice == "scissors":
        if user2_choice == "paper":
           u1_win = True

    if u1_win == True:
       print(f"{user1} wins the game! Congratulations!")
    else:
       print(f"{user2} wins the game! Congratulations!")

    if user1_choice != user2_choice:
        run_again = input("Do you want to play another round, yes or no? ").lower()
        if run_again == "yes":
            continue
        else:
            print("Game over. Thanks for playing!")
            break





