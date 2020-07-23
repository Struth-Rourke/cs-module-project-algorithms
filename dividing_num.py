# We'll say that a positive int divides iteself if every digit in the number divides  into the number evenly.
# For example, 128 divides itself since 1, 2, and 8 all divide into 128 evenly.
# And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides iteslef.

# Write a function to determine if a number divides itself
def divide_self(num):
    ## Pseudocode:
    
    # make an original copy of num
    # loop over each digit in num (while loop - while the current number still has digits)
        # get the right-most digit of num using num % 10
        # if digit is 0, return False
        # take that digit, get remainder of orginal num
        # if remainder is NOT 0, return False
        # remove the last digit from the number using // 10 (integer divison)
    # return True



print(divide_self(128)) # -> True
print(divide_self(12)) # -> True
print(divide_self(120)) # -> False







"""
##### ------------------ LOGICAL THOUGHT PROCESS (UPER) ------------------ #####

## UPER ##
Understand
Plan
Execute
Review


## UNDERSTAND 

# Inputs:
- A positive integer
- Does NOT contain a zero -- return False
- How large?
- Can we excpet bad data? No bad data

# Output:
- Return type? -- return Boolean (True or False)
- What conditions result in return type? 
- Formatted? Formatting? Error statements?



## PLAN
- Pseudocode:
    - Write out problems or thought process
    - Mess around with code to see what operations work
    - Google for specific issues you run into

- First-Pass Solution:
    - No Big O
    - Not focusing on performance or efficiency
    - Naive Approaches, etc. (could also be Brute Force where you try many 
      approaches and take the best results)

    EX:
    How to get a digit?
    - Convert to a string
    - % 10 to get the right most digit

- What code features based on the problem / context clues?
    (ex. "divide evenly" = %)
    (ex. "every digit" = loop)
    (ex. "determine if" = if statements)
