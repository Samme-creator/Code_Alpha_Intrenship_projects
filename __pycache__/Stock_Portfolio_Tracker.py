import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}


def display_available_stocks():
    """Display all available stocks and prices."""
    print("\nAvailable Stocks:")
    print("---------------------------")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock} : ${price}")
    print("---------------------------")


def get_user_portfolio():
    """Collect stock names and quantities from the user."""
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("❌ Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue

            portfolio[stock] = portfolio.get(stock, 0) + quantity

        except ValueError:
            print("❌ Please enter a valid number.")

    return portfolio


def calculate_portfolio_value(portfolio):
    """Calculate total investment value."""
    total_value = 0
    results = []

    print("\nPortfolio Summary")
    print("-------------------------------------")

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        total_value += value

        results.append((stock, quantity, price, value))

        print(f"{stock:5} | Qty: {quantity:<3} | Price: ${price:<5} | Value: ${value}")

    print("-------------------------------------")
    print(f"Total Investment Value: ${total_value}\n")

    return results, total_value


def save_to_file(results, total_value):
    """Save portfolio results to TXT and CSV files."""
    
    # Save TXT
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("---------------------------\n")

        for stock, qty, price, value in results:
            file.write(f"{stock} | Qty: {qty} | Price: {price} | Value: {value}\n")

        file.write(f"\nTotal Investment Value: {total_value}")

    # Save CSV
    with open("portfolio_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])

        for stock, qty, price, value in results:
            writer.writerow([stock, qty, price, value])

        writer.writerow(["", "", "Total", total_value])

    print("✅ Results saved to portfolio_summary.txt and portfolio_summary.csv")


def main():
    """Main program execution."""
    print("===================================")
    print("      Stock Portfolio Tracker      ")
    print("===================================")

    display_available_stocks()

    portfolio = get_user_portfolio()

    if not portfolio:
        print("No stocks entered.")
        return

    results, total_value = calculate_portfolio_value(portfolio)

    save = input("Do you want to save the result to a file? (yes/no): ").lower()

    if save == "yes":
        save_to_file(results, total_value)

    print("Thank you for using the Stock Portfolio Tracker.")


# Run the program
if __name__ == "__main__":
    main()