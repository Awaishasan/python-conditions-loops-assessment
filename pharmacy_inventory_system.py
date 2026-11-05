# Smart Pharmacy Inventory & Sales Management System
# Topic: Loop Structures (for loop, range(), conditions inside
# loops, counters and accumulators)
# Assignment 47 - Task 2
# Processes medicines one by one in a for loop, calculates
# sales and remaining stock, and gives a final daily report.


def get_number_of_medicines():
    """Ask how many medicines to process (a whole number above 0)."""
    while True:
        try:
            count = int(input("How many different medicines to process? "))
            if count > 0:
                return count
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_medicine_name():
    """Ask for a medicine name until a non-empty name is given."""
    while True:
        name = input("Enter medicine name: ").strip()
        if name:
            return name
        print("Medicine name cannot be empty. Please enter a valid name.")


def get_stock():
    """Ask for available stock (a whole number, 0 or more)."""
    while True:
        try:
            stock = int(input("Enter available stock (units): "))
            if stock >= 0:
                return stock
            print("Stock cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a whole number for stock.")


def get_price():
    """Ask for price per unit (Rs., more than 0)."""
    while True:
        try:
            price = float(input("Enter price per unit (Rs.): "))
            if price > 0:
                return price
            print("Price must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number for price.")


def get_quantity_sold():
    """Ask for quantity sold (a whole number, 0 or more)."""
    while True:
        try:
            quantity = int(input("Enter quantity sold (units): "))
            if quantity >= 0:
                return quantity
            print("Quantity sold cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")


def main():
    print("=" * 55)
    print("Smart Pharmacy Inventory & Sales Management System")
    print("=" * 55)

    # Accumulator for total revenue and counters for the final report
    total_revenue = 0.0
    total_medicines_processed = 0
    restock_count = 0
    restock_list = []

    number_of_medicines = get_number_of_medicines()

    # Process each medicine one by one using a for loop
    for medicine_number in range(1, number_of_medicines + 1):
        print(f"\n--- Medicine {medicine_number} ---")

        medicine_name = get_medicine_name()
        available_stock = get_stock()
        price_per_unit = get_price()
        quantity_sold = get_quantity_sold()

        total_medicines_processed += 1

        # Check whether the requested quantity is available in stock
        if quantity_sold > available_stock:
            print(f"Insufficient stock for {medicine_name}.")
            print(f"Available stock: {available_stock} units, "
                  f"requested: {quantity_sold} units.")
            print("Sale cannot be completed.")
            print(f"Remaining stock: {available_stock} units")
            # This medicine needs restocking because the
            # requested quantity could not be supplied.
            restock_count += 1
            restock_list.append(medicine_name)
            continue

        # Calculate the sales amount and the remaining stock
        sales_amount = quantity_sold * price_per_unit
        remaining_stock = available_stock - quantity_sold

        # Add this sale to the total revenue (accumulator)
        total_revenue += sales_amount

        print(f"Sales amount for {medicine_name}: Rs. {sales_amount:,.2f}")
        print(f"Remaining stock of {medicine_name}: "
              f"{remaining_stock} units")

        # Low-stock warning if remaining stock is below 10 units
        if remaining_stock < 10:
            print(f"Warning: Low stock for {medicine_name}! "
                  f"Only {remaining_stock} units left.")
            restock_count += 1
            restock_list.append(medicine_name)

    # Final report
    print("\n" + "=" * 55)
    print("Pharmacy Daily Sales Report")
    print("=" * 55)
    print(f"Total medicines processed   : {total_medicines_processed}")
    print(f"Total revenue               : Rs. {total_revenue:,.2f}")
    print(f"Medicines needing restock   : {restock_count}")
    if restock_list:
        print("Restock list:")
        for medicine_name in restock_list:
            print(f"- {medicine_name}")
    else:
        print("No medicines need restocking.")
    print("=" * 55)


if __name__ == "__main__":
    main()
