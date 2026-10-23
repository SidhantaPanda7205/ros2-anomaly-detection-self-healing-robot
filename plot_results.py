import os
import pandas as pd
import matplotlib.pyplot as plt

folder = os.path.expanduser('~/anomaly_ws/results')
csv_file = os.path.join(folder, 'odom_data.csv')

df = pd.read_csv(csv_file)

if df.empty:
    raise ValueError("CSV file has no data")

fig, ax = plt.subplots(3, 1, figsize=(10, 9))

ax[0].plot(df['time_sec'], df['x'], label='X position')
ax[0].plot(df['time_sec'], df['y'], label='Y position')
ax[0].set_title('Robot Position vs Time')
ax[0].set_ylabel('Position (m)')
ax[0].legend()
ax[0].grid(True)

ax[1].plot(df['time_sec'], df['linear_velocity'])
ax[1].set_title('Linear Velocity vs Time')
ax[1].set_ylabel('Velocity (m/s)')
ax[1].grid(True)

ax[2].plot(df['time_sec'], df['angular_velocity'])
ax[2].set_title('Angular Velocity vs Time')
ax[2].set_xlabel('Time (seconds)')
ax[2].set_ylabel('Angular velocity (rad/s)')
ax[2].grid(True)

plt.tight_layout()

output = os.path.join(folder, 'robot_results.png')
plt.savefig(output, dpi=150)
print(f'Graph saved to: {output}')

plt.show()
