# Vending Machine Project

## Description
This project implements a vending machine that supports multiple products with different prices and quantities. The machine accepts coins and notes of different denominations, dispenses the selected product, and returns change if necessary. It keeps track of available products and their quantities, handles multiple transactions concurrently, and ensures data consistency. The machine also provides an interface for restocking products and collecting money, and handles exceptional scenarios such as insufficient funds or out-of-stock products.


## Classes, Interfaces, and Exceptions

### Classes
- **Product** (`models/product.py`): Represents a product with a name, price, and quantity.
- **Coin** (`models/coin.py`): Represents a coin with a specific value.
- **Note** (`models/note.py`): Represents a note with a specific value.
- **Transaction** (`models/transaction.py`): Manages the amount inserted during a transaction.
- **VendingMachine** (`services/vending_machine.py`): Main class that handles product selection, payment processing, and dispensing products.
- **Inventory** (`services/inventory.py`): Manages the inventory of products.
- **Payment** (`services/payment.py`): Validates and processes payments.

### Interfaces
- **IVendingMachine** (`interfaces/ivending_machine.py`): Interface for vending machine operations.
- **IInventory** (`interfaces/iinventory.py`): Interface for inventory management.
- **IPayment** (`interfaces/ipayment.py`): Interface for payment processing.

### Exceptions
- **InsufficientFundsException** (`exceptions/insufficient_funds_exception.py`): Raised when there are insufficient funds for a transaction.
- **OutOfStockException** (`exceptions/out_of_stock_exception.py`): Raised when a selected product is out of stock.
- **InvalidDenominationException** (`exceptions/invalid_denomination_exception.py`): Raised when an invalid coin or note denomination is inserted.

## Design Patterns Used
- **Factory Pattern**: Used for creating instances of products, coins, and notes.
- **Strategy Pattern**: Used for handling different payment methods (coins and notes).
- **Observer Pattern**: Used for inventory management to notify when products are out of stock.
- **State Pattern**: Used for managing the state of the vending machine during different stages of a transaction.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shrikant-temburwar/low-level-design.git
   cd vending_machine
    ```
2. **Install dependencies:** This project does not have any external dependencies, so you can skip this step.
3. **Run the application:**
    ```bash
    python main.py
    ```

4. **Simulate a transaction:** The main.py file contains a sample transaction where coins are inserted, and a product is selected. You can modify this file to test different scenarios.
## Usage
* Insert Coin:
```Python
vending_machine.insert_coin(Coin(1.00))
```

* Insert Note:
```Python
vending_machine.insert_note (Note (10))
```
* Select Product:
```Python
vending_machine.select_product("Soda")
```
## Handling Exceptions
The vending machine handles various exceptions such as insufficient funds and out-of-stock products. These exceptions are raised during the transaction process and can be caught and handled appropriately.