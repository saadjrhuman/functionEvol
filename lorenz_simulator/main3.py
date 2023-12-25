import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def lorenz(x, y, z, sigma, rho, beta):
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return x_dot, y_dot, z_dot

dt = 0.01
num_steps = 10000

# Set parameters
sigma, rho, beta = 10., 28., 8./3.

# Set initial conditions for multiple attractors
initial_conditions = [
    (0., 1., 1.05),
    (1., -1., 0.5),
    (-1., 0., 1.5)
]

# Create figure and 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Lorenz Attractor")
ax.set_facecolor('black')

# Initialize line object
line, = ax.plot([], [], [], lw=0.5)

# Update function for the animation
def update(frame):
    x_vals, y_vals, z_vals = [], [], []
    for i, initial_condition in enumerate(initial_conditions):
        x, y, z = initial_condition
        xs = np.empty(num_steps + 1)
        ys = np.empty(num_steps + 1)
        zs = np.empty(num_steps + 1)
        xs[0], ys[0], zs[0] = x, y, z

        for j in range(num_steps):
            x_dot, y_dot, z_dot = lorenz(xs[j], ys[j], zs[j], sigma, rho, beta)
            xs[j + 1] = xs[j] + x_dot * dt
            ys[j + 1] = ys[j] + y_dot * dt
            zs[j + 1] = zs[j] + z_dot * dt

        x_vals.append(xs[:frame])
        y_vals.append(ys[:frame])
        z_vals.append(zs[:frame])

    line.set_data(np.concatenate(x_vals), np.concatenate(y_vals))
    line.set_3d_properties(np.concatenate(z_vals))
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_steps + 1, interval=10, blit=True)
plt.axis('off')
# Display the animation
plt.show()
