import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def lorenz(x, y, z, sigma=10, rho=28, beta=8/3):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

def update(frame, lines):
    for line in lines:
        x, y, z = line[0].get_data()
        dx, dy, dz = lorenz(x[-1], y[-1], z[-1])
        x = np.append(x, x[-1] + dx * dt)
        y = np.append(y, y[-1] + dy * dt)
        z = np.append(z, z[-1] + dz * dt)
        line[0].set_data(x, y)
        line[0].set_3d_properties(z)
    return lines

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

num_lines = 10  # Number of initial conditions
dt = 0.01  # Time step size

lines = []
for _ in range(num_lines):
    x0, y0, z0 = np.random.rand(3) * 20 - 10  # Random initial conditions
    color = np.random.rand(3)
    line, = ax.plot([], [], [], lw=0.5, color=color)
    line.set_data([], [])
    line.set_3d_properties([])
    lines.append((line, color))

ax.set_xlim(-20, 20)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 50)

ani = FuncAnimation(fig, update, frames=1000, fargs=(lines,), interval=10, blit=False)

plt.axis('off')
plt.show()
