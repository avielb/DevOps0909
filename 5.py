names = ["yaniv", "tom", "liran", "ben"]
other_names = ["yaniv", "tom", "liran", "ben"]
a = 5
d = 6
if a == d:
    print("a equals d")

if a is d:
    print("a is d")

if names is other_names:
    print("names is other names")

if type(names) is list:
    print("names is list")

if names == other_names:
    print("names is the same")

print(type(names))
print(list)
my_empty_list = [1]
if my_empty_list:
    print()
if len(my_empty_list) + 3 <= 5:
    print("hello")