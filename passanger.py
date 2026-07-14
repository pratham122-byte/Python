passanger=[]
while True: 
    print("1. Add Passanger")
    print("2.veiw Passanger")
    print("3.exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter the name of the passanger: ")
        passanger.append(name)
        print(f"{name} has been check-in.")
    elif choice==2:
        print("list of passanger:",passanger)
    elif choice==3:
        print("Thank you ,visit again")
        break
    else:
        print("Invalid choice")