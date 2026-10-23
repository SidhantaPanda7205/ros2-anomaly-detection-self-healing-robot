import csv
from pathlib import Path

import rosbag2_py
from rclpy.serialization import deserialize_message
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt

BASE = Path.home() / "anomaly_ws" / "results"


def extract_odom(bag_name, output_name):
    bag_path = BASE / bag_name
    reader = rosbag2_py.SequentialReader()

    reader.open(
        rosbag2_py.StorageOptions(
            uri=str(bag_path),
            storage_id="sqlite3"
        ),
        rosbag2_py.ConverterOptions("", "")
    )

    topics = reader.get_all_topics_and_types()
    if not any(t.name == "/odom" for t in topics):
        raise RuntimeError(f"/odom topic not found in {bag_name}")

    rows = []
    first_time = None

    while reader.has_next():
        topic, data, timestamp = reader.read_next()

        if topic != "/odom":
            continue

        msg = deserialize_message(data, Odometry)

        if first_time is None:
            first_time = timestamp

        t = (timestamp - first_time) / 1e9

        rows.append([
            t,
            msg.pose.pose.position.x,
            msg.pose.pose.position.y,
            msg.twist.twist.linear.x,
            msg.twist.twist.angular.z
        ])

    output_path = BASE / output_name

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "time_sec", "x", "y",
            "linear_velocity", "angular_velocity"
        ])
        writer.writerows(rows)

    print(f"{bag_name}: extracted {len(rows)} odometry messages")
    print(f"Saved: {output_path}")

    return rows


normal = extract_odom(
    "normal_run", "normal_odom.csv"
)
fault = extract_odom(
    "fault_run", "fault_odom.csv"
)

fig, axes = plt.subplots(2, 1, figsize=(11, 8))

axes[0].plot(
    [r[0] for r in normal],
    [r[3] for r in normal],
    label="Normal Run"
)
axes[0].plot(
    [r[0] for r in fault],
    [r[3] for r in fault],
    label="Fault Run"
)
axes[0].set_title("Normal vs Fault: Linear Velocity")
axes[0].set_xlabel("Time (seconds)")
axes[0].set_ylabel("Velocity (m/s)")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(
    [r[0] for r in normal],
    [r[4] for r in normal],
    label="Normal Run"
)
axes[1].plot(
    [r[0] for r in fault],
    [r[4] for r in fault],
    label="Fault Run"
)
axes[1].set_title("Normal vs Fault: Angular Velocity")
axes[1].set_xlabel("Time (seconds)")
axes[1].set_ylabel("Angular velocity (rad/s)")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()

output_graph = BASE / "normal_vs_fault_comparison.png"
plt.savefig(output_graph, dpi=200)
print(f"Comparison graph saved: {output_graph}")

plt.show()
