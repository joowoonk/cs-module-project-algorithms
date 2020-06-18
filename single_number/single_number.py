'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # start with first number of index and compare with next numbers in the list
    # if found duplicate first number of index goes up and  
    list = []
    for i in arr:
        #check each element in the list
        if i not in list:
            #if it's not in the list, then added inside
            list.append(i)
        else:
            #whenever same number is called next time then it removes it. 
            list.remove(i)
    return list.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")