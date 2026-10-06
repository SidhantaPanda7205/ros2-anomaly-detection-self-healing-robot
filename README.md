# ROS2-Based Anomaly Detection & Self-Healing Robot

## 📌 Project Overview

This project presents a ROS 2-based robotic system for detecting anomalies and performing a basic self-healing safety action using a TurtleBot3 Burger robot in Gazebo simulation.

The robot uses LiDAR sensor data to monitor its surroundings. When an obstacle or abnormal condition is detected within a predefined distance, the system identifies the condition as an anomaly and activates the self-healing safety mechanism by stopping the robot.

## 🎯 Objectives

- Detect abnormal conditions using LiDAR data.
- Monitor the robot's surroundings continuously.
- Detect nearby obstacles as potential anomalies.
- Automatically stop the robot when an anomaly is detected.
- Demonstrate fault detection and self-healing behavior in simulation.

## 🛠️ Technologies Used

- ROS 2 Humble
- Ubuntu 22.04
- Gazebo
- TurtleBot3 Burger
- Python
- LiDAR Sensor
- ROS 2 Topics

## 🏗️ System Architecture

```text
        LiDAR Sensor
             ↓
        /scan Topic
             ↓
    Anomaly Detection Node
             ↓
      Fault/Obstacle
        Detection
             ↓
     Self-Healing Node
             ↓
        /cmd_vel
             ↓
       Robot Stop


📂 Project Structure
anomaly_ws/
└── src/
    └── anomaly_robot/
        ├── anomaly_robot/
        │   ├── __init__.py
        │   ├── anomaly_detector.py
        │   ├── self_healing.py
        │   └── robot_controller.py
        ├── package.xml
        └── setup.py


⚙️ How the System Works
1.TurtleBot3 Burger is launched in Gazebo.
2.The LiDAR sensor continuously publishes data through the /scan topic.
3.The Anomaly Detector Node processes the LiDAR data.
4.If an obstacle is detected below the defined safety distance, an anomaly is reported.
5.The Self-Healing Node receives the sensor information.
6.A safety stop command is published through /cmd_vel.
7.The robot stops to prevent unsafe movement.


🚀 How to Run
1. Source ROS 2
source /opt/ros/humble/setup.bash


2. Source the project workspace
source ~/anomaly_ws/install/setup.bash


3. Set TurtleBot3 model
export TURTLEBOT3_MODEL=burger


4. Launch Gazebo
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py


5. Run Anomaly Detector
ros2 run anomaly_robot anomaly_detector


6. Run Self-Healing Node
Open another terminal and run-:
source /opt/ros/humble/setup.bash
source ~/anomaly_ws/install/setup.bash
ros2 run anomaly_robot self_healing


🔍 Example Output
Normal Condition-:
Anomaly Detector Started
Monitoring LiDAR /scan data...
Normal - Minimum distance: 0.xx m


Anomaly Detection-:
ANOMALY DETECTED!
Obstacle distance: 0.xx m


Self-Healing Action-:
Self-Healing Node Started
Monitoring robot for faults...
Obstacle/fault detected!
Self-healing action activated.


🧪 Testing
The system was tested in Gazebo using TurtleBot3 Burger.
The following components were verified:
. LiDAR /scan data
. Anomaly detection
. Obstacle detection
. Self-healing safety action
. /cmd_vel stop command
. ROS 2 node communication


🔮 Future Scope
- Automatic recovery and navigation after fault detection.
- Detection of different types of robot faults.
- Machine Learning-based anomaly detection.
- Real-time fault classification.
- Hardware implementation using a physical robot.
- Advanced autonomous recovery strategies.


👨‍💻 Project
ROS2-Based Anomaly Detection & Self-Healing Robot
Developed using ROS 2, Python, Gazebo and TurtleBot3.
