import numpy as np
import matplotlib.pyplot as plt
# Physical properties of the material
mass = 2.0 # Mass in kg
specific_heat = 900 # Specific heat capacity in J/(kg*K)
initial_temp = 300 # Initial temperature in Kelvin
# Generate final temperatures from 300 K to 1000 K
final_temp = np.linspace(300, 1000, 100)
# Calculate entropy change
entropy_change = mass * specific_heat * np.log(final_temp / initial_temp)
# Calculate heat transferred
heat_transferred = mass * specific_heat * (final_temp - initial_temp)

# Display selected results
print("Entropy Change Simulation")
print("-" * 35)
for i in [0, 25, 50, 75, 99]:
    print( f"Temperature: {final_temp[i]:.1f} K | "
           f"Heat: {heat_transferred[i]:.1f} J | "
           f"Entropy Change: {entropy_change[i]:.2f} J/K" )
# Create two plots
plt.figure(figsize=(12, 5))
# Plot 1: Entropy change versus temperature
plt.subplot(1, 2, 1)
plt.plot(final_temp, entropy_change, label="Entropy Change")
plt.xlabel("Final Temperature (K)")
plt.ylabel("Entropy Change (J/K)")
plt.title("Entropy vs Temperature")
plt.grid(True)
plt.legend()
# Plot 2: Heat transferred versus temperature
plt.subplot(1, 2, 2)
plt.plot(final_temp, heat_transferred, label="Heat Transferred")
plt.xlabel("Final Temperature (K)")
plt.ylabel("Heat (J)")
plt.title("Heat vs Temperature")
plt.grid(True)
plt.legend()
# Adjust layout and display plots
plt.tight_layout()
plt.show()