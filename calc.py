# imports

# globals

# functions
def print_menu():
    print("--------------")
    print("[1] Sum")
    print("[2] Subtract")
    print("----------------")


# plain instructions
print_menu()
opt = input("Select an option: ")

if opt == "1":
    # ask for 2 nums then print sum
