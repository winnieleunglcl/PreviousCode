def LetterChanges():
    string = input("Input the string to replace every letter with the letter following: ")
    for i in string:
        if i != " ":
           if (i == "z") or (i == "Z"):
              i = chr(ord(i)-25)
           else:
              i = chr(ord(i)+1)
           if i in 'aeiou':
              i = chr(ord(i)-32)
           print(i)
           
LetterChanges()
