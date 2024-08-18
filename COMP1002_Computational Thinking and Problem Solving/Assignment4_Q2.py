def genLegalStates():
  for M in ['E','W']:
      for C in ['E','W']:
          for G in ['E','W']:
              for W in ['E','W']:
                  if ((M != G and G==W) or (M != G and G==C)):
                    continue
                  #these 2 conditions represent the constraints that the goat cannot stay with the wolf alone and the cabbage cannot stay with the goat alone without the man
                  #'continue' function makes the program skip the next step 'print(M,C,G,W)' when the condition is met so that next loop can be ran
                  print(M,C,G,W)

genLegalStates()
