import random

list_of_chara = []
for i in range(33,127):
    list_of_chara.append(chr(i))


def pw_gen():
    pw = ""
    strength = input("Do you want a weak or strong random password? (weak/strong) ").lower()
    if strength == "strong":
        pwlen = random.randint(8,14)
        pw = "".join(random.sample(list_of_chara,pwlen))
    elif strength == "weak":
        pwlen = random.randint(4,7)
        pw = "".join(random.sample(list_of_chara,pwlen))
    else:
        print("Invalid input!")
    return pw


print(pw_gen())
