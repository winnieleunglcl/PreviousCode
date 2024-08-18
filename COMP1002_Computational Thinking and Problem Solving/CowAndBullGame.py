import random


def cow_bull_game(r):
  
    cow_bull = [0,0]  #[cow,bull]
    ans = ""
    n = 0
    
    print("Welcome to the Cows and Bulls Game!")
    print(r)

    while ans != r:
          ans = str(input("Enter a number: \n"))
          
          for i in range(len(r)):
              if ans[i] == r[i]: 
                  cow_bull[0] += 1    # answer correctly in correct place -> 1 cow
              elif ans[i] in r:
                  cow_bull[1] += 1    # answer correctly in incorrect place -> 1 bull

                 
          if cow_bull[0] > 1:
              print(f"{cow_bull[0]} cows",end = "")
          else:
              print(f"{cow_bull[0]} cow",end = "")
          if cow_bull[1] > 1:
              print(f", {cow_bull[1]} bulls")
          else:
              print(f", {cow_bull[1]} bull")

          cow_bull = [0,0]
          n += 1
          
    print(f"It tooke you {n} guess(es)!")

random = str(random.randint(1000,9999)) 
cow_bull_game(random)
