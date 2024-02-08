# MAVLink-Data-Loader
MAVLink is a serial protocol most commonly used to send data and commands between vehicles and ground stations.

This repository will be helpful to look at the data collected for flight missiions

Certain types of files are available at the end of the mission. One of them is '.bin' file, this '.bin' file consists of various struct data and it is difficult to load and look at the data.

In order to convert this data one can use 'Mission Planner' application which has an option to convert '.bin' file to '.mat' file. This '.mat' file can be easily loaded to MATLAB and look into data.

This repository is to load this MAVLink data into Python

