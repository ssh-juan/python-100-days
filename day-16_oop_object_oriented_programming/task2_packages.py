#https://pypi.org/
#A package differs from a module in the sense that it's actually a whole bunch of code.

#Pretty Table
#DOC: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
print(table)


#left align
table.align = "l"

print(table)