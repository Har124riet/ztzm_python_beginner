print("Welcome to MiniMart!")

cart = {}

while True:
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")

    choice = input()

    if choice == "1":
        item = input("Item: ")
        quantity = int(input("Quantity: "))
        cart[item] = cart.get(item, 0) + quantity

    elif choice == "2":
        item = input("Item to remove: ")
        cart.pop(item, None)

    elif choice == "3":
        if cart:
            for item, quantity in cart.items():
                print(f"{item}: {quantity}")
        else:
            print("Cart is empty.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")

print("Thank you for shopping! You bought:")

if cart:
    for item, quantity in cart.items():
        print(f"{item}: {quantity}")
else:
    print("Nothing (your cart was empty).")