import matplotlib.pyplot as plt

class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares, price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'price': price}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol]['shares'] > shares:
                self.portfolio[symbol]['shares'] -= shares
            else:
                del self.portfolio[symbol]
                print(f"All shares of {symbol} have been removed from the portfolio.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def track_performance(self):
        total_value = 0
        for symbol, data in self.portfolio.items():
            shares = data['shares']
            price = data['price']
            value = shares * price
            total_value += value
            print(f"{symbol}: Shares - {shares}, Price - ${price:.2f}, Value - ${value:.2f}")

        # Plot portfolio performance
        labels = list(self.portfolio.keys())
        sizes = [data['shares'] * data['price'] for data in self.portfolio.values()]
        explode = [0.1] * len(labels)  # explode all slices for better visualization
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Portfolio Composition')
        plt.show()

def main():
    tracker = PortfolioTracker()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter current price per share: "))
            tracker.add_stock(symbol, shares, price)
            print(f"{shares} shares of {symbol} added to the portfolio.")

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            tracker.remove_stock(symbol, shares)
            print(f"{shares} shares of {symbol} removed to the portfolio.")

        elif choice == '3':
            print("\nPortfolio Performance:")
            tracker.track_performance()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()