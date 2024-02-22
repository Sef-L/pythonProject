# Function to add new item to the inventory
def add_item(inventory):
    total_price = 0
    name = input("Enter the name of the item: ").lower()
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price for a 1 of said item: $"))
    total_price = price*quantity
    inventory.append({"name": name, "quantity": quantity, "price per item": price, "total price": total_price})
    # By using append, it further expands my list as seen as an example on the repository
    print(f"{name} added to the inventory.")


# Function to display current inventory
def display_inventory(inventory):
    print("\nCurrent Inventory:")
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price per {item['name']}: ${item['price per item']}, Total price: ${item['total price']}")


# Function to calculate the total value of inventory
def calculate_inventory_value(inventory):
    total_value = 0
    for item in inventory:
        total_value += item['total price']
    return total_value


# Function to sell items from inventory
def sell_item(inventory):
    display_inventory(inventory)
    print('\n')
    item_name = input("Enter the name of the item to sell: ").lower()
    for item in inventory:
        if item['name'] == item_name:
            quantity_to_sell = int(input(f"Enter the quantity of {item_name} to sell: "))
        if quantity_to_sell <= item['quantity']:
            item['quantity'] -= quantity_to_sell
            sale_amount = item['price per item'] * quantity_to_sell
            track_sales(sales_history, item_name, quantity_to_sell, sale_amount)
            print(f"{quantity_to_sell} {item_name}(s) sold for ${sale_amount}.")
            return
        else:
            print("Sorry, you have insufficient amount in the inventory.")
            return
    print("Item not found in inventory.")


# Function to restock the items in the inventory
def restock_item(inventory):
    item_name = input("Enter the name of the item to restock: ")
    for item in inventory:
        if item['name'] == item_name:
            quantity_to_add = int(input(f"Enter the quantity of {item_name} to restock: "))
            item['quantity'] += quantity_to_add
            print(f"{quantity_to_add} {item_name}(s) restocked.")
        return
    print("Item not found in inventory.")


# Function to track sales
def track_sales(sales_history, item_name, quantity_sold, sale_amount):
    sales_history.append({"item_name": item_name, "quantity_sold": quantity_sold, "sale_amount": sale_amount})
    print("Sale recorded.")


# Function to generate sales report
def generate_sales_report(sales_history):
    print("\nSales Report:")
    total_sales = 0
    for sale in sales_history:
        total_sales += sale['sale_amount']
        print(f"{sale['item_name']}, Quantity Sold: {sale['quantity_sold']}, Sale Amount: ${sale['sale_amount']}")
    print(f"\nTotal Sales: ${total_sales}")


# CLI Menu Interface
def menu():
    print("""\nWelcome to the Grocery Store Inventory Management System!)
    1 - to Add a new item to the inventory.
    2 - to Display the current inventory.
    3 - to Sell item.
    4 - to Restock an item.
    5 - to Calculate the inventory value.
    6 - to Generate a sales report.
    7 - to Exit""")

# Main Program, I like to edge!
inventory = []
sales_history = []
while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item(inventory)
    elif choice == 2:
        display_inventory(inventory)
    elif choice == 3:
        sell_item(inventory)
    elif choice == 4:
        restock_item(inventory)
    elif choice == 5:
        total_value = calculate_inventory_value(inventory)
        print(f"Total Inventory Value: ${total_value}")
    elif choice == 6:
        generate_sales_report(sales_history)
    elif choice == 7:
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 7.")


