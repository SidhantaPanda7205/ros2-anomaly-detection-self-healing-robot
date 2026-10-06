from setuptools import find_packages, setup

package_name = 'anomaly_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='raja',
    maintainer_email='raja@todo.todo',
    description='Anomaly detection and self-healing robot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'anomaly_detector = anomaly_robot.anomaly_detector:main',
        'self_healing = anomaly_robot.self_healing:main',
        'robot_controller = anomaly_robot.robot_controller:main',
    ],
},
)
