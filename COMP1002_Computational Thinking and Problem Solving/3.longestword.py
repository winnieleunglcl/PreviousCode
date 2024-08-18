def LongestWord():
    string = input("Input the string to find the largest word: ")
    x = string.split(" ")
    print ("The longest word is",(max(x, key=len)))

LongestWord()

def longword():
    string = input("Input the string to find the largest word: ").split(" ")
    longest = string[0]
    for i in range(len(string)):
        if len(string[i]) > len(longest):
            longest = string[i]       
    print ("The longest word is",longest)

longword()
