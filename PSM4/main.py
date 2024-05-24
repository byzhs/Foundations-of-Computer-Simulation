import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
dt = 0.1
t_max = 5
n = int(t_max / dt)

alpha = np.deg2rad(45)

m_sphere = 1
r_sphere = 0.1
I_sphere = 2 / 5 * m_sphere * r_sphere ** 2
v_sphere = 0
s_sphere = 0
gamma_sphere = 0

# Cylinder
m_cylinder = 1
r_cylinder = 0.1
I_cylinder = 1 / 2 * m_cylinder * r_cylinder ** 2
v_cylinder = 0
s_cylinder = 0
gamma_cylinder = 0

times = np.arange(0, t_max, dt)
positions_sphere = np.zeros(n)
positions_cylinder = np.zeros(n)
rotation_sphere = np.zeros(n)
rotation_cylinder = np.zeros(n)
energy_potential_sphere = np.zeros(n)
energy_kinetic_sphere = np.zeros(n)
energy_total_sphere = np.zeros(n)
energy_potential_cylinder = np.zeros(n)
energy_kinetic_cylinder = np.zeros(n)
energy_total_cylinder = np.zeros(n)

for i in range(n):
    acc_sphere = g * np.sin(alpha) / (1 + I_sphere / (m_sphere * r_sphere ** 2))
    v_sphere += acc_sphere * dt
    s_sphere += v_sphere * dt
    gamma_sphere += v_sphere / r_sphere * dt

    acc_cylinder = g * np.sin(alpha) / (1 + I_cylinder / (m_cylinder * r_cylinder ** 2))
    v_cylinder += acc_cylinder * dt
    s_cylinder += v_cylinder * dt
    gamma_cylinder += v_cylinder / r_cylinder * dt

    h_sphere = s_sphere * np.sin(alpha)
    h_cylinder = s_cylinder * np.sin(alpha)

    energy_potential_sphere[i] = m_sphere * g * h_sphere
    energy_kinetic_sphere[i] = 0.5 * m_sphere * v_sphere ** 2 + 0.5 * I_sphere * (v_sphere / r_sphere) ** 2
    energy_total_sphere[i] = energy_potential_sphere[i] + energy_kinetic_sphere[i]

    energy_potential_cylinder[i] = m_cylinder * g * h_cylinder
    energy_kinetic_cylinder[i] = 0.5 * m_cylinder * v_cylinder ** 2 + 0.5 * I_cylinder * (v_cylinder / r_cylinder) ** 2
    energy_total_cylinder[i] = energy_potential_cylinder[i] + energy_kinetic_cylinder[i]

    positions_sphere[i] = s_sphere
    positions_cylinder[i] = s_cylinder
    rotation_sphere[i] = gamma_sphere
    rotation_cylinder[i] = gamma_cylinder

fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# Position (Sphere)
axs[0, 0].plot(times, positions_sphere, label='Sphere')
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Position (m)')
axs[0, 0].set_title('Position vs Time (Sphere)')
axs[0, 0].legend()

# Rotation (Sphere)
axs[1, 0].plot(times, rotation_sphere, label='Sphere')
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Rotation (rad)')
axs[1, 0].set_title('Rotation vs Time (Sphere)')
axs[1, 0].legend()

# Energy (Sphere)
axs[2, 0].plot(times, energy_potential_sphere, label='Potential Energy')
axs[2, 0].plot(times, energy_kinetic_sphere, label='Kinetic Energy')
axs[2, 0].plot(times, energy_total_sphere, label='Total Energy')
axs[2, 0].set_xlabel('Time (s)')
axs[2, 0].set_ylabel('Energy (J)')
axs[2, 0].set_title('Energy vs Time (Sphere)')
axs[2, 0].legend()

# Position (Cylinder)
axs[0, 1].plot(times, positions_cylinder, label='Cylinder')
axs[0, 1].set_xlabel('Time (s)')
axs[0, 1].set_ylabel('Position (m)')
axs[0, 1].set_title('Position vs Time (Cylinder)')
axs[0, 1].legend()

# Rotation (Cylinder)
axs[1, 1].plot(times, rotation_cylinder, label='Cylinder')
axs[1, 1].set_xlabel('Time (s)')
axs[1, 1].set_ylabel('Rotation (rad)')
axs[1, 1].set_title('Rotation vs Time (Cylinder)')
axs[1, 1].legend()

# Energy (Cylinder)
axs[2, 1].plot(times, energy_potential_cylinder, label='Potential Energy')
axs[2, 1].plot(times, energy_kinetic_cylinder, label='Kinetic Energy')
axs[2, 1].plot(times, energy_total_cylinder, label='Total Energy')
axs[2, 1].set_xlabel('Time (s)')
axs[2, 1].set_ylabel('Energy (J)')
axs[2, 1].set_title('Energy vs Time (Cylinder)')
axs[2, 1].legend()

plt.tight_layout()
plt.show()
