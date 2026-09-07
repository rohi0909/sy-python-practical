# Product Inventory Management System

inventory = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000},
    {"name": "Headphones", "price": 2500}
]


def display_inventory():
    print("\n--- Product Inventory ---")
    if not inventory:
        print("Inventory is empty.")
        return

    for index, product in enumerate(inventory):
        print(f"{index}. {product['name']} - ₹{product['price']:.2f}")


def search_product():
    name = input("Enter product name to search: ").strip().lower()

    found = False

    for index, product in enumerate(inventory):
        if product["name"].lower() == name:
            print(f"\nProduct found!")
            print(f"Name: {product['name']}")
            print(f"Price: ₹{product['price']:.2f}")
            print(f"Index location: {index}")
            found = True
            break

    if not found:
        print("Product not found.")


def add_product():
    name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter product price: ₹"))
        if price < 0:
            print("Price cannot be negative.")
            return

        inventory.append({
            "name": name,
            "price": price
        })

        print(f"{name} added successfully.")

    except ValueError:
        print("Please enter a valid price.")


def update_price():
    name = input("Enter product name: ").strip().lower()

    for product in inventory:
        if product["name"].lower() == name:
            try:
                new_price = float(input("Enter new price: ₹"))

                if new_price < 0:
                    print("Price cannot be negative.")
                    return

                product["price"] = new_price
                print("Product price updated successfully.")
                return

            except ValueError:
                print("Please enter a valid price.")
                return

    print("Product not found.")


def sort_by_price():
    order = input("Sort ascending or descending? (a/d): ").strip().lower()

    if order == "a":
        inventory.sort(key=lambda product: product["price"])
        print("Inventory sorted from lowest to highest price.")

    elif order == "d":
        inventory.sort(key=lambda product: product["price"], reverse=True)
        print("Inventory sorted from highest to lowest price.")

    else:
        print("Invalid sorting option.")


# Main program
while True:
    print("\n===== PRODUCT INVENTORY SYSTEM =====")
    print("1. Display Inventory")
    print("2. Search Product")
    print("3. Add Product")
    print("4. Update Product Price")
    print("5. Sort by Price")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_inventory()

    elif choice == "2":
        search_product()

    elif choice == "3":
        add_product()

    elif choice == "4":
        update_price()

    elif choice == "5":
        sort_by_price()

    elif choice == "6":
        print("Exiting inventory system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")