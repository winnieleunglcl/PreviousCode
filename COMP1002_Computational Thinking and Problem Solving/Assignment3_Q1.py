def passingAt(f,t):
    ans = pow(f, t-1) * (1-f)
    return str(ans)

def passingBy(f,t):
    a = eval(passingAt(f,1))
    b = a
    for k in range (1,t):
      a = f*a
      b = b+a
    return str(b)

def a():
     f, T = 0.1, 4
     for i in range(1,T+1):
         print("f="+str(f)+",","Pr(T="+str(i)+")="+passingAt(f,i))
     f, T = 0.2, 5
     for i in range(1,T+1):
         print("f="+str(f)+",","Pr(T="+str(i)+")="+passingAt(f,i))

def main():
    f, T = 0.1, 4
    print("f="+str(f)+",","Pr(T<="+str(T)+")="+passingBy(f,T))
    f, T = 0.2, 5
    print("f="+str(f)+",","Pr(T<="+str(T)+")="+passingBy(f,T))

a()
main()


# Numbers of multiplications in: i) a loop to PassingAt = 11
#                                ii) PassingBy = 5
