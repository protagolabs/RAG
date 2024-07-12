Contents lists available at ScienceDirect 

![0_image_0.png](0_image_0.png)

![0_image_2.png](0_image_2.png)

![0_image_3.png](0_image_3.png)

![0_image_5.png](0_image_5.png)

![0_image_7.png](0_image_7.png)

Engineering Applications of Artificial Intelligence 

![0_image_1.png](0_image_1.png)

![0_image_4.png](0_image_4.png)

![0_image_6.png](0_image_6.png)

journal homepage: www.elsevier.com/locate/engappai An in-depth evaluation of deep learning-enabled adaptive approaches for detecting obstacles using sensor-fused data in autonomous vehicles Abhishek Thakur *, Sudhansu Kumar Mishra Department of EEE, BIT Mesra, Ranchi, Jharkhand, 835215, India 

| ARTICLE INFO   |
|----------------|

| Keywords:  Autonomous vehicles  Obstacle detection  Sensor fusion  Multi-sensor technologies  Deep learning   |
|---------------------------------------------------------------------------------------------------------------|

This paper delivers an exhaustive analysis of the fusion of multi-sensor technologies, including traditional sensors such as cameras, Light Detection and Ranging(LiDAR), Radio Detection and Ranging(RADAR), and ultrasonic sensors, with Artificial Intelligence(AI) powered methodologies in obstacle detection for Autonomous Vehicles 
(AVs). With the growing momentum in AVs adoption, a heightened need exists for versatile and resilient obstacle detection systems. Our research delves into study of literatures, where proposed approaches assimilate data from this diverse sensor suite, integrated through Deep Learning(DL) techniques, to refine AV performance. Recent advancements and prevailing challenges within the domain are thoroughly examined, with particular focus on the integration of sensor fusion techniques, the facilitation of real-time processing via edge and fog computing, and the implementation of advanced artificial intelligence architectures, including Convolutional Neural Networks(CNNs), Recurrent Neural Networks(RNNs), and Generative Adversarial Networks(GANs), to enhance data interpretation efficacy. In conclusion, the paper underscores the critical contribution of multi-sensor arrays and deep learning in enhancing the safety and reliability of autonomous vehicles, offering significant perspectives for future research and technological progress. 

| ABSTRACT   |
|------------|

## 1. **Introduction**

The advancement of AVs is significantly changing the landscape of transportation, promising improvements in mobility and traffic safety 
(Parekh et al., 2022). A key aspect of this transformation is the ability to detect and avoid obstacles, a task that is central to the safe operation of AVs (Yu and Marinov, 2020). This challenge often requires the integration of various sensor technologies, each contributing unique data. 

Cameras provide visual input, while technologies like Light Detection and Ranging (LiDAR) and Radio Detection and Ranging (RADAR) offer other critical environmental information (Yeong et al., 2021). By combining these diverse data sources, a more accurate and comprehensive view of the vehicle's surroundings can be achieved. Despite the potential of these technologies, there are issues quite challenging to address. Issues like sensor noise, inconsistent data, and redundant information can complicate the process. However, advancements in data processing methods are opening doors to more precise environmental interpretation and decision-making for autonomous navigation. The urgency of improving transportation safety is underscored by a disconcerting statistic from the World Health Organization (WHO), which https://doi.org/10.1016/j.engappai.2024.108550 Received 21 January 2024; Received in revised form 3 April 2024; Accepted 1 May 2024 Available online 9 May 2024 0952-1976/© 2024 Elsevier Ltd. All rights reserved.

reports an average of 2.4 road traffic deaths every minute worldwide (World Health Organization, 2023). This highlights the global need for safer transportation systems. Fig. 1 below offers a comparative view of how different sensor technologies contribute to vehicle perception, setting the stage for our discussion on innovative solutions in AV obstacle detection. 

Deep Learning (DL) has revolutionized obstacle detection in AVs, enabling the processing of complex and extensive data sets for more effective obstacle identification and avoidance (Sanil et al., 2020). This advancement leads to more refined detection and avoidance of obstacles. One of the key elements of this evolution is the use of Convolutional Neural Networks (CNNs), which have become vital for ensuring the safe navigation of AVs (Muhammad et al., 2020). Utilizing CNNs, these frameworks effectively recognize and classify potential hazards, including vehicles and pedestrians, through feature extraction from images (Devi et al., 2022; Liu et al., 2017; Rashid et al., 2019; Lee et al., 
2018). Other DL networks also support advanced object detection frameworks such as You Only Look Once (YOLO), Single Shot MultiBox Detector (SSD), and Faster Region-based Convolutional Neural Network 
(Faster R–CNN), etc. Expanding this capability, DL networks like Fully Convolutional Networks (FCN) and U-shaped Network (U-Net) have been employed for semantic segmentation (Mancini et al., 2016; Tran and Le, 2019). The integration of multi-modal sensor data, gathered from diverse sources like cameras, LiDAR and RADAR, is another area where DL contributes significantly (Koci´c et al., 2018; Fayyad et al., 
2020). Approaches like Multimodal Unsupervised Image-to-Image Translation (MUNIT) and FusionNet play a pivotal role in autonomously filtering and optimally integrating this raw sensor data. This approach amplifies the AV's capabilities in identifying and navigating around obstacles, even in complex environments. Lastly, the application of Recurrent Neural Networks (RNNs) and their variations, Long Short-Term Memory (LSTM) or Gated Recurrent Unit (GRU) networks, plays a crucial role in temporal analysis (Yuan et al., 2019; Jeong, 2022; Qian et al., 2022). This analysis is key to understanding and predicting the dynamics of the environment, like the movement of pedestrians or other vehicles, thereby enhancing the AVs' ability to proactively evade potential obstacles. 

The role of sensor fusion in AV is fundamental. It facilitates the combination of data from various sensors to offer a more reliable, complete, and unambiguous understanding of the environment than could be achieved by any of these sensors working in isolation. Selfdriving vehicles are typically equipped with multiple sensor technologies such as cameras, RADAR, LiDAR, ultrasonic sensors, and Inertial Measurement Units (IMUs), etc (Escamilla-Ambrosio and Lieven, 2005; Kim et al., 2018). Each of these sensors provides different types of data. For instance, cameras provide high-resolution images and are excellent for colour discrimination and texture analysis, but they are heavily affected by lighting conditions and have difficulty estimating distances. LiDAR, on the other hand, offers accurate distance measurements and can function in various lighting conditions, but it lacks the ability to discern colour and texture. RADAR sensors are proficient at detecting the velocity of other objects even in poor visibility conditions, yet they have lower spatial resolution. Ultrasonic sensors are effective for close-range detection but offer limited field of view (Yu and Marinov, 2020; Liu et al., 2020). Lastly, IMUs provide information about the vehicle's velocity, orientation, and gravitational forces, supporting the overall navigation system (Azam et al., 2020). Sensor fusion techniques aim to leverage the strengths of each sensor type to overcome their individual limitations, enhancing the robustness and reliability of the AV 
perception systems. Through data fusion, the vehicle can obtain a detailed, comprehensive, and accurate understanding of the surrounding environment. Sensor fusion in AV can be categorized into low-level 
(raw data) fusion, mid-level (feature) fusion, and high-level (decision) 
fusion. Low-level fusion combines the raw data from various sensors to generate a unified representation of the environment. This fusion method provides a comprehensive view of the surroundings but faces challenges due to the differences in the nature, format, and quality of data from different sensors. Mid-level fusion focuses on the extraction and combination of features from sensor data. Features can be specific patterns, structures, or objects identified within the data. While less comprehensive than low-level fusion, this method is more robust to sensor noise and variability. High-level fusion, on the other hand, focuses on decision making. Here, individual sensors make independent decisions, and these are then fused to provide a final decision. This fusion level is less affected by sensor errors but may lack the detail provided by the other two fusion methods. In the pursuit of achieving this level of sensor fusion, different fusion levels and associated models play a pivotal role. Fig. 2 below offers a glimpse into the data fusion architecture employed in AV. 

Table 1 provides an overview of various fusion levels in obstacle detection research, highlighting the combination of sensors (such as LiDAR, visual, and thermal cameras), the types of objects detected (e.g., 3D cars, 2D pedestrians), and the specific datasets utilized (including KITTI and KAIST Pedestrian Dataset). It encompasses studies from early to late fusion stages, offering a concise summary of contemporary methodologies and applications in this field. 

The compilation of research works in Table 1 is meticulously selected based on a set of defined criteria aimed at presenting a comprehensive overview of sensor fusion strategies within obstacle detection research. This selection is guided by the objective to highlight the innovative and 

![1_image_0.png](1_image_0.png)

![2_image_0.png](2_image_0.png)

| Table 1  Fusion strategies and sensor combinations in obstacle detection research.  Fusion  Reference Sensors Object Type Dataset(s)  Level  used  Early Wu et al. (2023) 3D-LiDAR,  visual  camera  3D Object (Car,  van, truck,  pedestrian,  cyclist)  KITTI  Early Abbasi et al.  LiDAR, HDmap  3D Car KITTI  (2022)  Early Zhang et al.  LiDAR, RGB  3D Object Self-recorded  (2021)  Camera  data  Late Yadav et al.  Visual  (2021)  camera,  thermal  camera  Multiple 2D  Self-recorded  objects  data  Early,  Middle,  Late  Broedermann  LiDAR,  et al. (2023)  visual  camera  Multiple 2D  KITTI  objects  Early,  Middle,  Late  2D Pedestrian KAIST  Pedestrian  Dataset  Early,  Middle,  Late  Dasgupta et al.  Visual  (2022)  camera,  thermal  camera  Cordts et al.  Visual  (2016)  camera,  LiDAR  Multiple 2D  Cityscape  objects  Early,  Middle,  Late  Geng et al.  LiDAR,  (2020)  visual  camera  2D Car KITTI  Early,  Ahmed et al.  Visual  Late  (2019)  camera,  thermal  camera  2D Pedestrian KAIST  Pedestrian  Dataset   |
|---|

diverse approaches that have significantly contributed to the field focusing on papers published from 2019 to 2023 to ensure inclusion of the latest advancements in sensor fusion techniques for obstacle detection. The chosen studies distinctly illustrate the use of various fusion levels, including early, middle, late, and hybrid stages. This choice is fundamental to understanding the full range of data integration techniques and their capacity to enhance obstacle detection. We have sought studies showcasing a variety of sensor combinations (e.g., LiDAR, visual, and thermal cameras) and their application in detecting a wide range of object types (from 3D cars to 2D pedestrians). This diversity underscores the adaptability of fusion techniques to different detection challenges and environmental conditions. Moreover, dataset utilization has been a significant factor in our inclusion criteria, favouring studies that not only utilize recognized datasets like KITTI and the KAIST Pedestrian dataset but also those that draw from proprietary or self-compiled data (Yadav et al., 2021; Broedermann et al., 2023; Dasgupta et al., 2022; Cordts et al., 2016). This approach underscores the efficacy and adaptability of sensor fusion strategies, attesting to their robustness and practical viability across a variety of datasets. Consideration is also given to the research's contribution to the field, with a focus on studies that have introduced innovative methods or have been particularly influential in advancing obstacle detection research. This aspect ensures that the selected works provide insight into the evolution and current state of the art in the field. Fig. 3 provides flowchart for the review strategy. 

Within the dynamic realm of AVs, the integration of deep learning with sensor fusion for obstacle detection emerges as a critical area of exploration. Real-world driving environments, characterized by their complexity and variability, necessitate the development of sophisticated and adaptable methods to ensure the safety and efficiency of navigation. 

This research paper conducts an in-depth examination of deep learning algorithms synergy with multi-modal sensor data to enhance obstacle detection capabilities. It provides a thorough analysis of current approaches and introduces novel experiments, aiming to shed light on advanced strategies that can be adapted to various driving contexts. As autonomous driving technologies are poised to revolutionize the transport sector, this study offers crucial insights paving the way for subsequent research and potentially accelerating advancements in the AV 
sector. 

## 2. **Brief History Of Av**

AV have been a topic of development for many years. Initially envisioned as a futuristic concept, they have gradually become a reality thanks to technological advancements. Over time, these vehicles have evolved from simple automated systems to complex machines capable of navigating without human input. This evolution reflects the progress in areas such as artificial intelligence, sensor technology, and computer programming. The concept of self-driving cars has a history that reaches back nearly 80 years, with its first known introduction at the 1939 World's Fair in New York (Norton, 2021). Various companies have ventured into creating AVs, like Waymo, Tesla and Uber ATG as depicted in Fig. 4. 

The subsequent evolution of sensor technology has been a significant driving force in the progress of AV. AVs depend on an array of sophisticated sensors to sense, comprehend, and engage with the surrounding 

![3_image_0.png](3_image_0.png)

environment (Murali et al., 2022). These sensors persistently scan the environment around the vehicle, allowing a continuous flow of information to the control systems. To understand the intricate mechanisms and varied aspects of these cars, Fig. 5 provides an in-depth look into working of self-driving cars, the levels of automation they possess, as well as their advantages and disadvantages. 

This evolution has been marked by several key milestones. In the early stages, the focus was primarily on developing basic automated functions, like cruise control, which laid the groundwork for more sophisticated systems. As technology advanced, particularly in the realms of computer vision and machine learning, these vehicles began to incorporate more complex features like lane-keeping assistance and collision avoidance. Each step forward in AV technology not only showcased the potential of integrating automation in vehicles but also highlighted the challenges and complexities involved in making fully autonomous driving a practical and safe reality. The AV market is experiencing significant growth, with its volume expanding from 22.99 million units in 2022 to a projected 55.12 million units by 2029. This increase represents a Compound Annual Growth Rate (CAGR) of 13.3% from 2023 to 2029. As of March 2022, vehicles with Level 3 autonomy and above represent only a small segment of the market, yet notable advancements have occurred (Murali et al., 2022). These include Waymo's initiation of the first driverless taxi service in Phoenix, Arizona in 2020, and Honda's release of the first legally certified Level 3 vehicle in March 2021. In the same year, Nuro received authorization for commercial autonomous delivery in California. December 2021 saw Mercedes-Benz gaining legal approval for a Level 3 vehicle, and in February 2022, Cruise began offering driverless taxi services in San Francisco, California. In China, public robotaxi trials have been conducted, with AutoX in Shenzhen's Pingshan District in 2020, and Baidu in Beijing's Shougang Park in 2021, which also served as a site for the 2022 Winter Olympics. Efforts from tech and automobile companies along with research from institutions like Carnegie Mellon University and DARPA, have significantly propelled the field forward. Table 2 offers a side-by-side comparison of autonomous driving milestones achieved by prominent companies and institutions. 

AV applications span across personal travel, cargo logistics, and public transit. While the benefits of AVs, such as enhanced safety, operational efficiency, and wide accessibility, are significant, they also come with challenges like potential technical failures, trust deficits, and cybersecurity vulnerabilities (Kim et al., 2021). The widespread adoption and success of AV largely hinge on public endorsement, stringent safety protocols, and suitable regulatory frameworks (Kroger, ¨ 2021). 

Public perception varies, with safety and trust being prevalent concerns, while pedestrian interactions necessitate changes in behaviour and increased trust in AV systems. Implementation hinges on public acceptance, the establishment of robust safety-focused systems, and comprehensive regulatory frameworks. Fig. 6 illustrates the primary components of AVs. 

Contemporary research focuses on improving object detection for AVs to mitigate obstructions, crucial in adverse weather conditions, cited in reference (Zhang et al., 2023a). Decision making and control serves as the AV's central processing unit, formulating navigation decisions, employing methods such as reinforcement learning and rule-based algorithms, referenced in (Likmeta et al., 2020). Communication and connectivity ensure AVs interact with their environment, utilizing protocols like Vehicle-to-Vehicle (V2V), 
Vehicle-to-Infrastructure (V2I), and Vehicle-to-Pedestrian (V2P) for maintaining essential communication links, as discussed in the literature. The core aspects of AV technology are summarized in Table 3. 

Table 4 outlines the obstacles to AV adoption and their possible remedies. 

![4_image_0.png](4_image_0.png)

![4_image_1.png](4_image_1.png)

(c)

![4_image_2.png](4_image_2.png)

AV utilizes an array of advanced sensors that provide a detailed understanding of the environment in which they are operating ( Modas et al., 2020 ; Ahmed et al., 2022 ). The two main categories of sensors are typically used in these systems: exteroceptive and proprioceptive ( Ortiz et al., 2022 ). Exteroceptive sensors are oriented towards understanding the external environment of the vehicle. They include cameras, which capture visual data in various light conditions, LiDAR sensors, which use laser beams to construct a detailed three-dimensional map of the environment, RADAR sensors, that use radio waves to determine the range, angle, or velocity of objects, and ultrasonic sensors, which use sound

| Table 2  Comparative overview of autonomous driving milestones by leading companies and institutions.  Company/  Project Autonomous Miles Key Insights  Institution  Tesla, Inc. Autopilot Over a billion miles Notable usage rates, with drivers regularly utilizing the autopilot system. Level  2 autopilot includes advanced perception control system  Waymo LLC Waymo One 4 million autonomous miles by end of  Achieved fully autonomous driving in controlled settings, signifying a step  2017  towards eliminating human-AI collaboration  Uber  Uber's Self-Driving Cars 2 million autonomous miles Noted issue with drivers placing too much trust in the system  Technologies  Google LLC Waymo (Previously Google's SelfDriving Car Project)  Highest on-road autonomous miles Significant investment in deep learning research for autonomous driving  Delphi  Autonomous Driving From San Francisco to New York, 99%  Comprehensive report can be found in source  Technologies  in autonomous mode  Audi AG Audi A8 with Traffic Jam Pilot 33% of miles autonomously driven First Level 3 model with commercially available traffic jam assist. Driver is  required to remain engaged and intervene as necessary  University of  Mcity Shuttle Launch imminent Public response available via news outlets and online blogs  Michigan   |
|---|

![5_image_0.png](5_image_0.png)

Fig. 6. Key aspects of AVs. 

| Table 3  Detailed overview of key aspects of AV.  Aspect Description Related   | Current Research                                                                  |                                                                  |                                                                                           |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Technologies                                                                   | Directions                                                                        |                                                                  |                                                                                           |
| Perception &  Computer  Vision                                                 | Improving object  detection and  classification,  adverse weather  performance    |                                                                  |                                                                                           |
| Decision-Making                                                                | The "brain" of                                                                    |                                                                  |                                                                                           |
| & Control                                                                      | the AV that  decides how to  navigate  How AVs  interpret the  world around  them | LiDAR, RADAR,  Cameras, Deep  learning algorithms  Reinforcement | Developing more                                                                           |
| learning, Rulebased systems                                                                                | sophisticated  decision-making  algorithms,  handling complex  traffic scenarios  |                                                                  |                                                                                           |
| Communication                                                                  | How AVs                                                                           |                                                                  |                                                                                           |
| & Connectivity                                                                 | communicate  with other  entities                                                 | V2V (Vehicle-toVehicle), V2I  (Vehicle-toInfrastructure),  V2P (Vehicle-toPedestrian)                                                                  | Enhancing  reliability and  security of  communications                                   |
| Cybersecurity                                                                  | Protection of  AVs from  digital threats                                          | Encryption,  Intrusion detection  systems                        | Developing  advanced  protective  measures, threat  detection and  mitigation  techniques |

| Table 4  Challenges in AV adoption and potential solutions.  Challenge Current State Proposed Solutions   | Areas for Future  Research                                       |                                                                                                                                                                         |                                                                             |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Safety                                                                                                    | High variability                                                 |                                                                                                                                                                         |                                                                             |
| Concerns                                                                                                  | in public  perception                                            | Exploring public  perceptions,  developing advanced  safety systems                                                                                                     |                                                                             |
| Trust Issues                                                                                              | Uncertainty  about reliability  of technology                    | Clear  communication on  safety measures,  improved safety  systems  Transparency about  system  functionality and  limitations,  extensive testing  and demonstrations | Understanding  public trust, ensuring  robust system  performance           |
| Regulatory                                                                                                | Diverse and                                                      |                                                                                                                                                                         |                                                                             |
| Hurdles                                                                                                   | sometimes  conflicting  regulations in  different  jurisdictions | Studying impacts of  regulations,  exploring  international  coordination                                                                                               |                                                                             |
| Cybersecurity                                                                                             | Potential  vulnerabilities to  cyberattacks                      | Harmonizing  regulations,  cooperation  between  stakeholders  Developing  advanced  protective  measures, threat  detection and  mitigation  techniques                | Research into new  threats and  countermeasures,  exploring ethical  issues |

waves to detect objects and estimate their distance from the vehicle. These sensors play a crucial role in environmental perception, allowing the vehicle to accurately estimate distances to nearby objects, assess light intensities and conditions, recognize road signs and markings, and capture other relevant environmental features like the movement of other road users (Jebamikyous and Kashef, 2022; Shi et al., 2021; Ma et al., 2020). Conversely, proprioceptive sensors are focused on the internal state of the vehicle. These sensors monitor various parameters that are related to the vehicle itself rather than its environment. Like, IMU are used to track the vehicle's motion and orientation, encoders measure the rotation of the wheels and other components, gyroscopes monitor the vehicle's orientation and rotation, magnetometers measure magnetic fields, often used to determine the vehicle's heading and, Global Navigation Satellite System (GNSS) receivers, which include technologies like Global Positioning System (GPS), provide precise location data (Xia et al., 2021; Ertugrul and Ulkir, 2020; Yan et al., 2021; Swaminathan et al., 2022). Fig. 7 depicts the types of sensors utilized in AVs. 

The navigation system of an AV integrates various components for precise operation. An IMU sensor is crucial for measuring the vehicle's motion and orientation, aiding in the accurate localization of the AV within its environment. Complementing this, high-definition maps provide detailed geographic data that enhances navigation capabilities. 

Technologies including LiDAR, Cameras, RADAR, and Ultrasonic Sensors are employed to measure distances, capture visual data, detect objects, and gauge proximity, respectively. These instruments are pivotal for the AV's recognition and analysis of its surroundings, which is essential for informed navigation. Subsequently, this data contributes to the determination of route design and choice, ultimately guiding the AV's movement regulation for safe and efficient travel. Sensor fusion is the process of combining data from multiple sensors in a way that enhances the quality and reliability of the information (Khayyam et al., 
2020). Fig. 8 illustrates the significance of sensors in the operation of AV. 

The analysis examines sensor types in AVs, assessing their error sensitivity, resilience to environmental factors, and influence on navigational certainty and system robustness. Each sensor's function within AVs and their value is briefly explained. Delving into the role of sensors ranging from LiDAR to GPS, their integration into the AV's instrumentation suite is considered, noting their accuracy, dependability, and essential data contribution. The examination brings to light the distinct strengths and constraints of the sensors, delineating their part in advancing AV navigation and safety mechanisms. The complex sensor network essential for AVs' advanced operations is clarified through this comparative perspective. In the context of deep learning-based adaptive methodologies for real-time tasks like obstacle detection, the ability of the system to intelligently process and act upon sensor input is critical 
(Ravindran et al., 2021). A combination of sensor types utilized in AVs is presented in Table 5, spotlighting their responsiveness, functionality, and practical applications. 

Expanding on the roles of sensor integration in AVs, the study investigates sensor specifications for varying autonomy levels. Level 1 autonomy, or Driver Assistance, primarily uses elementary sensors that support functions like adaptive cruise control and parking assistance. As vehicles progress to Level 2, or Partial Automation, there is an increased need for advanced sensors. Here, sophisticated cameras and an essential IMU enable features like lane keeping and refined vehicle motion tracking. At Level 3, Conditional Automation, a comprehensive array of sensors is required. The addition of LiDAR and advanced RADAR systems improves the detection and tracking of obstacles, while encoders provide detailed measurements of wheel speed and position, further supported by a precise GNSS receiver for exact location data. Level 4, or High Automation, demands even more advanced sensor technology. 

High-definition cameras for detailed object recognition and 360-degree LiDAR systems provide a comprehensive environmental understanding, with gyroscopes introduced for accurate orientation data. Finally, Level 5, Full Automation, incorporates the most complex and sophisticated sensor networks. A differential GNSS receiver ensures exceptional location precision, and an Inertial Navigation System (INS) maintains continuous locational and orientational information, independent of GNSS signals. This overview outlines the potential sensor combinations as vehicle autonomy levels increase. The specific sensor requirements and their roles at different autonomy stages are detailed further in Table 6. 

## 3.1. Camera (Vision) Sensor

Cameras are the essential part of perception mechanisms in AVs 
(Zaarane et al., 2020). Camera sensors, or vision systems, are integral to the operation of AVs. These sensors act as the eyes of the AV, capturing 

![7_image_0.png](7_image_0.png)

![7_image_1.png](7_image_1.png)

Table 5 

Comparative analysis of sensor types in AV: Sensitivity, utility, and applications. 

Sensor 

Type 

Sensitivity to Calibration 

Errors 

Sensitivity to 

Environmental Changes 

Contribution to 

Uncertainty 

Contribution to 

Redundancy 

Example in AVs Characteristics 

High (provides unique 3D data) 

3D mapping Provides precise distance 

information, valuable for 

redundancy 

Camera High (misalignment and 

distortions can cause 

errors) 

| Sensitivity to Calibration                   | Sensitivity to                                                                           |
|----------------------------------------------|------------------------------------------------------------------------------------------|
| Errors                                       | Environmental Changes  Moderate (affected by                                             |
| lead to major errors)                        | weather, but provides  stable 3D data)                                                   |
| distortions can cause  errors)               | Low (robust against most                                                                 |
| misalignment)                                | weather conditions)  High (lighting conditions  greatly affect output)                   |
| can affect distance  readings)               | Low (not directly                                                                        |
| accumulate over time)                        | affected by  environmental changes)  Moderate (affected by  surface material and  angle) |
| system with inherent  correction mechanisms) | High (affected by urban  canyons or indoor  environments)                                |

High (provides rich 

visual details) 

Object 

recognition 

Provides rich visual details, 

adding to the comprehensive 

understanding 

RADAR Low (more tolerant to 

misalignment) 

Low (robust against most 

weather conditions) 

Moderate (lower 

resolution can add to 

uncertainty) 

Moderate (provides 

speed and angle data) 

Adaptive cruise 

control 

Robust sensor for distance 

and speed, useful in 

challenging weather 

conditions 

Ultrasonic Moderate (misalignment 

can affect distance 

readings) 

Useful for close-range 

obstacle detection, adding a 

different perspective 

IMU High (drift errors can 

accumulate over time) 

Low (not directly affected by environmental changes) 

Inertial navigation 

Contributes unique inertial data, useful for short-term navigation 

GPS Low (global positioning 

system with inherent 

correction mechanisms) 

High (lighting conditions 

greatly affect output) 

High (processing errors 

can add to overall 

uncertainty) 

| Contribution to  Uncertainty  Low (high precision  reduces overall  uncertainty)  Moderate (lower  resolution can add to  uncertainty)  High (processing errors  can add to overall  uncertainty)  High (noise can add to  overall uncertainty)  High (drift errors  contribute to overall  uncertainty)  Moderate (errors can  occur in challenging  reception conditions)   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

High (noise can add to 

overall uncertainty) 

Low (limited range and 

precision) 

Close-range 

obstacle 

detection 

High (provides global 

positioning) 

Global 

positioning 

Provides global position 

information, valuable for 

long-range navigation 

| Contribution to  Redundancy  High (provides unique  3D data)  High (provides rich  visual details)  Moderate (provides  speed and angle data)  Low (limited range and  precision)  Moderate (provides  unique acceleration and  angular velocity data)  High (provides global  positioning)   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

detailed visual information from the vehicle's surroundings. Advanced computer vision algorithms then process this data, enabling the vehicle to identify and respond to obstructions. The final step involves a processor within the vehicle's AI computer system, which performs image transformation, detection, and segmentation to accurately interpret and utilize the visual data for navigation and decision-making. The constant innovation in camera technology has significantly improved the reliability and functionality of AVs. As a result, vision sensors play a crucial role in the perception and decision-making systems that supports autonomous driving. Fig. 9 displays the Valeo's 1 MP fisheye ETH, a resilient automotive camera that provides superior imagery under all circumstances (Valeo). 

Some of the unique advantages of camera includes detailed visual information about the environment, closely resembling the human vision, their ability to detect colour, which is crucial for recognizing traffic lights, road signs, lane markings, pedestrians, and other vehicular traffic (Juyal et al., 2021; Wang et al., 2022a; Severino et al., 2021; Iftikhar et al., 2022; Kim and Lee, 2022; Shahian Jahromi et al., 2019). They are highly effective for pattern recognition tasks, such as detecting and reading text or identifying objects based on their appearance. From an architectural viewpoint, camera systems in AVs can be divided into different classifications. Table 7 provides an overview of the main characteristics and features associated with various camera types. 

Camera systems, despite their advantages, present challenges such as sensitivity to lighting conditions, performance impact due to weather conditions, lens distortion, and the need for substantial computational resources. Intense sun glare can greatly diminish image clarity, depth perception, and colour accuracy, often leading to over-saturation. Snow Fig. 7. Sensors employed in AV. 

Fig. 8. Role of sensors in the functioning of AV. 

Table 6 

Detailed sensor requirements and their roles for different levels of vehicle autonomy. 

Level of Autonomy 

Sensor Requirement Role 

Level 1: Driver 

Assistance 

Basic Camera, RADAR, Ultrasonic Sensors, Basic GNSS Receiver 

Fig. 9. Valeo's 1 MP fisheye ETH is a durable automotive camera offering topquality visuals in all conditions (Valeo). 

![8_image_0.png](8_image_0.png)

| Detailed sensor requirements and their roles for different levels of vehicle  Sensor Requirement Role  Basic Camera, RADAR,  Ultrasonic Sensors, Basic  GNSS Receiver  Camera and RADAR are used  for adaptive cruise control and  collision avoidance. Ultrasonic  sensors are used for parking  assistance. GNSS Receiver for  basic navigation support.  Advanced Camera, RADAR,  Ultrasonic Sensors, Basic  GNSS Receiver, Basic IMU  In addition to the roles in Level  1, Advanced Cameras provide  lane keeping assistance. Basic  IMU aids in providing more  accurate vehicular motion  tracking.  Sensors from Level 2 are  enhanced. LiDAR and multimodal RADAR are introduced  for better obstacle detection  and tracking. Encoders provide  accurate wheel speed and  position. Advanced GNSS  provides more accurate geolocation data.  High-res Camera, Multimodal RADAR, 360-degree  LiDAR, Ultrasonic Sensors,  Advanced IMU, Encoders,  Advanced GNSS Receiver,  Gyroscope  Advanced Camera, Multimodal RADAR, LiDAR,  Ultrasonic Sensors, Advanced  IMU, Encoders, Advanced  GNSS Receiver  High-resolution cameras for  better object and signal  recognition. 360-degree LiDAR  for complete environment  perception. Gyroscope added  for more precise orientation  measurements.  High-res Camera, Multimodal RADAR, 360-degree  LiDAR, Ultrasonic Sensors,  Advanced IMU, Encoders,  Differential GNSS Receiver,  INS (Inertial Navigation  System)  In addition to sensors in Level  4, Differential GNSS Receiver  provides high-precision  location data. INS offers  continuous location and  orientation data even in GNSSdenied environments.   |
|---|

may cause image overexposure and obscure depth information. Rainstorms lower clarity and depth accuracy and alter colour perception due to light scattering. Hazy conditions result in washed-out images, affecting both depth and colour contrast. At night time, the resolution and depth information are compromised due to low light, and colour detail is generally lost. Fog similarly impacts all aspects by scattering light, which impairs clarity, depth accuracy, and colour saturation. Robust algorithms capable of handling a wide range of lighting and weather conditions, intrinsic camera calibration for distortion correction, and efficient design and implementation to handle high-resolution image data processing in real-time are essential for optimal performance. 

## 3.2. Light Detection And Ranging (Lidar)

LiDAR has emerged as a crucial technology in the field of remote sensing, proving itself to be an essential component in the development and operation of AV (Li and Ibanez-Guzman, 2020). These sensors play a crucial role in the sensory apparatus of AVs, using pulsed laser light to map out the vehicle's surroundings in three dimensions. These sensors are proficient in providing high-resolution, real-time data essential for obstacle detection and navigation (Fahey et al., 2021; Antah, 2021; Lin et al., 2021; Park and Cho, 2020; Pirhonen et al., 2022; Ibrahim et al., 2021). Table 8 provides details for key components of a LiDAR system. 

Unlike cameras, LiDAR is less affected by lighting conditions, offering consistent performance at both day and night. Its ability to generate precise 3D models of the environment makes it invaluable for the complex processing required for AV systems. LiDAR offers high spatial resolution and accuracy, which is essential for detailed environment modelling and obstacle detection. Fig. 10 depicts the elements of 3D 
LiDAR, data collection, and the map generation process utilized in one of Google's AV. 

However, despite its numerous advantages, one of the primary considerations in the adoption of LiDAR technology remains its cost. Historically, the high price of LiDAR systems has been a significant barrier to widespread adoption, particularly in consumer-grade applications. While the cost of LiDAR has indeed dropped significantly in recent years, making it more accessible for a broader range of applications, it remains a substantial investment. The reduction in price is attributed to advancements in manufacturing techniques, economies of scale, and intensified competition among suppliers. Nevertheless, the cost of these systems, especially those offering the highest resolution and longest range required for certain applications such as autonomous driving, can still be prohibitive for many companies and researchers. 

| Key components of a LiDAR system.  Component Function  Laser Emits pulses of light to measure distance  Scanner &  Directs the laser beams and gathers the reflected light  Optics  Photodetector Detects the reflected light pulses  Time-of-flight Measures the time taken for the light to travel to the object and  back  Data Processing Translates raw data into a 3D representation of the surrounding  environment   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Table 7  Comparative summary of camera technologies in automotive applications.  Camera Type Key Characteristics Pros   | Cons                                                                                             | Typical Applications                                             |                                                                               |                                                            |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------|
| Monocular (Gao et al.,  2020, 2023; Li et al.,  2023a)                                                                  | Regulated roads, image  processing, feature  extraction                                          |                                                                  |                                                                               |                                                            |
| Binocular (Real-Moreno  et al., 2021; Gao et al.,  2023)                                                                | Simple setup, closely matches human  colour perception, advanced algorithms  for depth inference | Low computational  requirements, easy calibration,  simple setup | Lacks native depth perception, less  robust depth compared to stereo  systems | Mobile robot positioning,  navigation, obstacle  avoidance |
| Fisheye (Mishra et al.,                                                                                                 | Ultra-wide-angle lenses, large field of                                                          | Extensive field of view, useful                                  | May introduce distortion, less detailed                                       | Near-field sensing,                                        |
| 2022)                                                                                                                   | view, useful for near-field sensing                                                              | for near-field applications                                      | depth perception                                                              | panoramic view  applications                               |
| Multi-view (Lv et al.,                                                                                                  | Multiple vantage points, high accuracy                                                           | High accuracy, reduced error                                     | Complex algorithms, high                                                      | High precision tasks,                                      |
| 2021)                                                                                                                   | through reduced matching error                                                                   | in matching                                                      | computation time and power                                                    | complex environments                                       |
| Utilizes two image sensors for native  depth perception, mimics human  binocular vision                                 | Provides depth perception,                                                                       | Higher computational needs,                                      |                                                                               |                                                            |
| better for obstacle detection                                                                                           | calibration complexity, complex  disparity interpretation                                        |                                                                  |                                                                               |                                                            |

![9_image_0.png](9_image_0.png)

This economic factor necessitates a careful cost-benefit analysis when considering the implementation of LiDAR technology. 

Three principal kinds of LiDAR sensors, categorized as 1D, 2D, and 3D, have applications across various domains (Raj et al., 2020). These sensors generate Point Cloud Data (PCD) in corresponding dimensions, inclusive of the objects' intensity information. In the context of autonomous driving, 64 or 128 channel LiDAR sensors are prevalent for generating high-resolution PCD. These sensors have been summarized in Table 9. 

LiDAR technology is a pivotal element in AVs, fulfilling five fundamental functions. For road marking recognition, Solid-State LiDAR is utilized to discern lane indicators and traffic signs, despite challenges with visibility and marking deterioration (Wu et al., 2021; Gannavaram V and Bejgam, 2021). In terms of regulating vehicle speed, for Micro-Electro-Mechanical Systems(MEMS) LiDAR measures distances to adjust speed in response to traffic flow, which can be complicated by the intricacies of traffic (Vutla et al., 2021; Stelzer et al., 2020). Assisted parking is facilitated by Flash LiDAR, which provides accurate spatial data for complex parking tasks, although limited space and high object density can pose difficulties (A. et al., 2021). For collision prevention, Mechanical LiDAR detects imminent obstacles, initiating pre-emptive measures, with challenges arising from sensor integration and response time (Lei et al., 2023). LiDAR technologies grant AVs the ability to safely manoeuvre through complex environments by offering precise, real-time spatial data, underscoring their significance in the progression of AVs. Further information on the specific functions and associated challenges of various LiDAR systems in automotive applications is compiled comprehensively in Table 10. 

Fig. 11 showcases the LiDAR Data Processing Sequence. Moving from left to right, the images illustrate a dense LiDAR point cloud, streamlined, and minimized LiDAR data, a point cloud segmented into the roadway and obstructions, and clustered obstructions within the segmented cloud. The prominent dark area in the centre represents the AV. 

| Table 10  Functions, descriptions, and challenges of various LiDAR types in automotive  applications.  Function Description Primary LiDAR  Potential  Type  Challenges  Obstacle  Detects and categorizes  Identification  objects such as vehicles,  pedestrians, and other  barriers in real time.  Mechanical Interference,  false positives  Roadway  Marking  Recognition  Solid-State Poor visibility,  wear on  markings  Adaptive Speed  Utilizes distance  Regulation  measurements to adapt  speed according to  traffic conditions.  Analyses and identifies  lane markings, traffic  signals, and road signs.  Micro-ElectroMechanical  Systems  (MEMS)  Traffic  complexity  Assisted  Aids in complex parking  Parking  manoeuvres by  providing precise spatial  measurements.  Flash Space  constraints,  object density  Collision  Helps prevent accidents  Prevention  by sensing objects in the  vehicle's pathway and  taking preventive action.  Mechanical Sensor fusion,  latency   |
|---|

## 3.3. Radio Detection And Ranging (Radar)

RADAR sensors are integral to the advanced safety systems and operational effectiveness of AV. They utilize the Doppler effect to determine the relative speed and position of identified obstacles (Ignatious et al., 2022; Burnett et al., 2021). Fig. 12 displays a RADAR device affixed to the front bumper (Electrek). 

Table 11 describes the fundamental elements of a RADAR system. 

Fig. 13 illustrates the processing pipeline of a RADAR sensor. 

There are various types of RADAR sensors utilized for different purpose of AV, as described in Table 12. 

To achieve comprehensive 360◦ coverage around the vehicle, it is essential to install multiple RADAR sensors at various locations on the 

| Overview and applications of different types of LiDAR dimensions.  Type Description   | Application                                                                           |                                                                       |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| 1D                                                                                    | Provides linear representation of the environment by measuring distance.              | Basic distance measurement applications.                              |
| LiDAR  2D                                                                             | Provides radial representation of the environment by measuring distance and angle.    | Enhanced spatial understanding, suitable for robotics and automation. |
| LiDAR  3D                                                                             | Provides a 3D representation of the environment by measuring the distance, angle, and | Comprehensive spatial understanding, ideal for AV and advanced        |
| LiDAR                                                                                 | elevation.                                                                            | robotics.                                                             |

![10_image_0.png](10_image_0.png)

![10_image_1.png](10_image_1.png)

| Basic components of a RADAR system.  Component Function  Transmitter Produces electromagnetic waves in the domain of radio or  microwaves  Transmitting  Propagates the electromagnetic waves produced by the  Antenna  transmitter  Receiving Antenna Receives the reflected waves that bounce off objects  Receiver Processes the received signals  Processor Determines the properties of the objects that reflected the  waves   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

car. Once the data from all these sensors is collected, it needs to be integrated and processed. Fig. 14 demonstrates the strategic positioning of RADAR sensors on a car to achieve 360◦ coverage. 

One of the most compelling advantages of RADAR is its resilience in challenging conditions such as fog, heavy rain, and darkness situations where optical sensors might struggle due to their reliance on light waves at a reasonable cost (Sun et al., 2020). Yet, despite their robustness in adverse weather conditions, RADAR systems present inherent limitations that impact their performance and application. Primarily, the resolution of RADAR sensors falls short compared to that of LiDAR and optical cameras, limiting their ability to distinguish closely spaced objects or accurately identify smaller obstacles which is a critical consideration in densely populated urban settings. Furthermore, interference among vehicle is a growing concern as the use of RADAR in autonomous vehicles increases. With vehicles often equipped with multiple RADAR 
units, the risk of these systems interfering with each other escalates, posing a challenge for manufacturers to address, especially given the critical safety functions these RADARs support. 

## 3.4. Ultrasonic Sensors

Within the realm of AV, the primary application of ultrasonic sensors is most evident in scenarios requiring meticulous low-speed manoeuvres (Nesti et al., 2023). Their strength lies in their adeptness at discerning objects in close proximity to the vehicle (Manoj et al., 2023). Perhaps one of their most crucial attributes is their independence from light conditions. This ensures that unlike optical systems, ultrasonic sensors maintain consistent performance even under challenging visibility conditions of night time or fog (Mohammed et al., 2020). They typically have a wide field of view, allowing for the detection of objects at various angles relative to the sensor. Fig. 15 illustrates the integration of ultrasonic sensors in the operations of AV. 

Table 13 provides an overview of the different types of ultrasonic sensors and their typical applications. 

Table 14 below provides a comprehensive overview of various environmental and traffic conditions impact on the performance of ultrasonic sensors in AV. It explains the specific challenges each condition presents to these sensors and illustrates deep learning techniques that can be adapted to mitigate these effects. Additionally, it offers recommendations for further optimizing the performance of ultrasonic sensors under these specific circumstances, ensuring the safe and effective operation of AV in diverse conditions. 

## 3.5. Inertial Measurement Units (Imu) Sensors

IMUs, are an integral component in the ever-evolving domain of AV 
to deduce the vehicle's orientation, its velocity, and its position changes (Zhao, 2023). IMU tracks the vehicle's acceleration and rotational rates, in three dimensions X, Y, and Z, contributing to the understanding of vehicle dynamics and movement (Khanum et al., 2023). They are integral for determining the vehicle's orientation and changes in positioning, aiding in accurate localization. Sensor components are made up of IMU sensors which are typically a mix of accelerometers, gyroscopes, and occasionally magnetometers (Abu-Alrub and Rawashdeh, 2023). An interesting capability is that the data from these sensors can be 

![11_image_0.png](11_image_0.png)

| Table 12  RADAR application matrix for AV.  Applications Short-Range  MediumRange (60  (24 GHz)  GHz)  Collision  Avoidance  Lane Change  Assist  Blind Spot  Detection  Adaptive  Cruise  Control  Pedestrian  Detection   |
|---|

Long-Range (77 GHz) 

Future LongRange (79 

GHz) 

Collision 

Avoidance 

Moderate Good Excellent Excellent 

Lane Change 

Assist 

Poor Moderate Good Excellent 

Blind Spot 

Detection 

Moderate Good Good Excellent 

Adaptive 

Cruise 

Control 

Poor Moderate Excellent Excellent 

Pedestrian 

Detection 

Poor Moderate Good Excellent 

Parking Assist Excellent Good Fair Poor 

combined with readings from other devices like cameras, LIDAR and 

![11_image_1.png](11_image_1.png)

RADAR. This fusion significantly enhances the efficacy of systems meant to detect obstacles (Mohamed et al., 2019; Ali et al., 2021). Fig. 16 displays IMU sensors incorporation with a range of sensing elements to gauge motion and direction. 

An IMU can calculate the shifts in position and orientation without needing reference points from outside the system (Seel et al., 2014). Table 15 outlines the characteristics and features of IMU sensors. 

In the context of fusing IMU data with other sensors data for obstacle detection, various combinations can arise. When IMU data is combined with visual inputs from a camera, there is a compensation for visual motion blur. Some potential models that can leverage this combination include multi-modal CNNs and Visual-Inertial Odometry Networks. 

Moving to another fusion type, pairing IMU with acoustic information obtained from an ultrasonic sensor can significantly enhance the detection of obstacles that are in close proximity. Models that could potentially benefit from this type of fusion are sequential CNN-RNN 
architectures. Lastly, when IMU data is integrated with depth information sourced from a depth camera, there is an enhancement in the threedimensional comprehension of an environment. This is particularly useful for detecting changes in elevation. Table 16 details the fusion of IMU data with other sensor modalities for obstacle detection in AV. 

## 3.6. Sensor Fusion Approaches In Autonomous Vehicles

Following the sections on sensor types used in AVs, it is crucial to 

![11_image_2.png](11_image_2.png)

understand the integration of these diverse data sources to enhance the 

![12_image_0.png](12_image_0.png)

Fig. 15. Ultrasonic sensor integration in autonomous vehicle operations. 

vehicle's perception and decision-making capabilities. This section delves into the various ways sensor fusion can happen, offering insights into the methodologies employed to integrate data from different sensors for improved outcomes. Sensor fusion can be broadly classified 

![12_image_1.png](12_image_1.png) into three primary levels based on the fusion stage, Low-Level Fusion (LLF), Mid-Level Fusion (MLF), and High-Level Fusion (HLF). 

Fig. 16. IMU sensors integrate a variety of sensing components to measure motion and direction (OFweek, 2021). 

| Table 13  Varieties of ultrasonic sensors.  Type Description   | Typical Applications                                                  | Operating                                     | Sensing Range      | Common            |                       |
|----------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|--------------------|-------------------|-----------------------|
| Frequency                                                      | Manufacturers                                                         |                                               |                    |                   |                       |
| Proximity Detection                                            | Detect presence or absence of an object based on                      | Detecting products on                         |                    |                   |                       |
| Ultrasonic Sensors                                             | sound wave reflection.                                                | manufacturing lines, vehicle  parking.        | 40–50 kHz          | 2 cm-3m           | SensComp, Parallax    |
| Distance Measuring                                             | Measure the distance between the sensor and an                        |                                               |                    |                   |                       |
| Ultrasonic Sensors                                             | object by calculating the time between wave  emission and its return. | Robotics navigation, measuring                | 20–40 kHz          | 2 cm-6m           | MaxBotix, PING        |
| liquid levels, toll booths.                                    |                                                                       |                                               |                    |                   |                       |
| Ultrasonic Through                                             | Uses a separate sender and receiver. The interruption                 |                                               |                    |                   |                       |
| Beam Sensors                                                   | of the continuous wave between them indicates an  object's presence.  | Counting items, detecting breaks              | 40–60 kHz          | 5 cm-5m           | Keyence, Siemens      |
| in continuous material flow.                                   |                                                                       |                                               |                    |                   |                       |
| Ultrasonic Reflective                                          | Detect objects by noting a change in the pattern of                   | Detecting liquid levels,                      |                    |                   |                       |
| Sensors                                                        | returned ultrasonic waves.                                            | monitoring stack height in  production lines. | 30–50 kHz          | 3 cm-4m           | Banner, Turck         |
| Doppler Effect                                                 | Measure an object's velocity by utilizing the Doppler                 | Measuring flow in pipes, traffic              | 20–30 kHz          | Variable based on | Endress + Hauser,     |
| Ultrasonic Sensors                                             | Shift in the returned wave frequency.                                 | speed monitoring.                             | application        | KROHNE            |                       |
| Open Structure                                                 | Have an open face for broader beam angles, allowing                   | Complex robotics applications for             | 25–45 kHz          | 2 cm-5m           | Pepperl + Fuchs, Sick |
| Ultrasonic Sensors                                             | a more extensive sensing range.                                       | wider detection angle.                        |                    |                   |                       |
| Closed Structure                                               | Sensing elements are enclosed in a protective                         |                                               |                    |                   |                       |
| Ultrasonic Sensors                                             | housing, ideal for environments with dust or  moisture.               | Outdoor or industrial settings                | 30–60 kHz          | 2 cm-6m           | Balluff, IFM          |
| with environmental challenges.                                 |                                                                       |                                               |                    |                   |                       |
| Analog Output                                                  | Provide continuous analog output representative of                    | Processes requiring exact                     | 20–60 kHz          | 2 cm-6m           | Omron, Microsonic     |
| Ultrasonic Sensors                                             | the distance to the target.                                           | distance tracking.                            |                    |                   |                       |
| Digital Output                                                 | Offer binary output based on the presence or absence                  | Object detection in assembly                  | 25–55 kHz          | 2 cm-5m           | Telemecanique         |
| Ultrasonic Sensors                                             | of an object within a predetermined range.                            | lines, vehicle parking sensors.               | Sensors, Panasonic |                   |                       |

| Table 14  Ultrasonic sensors in AV: Performance under various conditions.  Condition Performance Impact   | Deep Learning Adaptation                                     | Recommendation                                          |                                        |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------|----------------------------------------|
| High Traffic Areas                                                                                        | Frequent detection of obstacles due to the                   | Use neural networks trained on dense traffic scenarios  | Combine ultrasonic data with LiDAR/    |
| proximity of multiple vehicles.                                                                           | to filter false positives and rank obstacle importance.      | RADAR to improve accuracy.                              |                                        |
| Low Visibility (Fog, Rain)                                                                                | Moisture can attenuate ultrasonic waves,                     | Deep learning can be used to fuse ultrasonic data with  | Use sensors with protective coatings   |
| reducing sensor range.                                                                                    | other sensors to compensate for lost information.            | and integrate with cameras.                             |                                        |
| Tunnel or Enclosed Spaces                                                                                 | Excessive echoes due to close walls may                      | Neural networks trained on tunnel scenarios can         | Apply advanced echo discrimination     |
| confuse readings.                                                                                         | distinguish between walls and genuine obstacles.             | algorithms.                                             |                                        |
| Parking & Low-Speed                                                                                       | Increased relevance of ultrasonic sensors for                | Deep learning can enhance precision in determining      | Integrate with cameras for better      |
| Manoeuvres                                                                                                | detecting close-range obstacles.                             | the exact location and nature of nearby obstacles.      | spatial understanding.                 |
| Highway or High-Speed                                                                                     | Fast-moving objects might cause a Doppler                    | Neural networks optimized for high-speed scenarios      | Complement with long-range sensors     |
| Conditions                                                                                                | shift or rapid entry-exit from sensing range.                | can better predict and track fast-moving obstacles.     | like RADAR.                            |
| Changing Road Surfaces                                                                                    | Different surfaces (asphalt, gravel) can affect              | Use deep learning to adaptively change sensor           | Integrate ultrasonic sensors with road |
| reflection patterns.                                                                                      | sensitivity based on predicted road surface.                 | surface detection systems.                              |                                        |
| Near Pedestrians or Cyclists                                                                              | Soft materials (clothing) might absorb more                  | Neural networks can be trained to identify typical      |                                        |
| ultrasonic waves, reducing reflection.                                                                    | patterns for pedestrians and cyclists, improving  detection. | Fuse ultrasonic data with camera and  infrared sensors. |                                        |
| During Vehicle-to-Vehicle                                                                                 | Potential for interference from other vehicles'              | Deep learning can identify and filter out interference  | Use frequency-agile ultrasonic sensors |
| (V2V) Communication                                                                                       | ultrasonic systems.                                          | patterns, focusing on genuine obstacle detection.       | to reduce interference.                |

| Table 15  Characteristics and features of IMU.  Feature Description  Components Accelerometer, Gyroscope, (sometimes) Magnetometer  Measurement Axes Linear acceleration (X, Y, Z); Angular velocity (Pitch, Yaw,  Roll)  Output Frequency Typically, high-frequency, often hundreds to thousands of Hz  Resolution Can vary, but modern IMUs can have very high precision  Latency Generally, very low, suitable for real-time operations  Size & Weight Compact, lightweight - ideal for integration into vehicles  Cost Varied, but many cost-effective solutions available  Energy  Generally low, allowing for extended operation  Consumption   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1. Low-Level Fusion (LLF): LLF, also known as early fusion, combines raw data from various sensors directly, aiming to preserve data richness and enhance object detection and classification (Butt et al., 2022). For instance, a two-stage 3D obstacle detection architecture named 3D-Cross View Fusion (3D-CVF) illustrates LLF by integrating camera and LiDAR data at the raw level to improve obstacle detection accuracy (Yoo et al., 2020). 

2. Mid-Level Fusion (MLF): MLF fuses extracted features from different sensors, such as colour from cameras and spatial data from LiDAR that occurs after initial data processing (Anisha et al., 2023). This exploitation of complementary sensor characteristics is exemplified by Yue Li et al., where Symbolic Dynamic Filtering (SDF) integrates low-dimensional features from infrared sensors for dynamic target detection in communication-limited environments (Li et al., 2015). 

3. High-Level Fusion (HLF): HLF merges independent sensor decisions or inferences, focusing on the implications of data rather than the data itself (Dai et al., 2020). A noted application involves processing RADAR and LiDAR data separately before fusion through a non-linear Kalman Filter method for enhanced obstacle detection and state tracking (Shahian Jahromi et al., 2019). Preferred for its reduced computational demand, HLF may sometimes underutilize available sensory data. 

Each fusion level introduces distinct challenges and considerations. 

LLF demands significant computational effort and meticulous sensor alignment. MLF requires robust feature extraction algorithms to synthesize relevant information effectively. Conversely, HLF, though less computationally intensive, may overlook critical data by concentrating solely on decision-level information. Table 17 below provides comparative overview of sensor fusion levels in AV. 

The comparison of sensor fusion strategies has been mentioned in Fig. 17. 

The integration of multi-modal sensor data through LLF, MLF, and HLF plays a pivotal role in advancing the capabilities of autonomous vehicles. By leveraging LLF, MLF, and HLF, AV systems gain a more accurate, reliable, and comprehensive environmental understanding, which is essential for safe and efficient navigation. 

## 4. **A Comprehensive Exploration Of Deep Learning**

Deep learning, considered as an advancement of neural networks, serves as a core element of artificial intelligence and machine learning. The origin of deep learning can be traced back to 1943 when Walter Pitts and Warren McCulloch proposed the idea of Artificial Neural Networks 
(ANN), a model inspired by the operation principles of human neural networks (Rezaei et al., 2023). In modern applications, deep learning has been widely utilized in various fields such as object detection, environmental segmentation and semantic object identification, etc (Rafique et al., 2023). Self-Driving Cars (SDCs) employ a comprehensive suite of algorithms specifically tailored for obstacle detection, which frequently include deep learning methods like CNN, RNN, Deep Belief Networks (DBN), AutoEncoders (AE), You Only Look Once (YOLO), EfficientNets, and DETR (DEtection TRansformer) (Murthy et al., 2020; Sengupta et al., 2020; Abbas et al., 2019; Ma, 2022). For understanding temporal patterns in obstacle movement Long Short-Term Memory (LSTM) networks are used (Song et al., 2020). Generative Adversarial Networks (GANs) augment the primary detection capabilities by simulating potential obstacle scenarios (Aggarwal, 2021). Feature extraction and anomaly detection, essential for spotting unfamiliar obstacles, employ tools like Deep Belief Networks (DBN) (Dargan et al., 2020). 

More advanced neural techniques that contextualize obstacles, including Siamese Neural Networks, Transformers, Capsule Networks 
(CapsNet), and Vision Transformers (ViT), provide a holistic view of the vehicle's surroundings (Kang et al., 2022; Dulian and Murray, 2021; Itu and Danescu, 2022; Jeong et al., 2020). When crafting solutions for AVs, a combination of these algorithms often delivers optimal performance. Fig. 18 illustrates network designs used for obstacle recognition in AVs. 

CNNs play a significant role in AV proficiency by extracting key features from sensor data through convolution, excelling in tasks like image recognition and object segmentation (Triki, 2021). R-CNNs, an extension of CNNs, specialize in obstacle detection and localization in AVs. They segment an input image into region proposals, classify them, and localize detected objects, adapting to sensor data variability (Othmani, 2022). Fast R-CNNs improve computational efficiency by processing the entire image once to create a feature map, reducing the load and time for real-time AV obstacle detection (Mostafa et al., 2022; Ghosh, 2021). Faster R-CNNs further enhance this by integrating a Region Proposal Network (RPN), which generates region proposals within 

| Table 17  Comparative overview of sensor fusion levels in autonomous vehicles.  Sensor  Advantages Drawbacks Typical  Fusion Level  Applications  Low-Level  Fusion (  Butt et al.,  2022; Yoo  et al.,  2020)  3D obstacle  detection,  enhanced  environmental  modelling.  Mid-Level  Fusion (  Anisha  et al.,  2023; Li  et al.,  2015)  Maximizes data  richness, enhancing  detection accuracy.  High  computational  demand, precise  sensor calibration  needed.  Balances  computational load,  exploiting  complementary  sensor traits.  Potential loss of  raw data details,  requires effective  feature extraction.  Dynamic target  detection, object  classification.  High-Level  Fusion (  Dai et al.,  2020;(  Shahian  Jahromi  et al.,  2019)  Lower  computational  complexity; utilizes  independent sensor  decisions.  Risks discarding  valuable data by  focusing on highlevel decisions.  State tracking,  obstacle detection  with advanced  filtering methods.   |
|---|

| Fusion of IMU data with other sensor modalities for obstacle detection.  Fusion Type Secondary Sensor Benefits of Fusion   | Potential Deep Learning Models for Fusion   |                                                                              |                                                     |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------|
| IMU + Visual                                                                                                               | Camera                                      | Compensate for visual motion blur; Improve localization and pose estimation  | Multi-modal CNNs; Visual-Inertial Odometry Networks |
| IMU + Acoustic                                                                                                             | Ultrasonic Sensor                           | Enhance close-proximity obstacle detection; Improve underbody awareness      | Sequential CNN-RNN architectures                    |
| IMU + Depth                                                                                                                | Depth Camera                                | Enhance 3D understanding of surroundings; Improve elevation change detection | 3D CNNs; PointNet variants                          |

14

![14_image_0.png](14_image_0.png)

the network, allowing for real-time obstacle detection ( Othmani, 2022 ;
Masita et al., 2020 ; Mohamed et al., 2020 ). RNNs, designed for sequential data, utilize their memory feature to process time-series data small or overlapping objects ( Strbac et al., 2020 ; Sarda et al., 2021 ;
´orovi´c et al., 2018 ; Zhao et al., 2019 ; Terven and Cordova-Esparza, 2023 ; A. N and U. S. V, 2021 ). These algorithms collectively enhance obstacle detection and navigation in AVs, showcasing their potential in this domain. GANs and YOLO are instrumental in generating and detecting real-time images, respectively, essential for immediate obstacle identification. Siamese Neural Networks, effective at input comparison, are key in distinguishing obstacles from non-obstacles, enhancing the AV's response accuracy. ViTs, employing self-attention, efficiently detect irregular or small obstacles, crucial for comprehensive environmental perception. EfficientNets, balancing accuracy and computational efficiency, are integral in maintaining real-time processing in AV systems. DETR and AEs further contribute to object detection and data noise reduction, respectively, refining the overall sensory interpretation ( Tang et al., 2021 ; Wang et al., 2022b ; Mujkic et al., 2022 ). These algorithms' diverse and impactful roles are detailed in Table 18 and the subsequent subsections.

## 4.1. Transformer Networks

Introduced by Vaswani et al., the Transformer neural network is a pioneering architecture, specifically designed for intricate sequential data interpretation (Vaswani et al., 2017). Their application in adaptive obstacle detection in AVs is particularly notable, handling large volumes of sensor-fused data efficiently (Yuan et al., 2022). These networks stand out with their unique self-attention and multi-head attention mechanisms, enabling them to unravel intricate relationships within input sequences, thereby enhancing obstacle detection accuracy in dynamic driving conditions (Hu et al., 2022; Zhang et al., 2023b). A key advantage of Transformers over traditional RNNs and LSTMs is their ability to process data in parallel rather than sequential processing. This feature is crucial for AVs, providing a speed advantage essential for real-time decision-making in rapidly changing road scenarios. Transformers are highly scalable and flexible, capable of learning from extensive data and being employed in an end-to-end manner. This reduces the need for extensive pre-processing and feature engineering and allows them to 

| Table 18  Summary of different deep learning algorithms.  Algorithm Primary Characteristics   | Applications                                                                                                                                                      |                                                                             |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Convolutional  Neural Networks  (CNNs)                                                        | Image and video  recognition, autonomous  driving, medical imaging                                                                                                |                                                                             |
| Recurrent Neural                                                                              | Suited for sequential data as                                                                                                                                     | Natural language                                                            |
| Networks (RNNs)                                                                               | it has a "memory" effect                                                                                                                                          | processing, speech  recognition, time series  prediction                    |
| Long Short-Term                                                                               | A type of RNN that mitigates                                                                                                                                      |                                                                             |
| Memory (LSTM)                                                                                 | the "vanishing gradient"  problem, allowing it to learn  long sequences  Excellent for image  recognition tasks, uses  convolution operation to  extract features | Text generation, machine  translation, time series  analysis                |
| Generative  Adversarial  Networks (GANs)                                                      | Image generation, superresolution, image-to-image  translation                                                                                                                                                                   |                                                                             |
| You Only Look                                                                                 | Real-time object detection                                                                                                                                        |                                                                             |
| Once (YOLO)                                                                                   | system that recognizes  multiple objects in a single  glance  Consists of two networks  competing against each other  to improve results                          | Object detection in images,  video recognition,  autonomous driving         |
| Siamese Neural                                                                                | Learns to differentiate                                                                                                                                           |                                                                             |
| Networks                                                                                      | between two inputs;  excellent for tasks that  involve comparing  similarities or differences                                                                     | One-shot learning, face  recognition, signature  verification               |
| Transformers                                                                                  | Uses attention mechanisms  that weigh the significance of  different elements in the  input data                                                                  | Machine translation, text  summarization, speech  recognition               |
| Capsule Networks                                                                              | Uses dynamic routing to                                                                                                                                           |                                                                             |
| (CapsNet)                                                                                     | model hierarchical  relationships in data                                                                                                                         | Object segmentation, image  recognition, pose  estimation                   |
| Vision  Transformers  (ViT)                                                                   | Applies transformer  architectures to visual data,  representing an image as a  sequence of patches                                                               | Image recognition,  computer vision tasks                                   |
| EfficientNets                                                                                 | Uses a scaling method that  uniformly scales all  dimensions of depth/width/  resolution using a simple yet  effective compound  coefficient                      | Image classification, object  detection, transfer learning                  |
| DETR (DEtection                                                                               | Directly predicts the final set                                                                                                                                   |                                                                             |
| TRansformer)                                                                                  | of detections, eliminating the  need for complex anchor or  proposal systems                                                                                      | Object detection, panoptic  segmentation                                    |
| Deep Belief                                                                                   | Generative deep learning                                                                                                                                          |                                                                             |
| Networks (DBN)                                                                                | model composed of multiple  layers of latent variables                                                                                                            | Image recognition, motion  capture data classification,  document retrieval |
| Autoencoders (AE)                                                                             | Self-supervised learning  method used for learning  efficient codings of the input  data                                                                          | Dimensionality reduction,  anomaly detection,  denoising data               |

integrate diverse data types, like camera images and LiDAR point clouds, for a comprehensive environmental understanding. Despite their advantages, Transformers' computational intensity can be a constraint in resource-limited settings. This challenge demands ongoing research to develop more efficient Transformer variants, optimizing their application in AVs for enhanced real-time, adaptive obstacle detection. 

## 4.2. Generative Adversarial Networks (Gans)

In 2014, Goodfellow et al. introduced Generative Adversarial Networks (GANs) (Xie et al., 2021). GANs hold significant potential for improving the development and functionality of AV by generating realistic synthetic data, essential for training DL models (Menke et al., 2022). They provide an efficient solution to the challenges of collecting and annotating extensive real-world driving data, creating diverse traffic scenarios for comprehensive AV system training. In sensor data processing, GANs facilitate the conversion of complex inputs into more interpretable formats, improving AV systems' environmental understanding. For obstacle detection, GANs enrich training datasets with varied obstacle representations under different conditions, enhancing the robustness of detection systems. This capability improves detection accuracy and reliability. 

## 4.3. Spatial Pyramid Pooling Networks (Spp-Net)

SPP-nets represent a major advancement in AV technology, enabling CNNs to process images of varying sizes (Dewi et al., 2020). Traditional CNNs require fixed-size input images where sensor-captured scenes vary widely. SPP-nets overcome this by introducing a pooling layer that converts feature maps of any size into a fixed-length representation, preserving the original aspect ratios of input images (Wang et al., 2020). 

This capability is crucial in AV for maintaining accurate spatial relationships in a scene, such as the distances between obstacles, vital for safe navigation. SPP-nets generate fixed-size outputs from varied input sizes, allowing seamless integration with fully connected layers for crucial classification or regression tasks in complex driving scenarios 
(Park et al., 2018b). SPP-nets facilitate the conversion of diverse sensor data into standardized feature representations, enhancing the effectiveness of data integration. This leads to a more complete and coherent perception of the environment. In obstacle detection, SPP-nets effectively manage objects of different sizes and aspect ratios in the input images, which is crucial for recognizing potential hazards like pedestrians, vehicles, or unforeseen road obstructions. These networks preserve the hierarchical spatial relationships of objects, thereby enhancing the accuracy of object localization and classification. This ensures that autonomous vehicles respond correctly to dynamic and unpredictable road conditions. Fig. 19 depicts the architecture of an SPP-net. 

## 4.4. Single Shot Multibox Detector (Ssd)

The Single Shot Multibox Detector (SSD) algorithm plays a pivotal role in AVs due to its ability to detect objects in real time with high accuracy. Its unique approach, which involves performing detection in a single forward pass, eliminates the need for a separate region proposal phase, traditionally a bottleneck in the detection process. This efficiency is crucial in autonomous driving, where rapid response to environmental changes is vital for safety. The MultiBox feature of the SSD enables it to predict a variety of bounding box shapes and sizes at each feature map location, catering to the wide range of object sizes and aspect ratios found in driving scenarios, from distant pedestrians to large vehicles in close proximity. This adaptability is essential for coping with the variability of real-world scenes. The architecture of the SSD is specifically designed to fulfil the unique demands of real-time, accurate, and efficient object detection in AVs, making it a key component in obstacle detection and navigation (Xu et al., 2021). Its ongoing development holds promise for further enhancing its robustness and effectiveness in 

![16_image_0.png](16_image_0.png)

AV navigation. Fig. 20 provides a visual representation of the SSD
architecture.

## 4.5. Deep Belief Networks (Dbns)

DBNs, a class of generative probabilistic models with multiple layers of stochastic variables, are integral in AV ( Iftikhar et al., 2022 ). Their ability to learn complex data representations is crucial for AVs, which process high-dimensional and noisy sensory inputs ( Dairi et al., 2018 ). DBNs efficiently encode raw sensory data into compact, abstract representations, reducing dimensionality and emphasizing salient features. This aids in simplifying decision-making and control tasks in AVs, such as identifying critical road features for safe driving decisions. The probabilistic nature of DBNs equips them to manage sensor data uncertainty and noise, ensuring robust and reliable perception under various conditions. Recent advancements have merged DBNs with other sensor data like LiDAR and RADAR, enhancing obstacle detection and classification capabilities ( Bayoudh et al., 2021 ). This fusion provides a comprehensive environmental understanding, crucial for AV safety and efficiency. Overall, DBNs' contribution to AV obstacle detection is significant, offering a potent approach to complex sensor data processing.

Fig. 21 illustrates DBNs' structure and functionality.

## 4.6. Autoencoders (Aes)

Autoencoders (AEs) are neural network architectures with an encoder-decoder framework plays an essential role in AVs for their capability to learn efficient data representations ( Park et al., 2018a ).

They compress high-dimensional data into a lower-dimensional latent space, markedly reducing both data volume and computational demands, which is crucial for real-time AV systems. AEs retain critical information from input data, ensuring that important features like

![16_image_1.png](16_image_1.png)

ntworks
2. Visual Fig. ( AlGhamdi, 2023 ).

representation

![16_image_2.png](16_image_2.png)

vehicle positions and pedestrian locations are preserved despite the reduced dimensionality. This is vital for the safe navigation of AVs. Along with this, utilizing AEs in AVs is a strategic method for managing complex, high-dimensional, and noisy data, which is indispensable for effective operation. Variational Autoencoders (VAEs), a variant of AEs, incorporate probabilistic aspects into autoencoding (Azzalini et al., 
2021; Jagadish et al., 2021; Azizpour et al., 2020). This is particularly useful for generating new data, such as training data for simulating environments in AV robustness testing. The integration of AEs with CNNs and RNNs in AVs harnesses their combined strengths: AEs for data compression, CNNs for spatial pattern recognition, and RNNs for processing sequential data and capturing temporal dependencies. This combination creates a powerful system that enhances the vehicle's real-time data processing and decision-making capabilities. Fig. 22 provides a visual representation of an AE model, illustrating its symmetrical encoder and decoder structures, with "X" representing the input and "X^" the reconstructed output. 

## 4.7. Detection Transformer (Detr)

DETR (DEtection TRansformer) is a novel, end-to-end trainable architecture for object detection in AVs, notable for its simplicity and efficiency, as depicted in Fig. 23. It eliminates the need for complex components such as region proposals and non-maximum suppression, which are common in traditional models. This streamlining enables faster and more efficient visual data processing, crucial for real-time decision-making in dynamic AV environments. DETR employs a global attention mechanism to consider the entire scene, improving object detection, especially in complex environments like busy urban areas. 

Additionally, DETR is versatile, extending its capabilities to tasks like instance segmentation, providing detailed environmental understanding essential for safe AV navigation. Its architecture also enhances interpretability, a key factor in AV development and compliance with safety standards, by facilitating easier traceability of model decisions (Chromiak, 2021). DETR's approach represents a significant advancement in object detection technology for autonomous driving applications. 

Vision Transformers (ViT) are becoming increasingly important in AV systems for their ability to encode long-range spatial dependencies in visual data, essential for navigating complex environments (Kang et al., 
2022). Their self-attention mechanism enables the model to assess the significance of various parts of an input image, regardless of their spatial proximity. This allows AVs to recognize distant pedestrians as crucial as closer ones, providing a level of global context awareness that traditional CNNs, with their local receptive fields, find challenging 
(El-Ghamry et al., 2023). The parallel processing capability of ViTs, enhancing training efficiency, is another significant advantage (Diaz-Chito et al., 2016). AV systems necessitate training on large, 

![17_image_1.png](17_image_1.png)

![17_image_0.png](17_image_0.png)

high-resolution datasets to safely navigate diverse scenarios. ViTs' parallelization capacity allows for more efficient processing of these datasets compared to CNNs, potentially accelerating and economizing model training. Addressing the computational demands of ViTs during real-time processing is crucial in autonomous driving. Advancements in dedicated AI hardware accelerators are mitigating this challenge, enabling efficient operation of complex models like ViTs in vehicles (Xu et al., 2022a). Additionally, ViTs' ability to integrate multimodal data makes them well-suited for AV applications (Singh, 2023). Fig. 24 illustrates the ViTs model. 

## 4.8. Siamese Neural Networks(Snns)

SNNs are pivotal in the AV industry, excelling in similarity comparison tasks like object tracking and detection (Nandy et al., 2020). In autonomous driving, they compare sensory input data, like camera images or LIDAR point clouds, against established references, enhancing context-aware understanding of surroundings. For instance, SNNs effectively track objects within a scene, adapting to appearance changes or occlusions by comparing new inputs with previous references (Luo et al., 2022). This function is critical in dynamic urban environments for consistent object identification and safe navigation. Utilizing a twin-like structure, SNNs differentiate between similar and dissimilar pairs, producing embeddings where similar objects are closely aligned in the embedded space (Hayale et al., 2023). This ability is crucial for distinguishing between superficially similar but functionally distinct objects, such as differentiating between stationary and merging vehicles. 

The development of advanced variants like triplet networks, which compare an anchor input with both similar and dissimilar inputs, further enhances differentiation learning (Serrano et al., 2023). These advancements are driving richer environmental understanding and improved obstacle detection for AVs. Fig. 25 provides a visual representation of the SNNs model. 

![18_image_0.png](18_image_0.png)

5. **Deep learning techniques incorporating sensor fusion for** 

## Obstacle Detection 5.1. Data Pre-Processing

Following the multifaceted data collection from diverse sensors in 

![18_image_1.png](18_image_1.png)

autonomous vehicles, a meticulous data preprocessing sequence is essential to refine the raw inputs for enhanced perception and decisionmaking capabilities. This sequence commences with the data cleaning stage, a critical process aimed at rectifying cluttered and noisy data through noise reduction techniques such as Gaussian and median filtering, effectively minimizing random noise. Statistical methods further aid in outlier detection and removal, thus preparing the dataset for subsequent stages (Qi et al., 2020). 

Calibration procedures are then undertaken to reconcile the data from various sensors to a uniform physical frame of reference, crucial for mitigating discrepancies and ensuring data integrity. The data fusion phase encompasses temporal and spatial alignment, synchronizing data streams to a common timeframe and transforming disparate data to a unified coordinate system. Techniques like Kalman or particle filtering are then employed to synthesize the cleaned data, enhancing the overall situational awareness through a composite environmental representation (Chen et al). For example, the spatial precision of LiDAR data is enriched with the colour depth from cameras, culminating in a richer data mosaic. The subsequent feature engineering stage involves the extraction of relevant features imperative for tasks such as obstacle detection. This is accomplished through edge detection, texture analysis, and other such techniques. Dimensionality reduction methods like 

## 20

Principal Component Analysis (PCA) or Linear Discriminant Analysis (LDA) refine the feature set, retaining only those of utmost relevance, thereby optimizing computational efficiency and model performance (El-Ghamry et al., 2023; Diaz-Chito et al., 2016). Data augmentation techniques, including image flipping and rotation, supplement the dataset with varied perspectives, supporting the model's ability to generalize from the training data. Data formatting, the final step in the preprocessing pipeline, ensures that the dataset is aptly structured for the application of deep learning models. This encompasses normalization practices such as Min-Max scaling or Z-score normalization, which standardize feature scales, and data batching, which segments the data into optimal portions for the learning process (Abdennour et al., 2021). 5.2. *Sensor fusion technique and data combination for obstacle detection* Sensor fusion, an integral and complex component of AV development, plays a vital role in enhancing system robustness and dependability. The inception of multi-sensor data fusion is attributed to the Joint Directors of Laboratories (JDL) framework, which describes it as a complex, multi-level process encompassing the automated detection, association, correlation, estimation, and integration of data from multiple sources (White, 1991). Fig. 26 provides a cohesive environmental perception by integrating data from various sensors, such as cameras, RADARs, LiDAR, and ultrasonic devices. This harmonization is essential for creating a multidimensional understanding of the surroundings. The main advantage of sensor fusion is its ability to validate data from multiple sources, minimizing errors when, for example, a camera misinterprets distances in low visibility, while RADAR and LiDAR provide accurate measurements. 

The efficacy of sensor fusion is further demonstrated in diverse weather conditions. In fog, where visibility is low, and signal diffraction is significant, combining data from LiDAR, RADAR, and thermal cameras through advanced filtering and adaptive algorithms is critical for maintaining safety. Rainy conditions, which introduce reflection and scattering challenges, are countered by the use of LiDAR, RADAR, and weather sensors that employ adaptive methods for error correction, enhancing decision-making processes. Snow and wind present their unique obstacles, with snow causing occlusions and altering road textures, and wind affecting sensor noise and vibration. These are managed through multi-sensor calibration, dynamic thresholding, noise filtering, and robust estimation techniques to ensure stability and accurate vehicle control. Table 19 discusses the sensor fusion techniques used under various weather conditions. 

Sensor fusion techniques can be organized according to the origin of data, with multimodal fusion being a primary category. This technique combines data from various sensors to harness their collective strengths, significantly enhancing system capabilities beyond what any single sensor could achieve. This approach is critical for ensuring that the integration of data from diverse modalities addresses the limitations inherent in individual sensors. By prioritizing consistency in data alignment from various modalities, complementarity by diminishing uncertainties, and compatibility of algorithmic approaches, data structures, and specific tasks involved when integrating data from diverse modalities, multimodal fusion aims to produce outputs that are coherent, comprehensive, and highly reliable. Through such strategic data integration, systems become more accurate, robust, and adaptable, capable of delivering superior performance across a wide range of applications. 

Historically, sensor fusion relied on traditional methods such as Kalman filters and Bayesian networks, effective yet limited in adaptability, which has been detailed in Table 20 (Chen et al); Ounoughi and Yahia, 2023). However, with the advent of deep learning, a paradigm shift occurred, leading to more detailed obstacle understanding and improved adaptability in changing environments. Unlike traditional methods that follow set algorithms, deep learning-enabled systems learn from data, adapt to new scenarios, and improve over time. This adaptability makes them especially valuable in scenarios where the environment is constantly changing, like on busy roads with unpredictable elements. Sensor fusion strategies span from Early Fusion, integrating raw data at the start, to Late Fusion, combining processed data at the decision level, and Hybrid Fusion, which merges both strategies, as discussed in section 4.6. The comparison of sensor fusion strategies has been mentioned in Fig. 27. 

## 5.3. Deep Learning Based Sensor Fusion Technique For Obstacle Detection

As AVs continue to advance, the fusion of sensory data becomes increasingly complex and vital for accurate environmental perception and decision-making. Deep learning has emerged as a transformative force in this space, providing sophisticated methods to synthesize and interpret the diverse streams of data captured by an AV's array of sensors. These methods enable vehicles to transcend the limitations of individual sensors, offering a composite and detailed understanding of the surroundings that is crucial for safe navigation. For instance, CNNs excel in interpreting visual data from cameras, while RNNs and LSTMs process sequential data from RADAR and LiDAR, making sense of temporal sequences and spatial contexts (Shin and Su, 2020). Fusion strategies are chosen based on the requirement, with some models employing early fusion to integrate raw data at the start of the processing pipeline, others using late fusion to combine insights after individual processing, and still others utilizing a hybrid approach to benefit from both strategies. In the context of AVs, Z. Huang et al.'s research presents a deep neural network model that performs early fusion by taking visual and depth data to provide a detailed semantic segmentation for scene understanding, alongside controlling vehicle actions like steering and speed. 

The model's success in simulated urban environments demonstrates its potential, achieving a significant success rate in static navigation tasks and outperforming existing benchmarks (Huang et al., 2022). Arnav Vaibhav Malawade's work introduces "HydraFusion", an innovative context-aware sensor fusion technique that selectively integrates sensor data, considering the driving context to enhance the robustness of AV perception systems. This method optimizes the use of computational resources on energy-constrained AV platforms, demonstrating its practical applicability on an industry-standard hardware platform and showcasing improved performance in real-world conditions (Malawade et al., 2022). Fig. 27 illustrates a comparison of results obtained from individual sensors followed by those obtained through HydraFusion. 

Table 21 provides a succinct overview of deep learning fusion techniques, their key features, and applications in the realm of AV 
technology. 

The transformative impact of sensor fusion on AV functions is outlined in Table 22. It presents the positive effects and potential drawbacks of sensor fusion across various AV functions, such as object detection, collision avoidance, adaptive speed control, navigation, mapping, human-machine interaction, traffic sign recognition, lane keeping, and vehicle-to-vehicle (V2V) & vehicle-to-infrastructure (V2I) communication. Each function involves different sensor combinations, highlighting the complexity and multifaceted nature of sensor fusion within the AV 
landscape. 

Continuing the discourse on deep learning in AVs, the performance of sensor fusion techniques is critically appraised using specific evaluation metrics. These metrics are indispensable for assessing the accuracy and reliability of obstacle detection systems, which are central to the safety and functionality of AVs. Table 23 delineates these key evaluation metrics, starting with the Intersection over Union (IoU), which quantifies the accuracy of the obstacle localization by measuring the overlap between predicted and actual bounding boxes. precision and recall are fundamental metrics that respectively measure the correctness of positive predictions and the system's capacity to detect all actual obstacles. 

The Mean Average Precision (mAP) provides a comprehensive performance indicator by averaging the precision across all categories of obstacles, offering an overall effectiveness score of the detection system. 

![20_image_0.png](20_image_0.png)

![20_image_2.png](20_image_2.png)

l l

![20_image_4.png](20_image_4.png)

![20_image_5.png](20_image_5.png)

Fig. 26. Sensor fusion process
Different sensors and their data inputs Actionable Input : Navigate or avoid based on obstacle analysis

![20_image_1.png](20_image_1.png)

Obtain Data: Sensors l acquire environmental data

![20_image_3.png](20_image_3.png)

Data Cleaning Dataset cleaning and refinement Data Clean-up: Filtering noise improves data accuracy Confirm detections and remove false Standardise Data: facilitates smooth inclusion Sync sensor data for consistency Create a combined dataset for analysis Decision Making & Output l l l l l l l l l l l l l l positives l l l l l l l l l l l l

| Table 19  Sensor fusion techniques in different weather conditions.  Weather Condition Challenging Factors   | Required Sensors                | Fusion Techniques        | Impact on AV Performance           |                                    |
|--------------------------------------------------------------------------------------------------------------|---------------------------------|--------------------------|------------------------------------|------------------------------------|
| Fog (Manjunatha et al., 2023)                                                                                | Reduced visibility, Diffraction | LIDAR, RADAR, Thermal    | Enhanced filtering, Adaptive       | Maintain safety and accuracy       |
| of signals                                                                                                   | Camera                          | algorithms               |                                    |                                    |
| Snow/Ice (de Araujo et al., 2023)                                                                            | Occlusion, Reflection, Altered  | LIDAR, RADAR, Thermal    | Multisensor calibration, Dynamic   | Ensure proper navigation and       |
| road texture                                                                                                 | Camera                          | thresholding             | control                            |                                    |
| Rain (Hasanujjaman et al., 2023)                                                                             | Reflection, Absorption,         | LIDAR, RADAR, Weather    | Weather-adaptive methods, Error    | Minimize false detections and      |
| Scattering                                                                                                   | sensors                         | correction               | optimize response                  |                                    |
| Sand/Dust Storm (Hasanujjaman                                                                                | Reduced visibility, Abrasion    | LIDAR, RADAR, Protective | Vision enhancement, Particle       | Maintain operability and safeguard |
| et al., 2023)                                                                                                | measures                        | filtering                | equipment                          |                                    |
| Wind (Zhang et al., 2023a)                                                                                   | Sensor noise, Vibration         | Anemometers, LIDAR,      | Noise filtering, Robust estimation | Stabilize control and enhance      |
| RADAR                                                                                                        | handling                        |                          |                                    |                                    |

| Overview of traditional sensor fusion approaches in AV (Fayyad et al., 2020).  Method Description Strengths   | Limitations                      | Typical Use                      | Fusion Level                       |                         |           |
|---------------------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------|------------------------------------|-------------------------|-----------|
| Statistical                                                                                                   | Apply statistical models to      | Unknown correlation handling;    | Restricted to linear models;       | Estimation Processes    | Low       |
| Techniques                                                                                                    | structure sensory data           | Tolerance                        | Computationally intense            |                         |           |
| Probabilistic                                                                                                 | Utilize probability for sensory  | Manages uncertainty; Handles     | Needs prior system model           | Estimation/             | Low to    |
| Strategies                                                                                                    | information                      | nonlinear systems                | knowledge                          | Classification          | Medium    |
| Knowledge-based                                                                                               | Emulate human-like               | Addresses Uncertainty; Manages   | Relies on specific expertise and   | Classification/Decision | Medium to |
| Models                                                                                                        | intelligence mechanisms          | nonlinear systems                | knowledge extraction               | Making                  | High      |
| Evidence                                                                                                      | Implement Dempster's             | Assesses uncertainty; Identifies | High computational needs; Assumes  | Decision Making         | High      |
| Reasoning                                                                                                     | combination mechanism            | conflicts                        | evidence                           |                         |           |
| Interval Analysis                                                                                             | Divides the operating space into | Guarantees integrity; Complex    | Discretizes space; Computationally | Estimation Processes    | Low       |
| Theory                                                                                                        | intervals                        | nonlinear system handling        | complex                            |                         |           |

![21_image_0.png](21_image_0.png)

These metrics collectively form the basis for a rigorous evaluation framework for AV obstacle detection capabilities. 

To train and validate these sophisticated detection models, a collection of diverse datasets is employed. PASCAL VOC 2007/2012 and Microsoft COCO are pivotal datasets for multi-class object recognition, providing a variety of scenarios to refine models for particular obstacle types and complexities encountered in the real world. Specialized datasets like KITTI and the Waymo Open Dataset offer extensive sensor data and realistic driving conditions that are integral to developing robust and adaptable obstacle detection models. ModelNet and SceneFlow contribute to the training process by focusing on 3D object recognition and depth perception, aiding models in predicting threedimensional object attributes and spatial relationships. Table 24 presents a comparison of these datasets, highlighting their unique characteristics and contributions to model training. This diverse array of datasets ensures that obstacle detection models are well-rounded and capable of performing reliably across a spectrum of real-world conditions and scenarios, ultimately contributing to the advancement of autonomous vehicle technologies. These datasets, combined with the deep learning techniques outlined earlier, form a comprehensive ecosystem for the development and evaluation of cutting-edge sensor fusion systems in AVs. 

## 6. **Challenges And Future Directions**

Future research trends in multi-sensor data processing for obstacle detection in AVs are expected to be diverse and multidisciplinary. To tackle these issues comprehensively, Table 25 explores the challenges 

| Table 21  Deep learning approaches for sensor fusion in AV.  Approach/  Primary Purpose  Components or   | Applications or                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                          |                                                                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Technique                                                                                                | or Mechanism                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Key Features                                                                             | Benefits                                                                                         |
| FusionNet (  Subramani  et al., 2021)                                                                    | also trustworthy and verifiable, paving the way for their widespread  adoption and enhanced performance in diverse conditions.  Emphasizing machine learning, future directions involve developing  automated calibration and synchronization of various sensors, employing techniques like unsupervised and reinforcement learning to mitigate  variance in sensor readings and temporal misalignments. This  advancement would enhance the accuracy and reliability of environment perception. To combat the influence of environmental changes,  research is likely to focus on deep learning models that are resilient to  variations in lighting and weather, leveraging transfer learning, domain  adaptation, and data augmentation to maintain consistent AV performance. This approach will aim to provide robustness against electronic  interference and the dynamism of driving scenarios. The issue of sensor  noise and outliers, which can lead to false detections and impact safety,  is another area for innovation. The integration of advanced statistical  models and artificial intelligence for outlier detection promises to refine  data interpretation, thereby reducing the occurrence of false positives  and negatives. Processing the high-dimensional data generated by AV  sensors in a timely manner remains a critical requirement. Future  research is likely to invest in edge computing, hardware optimization,  and efficient deep learning architectures to process massive data streams                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                          |                                                                                                  |
| Handles diverse  sensors like RGB,  LiDAR; Hierarchical  feature extraction &  data integration          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                          |                                                                                                  |
| Multi-modal  Neural  Networks (  Schneider  et al., 2017)                                                | Sensor Data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Convolutional                                                                            |                                                                                                  |
| Fusion                                                                                                   | Layers, Fusion  Layers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Processes multiple  data types  concurrently;  Captures peculiarities  of each data type |                                                                                                  |
| Sensor Fusion  Transformer (  Chitta et al.,  2022)                                                      | Multi-sensor  Data  Management                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Separate Initial  Layers, Fusion  Layers                                                 | Correlates data from  different sensors;  Handles sequential  data with positional  significance |
| Transfer  Learning (Li  et al., 2020)                                                                    | Inter-sensor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Self-attention,                                                                          |                                                                                                  |
| Relationships                                                                                            | Positional  Encodings  Depends on                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Benefits scenarios                                                                       |                                                                                                  |
| source model                                                                                             | with limited labelled  data; Speeds up  training & potentially  improves  performance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                          |                                                                                                  |
| GANs  (Generative  Adversarial  Networks) (Li  et al., 2023b)                                            | Domain  Knowledge  Transfer  Synthetic Sensor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Generator,                                                                               | Augments training                                                                                |
| Data Generation                                                                                          | Discriminator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | datasets; Ensures  high-quality  synthetic samples                                       |                                                                                                  |
| VAEs  (Variational  AutoEncoders) (Li  et al., 2023b)                                                                                                          | Table 23  Key Evaluation Metrics in Obstacle Detection using sensor fused data.  Evaluation Metrics Description  Intersection over Union  A quantification of the overlap between the actual and  (IoU)  predicted bounding boxes for obstacles, ranging from  0 to 1.  Predictions Categorizes detections into True Positives (TP), False  Negatives (FN), and False Positives (FP), with IoU  calculated for each bounding box.  Precision Reflects how often the detector's predictions about  obstacles were correct, also known as the positive  predictive value.  Recall Represents the system's ability to accurately detect the  obstacles that are verified as ground truth.  Precision x Recall Curve A graphical representation that contrasts recall against  precision, seeking a point as close to (1.0, 1.0) as  possible, representing both high recall and precision for  obstacle detection.  Average Precision (AP) Provides an aggregated measure of precision across 11  uniformly spaced recall points for obstacles, computed  through interpolation of the precision values above a  specific recall threshold.  Mean Average Precision  Averages the AP across all categories of obstacles  (mAP)  present within a dataset.  Average Orientation  Assesses the ability of obstacle detection systems in  Similarity (AOS)  pinpointing obstacles and estimating their 3D  orientation.  Mean IoU (mIoU) Derives an average IoU for each type of obstacle within  a category, defaulting to 1 if no overlap is found  between the predictions and ground truth coordinates. |                                                                                          |                                                                                                  |
| Produces compact  representations;  Generates new  samples & detects  anomalies                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                          |                                                                                                  |
| Attention  Mechanisms (  Paigwar et al.,  2019)                                                          | Data  Representation  & Generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Compression &  Generation  Mechanisms                                                    |                                                                                                  |
| Dynamic Input                                                                                            | Varies with                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Emphasizes on more                                                                       |                                                                                                  |
| Weighting                                                                                                | architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | pertinent sensors;  Adjusts based on  reliability or  relevance of sensors               |                                                                                                  |
| Autoencoders (  Ohashi et al.,  2021)                                                                    | Data  Dimensionality  Reduction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Bottleneck                                                                               | Reduces noise and                                                                                |
| Architecture                                                                                             | redundancy; Retains  crucial features for  obstacle detection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                          |                                                                                                  |
| and potential research directions in multi-sensor data processing for  AVs.  Key areas include the development of advanced sensor fusion algorithms leveraging machine learning to integrate data from various sensors more effectively, innovation in sensor technologies to enhance  detection capabilities, utilization of synthetic and augmented datasets  for robust model training, and the exploration of collaborative sensing  techniques for shared situational awareness. Additionally, focusing on  edge computing for real-time data processing and advancing model  explainability will ensure these systems are not only more efficient but                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                          |                                                                                                  |

| Table 22  Impact of sensor fusion on key autonomous vehicle functions.  AV Function Primary Sensors Involved   | Fusion Techniques          | Positive Impact            | Potential Drawbacks               |                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------|----------------------------|-----------------------------------|----------------------------------|
| Object Detection & Collision Avoidance (                                                                       | LIDAR, RADAR, Cameras      | Multisensor Integration    | Improved detection accuracy;      | Complexity; Cost                 |
| Kotur et al., 2021)                                                                                            | Real-time response         |                            |                                   |                                  |
| Adaptive Speed Control (Liu et al., 2023)                                                                      | RADAR, GPS, Cameras        | Predictive Algorithms      | Smooth speed adjustments; Fuel    | Computation overhead;            |
| efficiency                                                                                                     | Calibration needs          |                            |                                   |                                  |
| Navigation & Mapping (Yan et al., 2023)                                                                        | GPS, LIDAR, Inertial Units | Map Matching; SLAM         | Precise localization; Robust path | Need for frequent updates; Map   |
| planning                                                                                                       | accuracy                   |                            |                                   |                                  |
| Human-Machine Interaction (Ghorbel                                                                             | Cameras, Microphones       | Multimodal Fusion          | Intuitive interaction; Enhanced   | Privacy concerns; Integration    |
| et al., 2019)                                                                                                  | safety alerts              | challenges                 |                                   |                                  |
| Traffic Sign Recognition (Mu et al., 2015)                                                                     | Cameras, LIDAR, Optical    | Image Recognition; Machine | Accurate recognition and          | Dependence on clear visuals;     |
| Sensors                                                                                                        | Learning                   | compliance                 | Maintenance                       |                                  |
| Lane Keeping (Biparva et al., 2022)                                                                            | Cameras, LIDAR, RADAR      | Tracking Algorithms; PID   | Enhanced stability and control in | Sensitivity to lane markings;    |
| Control                                                                                                        | lane                       | Complexity                 |                                   |                                  |
| V2V & V2I Communication (Khan et al.,                                                                          | Various sensors, DSRC,     | Protocol Integration;      | Improved coordination and traffic | Security risks; Interoperability |
| 2022)                                                                                                          | Cellular networks          | Security measures          | efficiency                        | issues                           |

23

| Table 24  Comparison of diverse datasets for autonomous vehicle object detection.  Dataset Characteristics Contribution to Model  Training  PASCAL VOC  Comprises 20 categories Suitable for multi-class object  2007/2012  recognition, helps in finetuning models for specific  obstacle categories  Microsoft COCO Over 330K fully segmented  images from complex  everyday scenes  Rich dataset that offers realworld complexity, beneficial  for training models to handle  diverse scenarios  ImageNet Contains 14,197,122 images  organized into 21,841  subclasses  Extensive image collection for  generalized training, useful for  pre-training models in largescale visual recognition  KITTI Autonomous driving dataset  with 2D and 3D bounding  boxes of objects in urban  driving scenarios  Specialized for autonomous  driving; training on this  dataset imparts realistic urban  obstacle detection skills  SceneFlow Synthetic dataset with stereo  Provides controlled  image pairs  environments and stereo data,  allowing models to learn depth  perception and 3D  understanding  ModelNet Clean collection of 3D  Computer-Aided Designs  (CAD) models of objects  Suitable for 3D object  recognition and analysis,  assists models in  understanding and predicting  3D shapes and orientations  OutdoorScene 200 images primarily  designed to test detections of  highly occluded and  truncated objects  Offers challenges related to  occlusion and truncation,  honing the model's ability to  detect partially visible  obstacles  Sydney Urban  Collected by a Velodyne HDL64E LiDAR in Sydney  Provides LiDAR data, crucial  Objects  for spatial awareness and  object detection in AV  Waymo Open  High-resolution sensor data  Dataset  collected by Waymo selfdriving cars in diverse  conditions  Comprehensive real-world  driving data, enhances the  model's robustness and  adaptability to various driving  conditions   |
|---|

rapidly, reducing latency and enabling real-time applications critical to autonomous navigation. Finally, improving model transparency and reliability remains a key concern, with the black-box nature of deep learning models posing significant challenges to validation and trust. Efforts in Explainable AI (XAI) and formal verification techniques will be crucial in enhancing model interpretability and ensuring the safety of AV systems. Overall, the future of obstacle detection in AVs lies in a more integrated approach, where the synergy between various sensor data and machine learning technologies lead to more sophisticated, reliable, and transparent driving systems. This will involve the creation of comprehensive datasets and the development of advanced algorithms that can navigate the complexities of real-world driving environments. 

## 7. **Conclusion**

The combination of deep learning and multi-sensor fusion in AVs has significantly improved their ability to detect obstacles. This advancement has been crucial in making AVs safer and more reliable. However, several challenges still need to be addressed for these systems to function optimally in all conditions. One of the main issues is the ability of AVs to perform accurately in different environmental settings, such as low light or bad weather, which can affect sensor performance. Developing deep learning models that can adapt to these changes is essential for ensuring the reliability of AVs in various scenarios. Another challenge is dealing with sensor noise, which can lead to incorrect readings and affect the vehicle's decision-making process. Advanced algorithms that can filter out this noise and accurately interpret sensor data are crucial for the efficient operation of AVs. Moreover, the decision-making process of AVs needs to be transparent and understandable. As AVs are designed to make complex decisions, it is important that we can understand and trust how these decisions are made. This is where techniques like XAI 
come into play, helping to make the AI's decision process clearer and more interpretable for humans. In summary, while deep learning and sensor fusion have brought significant improvements to AV technology, further advancements are needed to enhance their adaptability, noise handling, and decision-making transparency. Overcoming these challenges will be key to fully realizing the potential of AVs in various fields, including transportation and robotics. 

## Funding Source

This work did not receive funding from any institute or organization. 

## Credit Authorship Contribution Statement

Abhishek Thakur: Writing - original draft, Methodology, Conceptualization. **Sudhansu Kumar Mishra:** Writing - review & editing, Supervision. 

## Declaration Of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

| Table 25  Detailed examination of challenges and future research directions in multi-sensor data processing.  Current Challenge Specific Problems Example Impact on AV  Potential Future   | Specific Proposed Techniques                                                               | Anticipated Outcome                                             |                                                                      |                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Performance                                                                                                                                                                                | Directions                                                                                 |                                                                 |                                                                      |                                                                                |
| Sensor Calibration and  Synchronization (Yeong  et al., 2021)                                                                                                                              | Improved data accuracy,  Reliable environment  perception                                  |                                                                 |                                                                      |                                                                                |
| Environmental Changes (                                                                                                                                                                    | Light variations, Weather                                                                  |                                                                 |                                                                      |                                                                                |
| Zhao et al., 2023)                                                                                                                                                                         | conditions, Electronic  interference  Variance in sensor  readings, Temporal  misalignment | Incorrect obstacle detection,  Unreliable environment  mapping  | Machine learning for                                                 | Unsupervised learning                                                          |
| automated calibration                                                                                                                                                                      | algorithms, Reinforcement  learning                                                        | Improved model  resilience, Consistent  performance             |                                                                      |                                                                                |
| Sensor Noise and Outliers (  Sinha and Papadakis,  2013)                                                                                                                                   | Reduced sensor data  reliability, Inconsistent  model performance                          | Deep learning models  resilient to  environmental changes       | Transfer learning, Domain  adaptation, Data  augmentation techniques | Accurate data  interpretation, Reduced  false detections                       |
| High-Dimensional Data  Processing (Lu et al.,  2021)                                                                                                                                       | Irregular data patterns,                                                                   | False positive/negative                                         |                                                                      |                                                                                |
| False data spikes                                                                                                                                                                          | obstacle detection, Reduced  safety and efficiency                                         | Noise reduction and                                             | Advanced statistical                                                 |                                                                                |
| outlier detection                                                                                                                                                                          | methods, AI-based outlier  detection                                                       | Improved processing  speed, Enable real-time  applications      |                                                                      |                                                                                |
| Model Transparency and  Reliability (Pang et al.,  2023)                                                                                                                                   | Massive data streams,  Resource-intensive  processing                                      | Slower processing times,  Reduced real-time operation  capacity | Efficient data processing  algorithms and  structures                | Edge computing, Hardware  acceleration, Efficient deep  learning architectures |
| Black-box nature of deep  learning models,  Difficulties in validation                                                                                                                     | Reduced trust in model  outputs, Impediments to  safety-critical decisionmaking                                                                                            | Model interpretability                                          | Explainable AI (XAI)                                                 |                                                                                |
| and validation                                                                                                                                                                             | methods, Formal verification  techniques                                                   | Enhanced model  transparency, Improved  safety and trust        |                                                                      |                                                                                |

## Data Availability

No data was used for the research described in the article. 

## Acknowledgement

This work did not receive funding from any institute or organization. 

References A, R., V, K., Subramanian, S.C., Rajamani, R., 2021. On using a low-density Flash LiDAR 
for road vehicle tracking. ASME. J. Dyn. Sys., Meas., Control 143 (8), 081002. https://doi.org/10.1115/1.4050255. August 2021. 

A. N and U. S. V, 2021. Custom based obstacle detection using yolo v3 for low flying drones. In: 2021 International Conference on Circuits, Controls and Communications 
(CCUBE), Bangalore, India, pp. 1–6. https://doi.org/10.1109/ 
CCUBE53681.2021.9702739. 

Abbas, Q., Ibrahim, M.E., Jaffar, M.A., 2019. A comprehensive review of recent advances on deep vision systems. Artif. Intell. Rev. 52 (1), 39–76. 

Abbasi, R., Bashir, A.K., Alyamani, H.J., Amin, F., Doh, J., Chen, J., 2022. LiDAR point cloud compression, processing and learning for autonomous driving. IEEE Trans. 

Intell. Transport. Syst. 24 (1), 962–979. 

Abdennour, N., Ouni, T., Amor, N.B., 2021. November. The importance of signal preprocessing for machine learning: the influence of Data scaling in a driver identity classification. In: 2021 IEEE/ACS 18th International Conference on Computer Systems and Applications (AICCSA). IEEE, pp. 1–6. 

Abu-Alrub, N.J., Rawashdeh, N.A., 2023. RADAR odometry for autonomous ground vehicles: a survey of methods and datasets. IEEE Transactions on Intelligent Vehicles,vol. 9 (3), 4275–4291. https://doi.org/10.1109/TIV.2023.3340513. 

Aggarwal, Alankrita, 2021. Mamta Mittal, Gopi Battineni, Generative adversarial network: an overview of theory and applications. International Journal of Information Management Data Insights 1 (1), 100004. ISSN 2667–0968. 

Ahmed, S., Huda, M.N., Rajbhandari, S., Saha, C., Elshaw, M., Kanarachos, S., 2019. 

Pedestrian and cyclist detection and intent estimation for autonomous vehicles: a survey. Appl. Sci. 9 (11), 2335. 

Ahmed, H.U., Huang, Y., Lu, P., Bridgelall, R., 2022. Technology developments and impacts of connected and autonomous vehicles: an overview. Smart Cities 5, 382–404. https://doi.org/10.3390/smartcities5010022. 

AlGhamdi, R., 2023. Mitotic nuclei segmentation and classification using chaotic butterfly optimization algorithm with deep learning on histopathology images. 

Biomimetics 8 (6), 474. 

Ali, R., Liu, R., He, Y., Nayyar, A., Qureshi, B., 2021. Systematic review of dynamic multi-object identification and localization: techniques and technologies. IEEE 
Access 9, 122924–122950. 

Altch´e, F., de La Fortelle, A., 2017. An LSTM network for highway trajectory prediction. 

In: 2017 IEEE 20th International Conference on Intelligent Transportation Systems 
(ITSC), Yokohama, Japan, pp. 353–359. https://doi.org/10.1109/ 
ITSC.2017.8317913. 

Anisha, A.M., Abdel-Aty, M., Abdelraouf, A., Islam, Z., Zheng, O., 2023. Automated vehicle to vehicle conflict analysis at signalized intersections by camera and LiDAR 
sensor fusion. Transport. Res. Rec. 2677 (5), 117–132. 

Antah, Hatta, 2021. F.; khoiry, M.A.; Abdul Maulud, K.N.; Abdullah, A. Perceived Usefulness of airborne LiDAR technology in road design and management: a review. 

Sustainability 11773, 13. https://doi.org/10.3390/su132111773. 

Azam, S., Munir, F., Sheri, A.M., Kim, J., Jeon, M., 2020. System, design and experimental validation of autonomous vehicle in an unconstrained environment. 

Sensors 20 (21), 5999. 

Azizpour, M., da Roza, F., Bajcinca, N., 2020. End-to-End autonomous driving controller using semantic segmentation and variational autoencoder. In: 2020 7th International Conference on Control, Decision and Information Technologies (CoDIT), Prague, Czech Republic, pp. 1075–1080. https://doi.org/10.1109/ 
CoDIT49905.2020.9263921. 

Azzalini, D., Bonali, L., Amigoni, F., 2021. A minimally supervised approach based on variational autoencoders for anomaly detection in autonomous robots. IEEE Rob. Autom. Lett. 6 (2), 2985–2992. https://doi.org/10.1109/LRA.2021.3062597. 

Babak, S.J., Hussain, S.A., Karakas, B., Cetin, S., 2017. Control of autonomous ground vehicles: a brief technical review. In: IOP Conference Series: Materials Science and Engineering, vol. 224. IOP Publishing, 012029. No. 1. 

Bae, S., Saxena, D., Nakhaei, A., Choi, C., Fujimura, K., Moura, S., 2020. Cooperationaware lane change maneuver in dense traffic based on model predictive control with recurrent neural network. In: 2020 American Control Conference (ACC), Denver, CO, 
USA, pp. 1209–1216. https://doi.org/10.23919/ACC45564.2020.9147837. 

Baer, D., 2014. The Making of Tesla: Invention, Betrayal, and the Birth of the Roadster. 

11 November. 

Bayoudh, K., Knani, R., Hamdaoui, F., Mtibaa, A., 2021. A survey on deep multimodal learning for computer vision: advances, trends, applications, and datasets. Vis. 

Comput. 38, 2939–2970. 

Biparva, M., Fern´andez-Llorca, D., Gonzalo, R.I., Tsotsos, J.K., 2022. Video action recognition for lane-change classification and prediction of surrounding vehicles. 

IEEE Transactions on Intelligent Vehicles 7 (3), 569–578. 

Burnett, K., Schoellig, A.P., Barfoot, T.D., 2021. Do we need to compensate for motion distortion and Doppler effects in spinning RADAR navigation? IEEE Rob. Autom. 

Lett. 6 (2), 771–778. https://doi.org/10.1109/LRA.2021.3052439. 

Butt, F.A., Chattha, J.N., Ahmad, J., Zia, M.U., Rizwan, M., Naqvi, I.H., 2022. On the integration of enabling wireless technologies and sensor fusion for next-generation connected and autonomous vehicles. IEEE Access 10, 14643–14668. 

Broedermann, T., Sakaridis, C., Dai, D. and Van Gool, L., HRFuser: A multi-resolution sensor fusion architecture for 2D object detection, 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC), Bilbao, Spain, 2023, pp. 4159-4166, doi: 10.1109/ITSC57777.2023.10422432. 

T. Chen, Y. Cai, L. Chen and X. Xu, Sideslip angle fusion estimation method of three-Axis autonomous vehicle based on composite model and adaptive cubature kalman filter, in IEEE Transactions on Transportation Electrification, doi: 10.1109/ TTE.2023.3263592. 

Chitta, K., Prakash, A., Jaeger, B., Yu, Z., Renz, K., Geiger, A., 2022. Transfuser: Imitation with transformer-based sensor fusion for autonomous driving. IEEE Transactions on Pattern Analysis and Machine Intelligence 45 (11), 12878–12895. https://doi.org/ 
10.1109/TPAMI.2022.3200245. 

Cho, Kyunghyun, Merri¨enboer, Bart Van, Gulcehre, Caglar, Bahdanau, Dzmitry, Bougares, Fethi, Schwenk, Holger, Bengio, Yoshua, 2014. Learning Phrase Representations Using Rnn Encoder-Decoder for Statistical Machine Translation arXiv preprint arXiv:1406.1078. 

Chromiak, M., 2021. Exploring recent advancements of transformer based architectures in computer vision. Selected Topics in Applied Computer Science 59–75. 

Cordts, M., Omran, M., Ramos, S., Rehfeld, T., Enzweiler, M., Benenson, R., Franke, U., 
Roth, S., Schiele, B., 2016. The cityscapes dataset for semantic urban scene understanding. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Las Vegas, NV, USA, pp. 3213–3223, 27–30. 

Corovi ´ ´c, A., Ili´c, V., Ðuri´c, S., Marijan, M., Pavkovi´c, B., 2018. The real-time detection of traffic participants using YOLO algorithm. In: 2018 26th Telecommunications Forum 
(TELFOR), Belgrade, Serbia, pp. 1–4. https://doi.org/10.1109/ 
TELFOR.2018.8611986. 

Dai, B., Xu, F., Cao, Y., Xu, Y., 2020. Hybrid sensing data fusion of cooperative perception for autonomous driving with augmented vehicular reality. IEEE Syst. J. 

15 (1), 1413–1422. 

Dairi, A., Harrou, F., Senouci, M., Sun, Y., 2018. Unsupervised obstacle detection in driving environments using deep-learning-based stereovision. Robot. Autonom. Syst. 

100, 287–301. 

Dargan, S., Kumar, M., Ayyagari, M.R., Kumar, G., 2020. A survey of deep learning and its applications: a new paradigm to machine learning. Arch. Comput. Methods Eng. 

27, 1071–1092. 

Dasgupta, K., Das, A., Das, S., Bhattacharya, U., Yogamani, S., 2022. Spatio-contextual deep network-based multimodal pedestrian detection for autonomous driving. IEEE 
Trans. Intell. Transport. Syst. 23 (9), 15940–15950. 

de Araujo, P.R.M., Elhabiby, M., Givigi, S., Noureldin, A., 2023. A novel method for land vehicle positioning: invariant kalman filters and deep-learning-based RADAR speed estimation. IEEE Transactions on Intelligent Vehicles, vol. 8, no. 9, pp. 4275-4286, doi: 10.1109/TIV.2023.3287790. 

Devi, N.B., Kavida, A.C., Murugan, R., 2022. Feature extraction and object detection using fast-convolutional neural network for remote sensing satellite image. Journal of the Indian Society of Remote Sensing 50 (6), 961–973. 

Dewi, C., Chen, R.-C., Tai, S.-K., 2020. Evaluation of robust spatial pyramid pooling based on convolutional neural network for traffic sign recognition system. Electronics 889, 9. https://doi.org/10.3390/electronics9060889. 

Diaz-Chito, K., Hern´andez-Sabat´e, A., Lopez, ´ A.M., 2016. A reduced feature set for driver head pose estimation. Appl. Soft Comput. 45, 98–107. 

Dulian, A., Murray, J.C., 2021. Exploiting latent representation of sparse semantic layers for improved short-term motion prediction with Capsule Networks. In: 2021 IEEE 
International Conference on Robotics and Automation (ICRA), Xi'an, China, pp. 8537–8543. https://doi.org/10.1109/ICRA48506.2021.9561467. 

El-Ghamry, A., Darwish, A., Hassanien, A.E., 2023. An optimized CNN-based intrusion detection system for reducing risks in smart farming. Internet of Things 22, 100709. 

Electrek, 2016. Tesla gets a new supplier for advanced RADAR system. Available at: 
https://electrek.co/2016/11/28/tesla-delphi-advanced-RADAR-system/. (Accessed 29 March 2024). 

Ertugrul, Ishak, Ulkir, Osman, 2020. Analysis of MEMS-IMU Navigation System Used in Autonomous Vehicles. https://doi.org/10.5772/intechopen.92985. 

Escamilla-Ambrosio, P.J., Lieven, N., 2005. Sensor fusion approaches to guideway and obstacle detection in the autotaxi system. In: 2005 7th International Conference on Information Fusion, vol. 2. IEEE, p. 7. 

Fahey, T., Islam, M., Gardi, A., Sabatini, R., 2021. Laser beam atmospheric propagation modelling for aerospace LIDAR applications. Atmosphere 918, 12. https://doi.org/ 
10.3390/atmos12070918. 

Fayyad, J., Jaradat, M.A., Gruyer, D., Najjaran, H., 2020. Deep learning sensor fusion for autonomous vehicle perception and localization: a review. Sensors 20 (15), 4220. 

Gannavaram V, T.K., Bejgam, R., 2021. Brief study and review on the next revolutionary autonomous vehicle technology. In: 2021 International Conference on Advance Computing and Innovative Technologies in Engineering (ICACITE), Greater Noida, India, pp. 34–37. https://doi.org/10.1109/ICACITE51222.2021.9404763. 

Gao, B., Lang, H., Ren, J., 2020. Stereo visual slam for autonomous vehicles: a review. In: 
2020 IEEE International Conference on Systems, Man, and Cybernetics (SMC), 
Toronto, ON, Canada, pp. 1316–1322. https://doi.org/10.1109/ 
SMC42975.2020.9283161. 

Gao, Y., et al., 2023. Joint optimization of depth and ego-motion for intelligent autonomous vehicles. IEEE Trans. Intell. Transport. Syst. 24 (7), 7390–7403. https:// 
doi.org/10.1109/TITS.2022.3159275. 

García, F., de la Escalera, A., Armingol, J.M., 2013. Enhanced obstacle detection based on Data Fusion for ADAS applications. In: 16th International IEEE Conference on Intelligent Transportation Systems (ITSC 2013). IEEE, pp. 1370–1375. 

Geng, K., Dong, G., Yin, G., Hu, J., 2020. Deep dual-modal traffic objects instance segmentation method using camera and LiDAR data for autonomous driving. Rem. 

Sens. 12 (20), 3274. 

Ghorbel, Agn`es, Ben Amor, Nader, Jallouli, Mohamed, 2019. A survey on different human-machine interactions used for controlling an electric wheelchair. Procedia Computer Science 159, 398–407. 

Ghosh, R., 2021. On-road vehicle detection in varying weather conditions using faster RCNN with several region proposal networks. Multimed Tools Appl 80, 25985–25999. 

https://doi.org/10.1007/s11042-021-10954-5. 

Hasanujjaman, M., Chowdhury, M.Z., Hossan, M.T., Jang, Y.M., 2023. Autonomous vehicle driving in harsh weather: adaptive fusion alignment modeling and analysis. 

Arabian J. Sci. Eng. 1–10. 

Hayale, W., Negi, P.S., Mahoor, M.H., 2023. Deep siamese neural networks for facial expression recognition in the wild. IEEE Transactions on Affective Computing 14 (2), 
1148–1158. https://doi.org/10.1109/TAFFC.2021.3077248, 1 April-June. 

Hu, Z., Zhang, Y., Xing, Y., Zhao, Y., Cao, D., Lv, C., 2022. Toward human-centered automated driving: a novel spatiotemporal vision transformer-enabled head tracker. 

IEEE Veh. Technol. Mag. 17 (4), 57–64. https://doi.org/10.1109/ 
MVT.2021.3140047. 

Huang, Z., Sun, P., Boukerche, A., 2022. Towards A practical pedestrian detection method for supporting autonomous driving. In: ICC 2022-IEEE International Conference on Communications, Seoul, Korea, Republic of, pp. 1506–1511. https:// 
doi.org/10.1109/ICC45855.2022.9839149. 

Ibrahim, M., Akhtar, N., Jalwana, M.A.A.K., Wise, M., Mian, A., 2021. High definition LiDAR mapping of perth CBD, 2021 digital image computing: techniques and applications (DICTA). Gold Coast, Australia 1–8. https://doi.org/10.1109/ 
DICTA52665.2021.9647060. 

Iftikhar, S., Zhang, Z., Asim, M., Muthanna, A., Koucheryavy, A., Abd El-Latif, A.A., 
2022. Deep learning-based pedestrian detection in autonomous vehicles: substantial issues and challenges. Electronics 3551, 11. https://doi.org/10.3390/ electronics11213551. 

Ignatious, Henry Alexander, Sayed, Hesham-El, Khan, Manzoor, 2022. An overview of sensors in Autonomous Vehicles. Procedia Computer Science 198, 736–741. https:// 
doi.org/10.1016/j.procs.2021.12.315. ISSN 1877-0509. 

Itu, R., Danescu, R., 2022. Part-based obstacle detection using a multiple output neural network. Sensors 4312, 22. https://doi.org/10.3390/s22124312. 

Jagadish, D.N., Chauhan, A., Mahto, L., 2021. Autonomous vehicle path prediction using conditional variational autoencoder networks. In: Karlapalem, K., et al. (Eds.), 
Advances in Knowledge Discovery and Data Mining. PAKDD 2021. Lecture Notes in Computer Science, vol. 12712. Springer, Cham. https://doi.org/10.1007/978-3-03075762-5_11. 

Jebamikyous, H.-H., Kashef, R., 2022. Autonomous vehicles perception (AVP) using deep learning: modeling, assessment, and challenges. IEEE Access 10, 10523–10535. 

https://doi.org/10.1109/ACCESS.2022.3144407. 

Jeong, Y., 2022. Interactive lane keeping system for autonomous vehicles using LSTMRNN considering driving environments. Sensors 22 (24), 9889. 

Jeong, Y., Kim, S., Yi, K., 2020. Surround vehicle motion prediction using LSTM-RNN for motion planning of autonomous vehicles at multi-lane turn intersections. In: IEEE 
Open Journal of Intelligent Transportation Systems, vol. 1, pp. 2–14. https://doi. 

org/10.1109/OJITS.2020.2965969. 

Juyal, A., Sharma, S., Matta, P., 2021. Traffic sign detection using deep learning techniques in autonomous vehicles. In: 2021 International Conference on Innovative Computing, Intelligent Communication and Smart Electrical Systems (ICSES), 
Chennai, India, pp. 1–7. https://doi.org/10.1109/ICSES52305.2021.9633959. 

Kalatian, Arash, Farooq, Bilal, 2022. A context-aware pedestrian trajectory prediction framework for automated vehicles, Transportation Research Part C: Emerging Technologies 134, 103453. https://doi.org/10.1016/j.trc.2021.103453. ISSN 0968090X. 

Kang, M., Lee, W., Hwang, K., Yoon, Y., 2022. Vision transformer for detecting critical situations and extracting functional scenario for automated vehicle safety assessment. Sustainability 9680, 14. https://doi.org/10.3390/su14159680. 

Khan, A.R., Jamlos, M.F., Osman, N., Ishak, M.I., Dzaharudin, F., Yeow, Y.K., Khairi, K. 

A., 2022. DSRC technology in vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) IoT system for intelligent transportation system (its): a review. Recent Trends in Mechatronics Towards Industry 4.0: Selected Articles from iM3F 2020, Malaysia 97–106. 

Khanum, A., Lee, C.Y., Yang, C.S., 2022. Deep-learning-based network for lane following in autonomous vehicles. Electronics 11 (19), 3084. 

Khanum, A., Lee, C.-Y., Yang, C.-S., 2023. Involvement of deep learning for vision sensorbased autonomous driving control: a review. IEEE Sensor. J. 23 (14), 15321–15341. 

https://doi.org/10.1109/JSEN.2023.3280959, 15 July15. 

Khayyam, H., Javadi, B., Jalili, M., Jazar, R.N., 2020. Artificial intelligence and internet of things for autonomous vehicles. In: Jazar, R., Dai, L. (Eds.), Nonlinear Approaches in Engineering Applications. Springer, Cham. https://doi.org/10.1007/978-3-03018963-1_2. 

Kim, B.-J., Lee, S.-B., 2022. Safety evaluation of autonomous vehicles for a comparative study of camera image distance information and dynamic characteristics measuring equipment. IEEE Access 10, 18486–18506. https://doi.org/10.1109/ 
ACCESS.2022.3151075. 

Kim, J., Han, D.S., Senouci, B., 2018. RADAR and vision sensor fusion for object detection in autonomous vehicle surroundings. In: 2018 Tenth International Conference on Ubiquitous and Future Networks (ICUFN). IEEE, pp. 76–78. 

Kim, K., Kim, J.S., Jeong, S., Park, J.H., Kim, H.K., 2021. Cybersecurity for autonomous vehicles: review of attacks and defense. Comput. Secur. 103, 102150. 

Koci´c, J., Joviˇci´c, N., Drndarevi´c, V., 2018. November. Sensors and sensor fusion in autonomous vehicles. In: 2018 26th Telecommunications Forum (TELFOR). IEEE, 
pp. 420–425. 

Kotur, M., Luki´c, N., Kruni´c, M., Lukaˇc, Z., ˇ 2021. May. Camera and LiDAR sensor fusion for 3D object tracking in a collision avoidance system. In: 2021 Zooming Innovation in Consumer Technologies Conference (ZINC). IEEE, pp. 198–202. 

Kroger, ¨ W., 2021. Automated vehicle driving: background and deduction of governance needs. J. Risk Res. 24 (1), 14–27. 

Lee, J., Lee, S.K., Yang, S.I., 2018. An ensemble method of cnn models for object detection. In: 2018 International Conference on Information and Communication Technology Convergence (ICTC). IEEE, pp. 898–901. 

Lei, Y., Tian, T., Jiang, B., Qi, F., Jia, F., Qu, Q., 2023. Research and application of the obstacle avoidance system for high-speed railway tunnel lining inspection train based on integrated 3D LiDAR and 2D camera machine vision technology. Appl. Sci. 

7689, 13. https://doi.org/10.3390/app13137689. 

Li, Y., Ibanez-Guzman, J., 2020. LiDAR for autonomous driving: the principles, challenges, and trends for automotive LiDAR and perception systems. IEEE Signal Process. Mag. 37 (4), 50–61. https://doi.org/10.1109/MSP.2020.2973615. 

Li, Y., Jha, D.K., Ray, A., Wettergren, T.A., 2015. Feature level sensor fusion for target detection in dynamic environments. In: Proceedings of the 2015 American Control Conference (ACC), Chicago, IL, USA, pp. 1–3. 

Li, F., Shirahama, K., Nisar, M.A., Huang, X., Grzegorzek, M., 2020. Deep transfer learning for time series data based on sensor modality classification. Sensors 20 (15), 4271. 

Li, G., Chi, X., Qu, X., 2023a. Depth estimation based on monocular camera sensors in autonomous vehicles: a self-supervised learning approach. Automot. Innov 6, 268–280. https://doi.org/10.1007/s42154-023-00223-6. 

Li, Y., Liu, F., Xing, L., He, Y., Dong, C., Yuan, C., Chen, J., Tong, L., 2023b. Data generation for connected and automated vehicle tests using deep learning models. Accid. Anal. Prev. 190, 107192. 

Likmeta, A., Metelli, A.M., Tirinzoni, A., Giol, R., Restelli, M., Romano, D., 2020. 

Combining reinforcement learning with rule-based controllers for transparent and general decision-making in autonomous driving. Robot. Autonom. Syst. 131, 103568. 

Lin, C., Guo, Y., Li, W., Liu, H., Wu, D., 2021. An automatic lane marking detection method with low-density roadside LiDAR data. IEEE Sensor. J. 21 (8), 10029–10038. https://doi.org/10.1109/JSEN.2021.3057999, 15 April15. 

Liu, B., Zhao, W., Sun, Q., 2017. Study of object detection based on Faster R-CNN. In: 
2017 Chinese Automation Congress (CAC). IEEE, pp. 6233–6236. 

Liu, O., Yuan, S., Li, Z., 2020. November. A survey on sensor technologies for unmanned ground vehicles. In: 2020 3rd International Conference on Unmanned Systems 
(ICUS). IEEE, pp. 638–645. 

Liu, W., Hua, M., Deng, Z., Meng, Z., Huang, Y., Hu, C., Song, S., Gao, L., Liu, C., 
Shuai, B., Khajepour, A., 2023. A systematic survey of control techniques and applications in connected and automated vehicles. IEEE Internet Things J. vol. 10, no. 24, pp. 21892-21916, doi: 10.1109/JIOT.2023.3307002. 

Lu, Y., Ma, H., Smart, E., Yu, H., 2021. Real-time performance-focused localization techniques for autonomous vehicle: a review. IEEE Trans. Intell. Transport. Syst. 23 
(7), 6082–6100. 

Luo, Y., Shen, H., Cao, X., et al., 2022. Conversion of Siamese networks to spiking neural networks for energy-efficient object tracking. Neural Comput & Applic 34, 9967–9982. https://doi.org/10.1007/s00521-022-06984-1. 

Lv, M., Tu, D., Tang, X., Liu, Y., Shen, S., 2021. Semantically guided multi-view stereo for dense 3D road mapping. In: 2021 IEEE International Conference on Robotics and Automation (ICRA), Xi'an, China, pp. 11189–11195. https://doi.org/10.1109/ 
ICRA48506.2021.9561077. 

Ma, D., 2022. Recent advances in deep learning based computer vision. In: 2022 International Conference on Computers, Information Processing and Advanced Education (CIPAE). IEEE, pp. 174–179. 

Ma, Y., Wang, Z., Yang, H., Yang, L., 2020. Artificial intelligence applications in the development of autonomous vehicles: a survey. IEEE/CAA Journal of Automatica Sinica 7 (2), 315–329. https://doi.org/10.1109/JAS.2020.1003021. 

Malawade, A.V., Mortlock, T., Al Faruque, M.A., 2022. HydraFusion: context-aware selective sensor fusion for robust and efficient autonomous vehicle perception. In: 2022 ACM/IEEE 13th International Conference on Cyber-Physical Systems (ICCPS), 
Milano, Italy, pp. 68–79. https://doi.org/10.1109/ICCPS54341.2022.00013. 

Mancini, M., Costante, G., Valigi, P., Ciarfuglia, T.A., 2016. Fast robust monocular depth estimation for obstacle detection with fully convolutional networks. In: 2016 IEEE/ RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 
pp. 4296–4303. 

Manjunatha, H., Pak, A., Filev, D., Tsiotras, P., 2023. KARNet: kalman filter augmented recurrent neural network for learning world models in autonomous driving tasks. 

arXiv preprint arXiv:2305 14644. 

Manoj, B.S., Puneeth, Y., Yuvaraj, S., 2023. Automated vehicle braking system and driver Health monitoring system using IOT technology. In: 2022 OPJU International Technology Conference on Emerging Technologies for Sustainable Development 
(OTCON), Raigarh, Chhattisgarh, India, pp. 1–6. https://doi.org/10.1109/ 
OTCON56053.2023.10113976. 

Masita, K.L., Hasan, A.N., Shongwe, T., 2020. Deep learning in object detection: a review. In: 2020 International Conference on Artificial Intelligence, Big Data, Computing and Data Communication Systems (icABCD). IEEE, pp. 1–11. 

Menke, M., Wenzel, T., Schwung, A., 2022. Improving GAN-based domain adaptation for object detection. In: 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC), Macau, China, pp. 3880–3885. https://doi.org/ 
10.1109/ITSC55140.2022.9922138. 

Mishra, S., et al., 2022. Localization of a smart infrastructure fisheye camera in a prior map for autonomous vehicles. In: 2022 International Conference on Robotics and Automation (ICRA), Philadelphia, PA, USA, pp. 5998–6004. https://doi.org/ 
10.1109/ICRA46639.2022.9811793. 

Modas, A., Sanchez-Matilla, R., Frossard, P., Cavallaro, A., 2020. Toward robust sensing for autonomous vehicles: an adversarial perspective. IEEE Signal Process. Mag. 37 
(4), 14–23. https://doi.org/10.1109/MSP.2020.2985363. 

Mohamed, S.A., Haghbayan, M.H., Westerlund, T., Heikkonen, J., Tenhunen, H., 
Plosila, J., 2019. A survey on odometry for autonomous navigation systems. IEEE 
Access 7, 97466–97486. 

Mohamed, I.S., Capitanelli, A., Mastrogiovanni, F., Rovetta, S., Zaccaria, R., 2020. 

Detection, localisation and tracking of pallets using machine learning techniques and 2D range data. Neural Comput. Appl. 32, 8811–8828. 

Mohammed, A.S., Amamou, A., Ayevide, F.K., Kelouwani, S., Agbossou, K., Zioui, N., 
2020. The perception system of intelligent ground vehicles in all weather conditions: a systematic literature review. Sensors 20 (22), 6532. 

Mostafa, T., Chowdhury, S.J., Rhaman, M.K., Alam, M.G.R., 2022. Occluded object detection for autonomous vehicles employing YOLOv5, YOLOX and faster R-CNN. In: 2022 IEEE 13th Annual Information Technology, Electronics and Mobile Communication Conference (IEMCON), Vancouver, BC, Canada, pp. 405–410. 

https://doi.org/10.1109/IEMCON56893.2022.9946565. 

Mu, G., Xinyu, Z., Deyi, L., Tianlei, Z., Lifeng, A., 2015. Traffic light detection and recognition for autonomous vehicles. J. China Univ. Posts Telecommun. 22 (1), 
50–56. 

Muhammad, K., Ullah, A., Lloret, J., Del Ser, J., de Albuquerque, V.H.C., 2020. Deep learning for safe autonomous driving: current challenges and future directions. IEEE 
Trans. Intell. Transport. Syst. 22 (7), 4316–4336. 

Mujkic, E., Philipsen, M.P., Moeslund, T.B., Christiansen, M.P., Ravn, O., 2022. Anomaly detection for agricultural vehicles using autoencoders. Sensors 3608, 22. https://doi. org/10.3390/s22103608. 

Murali, P.K., Kaboli, M., Dahiya, R., 2022. Intelligent in-vehicle interaction technologies. 

Advanced Intelligent Systems 4 (2), 2100122. 

Murthy, C.B., Hashmi, M.F., Bokde, N.D., Geem, Z.W., 2020. Investigations of object detection in images/videos using various deep learning techniques and embedded platforms—a comprehensive review. Applied sciences 10 (9), 3280. 

Nandy, A., Haldar, S., Banerjee, S., Mitra, S., 2020. A survey on applications of siamese neural networks in computer vision, 2020 international conference for emerging technology (INCET). Belgaum, India 1–5. https://doi.org/10.1109/ 
INCET49848.2020.9153977. 

Nesti, T., Boddana, S., Yaman, B., 2023. Ultra-sonic sensor based object detection for autonomous vehicles. In: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), Vancouver, BC, Canada, pp. 210–218. 

https://doi.org/10.1109/CVPRW59228.2023.00026. 

Norton, P., 2021. Autonorama: the Illusory Promise of High-Tech Driving. Island Press. OFweek, 2021. The ultra-rapid development of MEMS technology in the 21st century has made automobiles a hot spot for MEMS innovation. Available at: https://znyj.ofwee k.com/news/2021-12/ART-23002-8110-30543298.html. (Accessed 29 March 2024). 

Ohashi, K., Nakanishi, K., Sasaki, W., Yasui, Y., Ishii, S., 2021. Deep adversarial reinforcement learning with noise compensation by autoencoder. IEEE Access 9, 143901–143912. 

Ortiz, F.M., Sammarco, M., Costa, L.H.M., Detyniecki, M., 2022. Applications and services using vehicular exteroceptive sensors: a survey. IEEE Transactions on Intelligent Vehicles 8 (1), 949–969. 

Othmani, M., 2022. A vehicle detection and tracking method for traffic video based on faster R-CNN. Multimed Tools Appl 81, 28347–28365. https://doi.org/10.1007/ 
s11042-022-12715-4. 

Ounoughi, C., Yahia, S.B., 2023. Data fusion for ITS: a systematic literature review. Inf. 

Fusion 89, 267–291. 

Paigwar, A., Erkent, O., Wolf, C., Laugier, C., 2019. Attentional pointnet for 3d-object detection in point clouds. In: In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops, 0–0. 

Pang, Z., Chen, Z., Lu, J., Zhang, M., Feng, X., Chen, Y., Yang, S., Cao, Y., 2023. A survey of decision-making safety assessment methods for autonomous vehicles. IEEE Intelligent Transportation Systems Magazine, vol. 16, no. 1, pp. 74-103, doi: 10.1109/MITS.2023.3292511. 

Parekh, D., Poddar, N., Rajpurkar, A., Chahal, M., Kumar, N., Joshi, G.P., Cho, W., 2022. 

A review on autonomous vehicles: progress, methods and challenges. Electronics 11 
(14), 2162. 

Park, J., Cho, N., 2020. Collision avoidance of hexacopter UAV based on LiDAR data in dynamic environment. Remote Sens 975, 12. https://doi.org/10.3390/rs12060975. 

Park, S.H., Kim, B., Kang, C.M., Chung, C.C., Choi, J.W., 2018a. Sequence-to-Sequence prediction of vehicle trajectory via LSTM encoder-decoder architecture. In: 2018 IEEE Intelligent Vehicles Symposium (IV), Changshu, China, pp. 1672–1678. 

https://doi.org/10.1109/IVS.2018.8500658. 

Park, K., Kim, S., Sohn, K., 2018b. Unified multi-spectral pedestrian detection based on probabilistic fusion networks. Pattern Recogn. 80, 143–155. 

Pirhonen, J., Ojala, R., Kivek¨as, K., Vepsal ¨ ainen, ¨ J., Tammi, K., 2022. Brake light detection algorithm for predictive braking. Appl. Sci. 2804, 12. https://doi.org/ 10.3390/app12062804. 

Qi, X., Fu, W., An, P., Wu, B., Ma, J., 2020. Point cloud preprocessing on 3D LiDAR data for unmanned surface vehicle in marine environment. In: 2020 IEEE International Conference on Information Technology, Big Data and Artificial Intelligence (ICIBA), 
vol. 1. IEEE, pp. 983–990. 

Qian, Y., Feng, S., Hu, W., Wang, W., 2022. Obstacle avoidance planning of autonomous vehicles using deep reinforcement learning. Adv. Mech. Eng. 14 (12), 
16878132221139661. 

Rafique, A.A., Gochoo, M., Jalal, A., et al., 2023. Maximum entropy scaled super pixels segmentation for multi-object detection and scene recognition via deep belief network. Multimed Tools Appl 82, 13401–13430. https://doi.org/10.1007/s11042022-13717-y. 

Raj, T., Hashim, F.H., Huddin, A.B., Ibrahim, M.F., Hussain, A., 2020. A survey on LiDAR 
scanning mechanisms. Electronics 741, 9. https://doi.org/10.3390/ 
electronics9050741. 

Rashid, M., Khan, M.A., Sharif, M., Raza, M., Sarfraz, M.M., Afza, F., 2019. Object detection and classification: a joint selection and fusion strategy of deep convolutional neural network and SIFT point features. Multimed. Tool. Appl. 78, 15751–15777. 

Ravindran, R., Santora, M.J., Jamali, M.M., 2021. Multi-object detection and tracking, based on dnn, for autonomous vehicles: a review. IEEE Sensor. J. 21 (5), 5668–5677. 

https://doi.org/10.1109/JSEN.2020.3041615, 1 March1. 

Real-Moreno, O., Rodríguez-Quinonez, ˜ J.C., Sergiyenko, O., Flores-Fuentes, W., 
Mercorelli, P., Ramírez-Hernandez, ´ L.R., 2021. Obtaining object information from stereo vision system for autonomous vehicles. In: 2021 IEEE 30th International Symposium on Industrial Electronics (ISIE), Kyoto, Japan, pp. 1–6. https://doi.org/ 
10.1109/ISIE45552.2021.9576262. 

Rezaei, S., Gbadegoye, J., Masoud, N., Khojandi, A., 2023. May. A deep learning-based approach for vehicle motion prediction in autonomous driving. In: 2023 International Conference on Control, Automation and Diagnosis (ICCAD). IEEE, 
pp. 1–6. 

Sahoo, G.K., Das, S.K., Singh, P., 2023. Two layered gated recurrent stacked long shortterm memory networks for driver's behavior analysis. S¯adhan¯a 48, 75. https://doi. 

org/10.1007/s12046-023-02126-y. 

Saleh, K., Hossny, M., Nahavandi, S., 2017. Driving behavior classification based on sensor data fusion using LSTM recurrent neural networks. In: 2017 IEEE 20th International Conference on Intelligent Transportation Systems (ITSC), Yokohama, Japan, pp. 1–6. https://doi.org/10.1109/ITSC.2017.8317835. 

Sanil, N., Rakesh, V., Mallapur, R., Ahmed, M.R., 2020. Deep learning techniques for obstacle detection and avoidance in driverless cars. In: 2020 International Conference on Artificial Intelligence and Signal Processing (AISP). IEEE, pp. 1–4. 

Sarda, A., Dixit, S., Bhan, A., 2021. Object detection for autonomous driving using YOLO 
algorithm. In: 2021 2nd International Conference on Intelligent Engineering and Management (ICIEM), London, United Kingdom, pp. 447–451. https://doi.org/ 
10.1109/ICIEM51511.2021.9445365. 

Schneider, L., Jasch, M., Frohlich, ¨ B., Weber, T., Franke, U., Pollefeys, M., R¨atsch, M., 
2017. Multimodal neural networks: RGB-D for semantic segmentation and object detection. In: Image Analysis: 20th Scandinavian Conference, SCIA 2017, Tromsø, Norway, June 12–14, 2017, Proceedings, Part I 20. Springer International Publishing, pp. 98–109. 

Seel, T., Raisch, J., Schauer, T., 2014. IMU-based joint angle measurement for gait analysis. Sensors 14 (4), 6891–6909. 

SemiEngineering, 2022. RADAR for automotive: why do we need RADAR? Available at. 

https://semiengineering.com/RADAR-for-automotive-why-do-we-need-RADAR/. (Accessed 29 March 2024). 

Sengupta, S., Basak, S., Saikia, P., Paul, S., Tsalavoutis, V., Atiah, F., Ravi, V., Peters, A., 
2020. A review of deep learning with special emphasis on architectures, applications and recent trends. Knowl. Base Syst. 194, 105596. 

Serrano, N., Bellogín, A., 2023. Siamese neural networks in recommendation. Neural Comput & Applic 35, 13941–13953. https://doi.org/10.1007/s00521-023-08610-0. 

Severino, A., Curto, S., Barberi, S., Arena, F., Pau, G., 2021. Autonomous vehicles: an analysis both on their distinctiveness and the potential impact on urban transport systems. Appl. Sci. 3604, 11. https://doi.org/10.3390/app11083604. 

Shahian Jahromi, B., Tulabandhula, T., Cetin, S., 2019. Real-time hybrid multi-sensor fusion framework for perception in autonomous vehicles. Sensors 4357, 19. https:// 
doi.org/10.3390/s19204357. 

Shi, X., Wong, Y.D., Chai, C., Li, M.Z.-F., 2021. An automated machine learning 
(AutoML) method of risk prediction for decision-making of autonomous vehicles. 

IEEE Trans. Intell. Transport. Syst. 22 (11), 7145–7154. https://doi.org/10.1109/ 
TITS.2020.3002419. 

Shin, N., Su, Y., 2020. Computer Vision for Self Driving Cars Using Multi-Class Learning and Deep Learning. 

Singh, A., 2023. Training strategies for vision Transformers for object detection. In: 
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (Pp. 110–118). 

Sinha, A., Papadakis, P., 2013. Mind the gap: detection and traversability analysis of terrain gaps using LIDAR for safe robot navigation. Robotica 31 (7), 1085–1101. 

Song, X., Chen, K., Li, X., Sun, J., Hou, B., Cui, Y., Zhang, B., Xiong, G., Wang, Z., 2020. 

Pedestrian trajectory prediction based on deep convolutional LSTM network. IEEE 
Trans. Intell. Transport. Syst. 22 (6), 3285–3302. 

Song, Y., Hyun, S., Cheong, Y.G., 2021. Analysis of autoencoders for network intrusion detection. Sensors 21 (13), 4294. 

Stelzer, P., Strasser, A., Pannagger, P., Steger, C., Druml, N., 2020. Monitor for safetycritical mirror drivers of MEMS micro-scanning LiDAR systems. In: 10th International Conference on Performance, Safety and Robustness in Complex Systems and Applications: PESARO, vol. 2020. IARIA, pp. 7–12. 

Strbac, B., Gostovic, M., Lukac, Z., Samardzija, D., 2020. YOLO multi-camera object detection and distance estimation, 2020 zooming innovation in consumer technologies conference (ZINC). Novi Sad, Serbia 26–30. https://doi.org/10.1109/ 
ZINC50678.2020.9161805. 

Subramani, P., Sattar, K.N.A., de Prado, R.P., Girirajan, B., Wozniak, M., 2021. Multiclassifier feature fusion-based road detection for connected autonomous vehicles. 

Appl. Sci. 11 (17), 7984. 

Sun, S., Petropulu, A.P., Poor, H.V., 2020. MIMO RADAR for advanced driver-assistance systems and autonomous driving: advantages and challenges. IEEE Signal Process. 

Mag. 37 (4), 98–117. 

Swaminathan, H.B., Sommer, A., Becker, A., Atzmueller, M., 2022. Performance evaluation of GNSS position augmentation methods for autonomous vehicles in urban environments. Sensors 8419, 22. https://doi.org/10.3390/s22218419. 

Tang, H., Wang, Y., Yuan, W., Sun, Y., 2021. An efficientnet based method for autonomous vehicles trajectory prediction, 2021 IEEE international conference on computer science, electronic information engineering and intelligent control technology (CEI). Fuzhou, China 18–21. https://doi.org/10.1109/ 
CEI52496.2021.9574480. 

Tang, Q., Liang, J., Zhu, F., 2023. A comparative review on multi-modal sensors fusion based on deep learning. Signal Process. 109165. 

Terven, J., Cordova-Esparza, D., 2023. A comprehensive review of YOLO: from YOLOv1 to YOLOv8 and beyond. Machine Learning and Knowledge Extraction 5 (4), 
1680–1716. https://doi.org/10.3390/make5040083. 

The Wall Street Journal, 2012. Google's driverless car draws political power. htt p://www.wsj.com/articles/Googles-Driverless-Car-Draws-Political-Power 
-20121012. (Accessed 29 March 2024). 

Tran, L.A., Le, M.H., 2019. Robust u-net-based road lane markings detection for autonomous driving. In: 2019 International Conference on System Science and Engineering (ICSSE). IEEE, pp. 62–66. 

Triki, Abdelaziz, 2021. Bassem Bouaziz, Jitendra Gaikwad, Walid Mahdi, Deep leaf: mask R-CNN based leaf detection and segmentation from digitized herbarium specimen images. Pattern Recogn. Lett. 150, 76–83. https://doi.org/10.1016/j. 

patrec.2021.07.003. ISSN 0167-8655. 

Uber, 2020. Under the hood of uber ATG's machine learning infrastructure and versioning control platform for self-driving vehicles. https://www.uber.com/en-IN/ 
blog/machine-learning-model-life-cycle-version-control. (Accessed 29 March 2024). 

Valeo. Valeo mobility kit. Available at. https://www.valeo.com/en/valeo-mobility-kit. 

(Accessed 29 March 2024). 

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., 
Polosukhin, I., 2017. Attention is all you need. Adv. Neural Inf. Process. Syst. 30. 

Vutla, Srinivasa Rao, Regalla, Srinivasa Prakash, Ramaswamy, Kannan, 2021. Life cycle assessment of cleanroom for micro-electro-mechanical systems fabrication with insights on sustainability. J. Clean. Prod. 282, 124520. https://doi.org/10.1016/j. jclepro.2020.124520. ISSN 0959-6526. 

Wang, X., Wang, S., Cao, J., Wang, Y., 2020. Data-driven based tiny-YOLOv3 method for front vehicle detection inducing SPP-net. IEEE Access 8, 110227–110236. https:// 
doi.org/10.1109/ACCESS.2020.3001279. 

Wang, C., Wang, X., Hu, H., et al., 2022a. On the application of cameras used in autonomous vehicles. Arch Computat Methods Eng 29, 4319–4339. https://doi.org/ 
10.1007/s11831-022-09741-8. 

Wang, D., Li, Z., Du, X., Ma, Z., Liu, X., 2022b. Farmland obstacle detection from the perspective of UAVs based on non-local deformable DETR. Agriculture 1983, 12. 

https://doi.org/10.3390/agriculture12121983. 

Waymo, 2018. Waymo safety report [Online]. Available. https://storage.googleapis. 

com/sdc-prod/v1/safetyreport/Safety%20Report%202018.pdf. Mar. 27, 2020. 

White, F.E., 1991. Data fusion lexicon. Joint Directors of Laboratories, Technical Panel for C 3, 19. 

Woodbridge, J., Anderson, H.S., Ahuja, A., Grant, D., 2018. Detecting homoglyph attacks with a siamese neural network. In: 2018 IEEE Security and Privacy Workshops 
(SPW). IEEE, pp. 22–28. 

World Health Organization, 2023. Road traffic mortality. https://www.who.int/data/ 
gho/data/themes/topics/sdg-target-3_6-road-traffic-injuries. (Accessed 29 March 2024). 

Wu, W., Huang, L., Chen, S., Bai, J., et al., 2021. Lane marking detection for highway scenes based on solid-state LiDARs. SAE Technical Paper. https://doi.org/10.4271/ 2021-01-7008, 2021-01-7008. 

Wu, Q., Li, X., Wang, K., Bilal, H., 2023. Regional feature fusion for on-road detection of objects using camera and 3D-LiDAR in high-speed autonomous vehicles. Soft Comput. 27 (23), 18195–18213. 

Xia, X., Hashemi, E., Xiong, L., Khajepour, A., Xu, N., 2021. Autonomous vehicles sideslip angle estimation: single antenna GNSS/IMU fusion with observability analysis. IEEE 
Internet Things J. 8 (19), 14845–14859. https://doi.org/10.1109/ 
JIOT.2021.3072354, 1 Oct.1. 

Xie, G., Yang, L.T., Yang, Y., Luo, H., Li, R., Alazab, M., 2021. Threat analysis for automotive can networks: a gan model-based intrusion detection technique. IEEE 
Trans. Intell. Transport. Syst. 22 (7), 4467–4477. https://doi.org/10.1109/ 
TITS.2021.3055351. 

Xu, X., Zhao, J., Li, Y., Gao, H., Wang, X., 2021. BANet: a balanced atrous net improved from SSD for autonomous driving in smart transportation. IEEE Sensor. J. 21 (22), 
25018–25026. https://doi.org/10.1109/JSEN.2020.3034356, 15 Nov.15. 

Xu, R., Xiang, H., Tu, Z., Xia, X., Yang, M.H., Ma, J., 2022a. V2x-vit: vehicle-toeverything cooperative perception with vision transformer. In: European Conference on Computer Vision (Pp. 107–124). Cham: Springer Nature Switzerland. 

Xu, Y., Wei, H., Lin, M., Deng, Y., Sheng, K., Zhang, M., Tang, F., Dong, W., Huang, F., 
Xu, C., 2022b. Transformers in computational visual media: a survey. Computational Visual Media 8, 33–62. 

Yadav, S.K., Tiwari, K., Pandey, H.M., Akbar, S.A., 2021. A review of multimodal human activity recognition with special emphasis on classification, applications, challenges and future directions. Knowl. Base Syst. 223, 106970. 

Yan, Z., Zhang, C., Yang, Y., Liang, J., 2021. A novel in-motion alignment method based on trajectory matching for autonomous vehicles. IEEE Trans. Veh. Technol. 70 (3), 
2231–2238. https://doi.org/10.1109/TVT.2021.3058940. 

Yan, P., Wen, W., Hsu, L.T., 2023. Integration of vehicle dynamic model and system identification model for extending the navigation service under sensor failures. IEEE Transactions on Intelligent Vehicles, vol. 9, no. 1, pp. 2236-2248, doi: 10.1109/ 
TIV.2023.3273185. 

Yeong, D.J., Velasco-Hernandez, G., Barry, J., Walsh, J., 2021. Sensor and sensor fusion technology in autonomous vehicles: a review. Sensors 21 (6), 2140. 

Yoo, J.H., Kim, Y., Kim, J., Choi, J.W., 2020. 3d-cvf: generating joint camera and LiDAR 
features using cross-view spatial feature fusion for 3d object detection. In: Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XXVII 16. Springer International Publishing, pp. 720–736. 

Yu, X., Marinov, M., 2020. A study on recent developments and issues with obstacle detection systems for automated vehicles. Sustainability 12 (8), 3281. 

Yuan, J., Wang, H., Lin, C., Liu, D., Yu, D., 2019. A novel GRU-RNN network model for dynamic path planning of mobile robot. IEEE Access 7, 15140–15151. 

Yuan, Z., Song, X., Bai, L., Wang, Z., Ouyang, W., 2022. Temporal-Channel transformer for 3D LiDAR-based video object detection for autonomous driving. IEEE Trans. Circ. 

Syst. Video Technol. 32 (4), 2068–2078. https://doi.org/10.1109/ 
TCSVT.2021.3082763. 

Zaarane, Abdelmoghit, Slimani, Ibtissam, Al Okaishi, Wahban, Atouf, Issam, Hamdoun, Abdellatif, 2020. Distance measurement system for autonomous vehicles using stereo camera. Array ume 5, 100016. https://doi.org/10.1016/j. array.2020.100016. ISSN 2590-0056. 

Zhang, Z., Liang, Z., Zhang, M., Zhao, X., Li, H., Yang, M., Tan, W., Pu, S., 2021. 

RangeLVDet: boosting 3D object detection in LiDAR with range image and RGB 
image. IEEE Sensor. J. 22 (2), 1391–1403. 

Zhang, Y., Carballo, A., Yang, H., Takeda, K., 2023a. Perception and sensing for autonomous vehicles under adverse weather conditions: a survey. ISPRS J. 

Photogrammetry Remote Sens. 196, 146–177. 

Zhang, C., Zhang, C., Guo, Y., Chen, L., Happold, M., 2023b. MotionTrack: end-to-end transformer-based multi-object tracking with LiDAR-camera fusion. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (Pp. 

151–160). 

Zhao, Changyu, 2023. Hirotaka Uchitomi, Taiki Ogata, Xianwen Ming, Yoshihiro Miyake, Reducing the device complexity for 3D human pose estimation: a deep learning approach using monocular camera and IMUs,. Eng. Appl. Artif. Intell. 124, 106639. https://doi.org/10.1016/j.engappai.2023.106639. ISSN 0952-1976. 

Zhao, Z.-Q., Zheng, P., Xu, S.-T., Wu, X., 2019. Object detection with deep learning: a review, in IEEE Transactions on neural networks and learning systems, vol. 30, no 11, 3212–3232. https://doi.org/10.1109/TNNLS.2018.2876865. 

Zhao, X., Fang, Y., Min, H., Wu, X., Wang, W., Teixeira, R., 2023. Potential sources of sensor data anomalies for autonomous vehicles: an overview from road vehicle safety perspective. Expert Syst. Appl. 121358. 