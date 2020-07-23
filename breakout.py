## Q1
def CenturyFromYear(year):
    return (year) // 100 + 1

# CHECK:
year = 2017
# print(CenturyFromYear(year))


## Q2
def calc_sum(num, iteration):
    lst = []
    for i in range(0, iteration):
        answer = (i + 1) * num
        lst.append(answer)
    return lst

# CHECK:
print(calc_sum(7, 5))


## Q3
def majority_vote(arr):
    # instantiate target 
    target = len(arr) // 2

    # loop over the values in the arr
    for i in arr:
        # if the count of the number i is greater than the target
        if arr.count(i) > target:
            # return the number
            return i
        else:
            return

# CHECK:
arr1 = ["A", "A", "B", "B", "B", "B"]
arr2 = ["A", "A", "B", "B", "C", "A", "A", "A"]
arr3 = ["Z", "Z", "B", "B", "C", "Z", "Z", "Z"]
print(majority_vote(arr2))
print(majority_vote(arr3))