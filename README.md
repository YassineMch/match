## Marvelmind Hardware Setup 
### Beacons Height 
* Werkstatt (157) 4,87m 
* Hiwi_Raum (115) 4m
* Matchtowe (159) 4,24m
* Drucker (81) 3,45m

### change user git and commit
* git config --global user.email
* git config --global user.name
* git commit -a

### Serial USB on Linux 
 * show all ACM USB ports '$sudo chmod 666 /dev/ttyACM0'
 * allow access to USB port ACM0 '$sudo chmod 666 /dev/ttyACM0'
 * Hedgehog Setting: In Interfaces -> Steaming Output must be Set to USB+Uart. Protocol on UART/USB output must be set to Marvelmind
 
### Add floor to Dashboard 
* right click on floor-> Add floormap
* upload map.png
* right click on the floor map and scale settig  

### Display frequency 
* rostopic hz /topicname

### TOCKEN and Username
* YassineMch
* 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 