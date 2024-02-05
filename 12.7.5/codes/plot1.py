import numpy as np
import matplotlib.pyplot as plt

# Given inductance value
L = 44e-3  # inductance in Henry

# Angular frequency range (from 0 to 10kHz)
omega = np.linspace(0, 10e3 * 2 * np.pi, 1000)  # 1000 points between 0 and 10 kHz

# Impedance calculation
H = abs(1j * omega * L)

# Plot magnitude response
plt.figure(figsize=(8, 6))
plt.plot(omega, H)
plt.title('Magnitude Response')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('|H(jω)|')
plt.grid(True)

# Save the plot as plot1.png
plt.savefig('plot1.png')

plt.show()

