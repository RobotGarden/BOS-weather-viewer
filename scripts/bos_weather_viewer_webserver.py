#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from flask import Flask
app = Flask(__name__)

state = {} # Dict to hold most recent topic values

def topic_callback(data, topic):
    state[topic] = data

@app.route("/")
def webroot():
    return repr(state)

if __name__ == '__main__':
    rospy.init_node("BOSWeatherViwerWebserver")
    rospy.Subscriber("/fy/temperature", Float32, topic_callback, "/fy/temperature")
    rospy.Subscriber("/fy/humidity", Float32, topic_callback, "/fy/humidity")
    try:
        app.run()
    except rospy.ROSInterruptException:
        pass
