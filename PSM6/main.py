import numpy as np
import matplotlib.pyplot as plt

length = np.pi
num_points = 10
dx = length / num_points
dt = 0.2
num_steps = 50

positions = np.zeros(num_points + 1)
for i in range(1, num_points):
    positions[i] = np.sin(i * dx)

velocities = np.zeros(num_points + 1)

kinetic_energies = []
potential_energies = []
total_energies = []

def calculate_acceleration(positions, dx):
    accelerations = np.zeros_like(positions)
    for i in range(1, num_points):
        accelerations[i] = (positions[i - 1] - 2 * positions[i] + positions[i + 1]) / dx ** 2
    return accelerations

def simulation_step(positions, velocities, accelerations, dt):
    half_velocities = velocities + 0.5 * accelerations * dt
    new_positions = positions + half_velocities * dt
    new_accelerations = calculate_acceleration(new_positions, dx)
    new_velocities = half_velocities + 0.5 * new_accelerations * dt
    return new_positions, new_velocities, new_accelerations

def calculate_energies(positions, velocities, dx):
    ek = 0.5 * np.sum(dx * velocities[1:num_points] ** 2)
    ep = 0.5 * np.sum((positions[1:num_points+1] - positions[:num_points]) ** 2 / dx)
    return ek, ep

acceleration = calculate_acceleration(positions, dx)
for _ in range(num_steps):
    positions, velocities, acceleration = simulation_step(positions, velocities, acceleration, dt)
    ek, ep = calculate_energies(positions, velocities, dx)
    et = ek + ep

    kinetic_energies.append(ek)
    potential_energies.append(ep)
    total_energies.append(et)

print("Kinetic Energies:", kinetic_energies)
print("Potential Energies:", potential_energies)
print("Total Energies:", total_energies)

plt.plot(kinetic_energies, label='Kinetic Energy')
plt.plot(potential_energies, label='Potential Energy')
plt.plot(total_energies, label='Total Energy')
plt.legend()
plt.xlabel('Time (steps)')
plt.ylabel('Energy')
plt.title('Energy Variation Over Time')
plt.show()
