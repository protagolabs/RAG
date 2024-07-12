Available online at www.sciencedirect.com

![0_image_2.png](0_image_2.png)

![0_image_3.png](0_image_3.png)

Procedia Computer Science 198 (2022) 736–741

![0_image_1.png](0_image_1.png)

International Workshop on Smart Communication and Autonomous Driving 

![0_image_0.png](0_image_0.png)

(SCAD 2021)
November 1-4, 2021, Leuven, Belgium An overview of sensors in Autonomous Vehicles International Workshop on Smart Communication and Autonomous Driving 
(SCAD 2021)
November 1-4, 2021, Leuven, Belgium An overview of sensors in Autonomous Vehicles Henry Alexander Ignatious*, Hesham-El-Sayed, Manzoor Khan Henry Alexander Ignatious*, Hesham-El-Sayed, Manzoor Khan College of Information Technology, United Arab Emirates University, Al Ain, UAE College of Information Technology, United Arab Emirates University, Al Ain, UAE

## Abstract

Autonomous driving is a rapidly developing technology that is also a source of debate. People believe that autonomous vehicles will provide a better future by increasing road safety, lowering infrastructure expenses, and improving mobility for children, the old, and the disabled. On the other hand, many individuals are concerned about incidences of automotive hacking, the likelihood of fatal crashes, and the loss of driving-related professions. Autonomous driving is, without a question, a complex and problematic technology for many people. To better comprehend how safe self-driving cars are, it's necessary to first understand how they function, as well as what kind of sensors autonomous vehicles use to determine where they should travel and recognize things on the road in order to avoid automobile accidents. Data collected by the sensors exhibit heterogeneous and multimodal characteristics, which are further fused to frame effective decision rules. Thus sensors play a major role in decision making activity of Autonomous Vehicles (AVs). In order to acquire more information related to the sensors, this paper analyses and summarizes different types of AV sensors based on their mandatory attributes. This analysis helps the readers to understand the contribution of the sensors towards decision-making in AVs and also summarizes the data types collected by different sensors. The summarized inferences will be an eye-opener to most of the budding researchers and students in the field of AVs to select the appropriate sensor based on their needs for their research. The study also gives brief information regarding the specifications of different categories of sensors manufactured by leading vendors in the market. Autonomous driving is a rapidly developing technology that is also a source of debate. People believe that autonomous vehicles will provide a better future by increasing road safety, lowering infrastructure expenses, and improving mobility for children, the old, and the disabled. On the other hand, many individuals are concerned about incidences of automotive hacking, the likelihood of fatal crashes, and the loss of driving-related professions. Autonomous driving is, without a question, a complex and problematic technology for many people. To better comprehend how safe self-driving cars are, it's necessary to first understand how they function, as well as what kind of sensors autonomous vehicles use to determine where they should travel and recognize things on the road in order to avoid automobile accidents. Data collected by the sensors exhibit heterogeneous and multimodal characteristics, which are further fused to frame effective decision rules. Thus sensors play a major role in decision making activity of Autonomous Vehicles (AVs). In order to acquire more information related to the sensors, this paper analyses and summarizes different types of AV sensors based on their mandatory attributes. This analysis helps the readers to understand the contribution of the sensors towards decision-making in AVs and also summarizes the data types collected by different sensors. The summarized inferences will be an eye-opener to most of the budding researchers and students in the field of AVs to select the appropriate sensor based on their needs for their research. The study also gives brief information regarding the specifications of different categories of sensors manufactured by leading vendors in the market. © 2021 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/) Peer-review under responsibility of the Conference Program Chairs.

© 2021 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) Peer-review under responsibility of the Conference Program Chairs
© 2021 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/) Peer-review under responsibility of the Conference Program Chairs.

Keywords: *Autonomous Vehicles (AVs), Autonomous Driving (AD), sensors, LiDAR, RADAR, Intelligent Transportation System (ITS*
* Corresponding author. Tel.: +971543781405; fax:+0-000-000-0000 .

E-mail address: 201990006@uaeu.ac.ae

## 1. **Introduction**

A self-driving vehicle is one that can sense its surroundings and operate without the need for human intervention. 

At no point is a human passenger required to assume control of the car, nor is a human passenger required to be present in the car at all. Self-driving cars are progressively gaining market penetration. While there were about 31 million machines with some level of automation in operation around the world in 2019, that number is predicted to rise to 54 million by 2024 [1]. As a result, the worldwide autonomous vehicle market is expected to expand. Although the market dropped by roughly 3% in 2020 because to the economic slowdown induced by the Covid-19 epidemic, the market is expected to rise by about 60% between 2020 and 2023 [2]. Rapid advancements in electronics, information, and communications technology (leading to downsizing and improved computer, sensor, and networking performance) have spawned various autonomous vehicle (AV) technologies. In real-world scenarios, most autonomous driving (AD) systems face similar obstacles and limits, such as safe driving and navigating in inclement weather, and safe interactions with pedestrians and other vehicles. Harsh weather conditions, such as glare, snow, mist, rain, haze, and fog, can have a substantial impact on the perception and navigation performance of perception-based sensors. In addition, AD issues in inclement weather are encountered in other limited AD contexts like agriculture and logistics. 

Because of the unpredictable situations and behaviors of other cars, these difficulties become more complex for onroad AVs. Placing a yield sign in an intersection, for example, can alter the behavior of approaching vehicles. As a result, in order to limit collision hazards, AVs must have a thorough prediction module that can identify all position future motions. Despite the fact that AD systems face many of the same issues in real-world circumstances, they differ dramatically in a number of ways. As a result, in AVs, a complete prediction module is essential for identifying all future position motions and reducing collision hazard. While AV systems differ differently from one another, they are always sophisticated systems with several subcomponents. The architecture of an Autonomous Driving (AD) system is described from two perspectives: technical, which includes the hardware and software components of the AD system, and functional, which explains the processing blocks necessary within the AV, from data gathering through vehicle control. From a technological standpoint, the two fundamental layers are hardware and software, with each layer containing multiple subcomponents that represent distinct parts of the entire system [3]. The paper is organized in the following hierarchy. Section two, discusses the background information related to multimodal fusion and decision making in AVs. Section three, briefs the overview of different sensors based on their characteristics. Section four, concludes the survey.

## 2. **Background And Related Work**

Sensors are devices that convert sensed events or changes in the environment into a numerical measurement that may then be processed. Sensors are divided into two categories based on their operational principle. Internal state sensors, also known as proprioceptive sensors, record the dynamical state of a dynamic system and detect internal data such as force, angular rate, wheel load, battery voltage, and so on. Inertial measurement units (IMU), encoders, inertial sensors (gyroscopes and magnetometers), and location sensors (Global Navigation Satellite System (GNSS) 
receivers) are examples of proprioceptive sensors. Exteroceptive sensors, or external state sensors, on the other hand, perceive and gather information from the system's environment, such as distance measurements or light intensity. Exteroceptive sensors include cameras, radio detection and range (Radar), light detection and range (LiDAR), and ultrasonic sensors. Additionally, sensors might be either passive or dynamic in nature. Autonomous sensors are crucial in automated driving because they allow automobiles to monitor their surroundings, recognize approaching impediments, and plan their routes securely [4]. They will eventually allow the automation system to take full control of the car when combined with automotive software and computers, saving drivers a substantial amount of time by performing chores in a much more efficient and safe manner. [5] [6]. Passive sensors, such as vision cameras, receive energy from their environment and provide outputs. Active sensors, such as LiDAR and radar sensors, emit energy into the environment and detect the environmental "response" to that energy to provide outputs. Sensors are vital in AVs for perception of the environment and vehicle localization for path planning and decision making, which are necessary before managing the vehicle's movements. To sense its surroundings, AV relies on numerous vision cameras, radar sensors, LiDAR sensors, and ultrasonic sensors. Other sensors, such as the Global Navigation Satellite System (GNSS), the Inertial Measurement Unit (IMU), and vehicle odometry sensors, are also utilized to determine the vehicle's relative and absolute positions. 

![2_image_0.png](2_image_0.png)

The sensors are split into three categories based on the wireless technology's transmission range: short-range, mediumrange, and long-range. The architecture design and execution of an AV is covered in [7], and several multi-sensor fusion solutions are discussed in [8]. [9], discusses recent breakthroughs and advancements in the perception and sensor technology for AVs. Multiple-target and multiple-source are coupled in [10] to construct an on-board sensor framework. [11]. [12], discusses resource allocation techniques for DSRC and C-V2X. Both of these technologies, however, are only appropriate for medium- and long-range communication and do not support low-latency applications. Figure 1, depicts the positioning of sensors for environment perception in common AV systems, as well as their coverage and uses and Figure 2, explains the processing of vehicular data collected from the sensors by the four main functional modules of the AV system.

## 3. **Overview About The Sensors**

This section summarizes the overall overview about different types of AV sensors based on their different properties. This section examines the benefits and drawbacks of the three basic sensors for environment perception in AV applications: cameras, LiDARs, and radars. 3.1 *Cameras* Cameras are one of the most widely used technologies for observing the environment. A camera produces crisp images of the surrounding by detecting lights emitted from the surroundings on a photosensitive surface (image plane) using a camera lens (placed in front of the sensor) [13-18]. Cameras are generally affordable, and when used in conjunction with appropriate software, they can identify both moving and stationary impediments within their field of vision, as well as produce high-resolution photographs of the surroundings. Table 1, illustrates the specifications of various stereo cameras.

3.2 *LiDAR*
LiDAR, or light detection and ranging, was first developed in the 1960s and has since been widely employed in the mapping of aeronautical and aerospace terrain. The first commercial LiDAR's with 2000 to 25,000 pulses per second (PPS) for topographic mapping applications were manufactured and deployed in the mid-1990s by laser scanner manufacturers [19]. LiDAR is a distant sensing technique that works on the principle of producing infrared or laser light pulses that reflect off of target objects. The equipment detects these reflections, and the time between emission and reception of the light pulse allows for distance estimate. LiDAR sensors produce data in the form of a series of points, also known as point cloud data (PCD), in 1D, 2D, and 3D areas, as well as object intensity information. The PCD comprises the x, y, and z coordinates as well as the intensity information of the obstacles inside the scene or surrounds for 3D LiDAR sensors. Table 2, depicts specifications of various LiDAR sensors.

3. *Radars* Before World War II, Radio Detection and Ranging, or Radar, was developed. It worked on the idea of emitting electromagnetic (EM) waves within the region of interest and receiving dispersed waves (or reflections) from targets for signal processing and determining range information. It determines the relative speed and position of identified obstacles using the Doppler property of EM waves [20]. The Doppler effect, also known as Doppler shift, describes how relative motion between a wave source and its targets causes variations or shifts in wave frequency. When the target travels towards the radar system's direction, the frequency of the detected signal rises (shorter waves) [21]. The general mathematical equation for a radar's Doppler frequency shift can be written as .

$f_D\;=\;\frac{2\times V_r\times f}{2}$ $=\frac{2\times V_r}{\Delta}$ . 
 = 2 ×  ×
 = 2 × 
 (1)
Where  is the Doppler frequency in Hertz (Hz),  is the relative speed of the target, () is the frequency of the transmitted signal, is the speed of the light (3 × 108 m/s) and ( is the wavelength of the emitted energy. Table 3, highlights the specifications of different Radar type sensors.

| Deep Information   |                           |                |          |          |          |                     |            |         |          |        |
|--------------------|---------------------------|----------------|----------|----------|----------|---------------------|------------|---------|----------|--------|
| Model              | Baseline                  | HFOV(o )       | VFOV(o ) | FPS(Hz)  | Range    | Img                 | Range      | Res     | FPS      |        |
| (mm)               | Res                       |                |          |          |          |                     |            |         |          |        |
| Roboception        | RC Viscard                | 160            | 61       | 48       | 25       | 0.5-3               | 1.2        | 0.5-3   | 0.03-1.2 | 0.8-25 |
| 160                |                           |                |          |          |          |                     |            |         |          |        |
| Carnegie           | MultiSense                |                |          |          |          |                     |            |         |          |        |
| Robotics           | S7 MultiSense S21B        | 70             | 80       | 49/80    | 30 max   | -                   | 2/4        | 0.4min  | 0.5-2    | 7.5-30 |
| 210                | 68-115                    | 40-68          | 30 max   | -        | 2/4      | 0.4min              | 0.5-2      | 7.5-30  |          |        |
| Ensenso            | N35-606-16                | 100            | 58       | 52       | 10       | 4max                | 1.3        |         |          |        |
| Framos             | D435e                     | 55             | 86       | 57       | 30       | 0.2-10              | 2          | 0.2 max | 0.9      | 30     |
| Nerian             | Karmin3                   | 50/100/250     | 82       | 67       | 7        | 3                   | 0.23/0.45/ | 2.7     | -        |        |
| 1.14min            |                           |                |          |          |          |                     |            |         |          |        |
| Intel              | D455 D$35 D415            | ≤ 90 ≤ 90 ≤ 90 |          |          |          |                     |            |         |          |        |
| Flir               | Bumblebee2 Bumblebee  XB3 | 95 50 55       | 86 86 85 | 57 57 40 | 30 30 30 | 20 max 10max 10 max | 3 3 3      | 0.4 min | ≤1       |        |
| 0.105min           | ≤1                        |                |          |          |          |                     |            |         |          |        |
| 0.16mm             | ≤1                        |                |          |          |          |                     |            |         |          |        |
| 120                | 66                        | 48/20          | 0.3/0.8  | 1.2      | −        |                     |            |         |          |        |
| 240                | 6                         | 16             |          |          |          |                     |            |         |          |        |

| FoV (HFOV)Horizontal resolution (HR0, Vertical Resolution (VR), Wavelength(λ) Category Company Model Channels/ FPS(Hz) Acc(m) RNG(m)   | VF                                                    | HFO             | HR                       | VR                            | 𝜆𝜆                               | Ref                  |                     |                                       |                       |                     |      |      |
|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------|--------------------------|-------------------------------|------------------------------------|----------------------|---------------------|---------------------------------------|-----------------------|---------------------|------|------|
| Layers                                                                                                                                 | OV                                                    | V(o )           |                          |                               |                                    |                      |                     |                                       |                       |                     |      |      |
| ( o )                                                                                                                                  |                                                       |                 |                          |                               |                                    |                      |                     |                                       |                       |                     |      |      |
| Velodyne                                                                                                                               | VLP-16 VLP– 32C HDL-32E HDL-64E VLS 128 (Alpha Prime) | 16 32 32 64 128 | 5-20 5-20 5-20 5-20 5-20 | ±0.03 ±0.03 ±0.02 ±0.02 ±0.03 | 1..100 1..200 2-100 3..120 Max 245 | 30 40 41.3 3 26.8 40 | 360 360 360 360 360 | 0.1-04 0.1-04 0.08- 0.33 0.09 0.1-0.4 | 2 0.33 1.33 0.33 0.11 | 903 903 903 903 903 | [15] |      |
| Mechanical / Spinning LiDARS                                                                                                           | Hesai                                                 | Pandar64        | 64                       | 10,20 10,20                   | ±0.02                              | 0.3..20              | 40                  | 360                                   | 0.2,0.4               | 0.167               | 905  | [16] |
| Pandar40P                                                                                                                              | 40                                                    | ±0.02           | 0.3..200                 | 40                            | 360                                | 0.2,0.4              | 0.167               | 05                                    |                       |                     |      |      |
| Ouster                                                                                                                                 | OSI-64 Gen1 OSI-16 Gen 1                              | 64              | 10,20                    | ±0.03                         | 0.8—120                            | 33.2                 | 360                 | 0.7.0.35                              | 0.53                  | 850                 | [17] |      |
| 16                                                                                                                                     | 10.20                                                 | ±0.03           | 0.8120                   | 33.2                          | 360                                | 0.53                 | 850                 |                                       |                       |                     |      |      |
| RoboSense                                                                                                                              | RS-LiDAR 32                                           | 32              | 5.10,20                  | ±0.03                         | 0.4-200                            | 40                   | 360                 | 0.18,10.3                             | 2                     | 905                 | [18] |      |
| 6                                                                                                                                      |                                                       |                 |                          |                               |                                    |                      |                     |                                       |                       |                     |      |      |
| LeiShen                                                                                                                                | C32-151A                                              | 32              | 5,10,20 5,10,20          | ±0.03                         | 0.5-..70                           | 32                   | 360                 | 0.09                                  | 1                     | 905                 | [19] |      |
| C16-700B                                                                                                                               | 16                                                    | 0.5..150        | 30                       | 360                           | 0.18,0.36                          | 2                    | 905                 |                                       |                       |                     |      |      |
| ±0.02                                                                                                                                  |                                                       |                 |                          |                               |                                    |                      |                     |                                       |                       |                     |      |      |
| Hokuyo                                                                                                                                 | YVT-35LXF0                                                       | -               | 20                       | ±0.05                         | 0.3..35                            | 40                   | 210                 | -                                     | -                     | 905                 | [20] |      |
| IBEO                                                                                                                                   | LUX 4L Standard LUX HD LUX SL                         | 4               | 25                       | 0.1                           | 50                                 | 3.2                  | 110                 | 0.25                                  | 0.8                   | 905                 | [21] |      |
| Solid State  LiDARS                                                                                                                    | 4 8                                                   | 25 25           | 0.1 0.1                  | 50 30                         | 3.2 6.4                            | 110 110              | 0.25 0.25           | 0.8 0.8                               | 905 905               |                     |      |      |
| SICK                                                                                                                                   | LDMRS400102S 01 HD LDMRS8001S01 HD                                                       | 4               | 50                       | -                             | 30                                 | 3.2                  | 110                 | 0.125- 0.5                            | -                     | -                   | [19] |      |
| 8                                                                                                                                      | 50                                                    | 50              | 6.4                      | 110                           | 0.125- 0.5                         | -                    | -                   |                                       |                       |                     |      |      |

![4_image_2.png](4_image_2.png)

![4_image_1.png](4_image_1.png)

![4_image_0.png](4_image_0.png)

Table 3: General specification of RADAR sensors. Acronyms first from first column top to bottom , Frequency(Freq), horizontal FoV(HFOV), 
Vertical FoV(VFOV), Range Accuracy (Range Acc), Velocity Range(Vel Range), ROS (Robotic Operating System)

| Aptiv Delpi                                                                                                                                 | Continental                                                                                  | SmartMicro           |              |                           |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------|--------------|---------------------------|
| Category                                                                                                                                    | ESR2.5                                                                                       | SRR@                 | ARS 408-21   | UMMR-96-T-153             |
| Freq(GHz)                                                                                                                                   | 76.5                                                                                         | 76.5                 | 76…77        | 79(77..81)                |
| HFOV(o )  Short-Range Mid-Range Long-Range                                                                                                  | ±45 ±10                                                                                      | ≥ 130 ≥ 130          |              |                           |
| ≥ 100 (squint beam)                                                                                                                         |                                                                                              |                      |              |                           |
| VFOV(o )                                                                                                                                    | 20                                                                                           |                      |              |                           |
| Short-Range                                                                                                                                 | 4.4                                                                                          | 10                   | 14           | 15                        |
| Long-Range                                                                                                                                  | ±75                                                                                          | ±9 ±60               |              |                           |
| Range(m) Short-Range Mid-Range Long-Range                                                                                                   | -                                                                                            | ±0.5 noise and ±0.5% | -            | <0.15 (or) 1% (bigger of) |
| bias                                                                                                                                        | <0.30 (or) 1% (bigger of) <0.50 (or) 1% (bigger of)                                          |                      |              |                           |
| Vel Range (km/h) Short-Range Mid-Range Long-Range                                                                                           | -                                                                                            | -                    | −400 … + 100 |                           |
| −400… + 200                                                                                                                                 | −340 … + 140 −340 … + 140                                                                    |                      |              |                           |
| IO Interfaces                                                                                                                               | CAN/Ethernet                                                                                 | PCAN                 | CAN          | CAN/Automotive Ethernet   |
| Table 4: Common comparison among sensor. "                                                                                                  | " sensors operate completely under specific conditions,"--" sensors performs reasonably well |                      |              |                           |
| under specific conditions,"×" sensors does not operate well under the specific factor relative to other sensors. Factors Camera LiDAR RADAR | Fusion                                                                                       |                      |              |                           |
| Range                                                                                                                                       | --                                                                                           | --                   |              |                           |
| Resolution                                                                                                                                  | --                                                                                           | ×                    |              |                           |
| Distance Accuracy                                                                                                                           | --                                                                                           |                      |              |                           |
| Velocity                                                                                                                                    | --                                                                                           | ×                    |              |                           |
| Color Perception, e.g Traffic lights                                                                                                        | ×                                                                                            | ×                    |              |                           |
| Object Detection                                                                                                                            | ×                                                                                            |                      |              |                           |
| Object Classification                                                                                                                       | ×                                                                                            | ×                    |              |                           |
| Lane Detection                                                                                                                              | ×                                                                                            | ×                    |              |                           |
| Obstacle Edge Detection                                                                                                                     | ×                                                                                            |                      |              |                           |
| Illuminations Conditions                                                                                                                    | ×                                                                                            |                      |              |                           |
| Weather Conditions                                                                                                                          | ×                                                                                            | --                   |              |                           |
| 3.4. Challenges associated with sensors                                                                                                     |                                                                                              |                      |              |                           |

Table 4: Common comparison among sensor. " " sensors operate completely under specific conditions,"--" sensors performs reasonably well under specific conditions,"×" sensors does not operate well under the specific factor relative to other sensors.

Factors Camera LiDAR RADAR Fusion

Range -- --

Resolution -- ×

Distance Accuracy --

Velocity -- ×

Color Perception, e.g Traffic lights × ×

Object Detection ×

Object Classification × ×

Lane Detection × ×

Obstacle Edge Detection × Illuminations Conditions ×

Weather Conditions × --

3.4. Challenges *associated with sensors*

Manufacturing reliable and robust designs of smart sensors for accurate and precise measurements is a 

challenging task for most of the sensor manufacturers. In wireless sensors handling faulty and unreliable communication error is another major challenging issue. The key issues with a wireless sensor networks are (i) selection of appropriate hardware and operating infrastructure, (ii) sensing network calibration, deployment, and programming model, and (iii) synchronization. Calibrating sensors before using them is a difficult task. LIDAR sensors do not provide color information of the perceived data, hence Point Cloud Data is often fused with different data collected from several sensors using eminent fusion algorithms. Due of their coarse resolutions compared to cameras, radar sensors are not often suited for object recognition applications. Bad climatic conditions also have an 

impact towards the functioning of the sensors. Researches are still in progress to reduce the existing challenges and improve the efficiency of the sensors.

## 4. **Conclusion**

This study has analysed several sensor types based on their key characteristics such as mode of operation, data type collected, general specifications and also discusses the strengths and weakness associated with every category of the sensors. The study summarizes the general specifications of different sensors manufactured by leading vendors in the market. In addition to points discussed above, the study also briefs the mechanism involved in the sensors to collect the vehicular data and also investigates and exhibits a sample sensor data format released by leading automobile manufacturer Ford. This analyses guides and motivates the potential AV researchers to acquire a depth knowledge regarding the operation and the data format collected by different AV sensors. Using this prior knowledge the budding researchers can select appropriate sensor type suitable for their research and will also acquire knowledge to organize and process the sensor data efficiently.

## References

[1] https://www.statista.com/topics/3573/autonomous-vehicletechnology/\#:~:text=While%20in%202019%2C%20there%20were,projected%20to%20grow%20as%20well.

[2] https://www.globenewswire.com/news-release/2020/05/20/2036203/0/en/Global-Autonomous-Cars-Market-2020-to-2030-COVID-19-
Growth-and-Change.html
[3] Yeong, D.J.; Barry, J.; Walsh, J. A Review of Multi-Sensor Fusion System for Large Heavy Vehicles Off Road in Industrial Environments. 

In Proceedings of the 2020 31st Irish Signals and Systems Conference (ISSC), Letterkenny, Ireland, 11–12 June 2020.

[4] Kuutti, S.; Bowden, R.; Jin, Y.; Barber, P.; Fallah, S. A Survey of Deep Learning Applications to Autonomous Vehicle Control. IEEE Trans. 

Intell. Transp. Syst. 2021, 22, 712–733
[5] Hu, J.-W.; Zheng, B.-Y.; Wang, C.; Zhao, C.-H.; Hou, X.-L.; Pan, Q.; Xu, Z. A Survey on multi-sensor fusion based obstacle detection for intelligent ground vehicles in off-road environments. Front. Inform. Technol. Electron. Eng. 2020, 21, 675–692. [CrossRef] 
[6] Mobile Robot Sensors. Available online: http://www.robotiksistem.com/robot_sensors.html (accessed on 24 November 2020) [7] Gonzalez-de-Santos, P.; Fernández, R.; Sepúlveda, D.; Navas, E.; Emmi, L.; Armada, M. Field Robots for Intelligent Farms— Inhering Features from Industry. Agronomy 2020, 10, 1638. [CrossRef] 
[8] Velasco-Hernandez, G.; Yeong, D.J.; Barry, J.; Walsh, J. Autonomous Driving Architectures, Perception and Data Fusion: A Review. In Proceedings of the 2020 IEEE 16th International Conference on Intelligent Computer Communication and Processing (ICCP 2020), ClujNapoca, Romania, 3–5 September 2020. 

[9] Giacalone, J.; Bourgeois, L.; Ancora, A. Challenges in aggregation of heterogeneous sensors of Autonomous Driving Systems. In Proceedings of the 2019 IEEE Sensors Applications Symposium (SAS), Sophia Antipolis, France, 11–13 March 2019. 

[10] Liu, X.; Baiocchi, O. A comparison of the definitions for smart sensors, smart objects and Things in IoT. In Proceedings of the 2016 IEEE 
7th Annual Information
[11] World Health Organization. Global Status Report on Road Safety; WHO: Geneva, Switzerland, 2018; ISBN 978-9241565684. [12] Wojciechowicz, T. Smart Sensor vs Base Sensor—what's the Difference? | Symmetry Blog. Available online: https: 
//www.semiconductorstore.com/blog/2018/Smart-Sensor-vs-Base-Sensor-Whats-the-Difference-Symmetry-Blog/3538/\#: ~{}:text=By%20using%20a%20smart%20sensor,achieve%20on%20a%20base%20sensor (accessed on 26 November 2020).

[13] Campbell, S.; O'Mahony, N.; Krpalcova, L.; Riordan, D.; Walsh, J.; Murphy, A.; Conor, R. Sensor Technology in Autonomous Vehicles: 
A review. In Proceedings of the 2018 29th Irish Signals and Systems Conference (ISSC), Belfast, UK, 21–22 June 2018.

[14] Shahian Jahromi, B.; Tulabandhula, T.; Cetin, S. Real-Time Hybrid Multi-Sensor Fusion Framework for Perception in Autonomous Vehicles. Sensors 2019
[15] Joglekar, A.; Joshi, D.; Khemani, R.; Nair, S.; Sahare, S. Depth Estimation Using Monocular Camera. IJCSIT 2011, 2, 1758–1763. [16] Garg, R.; Wadhwa, N.; Ansari, S.; Barron, J.T. Learning Single Camera Depth Estimation using Dual-Pixels. arXiv 2019, arXiv:1904.05822v3.

[17] Orbbec—Intelligent computing for everyone everywhere. Available online: https://orbbec3d.com/ (accessed on 4 December 2020) [18] Cronin, C.; Conway, A.; Walsh, J. State-of-the-Art Review of Autonomous Intelligent Vehicles (AIV) Technologies for the Automotive and Manufacturing Industry. In Proceedings of the 2019 30th Irish Signals and System Conference (ISSC), Maynooth, Ireland, 17–18 June 2019.

[19] Petit, F. The Beginnings of LiDAR—A Time Travel Back in History. Available online: https://www.blickfeld.com/blog/thebeginnings-oflidar/\#:~{}:text=Lidar%20technology%20emerged%20already%20in,such%20as%20autonomous%20driving%20today (December 2020).

[20] Shahian Jahromi, B.; Tulabandhula, T.; Cetin, S. Real-Time Hybrid Multi-Sensor Fusion Framework for Perception in Autonomous Vehicles. Sensors 2019, 19, 4357
[21] Jia, Y.; Guo, L.; Xin, W. Real-time control systems. In Transportation Cyber-Physical Systems, 1st ed.; Deka, L., Chowdhury, M., Eds.; 
Elsevier: Amsterdam, The Netherlands, 2018; pp. 81–113.