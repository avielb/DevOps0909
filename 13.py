def save_names():
    my_file = open("names.txt", "a")
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()


def show_name():
    my_file = open("names.txt", "r")
    for name in my_file.readlines():
            print("current name is: " + name, end='')

    # with open("names.txt", "r") as my_file:
    #     for name in my_file.readlines():
    #         print("current name is: " + name, end='')

for i in range(4):
    save_names()

show_name()