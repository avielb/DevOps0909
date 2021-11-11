print(list(range(100, 1, -5)))
names = ["ariel", "adi", "eran", "adir", "shahar"]
string_to_print = "Hello world!"
print(list(range(len(names))))
for i in range(len(names)):
    print(names[i])

for current_name in names:
    print(current_name)

a = 0
while a < 10:
    print("a is not yet 10")
    a = a + 1
    if a == 5:
        break

for i in range(1, 101):
    if i % 7 == 0:
        continue
    print(i)

a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)
else:
    print("finished successfully")