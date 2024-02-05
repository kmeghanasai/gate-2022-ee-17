import numpy as np
import matplotlib.pyplot as plt

# Given capacitance value
C = 60e-6  # capacitance in Farads

# Angular frequency range (from 0.1 to 10kHz)
omega = np.linspace(0.1, 10e3, 1000)  # 1000 points between 0.1 and 10 kHz

# Impedance calculation
H = abs(1 / (1j * omega * C))

# Plot magnitude response
plt.figure(figsize=(8, 6))
plt.plot(omega, H)
plt.title('Magnitude Response')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('|H(jω)|')
plt.grid(True)

# Save the plot as plot2.png
plt.savefig('plot2.png')

plt.show()

