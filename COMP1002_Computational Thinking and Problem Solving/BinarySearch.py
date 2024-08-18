# find whether or not the given number is inside the list and returns appropriate boolean

# look at elements by loop
def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element_to_find == element:
            return True
    return False

# look at element by binary search:
# middle element -->> given no. > or < middle_element?
# -->> ignore the elements not within the given no. range -->> middle element in the given no. range -->> [> or <] ?
# remainning no. == given no.??
def bin_search(order_list, element_to_find):
    start_index = 0
    end_index = len(order_list)-1

    while True:
        middle_index = (end_index - start_index) // 2

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element = order_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            start_index = middle_index
        else:
            end_index = middle_index
    

aList = [2,4,6,8,10]
print(find(aList, 5))
print(find(aList, 4))

print(bin_search(aList,5))
print(bin_search(aList,4))
