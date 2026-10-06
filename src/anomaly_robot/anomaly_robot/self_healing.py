import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class SelfHealing(Node):

    def __init__(self):
        super().__init__('self_healing')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info('Self-Healing Node Started')
        self.get_logger().info('Monitoring robot for faults...')

    def scan_callback(self, msg):

        valid_ranges = [
            r for r in msg.ranges
            if r > msg.range_min and r < msg.range_max
        ]

        if not valid_ranges:
            self.get_logger().warn(
                'LiDAR fault detected! Starting self-healing...'
            )

            stop = Twist()
            self.publisher.publish(stop)

            self.get_logger().info(
                'Robot stopped for safety recovery.'
            )

        elif min(valid_ranges) < 0.20:
            self.get_logger().warn(
                'Obstacle/fault detected! Self-healing action activated.'
            )

            stop = Twist()
            self.publisher.publish(stop)


def main(args=None):

    rclpy.init(args=args)

    node = SelfHealing()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
