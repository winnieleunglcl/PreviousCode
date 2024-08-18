#start of step 1

setwd(getwd())
data = read.csv("./q2_data/scores.csv",sep=",",header=TRUE)
names(data)[1] <- "StuID"
print(data)

#end of step 1


#start of step 2

mean_value = mean(data[1:10,4])
sd_value = sd(data[1:10,4])
median_value = median(data[1:10,4])
minimum_value = min(data[1:10,4])
maximum_value = max(data[1:10,4])
cat("The statistics for science scores are:\nmean =",mean_value,";\nstandard deviation =",sd_value,";\nmedian score =",median_value,";\nminimum socre =",minimum_value,";\nmaximum score =",maximum_value,".")

#end of step 2


#start of step 3

for(i in 3:5){
  mean_value = mean(data[1:10,i])
  sd_value = sd(data[1:10,i])
  for (j in 1:10){
    data[j,i] = (data[j,i]-mean_value)/sd_value
  }
}

print(data)

#end of step 3


#start of step 4

first_name <- data$StuName
last_name <- data$StuName

library(tibble)
data <- add_column(data,first_name,.after="StuName")
names(data)[3] <- "First Name"
data <- add_column(data,last_name,.after="First Name")
names(data)[4] <- "Last Name"

data$`First Name` <- sapply(strsplit(as.character(data$`First Name`)," ",fixed = TRUE),'[',1)
data$`Last Name` <- sapply(strsplit(as.character(data$`Last Name`)," ",fixed = TRUE),'[',2)
print(data)

#end of step 4


#start of step 5

grade <- vector()
for (i in 1:10){
  grade[i] <- data[i,5]*0.3 + data[i,6]*0.4 + data[i,7]*0.3
}

grade <- rank(-grade)

for(i in 1:length(grade)){
  if(grade[i] <= length(grade)*0.25){
    grade[i] = "A"
  }
  else if (grade[i] <= length(grade)*0.5){
    grade[i] = "B"
  }
  else if (grade[i] <= length(grade)*0.75){
    grade[i] = "C"
  }
  else{
    grade[i] = "D"
  }
}

data <- add_column(data,grade,.after="English")
names(data)[8] <- "Grade"

print(data)

#end of step 5


#start of step 6

write.csv(data,"./newscores.csv",row.names = FALSE)

#end of step 6

