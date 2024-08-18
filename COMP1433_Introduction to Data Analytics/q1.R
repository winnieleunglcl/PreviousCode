f1 <- function(x,n){
  sum = 0
  for (i in 1:n){         #just loop n times to reach the last element
    sum = sum + i*(x^i)   #each term in the sequence is in a format i * x^i (n is the largest value for i)
  }
  return(sum)
}

#given case
result1 = f1(1,3)
print(result1)


f2 <- function(x){
  if (length(x)==0){      #if x contains no element
    return(NA)
  }
  sum = 0
  for (i in 1:length(x)){           #loop for all elements in x
    if (x[i]%%2==0 | x[i]%%3==0){   #if an element in x is divisible by 2 or 3
      sum = sum + x[i]              #sum it up
    }
  }
  return(sum)                       #return sum, if no element in x is divisible by 2 or 3, the sum will be 0 by default
}

#given case
numbers2 <- c(1,3,5,6,8)
result2 = f2(numbers2)
print(result2)


f3 <- function(x,n){
  if (length(x)<n){      #if n is larger than size of x
    return(NA)
  }
  number = sort(x,partial=length(x)-n+1)[length(x)-n+1]  #find the n-th largest number in x
  return(number)
}

#given case
numbers3 <- c(1,3,5,6,8)
result3 = f3(numbers3,2)
print(result3)


f4 <- function(x){
  m = length(x)       #Calculate m (number of groups)
  n = 0
  for (i in 1:m){
    if (x[i] < 0){    #If there is any elements in x which is a negative integer
      return(NA)
    }
    else{
      n = n + x[i]    #Calculate n (total number of students)
    }
  }
  result = 1
  for (i in 1:m){
    result = result * ( factorial(n) / ( factorial(x[i]) * factorial(n-x[i]) ) )   #count possible solutions with the formula for combination
    n = n - x[i]
  }
  return(result)
}

#given case
numbers4 <- c(2,3,1)
result4 = f4(numbers4)
print(result4)
