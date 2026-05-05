def calculator():
    print("=== Smart Calculator ===")
    
    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator...")
            break

        if choice not in ['1','2','3','4']:
            print("Invalid choice, try again!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            print("Invalid input! Enter numbers only.")
            continue

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            if b == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", a / b)

calculator()