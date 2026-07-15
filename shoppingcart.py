cart=[]
while True:
    print("1. Add item to cart")
    print("2. Remove from cart")
    print("3. View cart")
    print("4.exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=input("Enter the item to add to cart: ")
        cart.append(item)
        print(f"{item} has been added to the cart.")
    elif choice==2:
        item=input("Enter the item to remove from cart: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} has been removed from the cart.")
        else:
            print(f"{item} is not in the cart.")
    elif choice==3:
        print("Items in your cart:")
        for item in cart:
            print(f"- {item}")
    elif choice==4:
        print(" Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
