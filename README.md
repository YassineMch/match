# Master Arbeit Yassine Mechri

## Marvelmind Hardware 
* Marvelmind Indoor Navigation System is an off-the-shelf indoor navigation system, designed to provide precise (±2cm) location data to autonomous robots
* Mobile beacon’s location is calculated based on a propagation delay of an ultrasonic pulses (Time-Of-Flight or TOF) between stationary and mobile beacons using trilateration algorithm. 

## Steps to set up the System

1. Place the Stationary Beacons on the wall in a way that will provide an optimal ultrasonic coverage. 
2. Connect the modem to a PC and run the Dashboard Software to wake up all the Beacons (stationary and Mobile)
3. The map will form and zoom in automatically  
4. Check that the radio settings on the modem and the radio settings on the beacon are the same
5. The distaces between the stationary beacons (x, y) will be measured systematically and displayed in a table .
6. The hight of the Sattionary beacons should be set manually:

 - Werkstatt (157) z: 4.87m, x:3.55m, y:7.83m
 - Hiwi_Raum (115) z: 4m
 - Matchtower (159) z: 4,24m
 - Drucker (81) z: 3,45m 


 7. add a map of the room and adjust its position according to known beacon position in the room: 

  - right click on floor-> Add floormap
  - upload map.png
  - right click on the floor map and scale settig  

* More detailed description of the system is to find on the manual privided by [Marvelmind] (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).


### Marvelmind using ROS

* Hedgehog Setting: In Interfaces -> Steaming Output must be Set to USB+Uart. Protocol on UART/USB output must be set to Marvelmind

* Get Location data from Hedgehog:
1. Connect hedgehog via USB and check for the port (usually /dev/ttyACM0 or /dev/ttyACM1 in case to mobile beacons are used)
2. Start roscore with `$roscore`
3. Start hedgehog data receiving script `$rosrun marvelmind_nav hedge_rcv_bin /dev/ttyACM0`
4. Show location data `$rostopic echo /hedge_pos_a`
5. Show IMU data `$rostopic echo /hedge_imu_fusion`

## Useful functions with ros 

* See which topics are published: `$rostopic list`
* display a specific topic: `$rostopic echo /topic_name`
* get info about the topic: `$rostopic info /topic_name`

* live visulisation of topics:
- use plotjuggler on host pc to visualize topic data `$rosrun plotjuggler plotjuggler`

* Recording of topics: `$ rosbag record --duration= /topic_name`

* display frequency of publishing: `$rostopic hz /topicname`

 ## start the Robot and Initialisation 

 * Change to sgilx `$ ssh agilx`
 * Connect to the robot `$ sudo chmod 666 /dev/ttyUSB0`
 * Connect to Hedge 1 `$ sudo chmod 666 /dev/ttyACM0`
 * Connect to Hedge 2 `$ sudo chmod 666 /dev/ttyACM1`
 * launch the robot, the hedges and the map in Agilex `$ roslaunch my_scripts start_omni_agilex.launch`
 * launch rviz and initialisation in rosmaster `$ roslaunch my_scripts initialisation.launch  `

 ### in case CAN connection failed 

 * `$ candump can0` in Agilex to check if CAN connection established
 * `$ rosrun scout_bringup bringup_can2usb.bash ` to connect to CAN in case no connection has been established
  
 ## start the sensor fusion with kalman extended filter