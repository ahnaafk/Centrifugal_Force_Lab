#Graph of Frequency vs Mass by Ahnaaf Khan @ March 30th, 2023

import matplotlib.pyplot as plt
import numpy as np

def find_slope(a, b):
    slope, intercept = np.polyfit(a,b,1)
    return slope, intercept

fig, ax = plt.subplots(figsize=(8, 6))

y = np.array([2.44, 1.81, 1.43, 1.22]) # frequency
x = np.array([1, 2, 3, 4]) # mass

x = 1/np.sqrt(x)

# Set plot title and axes labels
ax.set(title = "Frequency vs Mass",
       xlabel = "Mass (kg)",
       ylabel = "Frequency (Hz)")

ax.plot(x, y, marker='o', color="b")

slope, intercept = find_slope(x,y)

print(f"""Slope: {slope} \nIntercept: {intercept}""")

plt.show()
