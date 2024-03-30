import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher = self.create_publisher(String, 'greetings', 10)
        self.timer = self.create_timer(0.5, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = "Hello! ROS2 is fun"
        self.publisher.publish(msg)
        self.get_logger().info("Message published: %s" % msg.data)

def main():
    rclpy.init()
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

