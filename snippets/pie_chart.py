import matplotlib.pyplot as plt

# Daten
labels = ['Python', 'numpy', 'pandas', 'scikit-learn']
sizes = [35, 15, 30, 20]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Kuchendiagramm erstellen
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Data Science Toolkit')
plt.axis('equal')
plt.show()
