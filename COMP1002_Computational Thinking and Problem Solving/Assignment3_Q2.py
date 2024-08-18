import math

def rootTwo(n):

  appro = 1

  for k in range (1,n):
    value = 1+1/(appro+1)
    appro = value
  return appro


def main():
  print("RootTwo=",math.sqrt(2))
  for i in range(1,6):
      value = rootTwo(i)
      b = math.sqrt(2) - value
      if b < 0:
          b = b*-1
      print("Value with",i,"terms=",value,", error=",b)
 
main()

# Observation: when n increases, the error decreases.
#              This means that the more number of terms is used,
#              the more accurate is the approximation.
