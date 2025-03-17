import random

def generate_price():
    return round(random.uniform(1.00, 500.00), 2)

def calculate_change(amount, denominations):
    change = []
    amount = round(amount, 2)  # Ensure precision issues don't cause problems
    for denom in sorted(denominations, reverse=True):
        count, amount = divmod(amount, denom)
        amount = round(amount, 2)  # Avoid floating point precision issues
        if count:
            change.append((denom, int(count)))
    return change, amount  # Return leftover amount that couldn't be given back

def money_dispenser():
    print("Welcome to the KSA Money Dispenser!")
    denominations = [0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    history = []
    
    while True:
        price = generate_price()
        print(f"\nTotal price: {price:.2f} SAR")
        total_inserted = 0
        
        while total_inserted < price:
            try:
                user_input = input(f"Insert money ({', '.join(map(str, denominations))} SAR) or 'exit' to quit: ")
                if user_input.lower() == 'exit':
                    print("Exiting... Thank you!")
                    return
                bill = float(user_input)
                if bill not in denominations:
                    print("Invalid denomination.")
                    continue
                total_inserted = round(total_inserted + bill, 2)  # Ensuring rounding consistency
                print(f"Inserted: {total_inserted:.2f} SAR, Remaining: {max(0, round(price - total_inserted, 2)):.2f} SAR")
            except ValueError:
                print("Invalid input. Enter a valid amount or 'exit'.")
                continue
        
        change = round(total_inserted - price, 2)
        remaining_unreturned = 0
        
        if change > 0:
            print(f"Change: {change:.2f} SAR")
            breakdown, leftover = calculate_change(change, denominations)
            total_returned = sum(denom * count for denom, count in breakdown)
            total_returned = round(total_returned, 2)  # Ensuring correct rounding
            
            if leftover > 0:
                remaining_unreturned = leftover
                print(f"Warning: Unable to return exact change. Remaining balance retained: {leftover:.2f} SAR")
            
            for denom, count in breakdown:
                print(f" - {count} x {denom:.2f} SAR")
        else:
            print("Exact amount received. No change needed.")
        
        history.append({"price": price, "paid": total_inserted, "change": change - remaining_unreturned})
        
        print("\nTransaction Summary:")
        print(f" - Total transactions: {len(history)}")
        print(f" - Total amount processed: {sum(tr['price'] for tr in history):.2f} SAR")
        print(f" - Total change given: {sum(tr['change'] for tr in history):.2f} SAR")
        print(f" - Total retained balance due to unavailable change: {remaining_unreturned:.2f} SAR")
        
        if input("Continue? (yes/no): ").strip().lower() != 'yes':
            break
    
    print("\nThank you for using the KSA Money Dispenser!")

if __name__ == "__main__":
    money_dispenser()