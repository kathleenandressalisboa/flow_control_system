orders = []

def add_order():
    item = input('Item name: ')
    price = float(input('Price: '))

    orders.append((item, price))
    print("Order added successfully!")

def list_orders():
    if not orders:
        print('No orders found.')
        return

    for index, order in  enumerate(orders, start = 1):
        print(f"{index}.{order[0]} - ${order[1]:.2f}")

def show_total():
    total = sum(order[1] for order in orders)
    print(f"Total amount: ${total:.2f}")

def menu():
    while True:
        print("\n=== SnackBar Order Flow ===")
        print("1 - Add order")
        print("2 - List orders")
        print("3 - Show total")
        print("4 - Exit")
        option = input("Choose an option: ")
        if option == "1":
            add_order()
        elif option == "2":
            list_orders()
        elif option == "3":
            show_total()
        elif option == "4":
            print('Exiting...')
            break
        else:
            print('Invalid option.')

if __name__ == '__main__':
    menu()

