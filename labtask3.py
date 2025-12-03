# Mini Library System
# Course: Foundations of Programming using Python (ETCCFP103)
# Fully menu-driven program with file handling and OOP

class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        """Return book details in formatted string"""
        return f"{self.title:20} | {self.author:15} | {self.isbn:10} | {self.status}"


# Global book list
library = []


# -------------------- TASK 2: ADD BOOK --------------------
def add_book():
    print("\n--- Add New Book ---")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    isbn = input("Enter ISBN: ")

    # Optional Bonus: Duplicate ISBN validation
    for b in library:
        if b.isbn == isbn:
            print("❌ Book with this ISBN already exists!")
            return

    new_book = Book(title, author, isbn)
    library.append(new_book)
    print("✔ Book Added Successfully!")


# -------------------- TASK 2: SEARCH BOOK --------------------
def search_book():
    print("\n--- Search Book ---")
    key = input("Enter Title or ISBN to search: ")

    found = False
    for b in library:
        if b.title.lower() == key.lower() or b.isbn == key:
            print("\nBook Found:")
            print("-" * 60)
            print(b.display())
            print("-" * 60)
            found = True
    
    if not found:
        print("❌ No matching book found.")


# -------------------- TASK 2: REMOVE BOOK --------------------
def remove_book():
    print("\n--- Remove Book ---")
    isbn = input("Enter ISBN to remove: ")

    for b in library:
        if b.isbn == isbn:
            library.remove(b)
            print("✔ Book Removed Successfully!")
            return

    print("❌ Book not found!")


# -------------------- TASK 3: SAVE TO FILE --------------------
def save_records():
    print("\n--- Saving Records to library.txt ---")
    try:
        with open("library.txt", "w") as f:
            for b in library:
                f.write(f"{b.title},{b.author},{b.isbn},{b.status}\n")
        print("✔ Records Saved Successfully!")
    except Exception as e:
        print("❌ Error saving file:", e)


# -------------------- TASK 4: LOAD FROM FILE --------------------
def load_records():
    print("\n--- Loading Records from library.txt ---")
    try:
        with open("library.txt", "r") as f:
            library.clear()
            for line in f:
                title, author, isbn, status = line.strip().split(",")
                library.append(Book(title, author, isbn, status))
        print("✔ Records Loaded Successfully!")
    except FileNotFoundError:
        print("❌ library.txt not found!")
    except Exception as e:
        print("❌ Error loading file:", e)


# -------------------- TASK 5: DISPLAY ALL BOOKS --------------------
def display_all():
    print("\n--- Library Books ---")
    if len(library) == 0:
        print("No books available.")
        return

    print("-" * 60)
    print(f"{'Title':20} | {'Author':15} | {'ISBN':10} | Status")
    print("-" * 60)
    for b in library:
        print(b.display())
    print("-" * 60)


# -------------------- TASK 6: MENU --------------------
def menu():
    while True:
        print("\n===== MINI LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Remove Book")
        print("4. Display All Books")
        print("5. Save Records")
        print("6. Load Records")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            remove_book()
        elif choice == '4':
            display_all()
        elif choice == '5':
            save_records()
        elif choice == '6':
            load_records()
        elif choice == '7':
            print("Exiting Program... Goodbye!")
            break
        else:
            print("❌ Invalid Choice! Please try again.")


# Run the menu
menu()