'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    # if n < 0
    if n < 0:
        # there are no ways
        return 0
    # if n == 1
    if n == 1:
        # there is only one way to eat it
        return 1
    # if the cache value is greater than zero
    if cache[n] > 0:
        # return the cache value
        return cache[n]
    else:
        # recursively call the function on successively smaller numbers
        cache[n] = eating_cookies(n - 1, cache) 
                    + eating_cookies(n - 2, cache)
                    + eating_cookies(n - 3, cache)
        return cache[n]


    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
