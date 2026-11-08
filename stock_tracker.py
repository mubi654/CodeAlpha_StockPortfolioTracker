"""CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def get_portfolio():
    """Ask the user for stock names and quantities."""
    portfolio = {}
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter stock name and quantity. Type 'done' to finish.\n")

    while True:
        name = input("Stock name: ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Stock not found. Please choose from the list above.\n")
            continue

        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.\n")
            continue

        portfolio[name] = portfolio.get(name, 0) + quantity
        print(f"Added {quantity} x {name}\n")

    return portfolio


def build_report(portfolio):
    """Return the report text and the total investment."""
    lines = ["----- Portfolio Summary -----"]
    total = 0
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        total += value
        lines.append(f"{name}: {qty} x ${STOCK_PRICES[name]} = ${value}")
    lines.append("-----------------------------")
    lines.append(f"Total Investment: ${total}")
    return "\n".join(lines)


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return

    report = build_report(portfolio)
    print("\n" + report)

    save = input("\nSave result to a file? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write(report)
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
