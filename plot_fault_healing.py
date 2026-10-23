import csv
import os
import matplotlib.pyplot as plt

base = os.path.expanduser("~/anomaly_ws/results")
csv_file = os.path.join(base, "odom_data.csv")

times, linear, angular = [], [], []

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        times.append(float(row["time_sec"]))
        linear.append(float(row["linear_velocity"]))
        angular.append(float(row["angular_velocity"]))

fig, ax = plt.subplots(3, 1, figsize=(11, 9))

ax[0].plot(times, linear)
ax[0].set_title("Robot Linear Velocity - Fault Run")
ax[0].set_ylabel("Velocity (m/s)")
ax[0].grid(True)

ax[1].plot(times, angular)
ax[1].set_title("Robot Angular Velocity - Fault Run")
ax[1].set_ylabel("Angular velocity (rad/s)")
ax[1].grid(True)

ax[2].plot(times, linear, label="Linear velocity")
ax[2].plot(times, angular, label="Angular velocity")
ax[2].set_title("Robot Response During Operation")
ax[2].set_xlabel("Time (seconds)")
ax[2].legend()
ax[2].grid(True)

plt.tight_layout()
output = os.path.join(base, "fault_healing_graph.png")
plt.savefig(output, dpi=150)
print(f"Graph saved to: {output}")
plt.show()
