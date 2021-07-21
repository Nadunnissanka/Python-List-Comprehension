# List Comprehension

# using a list example
numbers_list = [1,2,3,4,5]
new_list = [n+1 for n in numbers_list]
# print(new_list)
# output -> [2, 3, 4, 5, 6]

# using a String example
name = "Angela"
new_list = [letter for letter in name]
# print(new_list)
# output -> ['A', 'n', 'g', 'e', 'l', 'a']

# using a range as example
numbers = range(1,5)
new_list = [n*2 for n in numbers]
# print(new_list)
# output -> [2, 4, 6, 8]

# using condionals in List Comprehension
names = ["Alex","Beth","Nadun","Chamath","Freddie","udara"]
long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
# output -> ['CHAMATH', 'FREDDIE']