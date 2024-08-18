def reverse_v1(string):
    string_list = string.split()
    return " ".join(string_list[::-1])

def reverse_v2(string):
    string_list = string.split()
    result = []
    for word in string_list:
        result.insert(0,word)
    return " ".join(result)

a = input("Input a long string to reverse its order: ")
print(reverse_v1(a))
print(reverse_v2(a))
