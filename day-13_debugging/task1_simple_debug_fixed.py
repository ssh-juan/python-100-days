#FIXED: Changed end of range from 20 to 21.
def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")

my_function()

# Describe the problem
# 1. What is the 'for loop' doing?
# It's counting in the range from 1 to 19 (20 is not counted)

# 2. When is the function meant to print "You got it"?
# When i == 20

# 3. What are your assumptions about the value of i?
# Never arrives at 20, because the 'range loop' finishes at 19.