#Nesting

#You can nest a list or even another dictionary inside a dictionary
# {
# Key: [List],
# Key2: {Dict}
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
print(travel_log)

# How to print 'Lille'
print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]
#Figure out how to print letter "D"
print(nested_list[2][1])

#Storing a dictionary
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

#Figure out how to print letter "Stuttgart"
print(travel_log["Germany"]["cities_visited"][2])


#Lists inside Dictionaries
#Dictionaries inside Dictionaries
#Lists inside Lists
#etc, many ways of organizing data