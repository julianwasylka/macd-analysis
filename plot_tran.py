import matplotlib.pyplot as plt
from tran_sim import generate_transactions
from macd import signal

def plot_budget(dates, budget_changes, nazwapliku, forget=0):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, budget_changes)
    print("Roznica kapitalu:", budget_changes[len(budget_changes) - 1] - budget_changes[0])
    if forget != 0: 
        plt.plot(dates, forget)
        print("Roznica kapitalu przy zapomnieniu:", forget[len(forget) - 1] - forget[0])
    plt.title('Budget Changes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Budget')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(nazwapliku, dpi=300)
    plt.show()

dates, _ = signal()
_, budget_changes, forget = generate_transactions(dates)
dates = dates[::-1]
dates1 = dates[:200]
bc1 = budget_changes[:200]
dates2 = dates[500:]
bc2 = budget_changes[500:]
plot_budget(dates, budget_changes, 'porownanie.png', forget)
plot_budget(dates1, bc1, 'poczatek.png')
plot_budget(dates2, bc2, 'koniec.png')