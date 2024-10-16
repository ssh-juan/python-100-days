#Range Function

print("Beginning of Loop 1")
#The last number from range is not included
for number in range(1,10):
    print(number)

print("\nBeginning of Loop 2")
#If number '10' needs to be included, we have to change from '10' to '11'
for number in range(1,11):
    print(number)

#The third parameter is optional. It will step the output on the input you gave
print("\nBeginning of Loop 3")
for number in range(1,11,3): #Result will be: '1,4,7,10' because it's taking a step of 3 characters
    print(number)