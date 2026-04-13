import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray  
from geometry_msgs.msg import Twist

class HolonomicController(Node):
    def __init__(self):
        super().__init__('holonomic_controller')
        
        self.publisher_ = self.create_publisher(
            Float64MultiArray, 
            '/wheel_controller/commands', 
            10)

       
        self.subscription = self.create_subscription(
            Twist, 
            '/cmd_vel', 
            self.callback, 
            10)
        
        self.get_logger().info('Holonomic Controller has been started!')

    def callback(self, msg):
        vx = msg.linear.x
        vy = msg.linear.y
        
        
        msg_array = Float64MultiArray()
        msg_array.data = [vx, vx, vx, vx, vy, vy, vy, vy]
        
        self.publisher_.publish(msg_array)

def main(args=None):
    rclpy.init(args=args)
    node = HolonomicController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()