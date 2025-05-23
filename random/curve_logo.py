import matplotlib.pyplot as plt
import numpy as np

cos = np.cos 
sin = np.sin
sqrt = np.sqrt 
pi = np.pi 

def surf(u, v):
    """
    https://en.wikipedia.org/wiki/Klein_bottle
    http://paulbourke.net/geometry/toroidal/  
    credit: crv.mktcap.eth
    """
    half = (0 <= u) & (u < pi)
    r = 4 * (1 - cos(u) / 2)
    x = 6 * cos(u) * (1 + sin(u)) + r * cos(v + pi)
    x[half] = (
        (6 * cos(u) * (1 + sin(u)) + r * cos(u) * cos(v))[half])
    y = 16 * sin(u)
    y[half] = (16 * sin(u) + r * sin(u) * cos(v))[half]
    z = r * sin(v)
    return x, y, z

# Generate points for the Klein bottle
u, v = np.linspace(0, 2 * pi, 40), np.linspace(0, 2 * pi, 40)
ux, vx = np.meshgrid(u, v)
x, y, z = surf(ux, vx)

# Create a 3D plot
fig = plt.figure(figsize=(30,10))
ax = fig.add_subplot(111, projection="3d")

# Plot the Klein bottle 
ax.plot_surface(x, y, z, cmap="jet", edgecolor="black")
plt.show()