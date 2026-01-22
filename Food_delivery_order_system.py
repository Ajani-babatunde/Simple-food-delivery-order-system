delivery_orders = []

def place_order():
    customer = input("Enter customer name: ")
    food = input("Enter food item: ")
    delivery_orders.append({"customer": customer, "food": food})
    print("Order placed successfully")

def view_orders():
    if not delivery_orders:
        print("No orders available")
    else:
        for order in delivery_orders:
            print("Customer:", order["customer"], "| Food:", order["food"])

def main():
    while True:
        print("1. Place Order")
        print("2. View Orders")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            place_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
