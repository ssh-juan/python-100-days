# Python Lists - Data Structure
# A way of organizing and storing data in Python
# https://docs.python.org/3/tutorial/datastructures.html

# fruits = [item1, item2]

states_of_usa = ["Delaware", "Pennsylvania"]
print(states_of_usa)
print(states_of_usa[0])
print(states_of_usa[1])
print(states_of_usa[-1])
print(states_of_usa[-2])

states_of_usa[1] = "Pencilvania"
print("\n" + states_of_usa[1])

#For example, there is a new state joining USA. How to add to the end of the arrays?
states_of_usa.append("New Jersey")
print("\n" + "New state added")
print(states_of_usa)

#What if there is a bunch of new states joining USA? Use '.extend', so I can input many values.
states_of_usa.extend(["Georgia", "Connecticut"])
print("\n" + "New states added")
print(states_of_usa)