# Simple Expense Tracker

expenses = []  # list to store only amounts

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("\n--- All Expenses ---")
        for amt in expenses:
            print(f"₹{amt:.2f}")

    elif choice == "3":
        if expenses:
            total = 0
            for amt in expenses:
                total += amt
            avg = total / len(expenses)
            print(f"\nTotal Expense = ₹{total:.2f}")
            print(f"Average Expense = ₹{avg:.2f}")
        else:
            print("No expenses yet.")

    elif choice == "4":
        with open("expenses.txt", "w") as f:
            for amt in expenses:
                f.write(str(amt) + "\n")
            total = 0
            for amt in expenses:
                total += amt
            avg = total / len(expenses) if expenses else 0
            f.write(f"\nTotal = {total}\n")
            f.write(f"Average = {avg}\n")
        print("✅ Expenses saved to 'expenses.txt'")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")