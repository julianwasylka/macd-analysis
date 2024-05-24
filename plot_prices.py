import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from read_files import read_Nin

x_values, y_values = read_Nin()

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values)
plt.xticks()
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.title('Nintendo Shares in 2016-20')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45, ha='right', visible=True)
plt.tight_layout()
plt.xlim(x_values.min(), x_values.max())
plt.savefig('Nintendo_2016-20.png', dpi=300)
plt.show()