def harry(s,t):
  
  # creat an array to store the number of each letter in string1 and string2
  # set each element for each lower case letter, i.e. 26 elements are there
  # a[0] represents the sum of the number of 'a' in string 1 and string 2, a[1] represents b and etc.
  
  a = [0]*26
  
  boolean = True
  for i in s:
    if i != " ":
      a[ord(i)-97] += 1
  for j in t:
    if j != " ":
      a[ord(j)-97] -= 1
  for k in range(0,26):
    if a[k] != 0:
      boolean = False
      break
  # if two strings satisfy the transformation, all the elements in a must equal to 0. Else, they do not
  
  print("Checking ",s,'" with "',t,'":',boolean)
  
  for m in range(0,26):
    if a[m] > 0 :
      print ("Too many",chr(m+97))
    if a[m] < 0 :
      print ("Too few",chr(m+97))
 # return the too many or too few occurances by refering to the ASCII code of each lower case letter
      



harry("tom marvolo riddle", "i am lord voldemort")
harry("harry potter", "my hero part")
harry("a computer", "our pet mac")

