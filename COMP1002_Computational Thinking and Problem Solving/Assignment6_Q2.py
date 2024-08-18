def addTable():

    # first, define the factors for addition
    xy = [0,1,2,3,4,5,6,7,8,9]
    # creat a list to store all the rows (i.e. all the results)
    results=[]
    for i in xy:
        # create lists to store each row
        rows = []
        for j in xy:
            # start addition, assign 0 infront of the number that is smaller than 10
            aResult = i + j
            if (aResult < 10):
               aResult = "0" + str(aResult)
            else:
               aResult = str(aResult)
            # assign the results to a list stroing the row
            rows.append(aResult)
        # store the rows in a list
        results.append(rows)
    return results



def main():
    table = addTable()
    for item in table:
        print(item)

main()
