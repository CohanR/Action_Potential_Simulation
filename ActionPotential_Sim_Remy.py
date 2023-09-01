import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d

# Gaussian function
def gaussian(x, mu, sigma, amplitude):
    return amplitude * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

# Define action potential phases
resting_potential = -70
depolarization_amplitude = 110
hyperpolarization_amplitude = -90

# Create time points and voltage values
time = np.linspace(0, 10, 500)  # Change the x-axis scale to milliseconds (0 to 10 ms)
voltage = np.ones_like(time) * resting_potential

# Depolarization
depolarization_center = 2.5
depolarization_sigma = 0.1
voltage += gaussian(time, depolarization_center, depolarization_sigma, depolarization_amplitude)

# Hyperpolarization
hyperpolarization_center = 3.5
hyperpolarization_sigma = 0.2
voltage += gaussian(time, hyperpolarization_center, hyperpolarization_sigma, hyperpolarization_amplitude - resting_potential)

# Smooth the action potential curve
time_smooth = np.linspace(time.min(), time.max(), 500)
spline = interp1d(time, voltage, kind='cubic')
voltage_smooth = spline(time_smooth)

# Create the plot and set the y-axis limits
fig, ax = plt.subplots()
ax.set_ylim(-100, 70)
ax.set_xlim(0, 10)  # Set x-axis limits to 0 to 10 ms
ax.set_xticks(np.arange(0, 11, 1))  # Set x-axis tick intervals to 1 ms
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Voltage (mV)')
ax.set_title('Action Potential')

# Add resting membrane potential line and 0 mV line
ax.axhline(y=resting_potential, color='gray', linestyle='--', alpha=0.5, zorder=1)
ax.axhline(y=0, color='black', linestyle='-', alpha=0.5, zorder=0)

# Add copyright text as an annotation
ax.annotate("© Remy Cohan", (0.97, 0.03), xycoords='axes fraction', fontsize=8, ha='right', va='bottom', alpha=0.3, zorder=3)

# Initialize the action potential line
line, = ax.plot([], [], color='blue', linewidth=2, zorder=2)

# Animation update function
def update(frame):
    line.set_data(time_smooth[:frame*2], voltage_smooth[:frame*2])
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=len(time_smooth)//2, interval=5, blit=True)

# Save the animation as a GIF
animation.save('action_potential_Remy_Cohan.gif', writer='pillow', fps=90)

