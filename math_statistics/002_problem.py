import numpy as np

# data
from matplotlib import pyplot as plt

age_groups = ['20-29', '30-39', '40-49', '50-59', '60 and above']
employees = [50, 80, 60, 40, 20]
mid_points = [24.5, 34.5, 44.5, 54.5, 65]

# mean calculation
mean_age = sum(np.array(mid_points) * np.array(employees)) / sum(employees)

print(f"The mean age group of the employees: {mean_age}")

# bar graph
plt.figure(figsize=(8,6))
plt.bar(age_groups, employees, color='blue', alpha=0.7)
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.title("Distribution of Employees' Ages")
plt.show()
