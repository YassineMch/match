# Master Arbeit Yassine Mechri

## Marvelmind Hardware 
* Marvelmind Indoor Navigation System is an off-the-shelf indoor navigation system, designed to provide precise (±2cm) location data to autonomous robots
* Mobile beacon’s location is calculated based on a propagation delay of an ultrasonic pulses (Time-Of-Flight or TOF) between stationary and mobile beacons using trilateration algorithm. 

### Steps to set up the System

1. Place the Stationary Beacons on the wall in a was that will provide an optimal ultrasonic coverage. dor a 2D navigation, 2 Stationary beacons are sufficient
2.  connect the modem to a PC and run the Dashboard Software to wake up all the Beacons (stationary and Mobile)
3. Check that the radio settings on the modem and the radio settings on the beacon are the same
4. enter the hight of the Sattionary beacons:

 - Werkstatt (157) z: 4.87m, x:3.55m, y:7.83m
 - Hiwi_Raum (115) z: 4m
 - Matchtower (159) z: 4,24m
 - Drucker (81) z: 3,45m 

 5. The map will form and zoom in automatically  
 6. add a map of the room and adjust the position of the beacons accoding to their current position in the room: 
  - right click on floor-> Add floormap
  - upload map.png
  -right click on the floor map and scale settig  

 More detailed description of the system is to find on the manual privided by [Marvelmind] (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).


### Marvelmind using ROS
* Hedgehog Setting: In Interfaces -> Steaming Output must be Set to USB+Uart. Protocol on UART/USB output must be set to Marvelmind
**Get Location data from Hedgehog:**
* connect hedgehog via USB and check for the port (usually /dev/ttyACM0)
* start roscore with `$roscore`
* start hedgehog data receiving script `$rosrun marvelmind_nav hedge_rcv_bin /dev/ttyACM0`
* show location data `$rostopic echo /hedge_pos_a`
* show IMU data `$rostopic echo /hedge_imu_fusion` ; `$rostopic echo /hedge_imu_raw`

### Useful functions with ros 
**Visulisation of topics**
- use plotjuggler on host pc to visualize topic data
**Recording of topics**
- rosbag record --duration=30 /hedge1/hedge_pos_ang
- rosbag record --duration=1m /amcl_pose /position_marvelmind_with_covariance /odom /cmd_vel /hedge1/hedge_imu_raw /hedge2/hedge_imu_raw /hedge1/hedge_pos_ang /hedge2/hedge_pos_ang



**FDisplay frequency of Publishing**
- rostopic hz /topicname

### setup git hub, kommit, push and pull
* git config --local user.email
* git config --local user.name
* git commit -a
* git push
* git pull

### steps to run Agilex and run rviz

* Change to sgilx `$ ssh agilx`
* Change user on .bashrc:
  - ` sudo nano .bashrc`
  - `source .bashrc`
* Connect to the robot `$ sudo chmod 666 /dev/ttyUSB0`
* Connect to Hedge 1 `$ sudo chmod 666 /dev/ttyACM0`
* Connect to Hedge 2 `$ sudo chmod 666 /dev/ttyACM1`
* Run Robot and Hedges and map `$ roslaunch my_scripts start_omni_agilex.launch` Agliex
* Run rviz im terminal 
* add Topics to rviz:
  - add /initialpose PoseWithCovariance 
  - add /cliked_point PoseWithCovariance
  - run `$ rosrun my_scripts remap_pose_mean_covariance.py `
  - change the Initial Position by running `$ rosrun my_scripts setup_initial_pose.py `

### can connection failed 
-candump can0
- `$ rosrun scout_bringup bringup_can2usb.bash `

### start the sensor fusion with kalman extended filter
* start Rviz
* start kalman filter
* start agilex