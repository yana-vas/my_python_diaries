import numpy as np
import pandas as pd

# data
from matplotlib import pyplot as plt

incomes = [30000, 35000, 45000, 47000, 50000, 52000, 55000, 60000, 65000, 70000]

# median calculation
median_income = np.median(incomes)

print(f"The median income: ${median_income}")

# mode calculation
mode_income = pd.Series(incomes).mode()
if mode_income.empty:
    print("There is no mode.")
else:
    print(f"The mode income: ${mode_income[0]}")

# box plot
plt.figure(figsize=(8,6))
plt.boxplot(incomes, vert=False)
plt.xlabel("Income")
plt.title("Income Distribution")
plt.show()
