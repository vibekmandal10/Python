import json

# Creating a dictionary
my_dict = {
    "name": "Vibek",
    "age": 24,
    "city": "Bokaro"
}

# Writing dictionary to a JSON file
with open("my_dict.json", "w") as json_file:
    json.dump(my_dict, json_file)
