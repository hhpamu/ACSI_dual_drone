# Control Stabilization for Bi-Quadcopter Payload Delivery System

This is the Github Repository for the Fall 2023 <a href="https://www.meche.engineering.cmu.edu/education/courses/24-774.html" target="_blank">24-774 Special Topics: Advanced Control Systems Integration</a> Final Project at <a href="https://www.cmu.edu/" target="_blank">Carnegie Mellon University</a>.

Team: Hima Pamu, Srikumar Brundavanam, Pete Blumenstein, Shang Shi and Ben Spin

## Overview
With the increasing utilization and interest in unmanned aerial vehicles (UAVs) in both the private and commercial sector, steps to increase payload capacity and flight reliability present significant challenges and opportunities. This paper details the design, implementation, and testing of a novel dual drone system, interconnected via a robust truss structure, with a hanging pendulum for a centralized payload. A pendulum-based payload system is central to this design. The focus was on developing and tuning a Cascaded PID controller within Simulink to manage the system's dynamics and ensure stability with variable payloads. The controller was further fine tuned iteratively on the hardware to address the unique dynamics introduced by the flexible truss structure and swinging payload. Field tests were conducted which demonstrated the system's capacity to withstand disturbance, handle variable payload weight, and perform simple turns and maneuvers stably. Our findings indicated that the dual-drone system significantly enhances payload capacity at 43 percent, and improves stability compared to a single drone solution. Therefore, we conclude that this system has potential application in a various fields, including package delivery, remote aid, and search and rescue operations. 

Our final <a href="https://github.com/hhpamu/ACSI_dual_drone/blob/main/Final%20Project%20Presentation.pdf" target="_blank">presentation</a> and <a href="https://github.com/hhpamu/ACSI_dual_drone/blob/main/ACSI_Final_Report_Team3.pdf" target="_blank">report</a> are available for reference. 

## Demonstration Videos
The full playlist of videos of our testing and final demo result can be found on <a href="https://www.youtube.com/playlist?list=PLhjMVMo-iKefzUKCguJFhuCKCUdmlcipk" target="_blank">YouTube</a> 

## Setup
To get started with the Crazyflie, follow this [Get Started Guide](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/). This guide goes through the hardware setup of the drone as well as setting up the Crazyradio and the Bitcraze Virtual Machine.

To flash new firmware on to the drone, follow this [Basic Guide](https://www.bitcraze.io/documentation/tutorials/getting-started-with-development/#new-fw).

Information on the Swarm Interface can be found [here](https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_swarm_interface/).

To control the flight of the drone and send commands, we used the Python Crazyflie API. Instructions and examples can be found [here](https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/python_api/).

All the Python scripts in this repo were written and ran in a **Python 3.9** Anaconda environment.

## Acknowledgements
- <a href="https://www.andrew.cmu.edu/user/capn/" target="_blank">Dr. Mark Bedillion</a>
- <a href="https://www.andrew.cmu.edu/user/amj1/" target="_blank">Dr. Aaron Johnson</a> 
- <a href="mailto:xkhai@cmu.edu">Khai Nguyen</a>

This project would not have been possible without the support of these individuals, and for that, the team is extremely grateful.

## Using This Project in Your Work
<!--
If you wish to use any part of this project's code or resources in your own work, please adhere to the following guidelines:

1. **Proper Attribution**:
   - You must give appropriate credit to this project and its authors.
   - Mention by name all current authors of this project.
   - Provide a link back to the original repository of this project.
   - The attribution should be in a manner consistent with the MIT License under which this project is released.

2. **For Students**:
-->
If you are a student considering using this project's materials, please first refer to your course policy.
Consult with your instructor or professor to ensure that using these materials does not conflict with any academic integrity policies of your educational institution.

### Attribution Format:
This project uses code from Control Stabilization for Bi-Quadcopter Payload Delivery System by Pamu H.H., Brundavanam S., Blumenstein P., Shi S., and Spin B., available at https://github.com/hhpamu/ACSI_dual_drone.


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/hhpamu/ACSI_dual_drone/blob/main/LICENSE) file for details.

