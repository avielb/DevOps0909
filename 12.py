import requests

# try:
#     my_variable = int(input("enter first number: "))
#     my_other_var = int(input("enter second number: "))
#     result = my_variable / my_other_var
#     print(result)
# except ZeroDivisionError as e:
#     print("could not divide by zero")
# except ValueError as e:
#     print("enter a normal number")
# except BaseException as e:
#     print(e.args)
# try:
#     requests.get("htpps://github.com")
# except BaseException as e:
#     print("something when wrong, check this: " + str(e.args))
# print("hello after the mess")


def get_user_age():
    input_from_user = int(input("enter your positive age: "))
    if input_from_user < 0:
        raise ValueError("Age can not be negative", "aa")

try:
    get_user_age()
except ValueError as e:
    print(e.args[0])