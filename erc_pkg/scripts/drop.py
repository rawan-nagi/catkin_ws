#!/usr/bin/env python
import rospy
from std_msgs.msg import String
 
def callback(data):
    if data == "goal is reached":
        pub.publish("1")
     
def drop():
    global pub
    rospy.init_node('drop', anonymous=True)
    pub = rospy.Publisher('drop', String, queue_size=10)
    rospy.Subscriber("goal_reached", String, callback)
    rate = rospy.Rate(10)
    rospy.spin()
   
if __name__ == '__main__':
    try:
        drop()
    except rospy.ROSInterruptException:
        pass
