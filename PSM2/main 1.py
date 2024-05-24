import pandas as pd
import matplotlib.pyplot as plt

GRAVITATIONAL_ACCELERATION = -10
TIME_STEP = 0.01
INITIAL_VELOCITY_X = 10
INITIAL_VELOCITY_Y = 10
MASS = 1
DRAG_COEFFICIENT = 0.2

time = 0
posX = 0
posY = 0.01
velocityX = INITIAL_VELOCITY_X
velocityY = INITIAL_VELOCITY_Y

posXImproved = 0
posYImproved = 0.01
velocityXImproved = INITIAL_VELOCITY_X
velocityYImproved = INITIAL_VELOCITY_Y

data = []

while posY > 0 or posYImproved > 0:
    # Euler's Method
    accelerationX = -DRAG_COEFFICIENT * velocityX / MASS
    accelerationY = GRAVITATIONAL_ACCELERATION - DRAG_COEFFICIENT * velocityY / MASS
    posX += velocityX * TIME_STEP
    posY += velocityY * TIME_STEP
    velocityX += accelerationX * TIME_STEP
    velocityY += accelerationY * TIME_STEP

    # Midpoint Method
    midVelocityX = velocityXImproved + accelerationX * TIME_STEP / 2
    midVelocityY = velocityYImproved + accelerationY * TIME_STEP / 2
    midAccelerationX = -DRAG_COEFFICIENT * midVelocityX / MASS
    midAccelerationY = GRAVITATIONAL_ACCELERATION - DRAG_COEFFICIENT * midVelocityY / MASS
    posXImproved += midVelocityX * TIME_STEP
    posYImproved += midVelocityY * TIME_STEP
    velocityXImproved += midAccelerationX * TIME_STEP
    velocityYImproved += midAccelerationY * TIME_STEP

    data.append([time, posX, posY, velocityX, velocityY, posXImproved, posYImproved])
    time += TIME_STEP

    if posY <= 0 and posYImproved <= 0:
        break

df = pd.DataFrame(data, columns=['Time', 'PosX', 'PosY', 'VelocityX', 'VelocityY', 'PosXImproved', 'PosYImproved'])
df.to_csv('projectile_motion.csv', index=False)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['PosX'], df['PosY'], label='Euler Method')
plt.plot(df['PosXImproved'], df['PosYImproved'], label='Midpoint Method')
plt.title('Projectile Motion Simulation')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.legend()
plt.grid(True)
plt.show()
