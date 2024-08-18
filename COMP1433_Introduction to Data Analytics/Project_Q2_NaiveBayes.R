#--------------------------------------------------------#
# Library
#--------------------------------------------------------#
# Install the package if it is not installed
list.of.packages <- c("ggplot2", "mice", "recipes", "stringr","gridExtra")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

# Import Library
library(ggplot2)
library(mice)
library(recipes)
library(stringr)
library(gridExtra)

#--------------------------------------------------------#
# Function
#--------------------------------------------------------#
"
  count_SurvivalBy(data,feature)
  Count The number of Surviver and Non-suviver at specific feature, 
  store as Matrix and return the Matrix.
"
count_SurvivalBy <- function(data,feature){
  count_survival <- c()
  count_Notsurvival <- c()
  Plor_Names <- sort(unique(feature))
  ColCount <- 0
  for(i in Plor_Names){
    ColCount <- ColCount + 1
    count_survival <- c(count_survival, length(which(data$Survived==1 & feature==i)))
    count_Notsurvival <- c(count_Notsurvival, length(which(data$Survived==0 & feature==i)))
  }
  SurvivalData_Matrix = matrix(c(count_survival,count_Notsurvival), nrow=2,ncol=ColCount,byrow = TRUE)
  colnames(SurvivalData_Matrix) <- Plor_Names
  rownames(SurvivalData_Matrix) <- c("Survival", "Not Survival")
  return(SurvivalData_Matrix)
}

"
  count_SurvivalBy(data,feature)
  Count The number of Surviver and Non-suviver at specific feature, 
  store as Matrix and return the Matrix.
"
count_SurvivalByTwoFeatures <- function(data,F1, F2){
  count_Surviver <- c()
  count_NonSurviver <- c()
  Plor_Names <- c()
  for (first in sort(unique(F1))){
    for (second in sort(unique(F2))){
      Plor_Names <- c(Plor_Names, paste(first, second,sep = " "))
      count_Surviver <- c(count_Surviver, length(which(F1 == first & F2 == second & data$Survived == 1)))
      count_NonSurviver <- c(count_NonSurviver, length(which(F1 == first & F2 == second & data$Survived == 0)))
    }
  }
  SurvivalMatrix_By_Pclass_Sex = matrix(c(count_Surviver,count_NonSurviver), nrow=2,ncol=length(Plor_Names), byrow = T)
  colnames(SurvivalMatrix_By_Pclass_Sex) <- Plor_Names
  rownames(SurvivalMatrix_By_Pclass_Sex) <- c("Survival", "Not Survival")
  return(SurvivalMatrix_By_Pclass_Sex)
}

"
  print_BarPlot(SurvivalData_Matrix, DataNameForxlab)
  Print the Plot to display the Survival Data which created by function - count_SurvivalBy(feature)
"
print_BarPlot <- function(SurvivalData_Matrix, DataNameForxlab){
  Plor_Names = colnames(SurvivalData_Matrix)
  # Draw the plot to show the Surviver and not non-surviver of each class
  Survival_Pclass_Plot <-barplot(SurvivalData_Matrix, col = c("green","red"), 
                                 names.arg = Plor_Names,beside=T, 
                                 ylim=range(pretty(c(0, SurvivalData_Matrix + 100))), 
                                 main=paste("Survival of Each",DataNameForxlab),
                                 xlab = DataNameForxlab ,ylab = "Count")
  text(Survival_Pclass_Plot, SurvivalData_Matrix, labels=SurvivalData_Matrix, pos = 3)
}

"
  DataMissingCount(data)
  Count out the sum of the missing value in each column in dataframe
"

DataMissingCount <- function(data){
  CountTitle <- colnames(data)
  MissingCount <- colSums(is.na(data) | data=="" | data=="U")
  MissingCount_Matrix <- matrix(MissingCount, nrow = length(CountTitle), ncol = 1, byrow = T)
  colnames(MissingCount_Matrix) <- "MissingCount"
  rownames(MissingCount_Matrix) <- CountTitle
  print(MissingCount_Matrix)
}

"
  calculate_Probability(DataMatrix)
  Calculate the Probability of Survival and Not Survival by DataMatrix,
  and then return Probabilities by Matrix
"
calculate_Probability <- function(DataMatrix){
  Survival_Chance <- c()
  NotSurvival_Chance <- c()
  Survival_Vector <- colnames(DataMatrix)
  for(i in 1:ncol(DataMatrix)){
    Survival_Chance <- c(Survival_Chance, (DataMatrix[1,i]/(DataMatrix[1,i] + DataMatrix[2,i])))
    NotSurvival_Chance <- c(NotSurvival_Chance, (DataMatrix[2,i]/(DataMatrix[1,i] + DataMatrix[2,i])))
  }
  Survival_Chance_Matrix = matrix(c(Survival_Chance,NotSurvival_Chance), nrow = 2, ncol = ncol(DataMatrix), byrow = TRUE)
  colnames(Survival_Chance_Matrix) <- Survival_Vector
  rownames(Survival_Chance_Matrix) <- c("P(S)", "P(NS)")
  return(Survival_Chance_Matrix)
}

"
  calculate_Probability_Age_ByMethod(Method)
  calculate the Survival probability of Age based the selected Method
  and then return Probabilities by Matrix
"

# Model with Naive Bayes Classifier
Calculate_Prob_S_NaiveBayesModel <- function(row, features){
  Prob_List <- c(SurvivalChance_Overall)
  if("Pclass" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Pclass[1,which(colnames(Probability_By_Pclass) == row$Pclass)])
  
  if("Sex" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Sex[1,which(colnames(Probability_By_Sex) == row$Sex)])
  
  if("NameTitle" %in% features)
    Prob_List <- c(Prob_List, Probability_By_NameTitle[1,which(colnames(Probability_By_NameTitle) == row$NameTitle)])
  
  if("FamilyCount" %in% features)
    Prob_List <- c(Prob_List, ifelse(row$FamilyCount>10, Probability_By_FamilyCount[1,9], 
                                     Probability_By_FamilyCount[1,which(colnames(Probability_By_FamilyCount) == row$FamilyCount)]))
  # Since the maximum value of feature FamilyCount is 0, any value greater than 10 will use the probability of 10 as the value used in the calculation
  
  if("Cabin" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Cabin[1,which(colnames(Probability_By_Cabin) == row$Cabin)])
  
  if("Embarked" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Embarked[1,which(colnames(Probability_By_Embarked) == row$Embarked)])
  
  if("Fare" %in% features)
    Prob_List <- c(Prob_List, ifelse((row[,"Fare"] >= 0 & row[,"Fare"] < GroupCut_Fare[1]), Probability_By_GroupedFare[1,1], 
                                     ifelse((row[,"Fare"] >= GroupCut_Fare[1] & row[,"Fare"] < GroupCut_Fare[2]), Probability_By_GroupedFare[1,2],
                                            ifelse((row[,"Fare"] >= GroupCut_Fare[2] & row[,"Fare"] < GroupCut_Fare[3]), Probability_By_GroupedFare[1,3],
                                                   ifelse((row[,"Fare"] >= GroupCut_Fare[3] & row[,"Fare"] < GroupCut_Fare[4]), Probability_By_GroupedFare[1,4],
                                                          ifelse((row[,"Fare"] >= GroupCut_Fare[4]),  Probability_By_GroupedFare[1,5]))))))
 
  Prob_S <- prod(Prob_List)
  return(Prob_S)
}

Calculate_Prob_NS_NaiveBayesModel <- function(row, features){
  #print(features)
  Prob_List <- c(NotSurvivalChance_Overall)
  
  if("Pclass" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Pclass[2,which(colnames(Probability_By_Pclass) == row$Pclass)])
  
  if("Sex" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Sex[2,which(colnames(Probability_By_Sex) == row$Sex)])
  
  if("NameTitle" %in% features)
    Prob_List <- c(Prob_List, Probability_By_NameTitle[2,which(colnames(Probability_By_NameTitle) == row$NameTitle)])
  
  if("FamilyCount" %in% features)
    Prob_List <- c(Prob_List, ifelse(row$FamilyCount>10, Probability_By_FamilyCount[2,9], 
                                     Probability_By_FamilyCount[2,which(colnames(Probability_By_FamilyCount) == row$FamilyCount)]))
  # Since the maximum value of feature FamilyCount is 0, any value greater than 10 will use the probability of 10 as the value used in the calculation
  
  if("Cabin" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Cabin[2,which(colnames(Probability_By_Cabin) == row$Cabin)])
  
  if("Embarked" %in% features)
    Prob_List <- c(Prob_List, Probability_By_Embarked[2,which(colnames(Probability_By_Embarked) == row$Embarked)])
  
  if("Fare" %in% features)
    Prob_List <- c(Prob_List, ifelse((row[,"Fare"] >= 0 & row[,"Fare"] < GroupCut_Fare[1]), Probability_By_GroupedFare[2,1], 
                                     ifelse((row[,"Fare"] >= GroupCut_Fare[1] & row[,"Fare"] < GroupCut_Fare[2]), Probability_By_GroupedFare[2,2],
                                            ifelse((row[,"Fare"] >= GroupCut_Fare[2] & row[,"Fare"] < GroupCut_Fare[3]), Probability_By_GroupedFare[2,3],
                                                   ifelse((row[,"Fare"] >= GroupCut_Fare[3] & row[,"Fare"] < GroupCut_Fare[4]), Probability_By_GroupedFare[2,4],
                                                          ifelse((row[,"Fare"] >= GroupCut_Fare[4]),  Probability_By_GroupedFare[2,5]))))))
  Prob_NS <- prod(Prob_List)
  return(Prob_NS)
}

#--------------------------------------------------------#
# Read Data From CSV Files
#--------------------------------------------------------#
dev.off()
# Set the current directory to directory of the opened file
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
currentdirectory <- getwd()

# Read Data from files
traindata = read.csv("./train.csv")
testdata = read.csv("./test.csv")
surviveresult = read.csv("./survive_none.csv") # Loading the template of survival result

#=======================================================================================================================
#                                       Data Exploration by traindata without Missing Value 
# The Exploration will be based on Neive Beyes Classifier
#=======================================================================================================================

#--------------------------------------------------------#
# Preparation. Finding of Missing Value
# We should find out the missing value in the traindata for the decision of handling these data
#--------------------------------------------------------# 
# Count the Missing Value in traindata
DataMissingCount(traindata)
# Result: There are three columns has missing values, 
# including Age (177), Cabin (687) and Embarked (2), where number in () is the number of missing value in the column.

"
**********************************
According to some articles about Neive Beyes Classifier, There are three common method to handling the missing data,
  1. Omit records with any missing values (Ignore rows with missing values)
  2. Omit only the missing attributes (Ignore columns with missing values)
  3. Compute likelihood based on observed attributes

Decision:
I.  According to the Missing Count of each feature, The most Missing values are Age and Cabin,
    We will not considering these two feature
II. Also, There are two missing values in Embarked, Because of the small number of nulls in there,
    We will try to compute the likelihood based on our observation
    
References:
https://datascience.stackexchange.com/questions/3711/how-does-the-naive-bayes-classifier-handle-missing-data-in-training
https://www.youtube.com/watch?v=EqjyLfpv5oA
**********************************
"

#--------------------------------------------------------#
# Preparation. 
#--------------------------------------------------------#
# Remove two feature with most Missing values (Age and Cabin)
traindata$Cabin <- NULL
traindata$Age <- NULL

#--------------------------------------------------------#
# Data(Pclass). Survival Data with Pclass
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_Pclass <- count_SurvivalBy(traindata,traindata$Pclass)
print_BarPlot(SurvivalMatrix_By_Pclass, "Pclass")
"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: Class 3 -> 372 of 491
         Class 2 -> 97 of 184
lowest:  Class 1 -> 80 of 216
-------------
"

#--------------------------------------------------------#
# Data(Pclass & Sex). Survival Data with Pclass and Sex
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_Pclass_Sex <- count_SurvivalByTwoFeatures(traindata,traindata$Pclass, traindata$Sex)
print_BarPlot(SurvivalMatrix_By_Pclass_Sex, "Pclass and Sex")
"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: Class 3 & M -> 300 of 347
         Class 2 & M -> 91 of 108
         Class 1 & M -> 77 of 122
         Class 3 & F -> 72 of 144
         Class 2 & F -> 6 of 76
lowest:  Class 1 & F -> 3 of 94
         
-------------
"

#--------------------------------------------------------#
# Data(FamilyCount). Survival Data with SibSp and Parch (FamilyCount)
#--------------------------------------------------------#
# We can Group the Parch and SibSp as Family to Analyze the survival probability of passengers with peers
# Remove SibSp and Parch and Replace it by FamilyCount
traindata$FamilyCount <- (traindata$Parch + traindata$SibSp)
traindata$SibSp <- NULL
traindata$Parch <- NULL

#ggplot(traindata, aes(FamilyCount, Survived)) + geom_point() + stat_smooth(method = "lm", 
#                                                                           formula = y ~ x) + ggtitle("Relationship between FamilyCount and Survived")
#ggplot(traindata, aes(FamilyCount)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
#  labs(title="Survival with FamilyCount", 
#       x="FamilyCount (Parch + SibSp)",
#       fill="Survived") + scale_fill_manual(values = c("red","green")) + 
#  scale_x_continuous(breaks = seq(0, max(traindata$Parch + traindata$SibSp), by = 1))

# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_FamilyCount <- count_SurvivalBy(traindata,traindata$FamilyCount)
print_BarPlot(SurvivalMatrix_By_FamilyCount, "FamilyCount")
"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: 0 -> 374 of 537
         1 -> 72 of 161
         2 -> 43 of 102
         5 -> 19 of 22
         4 -> 12 of 15
         3 -> 8 of 29
         6 -> 8 of 12
         10 -> 7 of 7
lowest:  7 -> 6 of 6
-------------
"

#--------------------------------------------------------#
# Data(Sex). Survival Data with Sex
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_Sex <- count_SurvivalBy(traindata,traindata$Sex)
print_BarPlot(SurvivalMatrix_By_Sex, "Sex")
"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: M -> 468 of 577
lowest:  F -> 81 of 314
-------------
"

#--------------------------------------------------------#
# Cut Title of Name and Group it to three common titles in traindata 
#--------------------------------------------------------#
# Find out the title of name in each passenger and find the Unique title 
NameTitles_All_Beforereplacement <- c()
for(NameTitle in traindata$Name){
  NameTitle <- str_sub(NameTitle, str_locate(NameTitle, ",")[ , 1] + 2, str_locate(NameTitle, "\\.")[ , 1] - 1)
  NameTitles_All_Beforereplacement <- c(NameTitles_All_Beforereplacement, NameTitle)
}
NameTitles_Unique <- unique(NameTitles_All_Beforereplacement)

print(NameTitles_Unique)
# There are 17 Titles can be found,
# For handle the data easily, we will replace some title to Common titles.
# ['Capt', 'Col', 'Don', 'Jonkheer', 'Major', 'Rev', 'Sir'] will be change to Mr
# ['the Countess', 'Mme', 'Lady'] will be change to Mrs
# ['Mlle', 'Ms'] will be Change to Miss
# and Dr will be Change to Mr or Mrs, It will based on Sex.

# Add NameTitle as new column into data
traindata$NameTitle <- NameTitles_All_Beforereplacement

MrList <- list('Capt', 'Col', 'Don', 'Jonkheer', 'Major', 'Rev', 'Sir')
MrsList <- list('the Countess', 'Mme', 'Lady')
MissList <- list('Mlle', 'Ms')
for(i in 1:nrow(traindata)){
  if(traindata[i,"NameTitle"] == "Mr" || traindata[i,"NameTitle"] == "Mrs" || traindata[i,"NameTitle"] == "Miss")
    next
  if(traindata[i,"NameTitle"] %in% MrList) 
    traindata[i,"NameTitle"] <- "Mr"
    else if (traindata[i,"NameTitle"] %in% MrsList)
      traindata[i,"NameTitle"] <- "Mrs"
      else if (traindata[i,"NameTitle"] %in% MissList)
        traindata[i,"NameTitle"] <- "Miss"
        else if (traindata[i,"NameTitle"] == "Dr"){
          if(traindata[i,"Sex"] == "male")
            traindata[i,"NameTitle"] <- "Mr"
          else traindata[i,"NameTitle"] <- "Mrs"
        }
            else if (traindata[i,"NameTitle"] == "Master"){
              if(traindata[i,"Sex"] == "male")
                traindata[i,"NameTitle"] <- "Mr"
              else traindata[i,"NameTitle"] <- "Mrs"
            }
}

# Remove Name Column, Because we created the Name Title Column already
traindata$Name <- NULL
traindata$NameTitle <- as.factor(traindata$NameTitle)

#--------------------------------------------------------#
# Data(Title). Survival Data with Name Title
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_NameTitle <- count_SurvivalBy(traindata,traindata$NameTitle)
print_BarPlot(SurvivalMatrix_By_NameTitle, "NameTitle")

"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: Mr -> 468 of 577
         Miss -> 55 of 185
lowest:  Mrs -> 26 of 129
-------------
"

#--------------------------------------------------------#
# Data(Title & Pclass) Survival Data with Name Title and Pclass
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_NameTitle_Pclass <- count_SurvivalByTwoFeatures(traindata,traindata$NameTitle, traindata$Pclass)
print_BarPlot(SurvivalMatrix_By_NameTitle_Pclass, "NameTitle and Pclass")

"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: Mr Class3 -> 300 of 347
         Mr Class2 -> 91 of 108
         Mr Class1 -> 77 of 122
         Miss Class3 -> 51 of 102
         Mrs Class3 -> 21 of 42
         Mrs Class2 -> 4 of 41
         Miss Class1 -> 2 of 48
         Miss Class2 -> 2 of 35
lowest:  Mrs 1 -> 1 of 46
-------------
"

#--------------------------------------------------------#
# Handle the missing value in Embarked
#--------------------------------------------------------#
MissingEmbarkedRow_Train <- traindata[is.na(traindata$Embarked), c(1,3,7)] # --> The PassengerId withour Embarked: 62, 830 and Fare is also 80
traindata_embarked <- subset(traindata, traindata$Embarked != "")
traindata_embarked <- droplevels(traindata_embarked)
ggplot(traindata_embarked, aes(Pclass, Fare, group=Pclass)) + geom_boxplot() + facet_grid(. ~ Embarked) + scale_x_continuous(breaks = seq(0, 3, by = 1)) + 
  geom_hline(aes(yintercept=80), # 80 is the fare result in MissingEmbarkedRow_Train 
             colour='red', lwd=1) + ggtitle("Prediction of Missing Value in Embarked and Fare Distribution with Pclass and Embarked") 
# From above result, We should exclude the possibility of these two passengers boarded at Q, because there are too few passengers boarded at Q,
# Next, These two passengers are in Class 1 (Pclass), and the fare is also 80. 
# Refer to the plot, There are many people in Class 1 and ther fare are also around 80,
# We should put these two passengers at C as First consideration not S
traindata$Embarked[c(62, 830)] <- "C"

#--------------------------------------------------------#
# Data(Embarked) survival Data with Embarked
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_Embarked <- count_SurvivalBy(traindata,traindata$Embarked)
print_BarPlot(SurvivalMatrix_By_Embarked, "Embarked")

"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: S -> 427 of 644
         C -> 75 of 170
lowest:  Q -> 47 of 77
-------------
"

#--------------------------------------------------------#
# Data(Embarked & Pclass) survival Data with Embarked and Pclass
#--------------------------------------------------------#
# Count out the number of Surviver (1) and non-surviver (0) and print out the related barplot
SurvivalMatrix_By_Embarked_Pclass <- count_SurvivalByTwoFeatures(traindata,traindata$Embarked, traindata$Pclass)
print_BarPlot(SurvivalMatrix_By_Embarked_Pclass, "Embarked and Pclass")

"
-------------
Observation: 
Sorting number of Non-Surviver in descending order:
Highest: S Class3 -> 286 of 353
         S Class2 -> 88 of 164
         S Class1 -> 53 of 127
         Q Class3 -> 45 of 72
         C Class3 -> 41 of 66
         C Class1 -> 26 of 87
         C Class2 -> 8 of 17
         Q Class2 -> 1 of 3
lowest:  Q Class1 -> 1 of 2
-------------
"

# Check again the Missing Count in traindata
# There should no any Missing Value
DataMissingCount(traindata)

#=======================================================================================================================
#                                                   Feature Engineering
# A. Calculate the probability in each feature and overall survival.
# B. Handle the missing data in testdata based on methods we mentioned in Data Exploration
#=======================================================================================================================

#=======================================================================================================================
# A. Calculate the probability in each feature and overall survival.
#=======================================================================================================================
#--------------------------------------------------------#
# P(OverallProb)
# Overall Survival and Not Survival Probability
#--------------------------------------------------------#
# Calculate the probability of overall survival and not survival 
SurvivalChance_Overall <- sum(traindata$Survived == 1) / ((sum(traindata$Survived == 0) + sum(traindata$Survived == 1)))
NotSurvivalChance_Overall <- sum(traindata$Survived == 0) / ((sum(traindata$Survived == 0) + sum(traindata$Survived == 1)))

#--------------------------------------------------------#
# P(Pclass)
# Survival and Not Survival Probability with Pclass
#--------------------------------------------------------#
# Calculate The Survival Probability
Probability_By_Pclass <- calculate_Probability(SurvivalMatrix_By_Pclass)

"
-------------
Observation: 
The ticket class will affect the survival probability, the lower ticket class, the less chance of survival
	            1         2         3
P(S)	0.6296296	0.4728261	0.2423625
P(NS)	0.3703704	0.5271739	0.7576375
-------------
"

#--------------------------------------------------------#
# P(FamilyCount)
# Survival and Not Survival Probability with SibSp and Parch (FamilyCount)
#--------------------------------------------------------#
# Calculate The Survival Probability
Probability_By_FamilyCount <- calculate_Probability(SurvivalMatrix_By_FamilyCount)

"
-------------
Observation: 
The survival rate will change according to the number of families. 
The survival rate is the highest when the number of families is 3. 
When it is greater than 3, there will be a sharp decline, 
that is, the survival rate of the family number of 4 or more is low

              0        1          2         3   4         5         6  7   10
P(S)	0.3035382	0.552795	0.5784314	0.7241379	0.2	0.1363636	0.3333333	 0	  0
P(NS)	0.6964618	0.447205	0.4215686	0.2758621	0.8	0.8636364	0.6666667	 1	  1  
-------------
"

#--------------------------------------------------------#
# P(Sex)
# Survival and Not Survival Probability with Sex
#--------------------------------------------------------#
# Calculate The Survival Probability
Probability_By_Sex <- calculate_Probability(SurvivalMatrix_By_Sex)

"
-------------
Observation: 
The survival probability of women is greater than men.
	
         female      male
P(S)	0.7420382	0.1889081
P(NS)	0.2579618	0.811091
-------------

"
#--------------------------------------------------------#
# P(Title)
# Survival and Not Survival Probability with Title
#--------------------------------------------------------#
# Calculate The Survival Probability
Probability_By_NameTitle <- calculate_Probability(SurvivalMatrix_By_NameTitle)

"
-------------
Observation: 
The result is similar to Sex, The survival probability of Miss and Mrs (Female) are higher than Mr (Male)
           Miss        Mr       Mrs
P(S)	0.7027027	0.1889081	0.7984496
P(NS)	0.2972973	0.8110919	0.2015504
-------------
"

#--------------------------------------------------------#
# P(Embarked)
# Survival and Not Survival Probability with Embarked
#--------------------------------------------------------#
# Calculate The Survival Probability
Probability_By_Embarked <- calculate_Probability(SurvivalMatrix_By_Embarked)

"
-------------
Observation: 
              C         Q         S
P(S)  0.5588235 0.3896104 0.3369565
P(NS) 0.4411765 0.6103896 0.6630435
-------------
"


#--------------------------------------------------------#
# P(Fare)
# Survival Probability with Grouped Fare
#--------------------------------------------------------#
# discretize refer to https://www.rdocumentation.org/packages/recipes/versions/0.1.9/topics/discretize
# Cut the fare to five group in traindata
GroupCut_Fare <- discretize(traindata$Fare, cuts=5)$breaks[2:5]

count_surviver <- c()
count_nonsurviver <- c()

# Group 1
count_surviver <- c(count_surviver, sum(traindata$Survived==1&(traindata$Fare >= 0 & traindata$Fare < GroupCut_Fare[1])))
count_nonsurviver <- c(count_nonsurviver, sum(traindata$Survived==0&(traindata$Fare >= 0 & traindata$Fare < GroupCut_Fare[1])))

# Group 2
count_surviver <- c(count_surviver, sum(traindata$Survived==1&(traindata$Fare >= GroupCut_Fare[1] & traindata$Fare < GroupCut_Fare[2])))
count_nonsurviver <- c(count_nonsurviver, sum(traindata$Survived==0&(traindata$Fare >= GroupCut_Fare[1] & traindata$Fare < GroupCut_Fare[2])))

# Group 3
count_surviver <- c(count_surviver, sum(traindata$Survived==1&(traindata$Fare >= GroupCut_Fare[2] & traindata$Fare < GroupCut_Fare[3])))
count_nonsurviver <- c(count_nonsurviver, sum(traindata$Survived==0&(traindata$Fare >= GroupCut_Fare[2] & traindata$Fare < GroupCut_Fare[3])))

# Group 4
count_surviver <- c(count_surviver, sum(traindata$Survived==1&(traindata$Fare >= GroupCut_Fare[3] & traindata$Fare < GroupCut_Fare[4])))
count_nonsurviver <- c(count_nonsurviver, sum(traindata$Survived==0&(traindata$Fare >= GroupCut_Fare[3] & traindata$Fare < GroupCut_Fare[4])))

# Group 5
count_surviver <- c(count_surviver, sum(traindata$Survived==1&(traindata$Fare >= GroupCut_Fare[4])))
count_nonsurviver <- c(count_nonsurviver, sum(traindata$Survived==0&(traindata$Fare >= GroupCut_Fare[4])))

SurvivalMatrix_By_Fare = matrix(c(count_surviver,count_nonsurviver), nrow=2,ncol=5,byrow = TRUE)
rownames(SurvivalMatrix_By_Fare) <- c("Survival", "Not Survival")
colnames(SurvivalMatrix_By_Fare) <- c(paste("0 ~",GroupCut_Fare[1]), 
                                      paste(GroupCut_Fare[1]," ~ ",GroupCut_Fare[2]), 
                                      paste(GroupCut_Fare[2]," ~ ",GroupCut_Fare[3]), 
                                      paste(GroupCut_Fare[3]," ~ ",GroupCut_Fare[4]), 
                                      paste(">",GroupCut_Fare[4]))

Probability_By_GroupedFare <- calculate_Probability(SurvivalMatrix_By_Fare)

#=======================================================================================================================
# B. Handle the missing data in testdata based on methods we mentioned in Data Exploration
#=======================================================================================================================
"
**********************************
Recap from the part of our Data Exploration 
According to some articles about Neive Beyes Classifier, There are three common method to handling the missing data,
  1. Omit records with any missing values (Ignore rows with missing values)
  2. Omit only the missing attributes (Ignore columns with missing values)
  3. Compute likelihood based on observed attributes

References:
https://datascience.stackexchange.com/questions/3711/how-does-the-naive-bayes-classifier-handle-missing-data-in-training
https://www.youtube.com/watch?v=EqjyLfpv5oA
**********************************
"

#--------------------------------------------------------#
# Preparation. Finding of Missing Value
# We should find out the missing value in the testdata for the decision of handling these data
#--------------------------------------------------------# 
# Count the Missing Value in traindata
DataMissingCount(testdata)
# Result: There are three columns has missing values, 
# including Age (86), Cabin (327) and Fare (1), where number in () is the number of missing value in the column.


"
Decision of handling the missing data in testdata:
I.  We ignored Age and Cabin in traindata, so we will also remove the Age and Cabin in testdata 
II. There is 1 missing value in Fare, Because of the small number of nulls in there,
    We will try to compute the likelihood based on our observation.
"

#--------------------------------------------------------#
# Handle The Missing Value of Age and Cabin in testdata
#--------------------------------------------------------#
testdata$Age <- NULL
testdata$Cabin <- NULL

#--------------------------------------------------------#
# Group the SibSp and Parch to FamilyCount in testdata
#--------------------------------------------------------#

# We can Group the Parch and SibSp as Family to Analyze the survival probability of passengers with peers
# Remove SibSp and Parch and Replace it by FamilyCount
testdata$FamilyCount <- (testdata$Parch + testdata$SibSp)
testdata$SibSp <- NULL
testdata$Parch <- NULL

#--------------------------------------------------------#
# Cut Title of Name and Group it to three common titles in testdata 
#--------------------------------------------------------#
# Replace the Name by NameTitle in testdata
# Find out the title of name in each passenger and find the Unique title 
NameTitles_All_Beforereplacement <- c()
for(NameTitle in testdata$Name){
  NameTitle <- str_sub(NameTitle, str_locate(NameTitle, ",")[ , 1] + 2, str_locate(NameTitle, "\\.")[ , 1] - 1)
  NameTitles_All_Beforereplacement <- c(NameTitles_All_Beforereplacement, NameTitle)
}
NameTitles_Unique <- unique(NameTitles_All_Beforereplacement)

print(NameTitles_Unique)
# There are 17 Titles can be found,
# For handle the data easily, we will replace some title to Common titles.
# ['Capt', 'Col', 'Don', 'Jonkheer', 'Major', 'Rev', 'Sir'] will be change to Mr
# ['the Countess', 'Mme', 'Lady'] will be change to Mrs
# ['Mlle', 'Ms'] will be Change to Miss
# and Dr will be Change to Mr or Mrs, It will based on Sex.

# Add NameTitle as new column into data
testdata$NameTitle <- NameTitles_All_Beforereplacement

MrList <- list('Capt', 'Col', 'Don', 'Jonkheer', 'Major', 'Rev', 'Sir')
MrsList <- list('the Countess', 'Mme', 'Lady','Dona')
MissList <- list('Mlle', 'Ms')
for(i in 1:nrow(testdata)){
  if(testdata[i,"NameTitle"] == "Mr" || testdata[i,"NameTitle"] == "Mrs" || testdata[i,"NameTitle"] == "Miss")
    next
  if(testdata[i,"NameTitle"] %in% MrList) 
    testdata[i,"NameTitle"] <- "Mr"
  else if (testdata[i,"NameTitle"] %in% MrsList)
    testdata[i,"NameTitle"] <- "Mrs"
  else if (testdata[i,"NameTitle"] %in% MissList)
    testdata[i,"NameTitle"] <- "Miss"
  else if (testdata[i,"NameTitle"] == "Dr"){
    if(testdata[i,"Sex"] == "male")
      testdata[i,"NameTitle"] <- "Mr"
    else testdata[i,"NameTitle"] <- "Mrs"
  }
  else if (testdata[i,"NameTitle"] == "Master"){
    if(testdata[i,"Sex"] == "male")
      testdata[i,"NameTitle"] <- "Mr"
    else testdata[i,"NameTitle"] <- "Mrs"
  }
}

# Remove Name Column, Because we created the Name Title Column already
testdata$Name <- NULL
testdata$NameTitle <- as.factor(testdata$NameTitle)

#--------------------------------------------------------#
# Handle The Missing Value of Fare in testdata
#--------------------------------------------------------#
# Find Missing Value in Fare
MissingFareRow_Test <- testdata[is.na(testdata$Fare), c("PassengerId","Pclass","FamilyCount")]
# Result: Missing Fare PassengerId = 1044 and Pclass = 3,FamilyCount = 0
Fare_Class3 <- testdata[testdata$Pclass == 3 & testdata$FamilyCount == 0, c("PassengerId","Pclass","Fare","FamilyCount")]
Fare_Class3 <- na.omit(Fare_Class3)
ggplot(Fare_Class3, aes(FamilyCount,Fare, group=Fare)) + ggtitle("Fare Distribution in Class 3 when FamilyCount = 0") + 
  geom_boxplot() + scale_x_continuous(breaks = seq(0, 10, by = 1)) + 
  scale_y_continuous(breaks = seq(0, 100, by = 10))
"
Result and Decision: 
The Fare Distribution in Class 3 when passenger is no any siblings / spouses and parents / children (FamilyCount = 0)
showing that the maximun Fare is less than 75 and most of fare is less than 10. We will replace this with the mean of Fare_Class3
"
testdata$Fare[testdata$PassengerId == 1044] <- mean(Fare_Class3$Fare)

# Check again the Missing Count in testdata
# There should no any Missing Value
DataMissingCount(testdata)

#=======================================================================================================================
#                                                 Final: Output the Surviver Result
#=======================================================================================================================
Features <- list("Pclass","NameTitle","Sex","FamilyCount","Fare", "Embarked")
for (i in 1:nrow(testdata)){
  # PMM Result
  Survived <- ifelse((Calculate_Prob_S_NaiveBayesModel(testdata[i,],Features) > Calculate_Prob_NS_NaiveBayesModel(testdata[i,],Features)), 1, 0)
  #cat(surviveresult[i,1],surviveresult[i,2],"-->",Survived, "\n")
  surviveresult[i,2] <- Survived
}

cat(sum(surviveresult$Survived == 1), sum(surviveresult$Survived == 0),"\n")

#--------------------------------------------------------#
# Write back the dataframe into CSV file
#--------------------------------------------------------#
# Write the data frame after the above operations to CSV file
output_file_name <- paste("Data_Result_NaiveBeyes_WithoutSex.csv",sep = "")
setwd(currentdirectory)
write.csv(surviveresult, paste(currentdirectory,"/",output_file_name,sep = ""), row.names = FALSE)

testdata$Survived <- surviveresult$Survived

#=======================================================================================================================
#                      Data Summaries: Summary all data in both two data after Handling Missing Value
#*** Before Execute this part, please execute the above statement first.
#=======================================================================================================================

#=======================================================================================================================
# Summary of each column in traindata
# Execute part by part
#=======================================================================================================================

#--------------Part 1 Start----------------
# Summary in Each Feature (Mean, Count, Median, Range)
summary(traindata$FamilyCount)
summary(traindata$Pclass)
summary(traindata$NameTitle)
summary(traindata$Fare)
summary(traindata$Embarked)
summary(traindata$Sex)

# Print Survival Distribution Plot that showing the result or statistics in Numeric data
SurvivalDistributionPlot_FamilyCount <- ggplot(traindata, aes(FamilyCount)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
  labs(title="FamilyCount Distribution of Surviver and Non-Surviver", 
       x="Age",
       fill="Survived") + scale_fill_manual(values = c("red","green"))

SurvivalDistributionPlot_Pclass <- ggplot(traindata, aes(Pclass)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
  labs(title="Pclass Distribution of Surviver and Non-Surviver", 
       x="Pclass",
       fill="Survived") + scale_fill_manual(values = c("red","green"))

SurvivalDistributionPlot_Fare <- ggplot(traindata, aes(Fare)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
  labs(title="Fare Distribution of Surviver and Non-Surviver", 
       x="Fare",
       fill="Survived") + scale_fill_manual(values = c("red","green"))

grid.arrange(SurvivalDistributionPlot_FamilyCount, SurvivalDistributionPlot_Pclass,
             SurvivalDistributionPlot_Fare,
             nrow = 2, ncol = 2)
#--------------Part 1 End----------------

#--------------Part 2 Start----------------
# Print BarPlots that showing the result or statistics in each feature
dev.off()
par(mfrow=c(3,3))
print_BarPlot(SurvivalMatrix_By_Pclass, "Pclass")
print_BarPlot(SurvivalMatrix_By_Pclass_Sex, "Pclass and Sex")
print_BarPlot(SurvivalMatrix_By_Sex, "Sex")
print_BarPlot(SurvivalMatrix_By_FamilyCount, "FamilyCount")
print_BarPlot(SurvivalMatrix_By_NameTitle, "NameTitle")
print_BarPlot(SurvivalMatrix_By_NameTitle_Pclass, "NameTitle and Pclass")
print_BarPlot(SurvivalMatrix_By_Embarked, "Embarked")
print_BarPlot(SurvivalMatrix_By_Embarked_Pclass, "Embarked and Pclass")
par(fig = c(.75, 1, 0, .25), oma = c(0, 0, 0, 0), mar = c(0, 0, 0, 0), new = TRUE)
legend("bottomright",
       c("Not Survived","Survived"),
       fill = c("red","green"),
       inset = c(0, 0), bty = "n", col = 1:4, cex = 1.5, xpd = T)

#--------------Part 2 End----------------


#=======================================================================================================================
# Summary of each column in testdata
#=======================================================================================================================
#--------------Part 3 Start----------------
# Summary in Each Feature (Mean, Count, Median, Range)
summary(testdata$FamilyCount)
summary(testdata$Pclass)
summary(testdata$NameTitle)
summary(testdata$Fare)
summary(testdata$Embarked)
summary(testdata$Sex)

# Count out the surviver and Non-surviver by following feature
SurvivalMatrix_By_Pclass_Test <- count_SurvivalBy(testdata,testdata$Pclass)
SurvivalMatrix_By_Pclass_Sex_Test <- count_SurvivalByTwoFeatures(testdata,testdata$Pclass, testdata$Sex)
SurvivalMatrix_By_FamilyCount_Test <- count_SurvivalBy(testdata,testdata$FamilyCount)
SurvivalMatrix_By_Sex_Test <- count_SurvivalBy(testdata,testdata$Sex)
SurvivalMatrix_By_NameTitle_Test <- count_SurvivalBy(testdata,testdata$NameTitle)
SurvivalMatrix_By_NameTitle_Pclass_Test <- count_SurvivalByTwoFeatures(testdata,testdata$NameTitle, testdata$Pclass)
SurvivalMatrix_By_Embarked_Test <- count_SurvivalBy(testdata,testdata$Embarked)
SurvivalMatrix_By_Embarked_Pclass_Test <- count_SurvivalByTwoFeatures(testdata,testdata$Embarked, testdata$Pclass)

# Print Survival Distribution Plot that showing the result or statistics in Numeric data
SurvivalDistributionPlot_FamilyCount <- ggplot(testdata, aes(FamilyCount)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
  labs(title="FamilyCount Distribution of Surviver and Non-Surviver", 
       x="Age",
       fill="Survived") + scale_fill_manual(values = c("red","green"))

SurvivalDistributionPlot_Pclass <- ggplot(testdata, aes(Pclass)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
  labs(title="Pclass Distribution of Surviver and Non-Surviver", 
       x="Pclass",
       fill="Survived") + scale_fill_manual(values = c("red","green"))

SurvivalDistributionPlot_Fare <- ggplot(testdata, aes(Fare)) + geom_density(aes(fill=factor(Survived)), alpha=0.6) + 
  labs(title="Fare Distribution of Surviver and Non-Surviver", 
       x="Fare",
       fill="Survived") + scale_fill_manual(values = c("red","green"))

grid.arrange(SurvivalDistributionPlot_FamilyCount, SurvivalDistributionPlot_Pclass,
             SurvivalDistributionPlot_Fare,
             nrow = 2, ncol = 2)

#--------------Part 3 End----------------

#--------------Part 4 Start----------------
# Print BarPlots that showing the result or statistics in each feature
dev.off()
par(mfrow=c(3,3))
print_BarPlot(SurvivalMatrix_By_Pclass_Test, "Pclass_Test")
print_BarPlot(SurvivalMatrix_By_Pclass_Sex_Test, "Pclass and Sex_Test")
print_BarPlot(SurvivalMatrix_By_FamilyCount_Test, "Sex_Test")
print_BarPlot(SurvivalMatrix_By_Sex_Test, "FamilyCount_Test")
print_BarPlot(SurvivalMatrix_By_NameTitle_Test, "NameTitle_Test")
print_BarPlot(SurvivalMatrix_By_NameTitle_Pclass_Test, "NameTitle and Pclass_Test")
print_BarPlot(SurvivalMatrix_By_Embarked_Test, "Embarked_Test")
print_BarPlot(SurvivalMatrix_By_Embarked_Pclass_Test, "Embarked and Pclass_Test")
par(fig = c(.75, 1, 0, .25), oma = c(0, 0, 0, 0), mar = c(0, 0, 0, 0), new = TRUE)
legend("bottomright",
       c("Not Survived","Survived"),
       fill = c("red","green"),
       inset = c(0, 0), bty = "n", col = 1:4, cex = 1.5, xpd = T)
#--------------Part 4 End----------------

#--------------Part 5 Start----------------
print(Probability_By_Embarked)
print(Probability_By_FamilyCount)
print(Probability_By_GroupedFare)
print(Probability_By_NameTitle)
print(Probability_By_Pclass)
print(Probability_By_Sex)
#--------------Part 5 End----------------






