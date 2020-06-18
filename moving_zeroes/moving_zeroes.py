'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # arr.append(arr.pop(i))
    list = []
    zeroList = []
    i = 0

    while i < len(arr):
        if arr[i] == 0:
            zeroList.append(arr[i])
        else:  #arr[i] > 0 or arr[i] < 0:
            list.append(arr[i])
        i += 1
    arr = list + zeroList
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")