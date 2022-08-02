## Marvelmind Hardware Setup 
### Beacons Height 
* Werkstatt (157) 4,87m x:3.55m y:7.83
* Hiwi_Raum (115) 4m
* Matchtower (159) 4,24m
* Drucker (81) 3,45m

### change user git and commit
* git config --local user.email
* git config --local user.name
* git commit -a

### Serial USB on Linux 
 * show all ACM USB ports '$sudo chmod 666 /dev/ttyACM0'
 * allow access to USB port ACM0 '$sudo chmod 666 /dev/ttyACM0'
 * Hedgehog Setting: In Interfaces -> Steaming Output must be Set to USB+Uart. Protocol on UART/USB output must 
 be set to Marvelmind

### ROS and Marvelmind
Get Location data from Hedgehog:
* connect hedgehog via USB and check for the port (usually /dev/ttyACM0)
* start roscore with `$roscore`
* start hedgehog data receiving script `$rosrun marvelmind_nav hedge_rcv_bin /dev/ttyACM0`
* show location data `$rostopic echo /hedge_pos_a`
* show IMU data `$rostopic echo /hedge_imu_fusion`
* set location where rosmaster is running in bashrc, needs to be set in hosts file too
* setup plotjuggler on host pc `$sudo apt-get install ros-noetic-plotjuggler-ros`
* use plotjuggler on host pc to visualize topic data `$rosrun 

### record a topic 

* rosbag record --duration=30 /hedge1/hedge_pos_ang

 
### Add floor to Dashboard 
* right click on floor-> Add floormap
* upload map.png
* right click on the floor map and scale settig  

### Display frequency 
* rostopic hz /topicname

### TOCKEN and Username
* YassineMch
* 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 
* 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:HiwiRaum

### transformation between map and odom
* AMCL

### run rviz and run the robot 
* 
* change to sgilx `$ ssh agilx`
* connect to the robot `$ sudo chmod 666 /dev/ttyUSB0`
* connect to Hedge 1 `$ sudo chmod 666 /dev/ttyACM0`
* connect to Hedge 2 `$ sudo chmod 666 /dev/ttyACM1`
* run Robot and Hedges and map `$ roslaunch my_scripts start_omni_agilex.launch` Agliex
* run rviz im terminal 
* add the map at rviz 
* add /initialpose PoseWithCovariance 
* add /cliked_point PoseWithCovariance
* change the Initial Position by running `$ rosrun my_scripts setup_initial_pose.py `
