#Graph of Frequency vs Magnitude of Tension & Radius & Mass by Ahnaaf Khan @ March 30th, 2023

import matplotlib.pyplot as plt
import numpy as np

def find_slope(a, b):
    slope, intercept = np.polyfit(a,b,1)
    return slope, intercept

fig, ax = plt.subplots(figsize=(8, 6))

y = np.array([2.44, 2.02, 1.69, 1.23, 2.02, 1.74, 2.06, 2.35, 2.44, 1.81, 1.43, 1.22]) # frequency
r = np.array([0.75, 0.75, 0.75, 0.75, 0.75, 0.65, 0.55, 0.45, 0.75, 0.75, 0.75, 0.75]) # radius
t = np.array([1.96, 1.47, 0.98, 0.49, 0.98, 0.98, 0.98, 0.98, 1.96, 1.96, 1.96, 1.96]) # magnitude of tension 
m = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]) # mass


x = np.sqrt(t)/np.sqrt(m * r)

# Set plot title and axes labels
ax.set(title = "Frequency vs Magnitude of Tension & Radius & Mass",
       xlabel = "Magnitude of Tension & Radius & Mass",
       ylabel = "Frequency (Hz)")

ax.plot(x, y, marker='o', color="b")

slope, intercept = find_slope(x,y)
print(x.shape)

print(f"""Slope: {slope} \nIntercept: {intercept}""")

plt.show()
