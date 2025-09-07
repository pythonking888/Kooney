def baby_love():
    print("Who do you love more?")
    print("1. Baby Girl")
    print("2. Baby Boy")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("You chose Baby Girl 👶")
    elif choice == "2":
        print("You chose Baby Boy 🧒")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the function
baby_love()