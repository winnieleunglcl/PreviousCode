import random

random_number = random.randint(1,9)
number_of_guesses = 0


while True:
      command = input("Guess the number between 1 and 9 or stop the game by input 'exit': ")

      if command.lower() == "exit":
          break        
      else:
          guess = int(command)
          number_of_guesses += 1

      if guess > random_number:
          print("Too high.")
      elif guess < random_number:
          print("Too low.")
      else:
          print("Exactly right!")
          print(f"You get the right answer in {number_of_guesses} attempts")      
          break


          

