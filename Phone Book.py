Phone_Book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla",
}


def Search_number(name: str):
    count = 0  # name could repeat
    for num, names in Phone_Book.items():
        if names.lower() == name.lower():
            print("The number is: " + num)
            count += 1
    if count == 0:
        print("Sorry, the name is not found")


def Search_name(number):
    found = Phone_Book.get(number)
    if found != None:
        print("The Name is: " + found)
    else:
        print("Sorry, the number is not found")


option = -1  # to start the while
while option != "0":
    option = input(
        "Choose: (1)-Search for a Number/Name | (2)-Add/Update Number | (3)-Show Phone Book | (0)-Exit: "
    )
    # Search
    if option == "1":
        lookfor = input("Enter The Name/Number (Number must be 10 digts): ")

    # Add/Update
    elif option == "2":
        new_name = input("Enter The Name: ")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        new_number = input("Enter The Number (must be 10 digts):")
        if not new_name.isalpha():
            print("This is invalid name ")
        elif not new_number.isnumeric() or len(new_number) != 10:
            print("This is invalid number ")
        else:
            Phone_Book.update({new_number: new_name})
    # Show Phone Book
    elif option == "3":
        for names, nums in Phone_Book.items():
            print(names, nums)
    # Exit
    elif option == "0":
        print("slam")
    # Wrong Option
    else:
        print("invalid Option")
