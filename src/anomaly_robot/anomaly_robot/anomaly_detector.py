import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class AnomalyDetector(Node):

    def __init__(self):
        super().__init__('anomaly_detector')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info('Anomaly Detector Started')
        self.get_logger().info('Monitoring LiDAR /scan data...')

    def scan_callback(self, msg):
        valid_ranges = [
            r for r in msg.ranges
            if r > msg.range_min and r < msg.range_max
        ]

        if not valid_ranges:
            return

        min_distance = min(valid_ranges)

        # Obstacle/anomaly threshold
        if min_distance < 0.30:
            self.get_logger().warn(
                f'ANOMALY DETECTED! Obstacle distance: {min_distance:.2f} m'
            )
        else:
            self.get_logger().info(
                f'Normal - Minimum distance: {min_distance:.2f} m'
            )


def main(args=None):
    rclpy.init(args=args)

    node = AnomalyDetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
