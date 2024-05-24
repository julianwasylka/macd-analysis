import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from macd import macd, signal

x_values, y_values = macd()
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, label='MACD')
x_sign, y_sign = signal()
plt.plot(x_sign, y_sign, label='SIGNAL')

cross_points = [x_values[i] for i in range(1, len(y_sign)) if (y_values[i-1] < y_sign[i-1] and y_values[i] > y_sign[i]) or (y_values[i-1] > y_sign[i-1] and y_values[i] < y_sign[i])]
cross_values = [y_values[i] for i in range(1, len(y_sign)) if (y_values[i-1] < y_sign[i-1] and y_values[i] > y_sign[i]) or (y_values[i-1] > y_sign[i-1] and y_values[i] < y_sign[i])]
plt.scatter(cross_points, cross_values, color='red', zorder=5)

plt.xticks()
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.title('Macd - Nintendo')
plt.xlabel('Date')
plt.ylabel('Macd')
plt.xticks(rotation=45, ha='right', visible=True)
plt.tight_layout()
plt.xlim(x_values.min(), x_values.max())
plt.savefig('macd.png', dpi=300)
plt.show()