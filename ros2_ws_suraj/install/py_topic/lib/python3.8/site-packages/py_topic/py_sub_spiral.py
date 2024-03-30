import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):

    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'greetings',
            self.callback,
            10)

    def callback(self, msg):
        self.get_logger().info("Received message: %s" % msg.data)

def main():
    rclpy.init()
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

