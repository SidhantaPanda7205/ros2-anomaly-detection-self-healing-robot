ROS 2 Anomaly Detection & Self-Healing Robot

1. Project Overview

This project focuses on developing a ROS 2-based robotic system that detects abnormal robot behavior and activates self-healing actions in a simulated environment using Gazebo. The system monitors robot movement, collects odometry data, detects simulated faults, and records results for analysis.

2. Objectives

- To monitor robot movement using ROS 2.
- To collect and analyze robot odometry data.
- To detect abnormal behavior and simulated faults.
- To activate self-healing actions when faults are detected.
- To compare normal and faulty robot behavior using graphs and recorded data.

3. Technologies Used

- Ubuntu 22.04
- ROS 2
- Gazebo Simulator
- Python
- TurtleBot3 (if configured)
- CSV data files
- Graph visualization

4. Key Features

- Robot movement monitoring
- Anomaly and fault detection
- Self-healing action activation
- Odometry data collection
- Normal, fault, and movement test scenarios
- Graph generation and result analysis
- ROS bag data recording

5. Project Structure

anomaly_ws/
├── results/
│   ├── normal_run/
│   ├── fault_run/
│   └── movement_run/
├── final_backup/
├── src/
└── README.md

6. Working Methodology

1. Start the ROS 2 environment and Gazebo simulation.
2. Launch the robot and monitor its movement.
3. Collect odometry and simulation data.
4. Run the anomaly detection process.
5. Detect abnormal behavior or simulated faults.
6. Activate the self-healing response.
7. Save the collected data and generate graphs.
8. Compare normal and faulty robot behavior.

7. Results

The project stores simulation recordings, CSV files, and generated graphs in the "results/" and "final_backup/" directories. These results help analyze robot movement and evaluate the behavior of the anomaly detection and self-healing system.

8. Applications

- Autonomous robotics
- Robot fault monitoring
- Robotics simulation and testing
- Intelligent fault recovery systems
- Research in reliable robotic systems

9. Future Enhancements

- Improve anomaly detection accuracy.
- Add more fault scenarios.
- Develop real-time monitoring dashboards.
- Include additional performance metrics.
- Test the system under more simulated conditions.

10. Conclusion

This project demonstrates a ROS 2-based approach to anomaly detection and self-healing in robotic simulation. By monitoring robot behavior, collecting data, and activating recovery actions, the system supports research into more reliable and fault-tolerant robotic applications.

GitHub Repository

https://github.com/SidhantaPanda7205/ros2-anomaly-detection-self-healing-robot
