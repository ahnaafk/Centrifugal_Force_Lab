#Graph of Frequency vs Magnitude of Tension by Ahnaaf Khan @ March 30th, 2023

import matplotlib.pyplot as plt
import numpy as np

def find_slope(a, b):
    slope, intercept = np.polyfit(a,b,1)
    return slope, intercept

fig, ax = plt.subplots(figsize=(8, 6))

y = np.array([2.44, 2.02, 1.69, 1.23,]) # frequency
x = np.array([1.96, 1.47, 0.98, 0.49]) # magnitude of tension

x = np.sqrt(x)


# Set plot title and axes labels
ax.set(title = "Frequency vs Force of Tension",
       xlabel = "Force of Tension (N)",
       ylabel = "Frequency (Hz)")

ax.plot(x, y, marker='o', color="b")

slope, intercept = find_slope(x,y)

print(f"""Slope: {slope} \nIntercept: {intercept}""")

plt.show()
