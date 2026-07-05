print("Welcome to MiniMart!")

cart = {}

choice = input("\n1. Add  2. View  3. Remove  4. Exit: ")

while choice != "4":
    if choice == "1":
        item = input("Item: ")
        quantity = int(input("Quantity: "))
        cart[item] = cart.get(item, 0) + quantity

    elif choice == "2":
        if cart:
            print(cart)
        else:
            print("Cart is empty")

    elif choice == "3":
        item = input("Item to remove: ")
        cart.pop(item, None)

    else:
        print("Invalid choice")

    choice = input("\n1. Add  2. View  3. Remove  4. Exit: ")

if cart:
    print("\nFinal Cart:", cart)
else:
    print("\nFinal Cart: Empty")