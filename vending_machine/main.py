from services.vending_machine import VendingMachine
from models.product import Product
from models.coin import Coin
from models.note import Note

def example1(vending_machine):
    try:
        print("\nExample 1: Successful Purchase with Exact Change")
        print("Inserting coin: $1.00")
        vending_machine.insert_coin(Coin(1.00))
        print("Inserting coin: $0.50")
        vending_machine.insert_coin(Coin(0.50))
        print("Selecting product: Soda")
        change = vending_machine.select_product("Soda")
        print(f"Product dispensed. Change returned: ${change:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def example2(vending_machine):
    try:
        print("\nExample 2: Purchase with Insufficient Funds")
        print("Inserting coin: $1.00")
        vending_machine.insert_coin(Coin(1.00))
        print("Selecting product: Soda")
        change = vending_machine.select_product("Soda")
        print(f"Product dispensed. Change returned: ${change:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def example3(vending_machine):
    try:
        print("\nExample 3: Purchase with Change Returned")
        print("Inserting coin: $1.00")
        vending_machine.insert_coin(Coin(1.00))
        print("Inserting coin: $1.00")
        vending_machine.insert_coin(Coin(1.00))
        print("Selecting product: Soda")
        change = vending_machine.select_product("Soda")
        print(f"Product dispensed. Change returned: ${change:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def example4(vending_machine):
    try:
        print("\nExample 4: Out of Stock Product")
        print("Inserting coin: $1.50")
        vending_machine.insert_coin(Coin(1.00))
        vending_machine.insert_coin(Coin(0.50))
        print("Selecting product: Soda")
        change = vending_machine.select_product("Soda")
        print(f"Product dispensed. Change returned: ${change:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def example5(vending_machine):
    try:
        print("\nExample 5: Using Notes")
        print("Inserting note: $10.00")
        vending_machine.insert_note (Note (10))
        print("Selecting product: Soda")
        change = vending_machine.select_product("Soda")
        print(f"Product dispensed. Change returned: ${change:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    products = [
        Product("Soda", 1.50, 10),
        Product("Chips", 1.00, 5),
        Product("Candy", 0.75, 20)
    ]
    vending_machine = VendingMachine(products)

    example1(vending_machine)
    example2(vending_machine)
    example3(vending_machine)
    example4(vending_machine)
    example5(vending_machine)

if __name__ == "__main__":
    main()
