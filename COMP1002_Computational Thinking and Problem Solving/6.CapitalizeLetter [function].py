def LetterCapitalize():
    string = input("Input the string to capitalze the first letter of each word: ")
    words = string.split(" ")
    for i in range(0,len(words)):
        words[i] = chr(ord(words[i][0])-32) + words[i][1:]
        a = " ".join(words)
    print(a)
    
LetterCapitalize()
