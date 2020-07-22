'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # instantiate empty product list
    product = []

    # loop over items in the arr, enumerated so that I can access the index
    for index, j in enumerate(arr):
        # create a new, copy of the array
        new_arr = arr.copy()
        # remove the i indexed element from the list
        new_arr.pop(index)
        # instantiate product counter
        prod = 1
        # loop over the numbers in the new_arr
        for nums in new_arr:
            # multiple the prod by the nums in the list
            prod *= nums
        # append the answer to the empty product list
        product.append(prod)

    return product





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
