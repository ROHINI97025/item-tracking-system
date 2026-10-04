import json
import os


class Item:
    def __init__(self, item_id, name, category, quantity):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity
        }


class ItemTrackingSystem:
    def __init__(self, filename="items.json"):
        self.filename = filename
        self.items = []
        self.load_items()

    def load_items(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                self.items = [
                    Item(
                        item["item_id"],
                        item["name"],
                        item["category"],
                        item["quantity"]
                    )
                    for item in data
                ]

            except (json.JSONDecodeError, KeyError):
                self.items = []

    def save_items(self):
        with open(self.filename, "w") as file:
            json.dump(
                [item.to_dict() for item in self.items],
                file,
                indent=4
            )

    def add_item(self):
        item_id = input("Enter item ID: ").strip()

        if any(item.item_id == item_id for item in self.items):
            print("Item ID already exists.")
            return

        name = input("Enter item name: ").strip()
        category = input("Enter category: ").strip()

        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        item = Item(item_id, name, category, quantity)
        self.items.append(item)
        self.save_items()

        print("Item added successfully.")

    def view_items(self):
        if not self.items:
            print("No items available.")
            return

        print("\n--- Item List ---")

        for item in self.items:
            print(
                f"ID: {item.item_id} | "
                f"Name: {item.name} | "
                f"Category: {item.category} | "
                f"Quantity: {item.quantity}"
            )

    def search_item(self):
        search_id = input("Enter item ID to search: ").strip()

        for item in self.items:
            if item.item_id == search_id:
                print("\nItem found:")
                print(f"ID: {item.item_id}")
                print(f"Name: {item.name}")
                print(f"Category: {item.category}")
                print(f"Quantity: {item.quantity}")
                return

        print("Item not found.")

    def update_item(self):
        item_id = input("Enter item ID to update: ").strip()

        for item in self.items:
            if item.item_id == item_id:

                print("Leave a field empty to keep its current value.")

                name = input(f"Enter new name [{item.name}]: ").strip()
                category = input(
                    f"Enter new category [{item.category}]: "
                ).strip()
                quantity_input = input(
                    f"Enter new quantity [{item.quantity}]: "
                ).strip()

                if name:
                    item.name = name

                if category:
                    item.category = category

                if quantity_input:
                    try:
                        quantity = int(quantity_input)

                        if quantity < 0:
                            print("Quantity cannot be negative.")
                            return

                        item.quantity = quantity

                    except ValueError:
                        print("Invalid quantity.")
                        return

                self.save_items()
                print("Item updated successfully.")
                return

        print("Item not found.")

    def delete_item(self):
        item_id = input("Enter item ID to delete: ").strip()

        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                self.save_items()

                print("Item deleted successfully.")
                return

        print("Item not found.")


def main():
    system = ItemTrackingSystem()

    while True:
        print("\n===== ITEM TRACKING SYSTEM =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            system.add_item()

        elif choice == "2":
            system.view_items()

        elif choice == "3":
            system.search_item()

        elif choice == "4":
            system.update_item()

        elif choice == "5":
            system.delete_item()

        elif choice == "6":
            print("Exiting Item Tracking System.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()