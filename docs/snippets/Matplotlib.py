import matplotlib.pyplot as plt

# Basic Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()

# Line Styles and Markers
plt.plot(x, y, linestyle='--', marker='o', color='r')
plt.show()

# Axis Labels and Title
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Title')
plt.show()

# Multiple Plots
plt.subplot(1, 2, 1)
plt.plot(x, y, color='r')
plt.subplot(1, 2, 2)
plt.plot(y, x, color='b')
plt.show()

# Bar Chart
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]
plt.bar(x, y)
plt.show()

# Histogram
data = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5]
plt.hist(data, bins=5)
plt.show()

# Scatter Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.show()

# Pie Chart
sizes = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

# Saving Figure
plt.plot(x, y)
plt.savefig('plot.png')

# Customizing Figure Size
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.show()
