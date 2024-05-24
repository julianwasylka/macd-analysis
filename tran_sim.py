from read_files import read_Nin
from macd import macd, signal

def generate_transactions(dates):
    _, macd_values = macd()
    _, signal_values = signal()
    macd_values = macd_values[:len(signal_values)]
    _, prices = read_Nin()
    transactions = []
    in_position = False
    budget = 10000
    budget_history = []
    budget_history.append(budget)
    shares = 0

    shares_to_forget = budget // prices[0]
    budget_forget = []
    budget_forget.append(shares_to_forget*prices[0])

    for i in range(1, len(dates)):
        if macd_values[i] > signal_values[i] and macd_values[i - 1] <= signal_values[i - 1]:
            if not in_position:
                shares_to_buy = budget // prices[i]
                if shares_to_buy > 0:
                    transactions.append((dates[i], 'BUY', prices[i], shares_to_buy, budget))
                    shares += shares_to_buy
                    budget -= shares_to_buy * prices[i]
                    in_position = True

        elif macd_values[i] < signal_values[i] and macd_values[i - 1] >= signal_values[i - 1]:
            if in_position:
                transactions.append((dates[i], 'SELL', prices[i], shares, budget))
                budget += shares * prices[i]
                shares = 0
                in_position = False
        budget_history.append(budget + shares*prices[i])
        budget_forget.append(shares_to_forget*prices[i])
    if in_position:
        transactions.append((dates[i], 'SELL', prices[i], shares, budget))
        budget += shares*prices[i]

    #for date, action, price, quantity, tbudget in transactions:
     #   print(f"{date}: {action} {quantity} shares at price {price} each. Budget before: {tbudget}")
    return dates, budget_history, budget_forget
