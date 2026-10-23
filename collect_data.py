import csv
import os
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class Collector(Node):
    def __init__(self):
        super().__init__('odom_csv_collector')
        path = os.path.expanduser(
            '~/anomaly_ws/results/odom_data.csv')
        self.file = open(path, 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow([
            'time_sec', 'x', 'y', 'linear_velocity',
            'angular_velocity'
        ])
        self.start = self.get_clock().now()
        self.sub = self.create_subscription(
            Odometry, '/odom', self.callback, 10)
        self.count = 0
        self.get_logger().info('Waiting for odometry...')

    def callback(self, msg):
        t = (self.get_clock().now() - self.start).nanoseconds / 1e9
        self.writer.writerow([
            t,
            msg.pose.pose.position.x,
            msg.pose.pose.position.y,
            msg.twist.twist.linear.x,
            msg.twist.twist.angular.z
        ])
        self.count += 1
        if self.count % 20 == 0:
            self.file.flush()
            self.get_logger().info(
                f'Recorded {self.count} rows')

    def destroy_node(self):
        self.file.close()
        super().destroy_node()

def main():
    rclpy.init()
    node = Collector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
