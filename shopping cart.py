print("welcome to MiniMart!")
cart ={}

while (choice := input("/n1.Add 2.View 3. Remove 4.Exit:")) != '4':
    if choice =='1':
        items = input("item:")
        quantity = int(input("quanty:"))
        cart[items] = cart.get(items,0)+ quantity
    elif choice =='2':
        print(cart if cart else "Cart is empty")
    elif choice =='3':
        cart.pop(input("Item to remove:"),None)
    else:
        print("Invalid choice")
    
print("/nFinalCart:,cart if cart else "empty")