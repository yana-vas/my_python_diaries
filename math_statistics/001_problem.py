import matplotlib.pyplot as plt

# data
subjects = ['Mathematics', 'Science', 'History', 'Art', 'Physical Education']
students = [45, 35, 30, 20, 20]

# probability calculation
total_students = sum(students)
prob_math = students[0] / total_students

print(f"The probability that a randomly selected student likes Mathematics more than any other subject: {prob_math}")

# pie chart
plt.figure(figsize=(6,6))
plt.pie(students, labels=subjects, autopct='%1.1f%%')
plt.title("Students' Favorite Subjects")
plt.show()
