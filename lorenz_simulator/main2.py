import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def lorenz(x, y, z, sigma, rho, beta):
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return x_dot, y_dot, z_dot

dt = 0.01
num_steps = 10000
num_lines = 2

# Set parameters
sigma, rho, beta = 10., 28., 8./3.

# Set initial conditions for multiple lines
np.random.seed(42)  # Set a seed for reproducibility
center = np.array([0.0, 0.0, 20.0])  # Desired center of the attractor
deviation = 5.0  # Maximum deviation from the center

# Generate two initial conditions that are very close
initial_conditions = np.random.randn(2, 3) * deviation + center
initial_conditions[1] = initial_conditions[0] + 1.2e-10


xs = np.zeros((num_lines, num_steps + 1))
ys = np.zeros((num_lines, num_steps + 1))
zs = np.zeros((num_lines, num_steps + 1))
xs[:, 0] = initial_conditions[:, 0]
ys[:, 0] = initial_conditions[:, 1]
zs[:, 0] = initial_conditions[:, 2]

# Perform integration using Euler's method for each line
for i in range(num_lines):
    for j in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i, j], ys[i, j], zs[i, j], sigma, rho, beta)
        xs[i, j + 1] = xs[i, j] + x_dot * dt
        ys[i, j + 1] = ys[i, j] + y_dot * dt
        zs[i, j + 1] = zs[i, j] + z_dot * dt

# Create 3D plot
fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Update function for the animation
lines = []
colors = ['blue', 'yellow']  # Set custom colors for the lines

for i in range(num_lines):
    line, = ax.plot([], [], [], lw=0.5, color=colors[i])
    lines.append(line)

def update(frame):
    for i in range(num_lines):
        lines[i].set_data(xs[i, :frame], ys[i, :frame])
        lines[i].set_3d_properties(zs[i, :frame])
    return lines

# Set the axes limits
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 30)
ax.set_zlim(0, 60)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_steps+1000000, interval=1, blit=True)

# Hide the axes and set the title
ax.axis('off')

# Set the starting azimuth to 133 degrees
ax.view_init(elev=-1, azim=-44)


# Save the animation in 1080p resolution
#ani.save('lorenz_attractor_1080p.mp4', writer='ffmpeg', dpi=240)

# Set subplot parameters
plt.subplots_adjust(left=0, bottom=0, wspace=0, hspace=0, right=1, top=1)
plt.rcParams['lines.antialiased'] = True

plt.show()
