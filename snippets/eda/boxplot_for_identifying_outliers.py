import matplotlib.pyplot as plt
import random

random.seed(42)

# Beispieldaten mit jeweils zwei Ausreißern
male_data = [random.randint(31,67) for _ in range(1000)]
male_data.extend([107,7])

female_data = [random.randint(28,70) for _ in range(1000)]
female_data.extend([115,108])

plt.boxplot([male_data, female_data])
plt.title("Box Plot zur Erkennung von Ausreißern")
plt.ylabel("Alter")
plt.ylim(bottom=0)
plt.xticks([1, 2], ["Männer", "Frauen"])

plt.show()