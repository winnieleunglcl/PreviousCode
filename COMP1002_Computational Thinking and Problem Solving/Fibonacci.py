def fibonnaci():
    number = int(input("How many fibonnaci numbers you wanted to generate? "))
    a = 0
    b = 1
    list_of_fibonnaci = []
    if number == 0:
        return list_of_fibonnaci
    else:
        for i in range(number):
            a,b = b,a+b
            list_of_fibonnaci.append(a)
        return list_of_fibonnaci

print(fibonnaci())

