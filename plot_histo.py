import matplotlib.pyplot as plt
import numpy as np
from macd import macd, signal

x_values, y_values = macd()
x_sign, y_sign = signal()
y_values = y_values[:len(y_sign)]

diff = np.array(y_values) - np.array(y_sign)

plt.figure(figsize=(12, 6))
plt.bar(x_sign, diff, color='grey', alpha=0.5, width=2.0)
plt.title('Difference between MACD and SIGNAL')
plt.xlabel('Dates')
plt.ylabel('Diffrences')
plt.grid(True)
plt.tight_layout()
plt.savefig('Histogram.png', dpi=300)
plt.show()