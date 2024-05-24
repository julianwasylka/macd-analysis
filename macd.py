from read_files import read_Nin

def ema(prices, N):
    sum1, sum2 = 0, 0
    a  = 2/(N + 1)
    for i in range(N+1):
        sum1 += ((1 - a)**i) * (prices[len(prices) - 1 - i])
        sum2 += (1 - a)**i
    return sum1/sum2

def macd():
    dates_df, prices_df = read_Nin()
    prices = prices_df.values.flatten()
    dates = dates_df.values.flatten()[:len(prices) - 31]
    macd = []
    for i in range(30, len(prices) - 1):
        p = prices[:i]
        macd.append(ema(p, 12) - ema(p, 26))
    return dates, macd

def signal():
    dates, vmacd = macd()
    dates = dates[:len(vmacd) - 11]
    signal = []
    for i in range(10, len(vmacd) - 1):
        p = vmacd[:i]
        signal.append(ema(p, 9))
    return dates, signal