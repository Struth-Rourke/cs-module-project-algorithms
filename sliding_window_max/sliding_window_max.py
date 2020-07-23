"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""

def sliding_window_max(nums, k):
    ## v_1
    # instantiate max counter
    max = 0

    ## START:
    print("\n** START **\n")
    print("max_START:", max)
    
    # instantiate an empty list to hold the outputs
    max_arr = []
    # loop through the nums less the window + 1 BECAUSE of the exclusive nature
    # of lists
    for i in range(0, len(nums) - k + 1):
        # set the max counter as the first indexed value
        max = nums[i]

        ## CHECK:
        print(f"\n## A-{i} ##")
        print("---------------------")
        print(f"i_idx = {i}")
        print(f"i_val = {nums[i]}")
        print("max:", max)
        print("\n")

        # loop over the number of elements in the window
        for j in range(0, k):
            
            ## CHECK:
            print(f"\n## A-{i} = B-{j} ##")
            print("max:", max)
            print(f"i_idx = {i}\nj_idx = {j}")
            print(f"nums[i + j]_idx: {i + j}")
            print(f"i_val = {nums[i]}\nj_val = {nums[j]}")
            print(f"nums[i + j]_value: {nums[i + j]}")
            print("\n")

            # if either the i or j indexed value is larger than the max
            if nums[i + j] > max:
                # set the max as the larger of the two index values
                max = nums[i + j]
                print(f"NEW MAX: {max}\n")
            else:
                print("NO NEW MAX\n")
        
        # append the max of the three elements in the window, to the max_arr
        max_arr.append(max)


    # ## v_1 -- Raw Code
    # # instantiate max counter
    # max = 0
    # # instantiate an empty list to hold the outputs
    # max_arr = []
    # # loop through the nums less the window + 1 BECAUSE of the exclusive nature
    # # of lists
    # for i in range(0, len(nums) - k + 1):
    #     # set the max counter as the first indexed value
    #     max = nums[i]
    #     # loop over the number of elements in the window
    #     for j in range(0, k):
    #         # if either the i or j indexed value is larger than the max
    #         if nums[i + j] > max:
    #             # set the max as the larger of the two index values
    #             max = nums[i + j]

    #     # append the max of the three elements in the window, to the max_arr
    #     max_arr.append(max)


    # ## v_2
    # # instantiate index value
    # index = 0
    # # instantiate empty list
    # max_arr = []
    # # while the index + the (window-1) -- exclusive aspect of lists again --
    # # is less than the len of the arr
    # while index + (k - 1) < len(nums):
    #     # append the max of the window to the max_arr
    #     max_arr.append(max(nums[index : (index + k)]))
    #     # increase index
    #     index += 1

    return max_arr





if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, 4, 5, 3, 6, 7]
    k = 3

    print(f"\nOutput of sliding_window_max function is: {sliding_window_max(arr, k)}\n")
