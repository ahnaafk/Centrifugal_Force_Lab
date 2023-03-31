#Graph of Frequency vs Magnitude of Tension by Ahnaaf Khan @ March 30th, 2023

import matplotlib.pyplot as plt
import numpy as np

def find_slope(a, b):
    slope, intercept = np.polyfit(a,b,1)
    return slope, intercept

fig, ax = plt.subplots(figsize=(8, 6))

y = np.array([2.02, 1.74, 2.06, 2.35]) # frequency
x = np.array([0.75, 0.65, 0.55, 0.45]) # radius

x = 1/np.sqrt(x)

# Set plot title and axes labels
ax.set(title = "Frequency vs Radius",
       xlabel = "Radius (m)",
       ylabel = "Frequency (Hz)")

ax.plot(x, y, marker='o', color="b")

slope, intercept = find_slope(x,y)

print(f"""Slope: {slope} \nIntercept: {intercept}""")

plt.show()
