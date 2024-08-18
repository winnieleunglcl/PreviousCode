install.packages("ggplot2")
library("ggplot2")

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

T <- c(5000,10000,15000,20000,25000,30000)  #growing values of T

fortunes <- vector()

for(i in 1:length(T)){
  for (j in 1:20){
    number = runout_or_not(T[i])
    fortunes <- c(fortunes,number)  #store the possible values of N according to different values of T
  }
}

#the length of T must be equal to the length of fortunes so that the data can be plotted
T <- c(rep.int(5000,20),rep.int(10000,20),rep.int(15000,20),rep.int(20000,20),rep.int(25000,20),rep.int(30000,20))

record <- data.frame(T,fortunes)

ggplot(record,aes(x=T,y=fortunes,color=T))+geom_point(size=3)+geom_smooth(method="lm")+xlab("T gambles")+ylab("N's expected value($)")+ggtitle("Change of N¡¦s expected value when T grows")
