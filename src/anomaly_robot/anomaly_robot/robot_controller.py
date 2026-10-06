import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(1.0, self.control_robot)

        self.get_logger().info('Robot Controller Started')
        self.get_logger().info('Publishing velocity commands...')

    def control_robot(self):
        msg = Twist()

        msg.linear.x = 0.2
        msg.angular.z = 0.0

        self.publisher.publish(msg)

        self.get_logger().info('Robot moving forward...')


def main(args=None):
    rclpy.init(args=args)

    node = RobotController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
