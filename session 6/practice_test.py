profile = {
    "name" : "Joshua Ehd",
    "age" : 27,
    "address" : "Cebu City, Cebu 6000"
}

# add new key-value pair
profile.update({"isEmployed" : True})

# update new key-value pair
profile["isEmployed"] = False

# remove first key
profile.pop("name")

print(profile)

