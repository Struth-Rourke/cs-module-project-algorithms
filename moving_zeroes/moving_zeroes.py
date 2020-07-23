'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # instantiating an empty, new_arr
    new_arr = []
    # loop over items in the array
    for i in arr:
        # if the value of the item in the array is not zero
        if i != 0:
            # append the value to the list
            new_arr.append(i)
    
    # loop over the items again, seperately (second occasion)
    for j in arr:
        # if the value of the item in the array IS zero
        if j == 0:
            # append it to the list
            new_arr.append(j)

    return new_arr





if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
