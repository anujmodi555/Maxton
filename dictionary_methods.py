sample_dict = {"apple": 3, "mango": 5, "banana": 1, "orange": 9, "litchi": 3, "kiwi": 2}
# Make a list of Dictionary values
list_a = sample_dict.keys()
print(list(list_a))


# Sort Dictionary by Values
def sort_dict(sample_dict):
    return sorted(sample_dict.items(), key=lambda x: x[1])


print(sort_dict(sample_dict))
