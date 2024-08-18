runout_or_not <- function(gamble){
  fortune = 100               #initial fortune = 1
  for (i in 1:gamble){        #loop for T gambles
    random = runif(1)         #generate a continuous uniform random variable
    if (random<0.49){         #if the gambler wins
      fortune = fortune + 1   #he wins $1
    }
    else {                    #if the gambler loses
      fortune = fortune - 1   #he loses $1
    }
  }
  return(fortune)
}


calculate_prob <- function(gamble){
  prob = 0
  count = 0
  for(i in 1:100){                   #get 100 results so it is convenient for calculating probability
    result = runout_or_not(gamble)
    if (result>0){                   #if the gambler has not yet run out of money after T gambles
      count = count + 1              
    }
  }
  prob = count / 100
  return(prob)
}


T <- c(100,1000,10000,100000)

for (i in 1:length(T)){
  print(calculate_prob(T[i]))
}
