import numpy as np
import matplotlib.pyplot as plt
import math as m

G = 6.6743e-11
dt = 7200
n = m.ceil(31556926 / dt)
mass_moon = 7.347e22

mass_earth = 5.972e24
moon_distance = 384000000
moon_velocity = m.sqrt(G * mass_earth / moon_distance)

mass_sun = 1.989e30
sun_distance = 1.5e11
sun_velocity = m.sqrt(G * mass_sun / sun_distance)

moon_x, moon_y, moon_vx, moon_vy = 0, moon_distance, moon_velocity, 0
earth_x, earth_y, earth_vx, earth_vy = 0, sun_distance, sun_velocity, 0

moon_radius = np.zeros(n)
moon_theta = np.zeros(n)
earth_xpos = np.zeros(n)
earth_ypos = np.zeros(n)

for i in range(n):
    moon_radius[i] = np.sqrt((moon_x + earth_x)**2 + (moon_y + earth_y)**2)
    moon_theta[i] = np.arctan2(moon_y + earth_y, moon_x + earth_x)
    earth_xpos[i], earth_ypos[i] = earth_x, earth_y

    rel_x, rel_y = 0 - moon_x, 0 - moon_y
    distance_to_earth = m.sqrt(rel_x**2 + rel_y**2)
    unit_x, unit_y = rel_x / distance_to_earth, rel_y / distance_to_earth
    acceleration = G * mass_earth / distance_to_earth**2
    acceleration_x, acceleration_y = unit_x * acceleration, unit_y * acceleration

    mid_moon_x, mid_moon_y = moon_x + moon_vx * dt / 2, moon_y + moon_vy * dt / 2
    mid_moon_vx, mid_moon_vy = moon_vx + acceleration_x * dt / 2, moon_vy + acceleration_y * dt / 2
    dx, dy = mid_moon_vx * dt, mid_moon_vy * dt
    dvx, dvy = acceleration_x * dt, acceleration_y * dt

    moon_x, moon_y = moon_x + dx, moon_y + dy
    moon_vx, moon_vy = moon_vx + dvx, moon_vy + dvy

    rel_sun_x, rel_sun_y = 0 - earth_x, 0 - earth_y
    distance_to_sun = m.sqrt(rel_sun_x**2 + rel_sun_y**2)
    sun_unit_x, sun_unit_y = rel_sun_x / distance_to_sun, rel_sun_y / distance_to_sun
    sun_acceleration = G * mass_sun / distance_to_sun**2
    sun_acceleration_x, sun_acceleration_y = sun_unit_x * sun_acceleration, sun_unit_y * sun_acceleration

    mid_earth_x, mid_earth_y = earth_x + earth_vx * dt / 2, earth_y + earth_vy * dt / 2
    mid_earth_vx, mid_earth_vy = earth_vx + sun_acceleration_x * dt / 2, earth_vy + sun_acceleration_y * dt / 2
    dx, dy = mid_earth_vx * dt, mid_earth_vy * dt
    dvx, dvy = sun_acceleration_x * dt, sun_acceleration_y * dt

    earth_x, earth_y = earth_x + dx, earth_y + dy
    earth_vx, earth_vy = earth_vx + dvx, earth_vy + dvy

moon_xpos = moon_distance * np.cos(moon_theta)
moon_ypos = moon_distance * np.sin(moon_theta)

moon_position = np.column_stack((moon_xpos, moon_ypos))
earth_position = np.column_stack((earth_xpos, earth_ypos))

moon_max_x = np.max(np.abs(moon_position[:, 0]))
moon_max_y = np.max(np.abs(moon_position[:, 1]))
earth_max_x = np.max(np.abs(earth_position[:, 0]))
earth_max_y = np.max(np.abs(earth_position[:, 1]))

plt.figure()
plt.plot(moon_position[:, 0], moon_position[:, 1], label="Moon")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Moon Orbit")
plt.xlim(-moon_max_x, moon_max_x)
plt.ylim(-moon_max_y, moon_max_y)
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(earth_position[:, 0], earth_position[:, 1], label="Earth")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Earth Orbit")
plt.xlim(-earth_max_x, earth_max_x)
plt.ylim(-earth_max_y, earth_max_y)
plt.legend()
plt.grid()
plt.show()

G = 6.6743e-11
dt = 7200
n = m.ceil(31556926 / dt)
mass_moon = 7.347e22
mass_earth = 5.972e24
mass_sun = 1.989e30
moon_distance = 384000000
sun_distance = 1.5e11
moon_velocity = m.sqrt(G * mass_earth / moon_distance)
sun_velocity = m.sqrt(G * mass_sun / sun_distance)

moon_x, moon_y, moon_vx, moon_vy = 0, moon_distance, moon_velocity, 0
earth_x, earth_y, earth_vx, earth_vy = 0, sun_distance, sun_velocity, 0

moon_position = np.zeros((n, 2))
earth_position = np.zeros((n, 2))
moon_relative_to_sun = np.zeros((n, 2))

for i in range(n):
    distance_to_earth = m.sqrt(moon_x**2 + moon_y**2)
    acceleration = -G * mass_earth / distance_to_earth**3
    moon_vx += acceleration * moon_x * dt
    moon_vy += acceleration * moon_y * dt
    moon_x += moon_vx * dt
    moon_y += moon_vy * dt
    moon_position[i] = [moon_x, moon_y]

    distance_to_sun = m.sqrt(earth_x**2 + earth_y**2)
    sun_acceleration = -G * mass_sun / distance_to_sun**3
    earth_vx += sun_acceleration * earth_x * dt
    earth_vy += sun_acceleration * earth_y * dt
    earth_x += earth_vx * dt
    earth_y += earth_vy * dt
    earth_position[i] = [earth_x, earth_y]

    moon_relative_to_sun[i] = moon_position[i] + earth_position[i]

plt.figure(figsize=(10, 6))
plt.plot(moon_relative_to_sun[:, 0], moon_relative_to_sun[:, 1], label="Moon's trajectory relative to Sun")
plt.plot(earth_position[:, 0], earth_position[:, 1], label="Earth's trajectory around Sun", linestyle='--')
plt.scatter(0, 0, color='orange', label='Sun')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Moon's Trajectory Relative to the Sun")
plt.legend()
plt.grid()
plt.show()
