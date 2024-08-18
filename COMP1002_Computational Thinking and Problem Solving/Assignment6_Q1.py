def crypto(m,N,order):

    
# first, find the total number of characters after encryption or decryption (including z) 
# it can be found by the remainder of dividing length of the message (m) by the number of columns (N)
    number_of_character = len(m)
    while number_of_character % N != 0:
        number_of_character += 1

        

# create lists with the total number of characters to store each character in the message and assign each of them in corresponding place
    index = 0
    letters = [""]*number_of_character
    for j in m:
        letters[index] = j
        index += 1



# fill in the last row's empty space with "z" if necessary
    for k in range(0,number_of_character):
        if letters[k] == "":
            letters[k] = "z"

            

# find number of rows
    number_of_row = number_of_character // N




    
# let user input to decide performing encryption or decrpytion  
    D_or_E = input("Please enter your choice (E/D): ")
    

# loop the input session until the user input a valid choice
    while (D_or_E != "E") and (D_or_E != "e") and (D_or_E != "D") and (D_or_E != "d"):
        D_or_E = input("Invalid choice, please try again: ")




    result = ""
    all_elements=[]
    index = 0     

    
# start the encryption process
    if D_or_E == "E" or D_or_E == "e":
        

       for i in range(number_of_row):
           row = []
           # store each group of N elements in a 'row'
           for q in range(N):
               row.append(letters[index])
               index += 1
           # store all 'rows' in a 'table'
           all_elements.append(row)


       # Transform the lists of chracters from 'horizontal' lists to 'vertical' strings. 
       for i in range(N):
           for q in range(number_of_row):
               result += all_elements[q][order[i]-1]
               # since index starts from 0,
               # each column order should be reduced by 1 as to retrieve corresponding column's chracters


               
                
# start the decryption process
    else:
        
       # reverse the encryption process
       for i in range(N):
           row = []
           # store each group of (number_of_row) elements in a 'column'
           for q in range(number_of_row):
               row.append(letters[index])
               index += 1
           # store all 'columns' in a 'table'
           all_elements.append(row)

       # Transform the lists of chracters from 'vertical' lists to 'horizontal' strings. 
       for i in range(number_of_row):
            for q in range(N):
                result += all_elements[order.index(q+1)][i]



# return the transformed message            
    return result




print(crypto("hellohowdoyoudo",3,(1,2,3)))
print(crypto("hellohowdoyoudo",3,(2,3,1)))
print(crypto("eowydlhdoohloou",3,(2,3,1)))
print(crypto("ordpfhntanlntpoeeondtanayteimieaolrbffkz",4,(2,3,1,4)))
print(crypto("harrypotterandvoldemort",5,(2,1,4,3,5)))

        
