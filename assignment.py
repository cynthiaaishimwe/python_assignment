# 
def sum_nums(*nums):
    total = 0
    for i in nums:
     total+=i
    return total

print(sum_nums(20,30,10,2,1))

#3. Write a function that takes an unknown number of keyword arguments and returns a dictionary where the keys are the argument names and
# the values are the argument values.


# Write a function that takes an unknown number of keyword arguments, each with a string value. The function should concatenate all the strings and return the resulting string.

def unknown_number(**kwargs):
    output = ""
    for key, value in kwargs.items():
        output += value
    return output
print(unknown_number(a="my name ", b="is ", c="cynthia", d="ishimwe ", e="I am Rwandese"))