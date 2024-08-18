#q4(2)

setwd(getwd())
age <- read.table("./q4_data/age.txt",sep="\n")
height <- read.table("./q4_data/height.txt",sep="\n")
record <- data.frame(age,height)
names(record)[1] <- "age"
names(record)[2] <- "height"


#calculate line equation

mean_age = mean(record[,1])
mean_height = mean(record[,2])

sample_variance = 0
for(i in 1:50){
  sample_variance = sample_variance + (record[i,1] - mean_age) ^ 2
}
sample_variance = sample_variance * (1/49)

sample_covariance = 0
for (i in 1:50){
  sample_covariance = sample_covariance + (record[i,1]-mean_age)*(record[i,2]-mean_height)
}
sample_covariance = sample_covariance * (1/49)

deriative_b1 = sample_covariance / sample_variance
deriative_b0 = mean_height - deriative_b1 * mean_age

cat("Line equation:",deriative_b1,"x +",deriative_b0)


#draw graph

install.packages("ggplot2")
library("ggplot2")
ggplot(record,aes(x=age,y=height))+geom_point(color="blue")+ggtitle("Age vs. Height")+xlab("Age (year)")+ylab("Height (meter)")+geom_smooth(method="lm",color="red")
