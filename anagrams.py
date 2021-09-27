input = ['cba', 'omn', 'mno', 'bac', 'abc', 'atbc']
list_a = {}
for word in input:
    sorted_string = str(sorted(word))
    if sorted_string in list_a:
        list_a[sorted_string].append(word)
    else:
        list_a[sorted_string] = [word]
print(list(list_a.values()))
#Output - [['cba', 'bac', 'abc'], ['omn', 'mno'], ['atbc']]

# simple lambda function to check whether two strings are anagrams or not
are_anagrams = lambda x, y: str(sorted(x.lower())) == str(sorted(y.lower()))
# calling the function
print(are_anagrams('cat', 'tac'))
print(are_anagrams('cat', 'Tac'))
print(are_anagrams('cat', 'dog'))