import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 1.0
m = 1.0

alpha0 = np.pi / 4
omega0 = 0.0

t_max = 10
dt = 0.01
steps = int(t_max / dt) + 1

times = np.linspace(0, t_max, steps)


def initialize_arrays():
    alpha = np.zeros(steps)
    omega = np.zeros(steps)
    alpha[0] = alpha0
    omega[0] = omega0
    return alpha, omega


def heuns_method():
    alpha, omega = initialize_arrays()
    for i in range(steps - 1):
        # Predictor step
        alpha_pred = alpha[i] + omega[i] * dt
        omega_pred = omega[i] - (g / l) * np.sin(alpha[i]) * dt
        alpha[i + 1] = alpha[i] + 0.5 * (omega[i] + omega_pred) * dt
        omega[i + 1] = omega[i] - 0.5 * (g / l) * (np.sin(alpha[i]) + np.sin(alpha_pred)) * dt
    return alpha, omega


def rk4_method():
    alpha, omega = initialize_arrays()
    for i in range(steps - 1):
        k1_alpha = omega[i]
        k1_omega = -(g / l) * np.sin(alpha[i])

        k2_alpha = omega[i] + 0.5 * k1_omega * dt
        k2_omega = -(g / l) * np.sin(alpha[i] + 0.5 * k1_alpha * dt)

        k3_alpha = omega[i] + 0.5 * k2_omega * dt
        k3_omega = -(g / l) * np.sin(alpha[i] + 0.5 * k2_alpha * dt)

        k4_alpha = omega[i] + k3_omega * dt
        k4_omega = -(g / l) * np.sin(alpha[i] + k3_alpha * dt)

        alpha[i + 1] = alpha[i] + (dt / 6) * (k1_alpha + 2 * k2_alpha + 2 * k3_alpha + k4_alpha)
        omega[i + 1] = omega[i] + (dt / 6) * (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega)
    return alpha, omega


def plot_results(alpha, omega, method_name):
    kinetic_energy = 0.5 * m * (l * omega) ** 2
    potential_energy = m * g * l * (1 - np.cos(alpha))
    total_energy = kinetic_energy + potential_energy
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(times, alpha, label='α (Angle)')
    plt.title(f'Angular Position (α) - {method_name}')
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')

    plt.subplot(2, 2, 2)
    plt.plot(times, omega, label='ω (Angular velocity)')
    plt.title(f'Angular Velocity (ω) - {method_name}')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular velocity (rad/s)')

    plt.subplot(2, 2, 3)
    plt.plot(times, kinetic_energy, label='Kinetic Energy')
    plt.plot(times, potential_energy, label='Potential Energy')
    plt.plot(times, total_energy, label='Total Energy')
    plt.title(f'Energies - {method_name}')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()

    plt.tight_layout()
    plt.show()

alpha_heuns, omega_heuns = heuns_method()
plot_results(alpha_heuns, omega_heuns, "Heun's Method")

alpha_rk4, omega_rk4 = rk4_method()
plot_results(alpha_rk4, omega_rk4, "RK4 Method")
import numpy as np
import matplotlib.pyplot as plt

g = 9.81  # Acceleration due to gravity (m/s^2)
l = 1.0   # Length of the pendulum (m)
m = 1.0   # Mass of the pendulum (kg)

alpha0 = np.pi / 4  # Initial angle (radians)
omega0 = 0.0        # Initial angular velocity (rad/s)

t_max = 10         # Total time (s)
dt = 0.01          # Time step (s)
steps = int(t_max / dt) + 1  # Number of steps

times = np.linspace(0, t_max, steps)

def euler_method():
    alpha = np.zeros(steps)
    omega = np.zeros(steps)
    alpha[0] = alpha0
    omega[0] = omega0

    for i in range(steps - 1):
        alpha[i + 1] = alpha[i] + omega[i] * dt
        omega[i + 1] = omega[i] - (g / l) * np.sin(alpha[i]) * dt

    return alpha, omega

def calculate_energies(alpha, omega):
    kinetic_energy = 0.5 * m * (l * omega)**2
    potential_energy = m * g * l * (1 - np.cos(alpha))
    total_energy = kinetic_energy + potential_energy
    return kinetic_energy, potential_energy, total_energy

def plot_energies(times, kinetic_energy, potential_energy, total_energy, method_name):
    plt.figure(figsize=(10, 6))
    plt.plot(times, kinetic_energy, label='Kinetic Energy')
    plt.plot(times, potential_energy, label='Potential Energy')
    plt.plot(times, total_energy, label='Total Energy')
    plt.title(f'Energy of a Pendulum Over Time Using {method_name}')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()
    plt.show()

alpha_euler, omega_euler = euler_method()
kinetic_energy, potential_energy, total_energy = calculate_energies(alpha_euler, omega_euler)
plot_energies(times, kinetic_energy, potential_energy, total_energy, "Euler Method")
