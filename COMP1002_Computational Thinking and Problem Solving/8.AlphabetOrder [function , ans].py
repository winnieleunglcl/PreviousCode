def AlphabetSoup(string):
    chars = list(string)
    sortedChars = sorted(chars)
    return "".join(sortedChars)


print (AlphabetSoup("coderbyte"))
