# imports

# globals

# functions
def print_menu():
    print("--------------")
    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("----------------")


# plain instructions
print_menu()
opt = input("Select an option: ")

num1 = float(input(" enter num1: "))
num2 = float(input(" enter num2: "))


if opt == "1":
    total = num1 + num2
    print("the total is:" + str(total))

elif opt == "2":
    total = num1 - num2
    print("the total is:" + str(total))

elif opt == "3":
    total = num1 * num2
    print("the total is:" + str(total))

elif opt == "4":
	if num2 == 0:
		print("can not divide by zero")

else:
    total = num1 / num2
    print("the total is:" + str(total))


