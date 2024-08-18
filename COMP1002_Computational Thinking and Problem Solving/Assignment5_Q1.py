def move(s1,s2):
   direction = ["E","W"]
   # avaliable directions are east and west
   i = 0
   illegal = [""] * 6
   # illegal is an array to store all illegal states
   for C in direction:
       for G in direction:
           for M in direction:
               for W in direction:
                   if ((M != G and G==W) or (M != G and G==C)):
                       x = "" + C + G + M + W
                       illegal[i] = x
                       i += 1

   print(s1,s2,end = " ")
   # first, print the s1 and s2 since it depends on user's input and it will not change after implementing the program
   
   for j in illegal:
           if s1==j or s2 == j:
              print ("Illegal move")
              return
   c = 0
   for i in range(0,4):
          if s2[i] != s1[i]:
             c+=1
   if c>2:
      print("illegal move")
      return

   # define illegal move, condition 1: s2 == illegal states
   #                      condition 2: more than 2 elements move
   
   chara = ["Cabbage","Goat","Man","Wolf"]
   a = False
   v = ""

   for i in range(0,4):
          if s2[i] != s1[i]:
             if a == True:
                  print(" and",chara[i], end = "")
                  a = False
                  break                  
             v = s2[i]
             print(chara[i], end = "")
             a = True
   # find whether only the man moves or the man moves with another element
   # use v to find the direction of moving

   print(" move", end = "")
   if a:
      print("s" , end = "")
   if v == "W":
      print(" from east to west")
   else:
      print(" from west to east")

sol = ("EEEE","EWWE","EWEE","WWWE","WEEE","WEWW","WEEW","WWWW")
for i in range(1,len(sol)):
    move(sol[i-1],sol[i])
print()
sol = ("EEEE","EWWE","EWEE","EWWE","EWEE","WWWE","WEEE","WEWW","WEEW","WWWW")
for i in range(1,len(sol)):
    move(sol[i-1],sol[i])
print()
sol =("EEEE","EWWE","EWEE","WWWE","WWEE","WWWE","EWEE","WWWW")
for i in range(1,len(sol)):
    move(sol[i-1],sol[i])
