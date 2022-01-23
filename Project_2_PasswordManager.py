print("\n******** Password Manager ********\n")

option = input("Enter what you want to do (Add/View) --> ")

if option.lower() == "add":
    accName = input("\nEnter account name: ")
    accPass = input("Enter account password: ")
    print("\nConratulations!!! Your password is added.\n")

    with open("acc.txt", "a") as f:
        f.write(f"{accName} | {accPass}\n")

else:
    print("\nList of your saved passwords -->\n")

    with open("acc.txt") as f:
        info = f.read()
        print(info)

print("******** ______________ ********\n")
