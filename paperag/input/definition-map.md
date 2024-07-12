ARTICLE IN **PRESS**

![0_image_1.png](0_image_1.png)

JID: FMRE [m5GeSdc;July 1, 2024;10:0]
Fundamental Research xxx (xxxx) xxx Contents lists available at ScienceDirect

![0_image_0.png](0_image_0.png)

# Fundamental Research

journal homepage: http://www.keaipublishing.com/en/journals/fundamental-research/
Review Review and challenge: High definition map technology for intelligent connected vehicle Mengmeng Yanga,1, Kun Jianga, Benny Wijayaa,1, Tuopu Wena, Jinyu Miaoa, Jin Huanga, Cao Zhonga, Wei Zhang b, Huixian Chenc, Diange Yanga,∗
a School of Vehicle and Mobility, Tsinghua University, Beijing 100084, China b Ministry of Natural Resources, Beijing 100812, China c Map Supervision Center, Ministry of Natural Resources, Beijing 100830, *China* a r t i c l e i n f o Article *history:*
Received 3 April 2023 Received in revised form 9 January 2024 Accepted 9 January 2024 Available online xxx

| Keywords: High definition (HD) map Highly automated driving (HAD) map Digital map Intelligent connected vehicle (ICVs) Autonomous driving   |
|---------------------------------------------------------------------------------------------------------------------------------------------|

## 1. Introduction

As economies and societies evolve, maps have become an indispensable part of people's daily lives. People can effortlessly travel by following the navigation information to any destination planned by their map app on their smartphones. For ICVs, the map plays an even more critical role in localization, navigation, and many other core functions
[1]. Furthermore, different levels of autonomy require a different level of the map, as outlined in Table. 1. According to the definition of autonomy levels by SAE [2], for Level 1(L1)-Level 2(L2), where drivers still retains primary control of the vehicles while can function effectively with an Advanced Driver-Assistance System (ADAS) map offering sub-meter accuracy. These navigational maps are enough to assist drivers in performing the driving task correctly. However, as vehicles advance towards higher levels of automation, the need for more precise and accurate maps becomes imperative. For Level 4(L4) and Level 5(L5) autonomy, where the vehicle assumes most or all driving functions, a highly automated driving (HAD) map is paramount. These maps will provide detailed and critical information about the driving environment, enabling automated driving systems to react better than human drivers.

∗ Corresponding author. 1 These authors contributed equally to this work.

An accurate and up-to-date High Definition (HD) Map is critical for an intelligent vehicle to drive safely and effectively. Although research in this area is growing, there is still a lack of clarity in defining HD maps for intelligent connected vehicles (ICVs). This gap in knowledge is particularly challenging for new researchers, who often struggle to find suitable HD map datasets due to a lack of comprehensive reviews on current HD map products, as far as the authors' knowledge. Thus, this article aims to bridge this gap by providing a thorough analysis of the core ideas of HD map technology. Initially, this paper presents the brief history of HD map. Following this, it describes the taxonomy and ontology of HD maps, complete with the HD map contents and existing standards. An insight into the mapping process is also given by discussing the algorithms used for creating and updating HD maps. This manuscript also lists current HD map products and the open-sourced dataset available for interested researchers in this space. As part of this study, the authors also describe common applications of HAD maps in ICVs. Finally, the article highlight the key research challenges and potential future directions in this field. Addressing these challenges is vital for the advancement and integration of HD maps for ICVs.

HAD map contains plenty of road information, such as lanes, traffic lights, crosswalks, and more, offering essential prior knowledge for various core functions in automated driving. These include perception, positioning, decision-making, and control [1]. The primary application of the HAD map is facilitating high-precision vehicle localization.

Accurate localization and positioning are essential prerequisites for the safety and reliability of autonomous driving, enabling vehicles to make correct decisions and control themselves according to their perceived surroundings. The most commonly used method is the Global Navigation Satellite System (GNSS). However, GNSS often falls short in precision, which is critical to autonomous driving [3]. The localization performance further deteriorates when the vehicles go through areas with frequent signal loss, such as tunnels, or where elevation varies, like overpasses. Traditional high-precision localization methods, like Inertial Measurement Unit (IMU) or light detection and ranging (LiDAR)
sensors, are costly and not feasible for mass production due to budget constraints. Recent advancements in HAD mapping technology have enabled decimeter-level vehicle localization using low-cost sensors, such as cameras. It can be enhanced with the contextual information provided by HAD map [4].

https://doi.org/10.1016/j.fmre.2024.01.006 2667-3258/© 2024 The Authors. Publishing Services by Elsevier B.V. on behalf of KeAi Communications Co. Ltd. This is an open access article under the CC
BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/)

## A B S T R A C T

 

JID: FMRE [m5GeSdc;July 1, 2024;10:0]

| Automated driving level classification of SAE [2]. Level Title Description                           | Map                                                                                   | Precision                                                                                                                        | Necessity         |                  |                                          |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------|
| Driver scenario 1 (DA)                                                                               | Driving assistance                                                                    | The vehicle features a single automated system (e.g., it monitors speed through cruise control                                   | ADAS map          | Sub-meter level  | Optional                                 |
| 2 (PA)                                                                                               | Partial driving                                                                       | The vehicle can perform steering                                                                                                 |                   |                  |                                          |
| automation                                                                                           | and acceleration, the human still monitors all tasks and can take control at any time | ADAS map                                                                                                                         | Sub-meter level   | Optional         |                                          |
| Automated driving system ('system') scenario 3 (CA) Conditional driving The vehicle can perform most | ADAS map + HD map                                                                     | Sub-meter level,                                                                                                                 | Optional          |                  |                                          |
| automation                                                                                           | driving tasks, but human override                                                     | Centimeter level                                                                                                                 |                   |                  |                                          |
| is still required                                                                                    |                                                                                       |                                                                                                                                  |                   |                  |                                          |
| 4 (HA)                                                                                               | High driving automation                                                               | The vehicle performs all driving tasks under specific circumstances, geofencing is required, a human override is still an option | ADAS map + HD map | Sub-meter level, | Compulsory                               |
| Centimeter level                                                                                     |                                                                                       |                                                                                                                                  |                   |                  |                                          |
| 5 (FA)                                                                                               | Full driving automation                                                               | The vehicle performs all driving tasks under all conditions, zero human attention or interaction is required                     | HD map            | Centimeter level | Compulsory (Required real-time updating) |

The fundamental approach is to match the geometric features present in both the camera images and the map, which aids in inferring the vehicle position and orientation relative to the map. The key features for this process typically involve lane markings, traffic signs [5], or other semantic-level features [6]. To optimize memory usage, a compressed semantic HAD map could support high-precision localization while being resource-efficient [7]. The extensive information on lanes, traffic lights, crosswalks, and more stored in the HAD map acts as an additional sensor for environment perception. For example, it simplifies traffic light recognition by providing the light's location, type, and the road's slope, allowing for easy extraction of the region of interest (ROI) [8], and selection of an appropriate classifier [9]. 3D object detection also benefited from a HAD map through a bird's eye-view to enhance the understanding of surroundings [10]. Besides, the sensing range of the vehicle could be extended beyond the line of sight and field of view by fusing the vehicles' environmental information in the map, which could greatly improve perception capability [11]. HAD map is particularly useful in scenarios like dynamic visual occlusion, which may otherwise cause even cooperative perception to fail.

As they become more standardized, HAD maps can serve as a shared, real-time updated data structure among autonomous vehicles, effectively creating a crowdsourced solution. This comprehensive map data provides a reliable baseline for other onboard sensors. For example, a study [12] shows a multi-radar online self-calibration method using the precise locations of street lamps and traffic signs from the HAD map.

HAD maps are also instrumental in motion planning and decisionmaking. Initially, path planning utilized digital maps in platforms like Google and Baidu maps. However, HAD maps, with detailed information on road conditions, static objects, and traffic rules, offer more constraints for local motion planning and decision-making. They allow direct extraction of intersection geometries and real-time traffic situations for motion planning and control [13]. This was exemplified in the 2018 Intelligent Vehicles Future Challenge, where the 'Pioneer' team from Xi'an Jiangtong University, leveraging HD maps, won the championship
[14]. The team used the OpenStreetMap structure to build the map and generated a path set based on vehicle location, target points, lane states, and traffic rules from the HAD map. Overall, HAD maps play a vital role in localization, perception, navigation, motion planning, decisionmaking, and, ultimately, the safety of autonomous driving.

Numerous mapping enterprises and autonomous driving companies have showcased significant research and development in achieving full driving automation with the basis of the HAD map. Baidu, through its

![1_image_0.png](1_image_0.png)

Project Apollo has been leading the way among Asian companies in this direction. On their autonomous driving platform, the HAD map serves as a vital component, contributing to modules such as localization, perception, routing, motion planning, prediction, and vehicle control [1].

In September 2020, Baidu Apollo unveiled its Robotaxi, during a live broadcast at Beijing Shougang Industrial Park. This event marks the beginning of a new milestone in vehicle autonomy research. Similarly, Mobileye released an edited video depicting urban autonomous driving tests, which can be seen in Fig. 1. In one instance, a huge truck stopped in front of the vehicle and hindered it from perceiving frontal situations. Initially, the vehicle hesitated, unable to determine if the truck had stopped due to a red traffic light or other reasons. However, with the assistance of the HAD map, it was identified that the truck remained stationary even after the light turned green. Consequently. the vehicle successfully changed lanes to continue its path, without driver intervention.

Other notable companies like TomTom, Waymo,and Momenta have also dedicated efforts to develop HAD map. They have demonstrated remarkable achievements by integrating HAD maps into autonomous driving tasks.

While many research works have focused on addressing specific facets of autonomous driving with the HAD map as a potential solution, there is a notable gap in the literature concerning the comprehensive definition, historical development, classification, modeling, mapping processes, updates, and application of the HAD map. Consequently, this paper aims to comprehensively define the high-definition map and explore its updates and applications for autonomous driving. Furthermore, it will touch upon the ongoing challenges regarding the develop-
Fig. 2. The organizational structure of this survey HAD map.

ment of this technology. The framework of this paper is illustrated in Fig. 2.

1. A comprehensive survey of high definition map for the intelligent connected vehicle.

2. A forward look from the history, standardization, building, and maintenance to its application.

3. Comparison between standards, models, algorithms, and opensource datasets.

4. A list of the overall challenges for developing a high-definition map.

The structure of the remainder of the paper is organized as follows. Section 2 delves into the history of HAD maps. Section 3 discusses the definition, contents, classification, and mapping standard.

Section 5 briefly analyzes HAD map mapping, updates, products, and open-source map datasets. Section 6 explores the application of the HAD map, which consists of localization, cooperative perception, and intelligent decision-making. The prospective future development and challenges associated with the HAD map are written in Section 7. Section 7 draws conclusions based on current research.

## 2. Digital Map History

Initially, digital maps were used similarly to paper maps but were more portable [16]. Early digital maps offered a "virtual image" of roadways typically delineated by the landscape enclosing the surrounding area, which was essentially the same functionality as paper maps. Unlike most paper maps, digital maps are machine-readable. Digital maps allow quickly synchronizing changes from map data servers, representing the changing reality in real-time. The late 1900s enlarged the role of the digital map as digital maps increased along with the growth of Global Navigation Satellite Systems (GNSS). The old "virtual views" no longer make up the entire Navigation Digital Map. The Mazda Eunos Cosmo was the first automobile with an integrated Global Positioning System (GPS) and digital maps in 1990 [17]. Then, navigation digital maps were widely employed on automobiles to establish the vehicle's location, carry out map matching, compute routes, and provide drivers with directions. Their updating capability allows the inclusion of new roads and locations, enhancing their utility.

With time, digital map navigation has been refined to include live traffic updates, points of interest, and service locations, making them more 'user-friendly'. Modern computerized navigation maps boast an accuracy range of 5 to 20 meters in urban settings. The 2000s saw the advent of the Advanced Driving Assistance System (ADAS), incorporating
 

![2_image_0.png](2_image_0.png)

![2_image_1.png](2_image_1.png)

JID: FMRE [m5GeSdc;July 1, 2024;10:0]
basic warning and cruising features alongside the development of vehicle intelligence. This period also marked the introduction of ADAS maps, designed to support ADAS and autonomous driving [18,19]. ADAS maps enhance digital maps with more accurate road geometry, like road curvature and road slope, and richer road attributes, such as lane width, number of lanes, and speed limits, along with traffic signs and traffic lights, are all added by ADAS maps to the existing digital maps. Thus, ADAS maps extend beyond navigation, providing dynamic traffic data to bolster ADAS functionality and covering SAE's L1 and L2 levels of driving automation. The ADASIS Forum has established guidelines for ADAS Horizon and standardized map data interfaces like ADASISv1 and v2, with an accuracy of approximately 50 cm.

The concept of "high-definition map" idea was conceived in 2010 at a Mercedes-Benz research planning session. In 2013, a fully autonomous Mercedes Benz S-Class S 500 completed a 103 km journey on urban and country roads using high-resolution maps [20]. Designed to capture all relevant environmental variables for driving, which sensors alone might not accurately detect, HD maps introduced novel features for vehicle perception and localization.

These maps, offering 3D representations, integrate closely with localization functions and support the planning and control modules. Beyond mere navigation aids, they are pivotal for high-level automated driving (SAE L3 and above), hence the term High Automated Driving (HAD) Map. HAD Maps encompass a broader range of data, including dynamic information like real-time traffic and sensor data and detailed static road-level data. Their comprehensive static information surpasses that of standard maps. Functioning as virtual sensors, HAD Maps enhance vehicle safety without complicating the hardware system. Standards associated with HAD Maps include the Tsinghua Seven layers HD
map model [21], OpenDRIVE, and Local Dynamic Map (LDM) [22]. LDM
provides a framework for hierarchically storing dynamic and static elements, while the Tsinghua model offers an in-depth representation of the environment for highly automated driving. HAD Maps achieve an impressive accuracy of 10 20 cm.

Despite these maps evolving gradually, there are still certain discrepancies between digital maps, ADAS maps, and high-definition maps. The following table illustrates how high-definition, conventional, and ADAS
maps differ from one another in terms of map users, functionalities, accuracy, frequency of updates, and content. The specifics are displayed in Table 2.

## 3. What Is A High-Definition Map ?

In this section, we aim to clarify the definition and the components of a high-definition map. Additionally, we present different classifications of map representation, enhancing the readers' comprehension of map data. Here, we also provide all of the standards that have been commonly referenced in the literature. Finally, we summarize all of this information in the last subsection.

## 3.1. The Definition Of Hd Map

HAD maps offers precise and reliable information about the driving environment for vehicles. In addition to serving as a navigational tool, HAD Map can function as an effective "sensor". After a vehicle has been localized on the map [19], it offers precise information about both the immediate and extended surrounding area. Furthermore, it is a component of the digital infrastructure that supports not just automated driving also several other applications, including smart cities, safety, and urban planning and management [23].

As the role of machines in driving expands, digital maps evolve beyond mere navigation tools. Traditional GPS solutions fail to provide the accurate and dynamic data required for autonomous vehicles.

Autonomous driving software requires self-updating mapping systems specifically designed for these vehicles, enhancing their perception of the environment. Utilizing HAD mapping technology, an autonomous

| Table 2 The features of digital map, ADAS map and HAD map. Feature Navigation Digital Map                                               | ADAS map                                                                                                   | HAD Map                                                                             |                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| User                                                                                                                                    | Drivers                                                                                                    | Intelligent vehicle, ADAS system                                                    | Intelligent vehicle, autonomous driving system                                    |
| Function                                                                                                                                | Navigation and search                                                                                      | ACC, LDW, LKA, and FCW.                                                             | Environmental perception, high-precision positioning, and path planning decision. |
| Object Types                                                                                                                            | static objects                                                                                             | and dynamic objects                                                                 | Static and dynamic objects                                                        |
| Route Planning                                                                                                                          | Global path planning                                                                                       | Local path planning/global path planning                                            | Local path planning                                                               |
| Resolution                                                                                                                              | 5-20 meters                                                                                                | Meters and sub-meters                                                               | 0.1-0.2 meters                                                                    |
| Updating                                                                                                                                | Permanent static data                                                                                      |                                                                                     |                                                                                   |
| Frequency                                                                                                                               | (update frequency: about 3 months), semi-permanent static data (update frequency: about 1 hour)            | Permanent static data (frequency approximately 1 month), semi-permanent static data |                                                                                   |
| (frequency approximately 1 hour), semi-dynamic data (frequency approximately 1 minute), dynamic data (frequency approximately 1 second) |                                                                                                            |                                                                                     |                                                                                   |
| Semantic                                                                                                                                | Road names                                                                                                 | Road names and map element information                                              |                                                                                   |
| Information Road Names                                                                                                                  | Important                                                                                                  | Less Important                                                                      | Less Important                                                                    |
| Location                                                                                                                                | GPS                                                                                                        | High dimensional data matching                                                      |                                                                                   |
| Content                                                                                                                                 | Road-level data, such as road                                                                              | High-precision road-level data: road                                                | Detailed and high-precision road-level                                            |
| shape, slope, direction                                                                                                                 | shape, slope, curvature, paving, and                                                                       | data, including lane models, components,                                            |                                                                                   |
| direction.                                                                                                                              | attributes, and targets. Multiple information layers: sensing layer, positioning layer, and dynamic layer. |                                                                                     |                                                                                   |
| ACC: Adaptive Cruise Control, LDW: Lane Departure Warning, LKA: Lane Keep Assistance, FCW: Forward Collision Warning                    |                                                                                                            |                                                                                     |                                                                                   |

vehicle can localize itself with high precision, accurately mapping its position relative to itssurroundings. HAD maps assimilate and analyze data from multiple sources in real-time, including vehicle sensors, LiDAR, onboard cameras, satellite imaging, and GPS. This integration differs significantly from conventional maps designed for general navigation. The amalgamation of this data provides a comprehensive, up-to-date understanding of road gradients, boundaries, traffic signals, lane positions, anticipated curves, and safety conditions. As such, high-definition maps redefine the standards for in-car navigation systems in autonomous vehicles [24,25], offering an exceptionally accurate depiction of the route." Definition 1. High-Definition Map (HD map) is an accurate and detailed expression of the road traffic scene. Compared with the traditional navigation electronic map, the content of the expression is more abundant. HD map belonging to the lane level has higher accuracy, reaching the centimeter-level accuracy requirements. The map data must be updated at a high frequency to ensure the authenticity of the map data to provide map matching to assist the environmental perception and path planning tasks.

Definition 2. The Highly Automated Driving Map (HAD map) constitutes a real-time, dynamic, multi-layered data characterized by centimeter-level precision. As a cornerstone in the realm of automated driving, the HAD map underpins critical functionalities such as positioning, planning, decision-making, and control, thereby ensuring safety and reliability. It encompasses a detailed representation of both static road features and dynamic traffic elements, including roads, lane lines, curbs, and traffic signs. Beyond capturing these map elements' geometric and topological relationships, the HAD map also integrates multidimensional information, such as confidence levels. Moreover, the representation of HAD maps extends beyond point cloud and vector maps, encompassing semantic maps, grid maps, and various other formats.

Definition 3. Automated driving high-precision map is type of data characterized by accurate positional information and an extensive array of road elements information. This map integrates 2D and 3D representations, vector and raster formats, as well as point cloud and semantic map [26]. It provides essential prior knowledge for intelligent driving and understanding of real roads, similar to the human brain's perception of actual road conditions. Additionally, this map also predicts complex road scenarios for the intelligent vehicle and mitigating potential driving risks, which is the core foundation for realizing automated driving.

As a crucial component in developing autonomous driving technology, the automated driving map plays a pivotal role in high-precision positioning, intelligent navigation, control, and other aspects directly influencing to the safety, stability, and comfort of autonomous driving.

Furthermore, it is one of the core key technologies of autonomous driving.

## 3.2. The Contents Of Had Map

To provide enough information to assist autonomous driving, the HAD map contains many types of elements. Generally, the elements of an HAD map can be divided into two categories: static elements and dynamic elements.

## 3.2.1. Static Elements

The static elements in the HAD map can be divided into basic road features and supplementary static elements, as the basic features of the structural road environment, road, junction, and lane are essential in global path planning and local driving decisions. The local environment also has supplementary static elements, such as traffic signs, bridges, railway crossings, platforms, and road lamps [24]. These elements can be divided into three categories according to their relationship with the road network: on-road elements, accessories, and off-road elements. Onroad elements include tunnels, bridges, and railway crossings, which are part of the road network and can be described as properties of roads or junctions. Road accessories are the functional elements related to traffic rules. Traffic lights, signs, and road marks can represent traffic rules in the lane property. Crosswalk is also an accessory highly related to the driving process [21]. According to geographic data files (GDF) standards [27], some road accessories are still not included, namely environment facilities, road lamps, guideposts, road cameras, and guard rails. The last type of supplementary elements, off-road elements, includes parking lots, and bus platforms. These functional elements can give some indications to the driving process.

## 3.2.2. Dynamic Elements

The dynamic elements in the HAD map can be divided into two categories: the dynamic physical entities and the dynamic information, such as traffic light status, weather conditions, and temporary speed limit.

The dynamic elements are constructed in the HAD map through vehicleto-everything (V2X) [21,28].

Dynamic physical entities include ego vehicles, obstacles, and free areas. The status of the ego vehicle is crucial for making driving decisions. Dynamic obstacles primarily include vehicles, pedestrians, and
 

![4_image_1.png](4_image_1.png)

JID: FMRE [m5GeSdc;July 1, 2024;10:0]
Fig. 3. Example of local OGMs generated from the fusion between **camera** and LiDAR data between intelligent connected vehicle: (a) ego vehicle (b) vehicle 1. The figures are obtained from Zheng et al. [29] work.

cyclists. It is important to note that stationary dynamic obstacles are also classified as dynamic obstacles, as treating them as static could pose risks if they unexpectedly move. Since vehicles, pedestrians, and cyclists are the most common traffic participants and have quite different dynamic characteristics and behaviour modes, they are represented separately with specific properties. Due to the highly dynamic properties of these physical entities, they should be updated at a high frequency through V2X [24].

Dynamic information, on the other hand, encompasses traffic light data, traffic conditions, weather, and temporary traffic regulations. Traffic light details and status, including flow and density, are typical elements in commercial electronic maps. Weather information plays a significant role in perception, decision-making, and vehicle control. Accurately quantifying weather effects can aid in adjusting control algorithms for enhanced safety. Temporary traffic rules, such as speed limits, restricted vehicle access (like bus lanes during certain hours), and accident reports are also dynamic elements. These rules often vary based on road weather conditions and can be viewed as time-dependent properties, similar to the regulations indicated by traffic signs [21].

## 3.3. Classification Of Different Had Maps

Derived from a variety of map elements, high-definition maps can

## Be Represented In Different Forms, Such As:

3.3.1. Raster map (Occupancy grid *Map)*
Raster map is also known as the occupancy grid map (OGM). It was first proposed by Moravec and Elfes [28,30,31]. The surrounding environment is modelled by dividing the space into uniform cell grids (either 2D or 3D), which store corresponding information as shown in Fig. 3
[32]. Han et al. [33] proposed a 2.5D version that adds the height data on the grid cell rather than converting it into a 3D grid map.

The type of information stored can either be occupancy probability [34,35], reflection intensity [36], probability distribution [37], or distance information [30]. The size of the cell grids determined the resolution and required storage space of the map. This type of map can be used to determine the movements of pedestrians [38], vehicle position
[39], and vehicle navigation [40].

## 3.3.2. Point Cloud Map

The rapid development of light detection and ranging (LiDAR) technology lowered the barriers to point cloud maps. Therefore, many HD
map providers have employed point cloud maps, such as HERE, TomTom, and Waymo. [31]. Point cloud maps offer discrete and dense samplings of the environment, capturing accurate 3D coordinates of points for a high-quality representation of the world which can be seen in Fig. 4
[41]. In Simultaneous Localization and Mapping (SLAM), the map includes only landmarks or even a sparse 3D point cloud, called a 3D
sparse map[16]. The advantage of point cloud maps is that they densely

![4_image_0.png](4_image_0.png)

![4_image_2.png](4_image_2.png)

model the entire environment and preserve rich environmental information [42]. Their disadvantage is that the storage space required will grow exponentially as the mapped area expands, which inconveniences maps' storage, transmission, and application [31]. There have been a lot of use cases for localization [43] and navigation [44] since the data provided by LiDAR is considered state-of-the-art in terms of ranging precision and accuracy.

3.3.3. Geometric feature map Geometric feature maps represent the elements in an abstract, vectorized form. The elements are stored as points, lines, surfaces, and other basic geometric entities as illustrated in Fig. 5. Thus the map provides the information needed for positioning while saving storage space [30].

The advantage of this method is that the geometric features are sparse and can store information efficiently. However, it requires heavy labor to extract features offline in the map-building process [31].

## 3.3.4. Topological Map

A topological map is a graph composed of nodes and edges [45,46],
primarily focusing on connectivity between various map elements [30].

Topological maps do not focus on the accuracy and structural details of the map, which is a more compact form of expression, which can be seen in Fig. 6. However, when dealing with complex structures, it is necessary to implement appropriate graph segmentation [26]. These maps are particularly useful in street-level navigation and path-planning tasks. Besides, it can be integrated with semantic information to enhance vehicle perception and localization robustness in complex and dynamic environments. Readers interested in the information regarding topological mapping through vision-based methods can refer to [47].

## 3.3.5. Intensity Map

The intensity value is a metric indicating the pulse strength generated by a laser radar at a specific point. This value is determined by the reflectivity of the object scanned by the LiDAR pulse, which in turn is dependent on the wavelength used. Consequently, the intensity of the

![5_image_0.png](5_image_0.png)

Fig. 6. Illustration of topological map of an intersection where the **lane**

![5_image_1.png](5_image_1.png) nodes are connected to clearly define the permitted lanes for **planning** tasks. Red dots indicate exit, and blue dots indicate entry.

Fig. 7. The example of intensity map obtained from LiDAR **frames**.

![5_image_2.png](5_image_2.png)

Fig. 8. Road semantics mapping based on crowdsourced **data**. The figure is taken from Wijaya et al. [51] work with permission from the authors.

echo varies with the composition of the surface object that reflects the echo as shown in Fig. 7 [48,49].

 =
√2∕ (1)

## = ∑̇∕ ∑ (2)

Among ,,, represents the intensity value of the grid cell (,); ,,
is the ℎ weight value of cell (,); , is the gray value of cell (,).

The intensity map is a two-dimensional representation created through raster processing and projection calculation. This map is derived directly based on the intensity values obtained from raw LiDAR data. Bârsan et al. [50] proposes a real-time localization at 15 Hz by using a LiDAR intensity map and achieves centimeter-level accuracy.

3.3.6. Semantic map The semantic map layer plays a crucial role in providing a higher level of understanding of the environment compared to traditional maps. The semantic map contains information about the meaning and function of objects and features in the environment, allowing autonomous vehicles to understand their surroundings better and make more informed decisions [56,57]. The depiction of this map can be seen in Fig. 8. The construction of a semantic map follows some basic principles:
1. All data must be consistent with the geometric layer information of the vehicle.

2. The data obtained by the vehicle itself is the most reliable source of information.

3. Make full use of existing data resources, such as navigation maps, and build semantic maps based on them.

A semantic map is not an independent map layer. It can be mapped into a geometric map, a vector map, a road network map, a point cloud map, and other maps.

## 3.3.7. Density Map

Density maps, also known as dense maps, are also used in autonomous driving research. This map serves as an intermediate representation of targets in the areas as can be seen in Fig. 9. Several recent techniques [55,58,59] can obtain accurate counting performance. This map is useful for assessing an area's traffic density, which is valuable in the path-planning algorithm for efficient and safe autonomous driving purposes.

## 3.4. The Current Map Standards

The complexity of the driving environment requires that the elements of the HAD map be organized in a standardized data structure for comprehensive understanding [26]. A standard format and model not only provide convenient access to necessary data for users but also ensure uniformity across different platforms. Numerous standard institutes and companies are developing their unique map standards. This section will introduce some of the most influential standards in the industry and examine their approaches to organizing environmental elements. Notable standards in the autonomous driving sector include OpenDRIVE, NDS, LDM, ADASIS, lanelet, and Tsinghua HAD map are the most influential HAD map standards in the autonomous driving industry [26,60].

Among them, OpenDRIVE [61–63] and NDS [64] predominantly concentrate on the static map model, providing a thorough understanding of the static structural road environment. Conversely, LDM [65,66] focuses on dynamic elements. Lanelet [67,68] presents an efficient map representation for autonomous driving. ADASIS focuses on data transmission and its application in ADAS [69]. In this chapter, we will introduce the typical map standards and models.

## 3.4.1. Opendrive

OpenDRIVE [61–63] is an open-source map format created by the enterprise alliance engaged in simulation development. It encompasses road networks and topologies while supporting the 3D geometric information representation for autonomous driving. OpenDRIVE map is organized as a hierarchical repository in XML format, which is more suitable for automated driving simulation. This format is often adopted for static information expression and centralized storage. It is realised according to a strict hierarchical inheritance relationship. With road links and junctions as basic units, with additional elements like lanes and traffic signs being methodically integrated into hierarchical layers. The most significant feature of the OpenDRIVE map is its distinct and clear structure as shown in Fig. 10.

1. Coordinate system: Latitude and longitude are transformed to a ground plane with the north-east-sky ground coordinate system. The road geometry is calculated from the ground coordinate. The elements along the road, such as lanes and traffic signs, are represented in the  −  coordinate. The  axis is set along the road center line, while the  axis is set vertically to the road center line. See Fig. 11.

2. Road network: A road in the OpenDRIVE network comprises several key components:
(a) Reference **line:** This is typically the road's center line. The reference line can be a straight line, a clothoid, or a circular arc. Additional road attributes like elevation and traffic signs are specified along the reference line.

 

![6_image_0.png](6_image_0.png)

JID: FMRE [m5GeSdc;July 1, 2024;10:0]

![6_image_1.png](6_image_1.png)

Fig. 10. The structure inside an OpenDRIVE map consists of traffic simulation, vehicle dynamics, and sensor **simulation**.

![6_image_3.png](6_image_3.png)

(b) Lanes and lane **properties:** Each road may contain one or more lanes. The basic format of a lane includes its basic properties (like connection relationship, lane type, length, and speed limit), which are stored as strings.

(c) 3D geometry **information:** This section includes sectional lines with four basic geometry types: straight line, clothoid, circle arc, and polynomial. Essential parameters for each geometry type and start-end points are detailed.

(d) Elevation Profile and Section **Shape:** A cubic curve represents the elevation profile and illustrates the height-longitudinal distance (height-) relationship. Based on the longitudinal coordinate (), the section shape is depicted through the height-width
(height-) relationship.

![6_image_2.png](6_image_2.png)

(e) Lane boundary **information:** This covers the colour, type (solid or broken), material, and width of lane boundaries.

(f) Additional **Information:** OpenDRIVE maps also support elements beyond the road network, such as stations, railways, and parking lots. This information and road and junction data form the complete XML file.
3.4.2. NDS *format* In the NDS map [64], the whole earth's surface is divided into tiles by quadtree. The higher the level in the quadtree, the smaller the tiles. Each tile is given an ID number, as shown in Fig. 12. Different types of information are stored in different building blocks. The information in each tile is stored in the building blocks. Considering the high complexity of the NDS format, here we will only introduce some basic information provided by the NDS format.

1. Road **Information:** This information is stored in the 13th tile. The overall representation of earth's surface is included in tiles 2-13. This category entails road links, junctions, and road geometry information. The road geometry information is similar to that in OpenDRIVE
maps.

 

JID: FMRE [m5GeSdc;July 1, 2024;10:0]

![7_image_0.png](7_image_0.png)

![7_image_2.png](7_image_2.png)

to ADAS **functionalities**.
Fig. 14. LDM layers' structures consist of highly dynamic, transient dynamic, transient static, and permanent **static**. The figure is obtained from
[70] works.

2. Lane **Representation:** In the context of ADAS and autonomous driving applications, the lanes in NDS maps are defined by their basic properties, connection relationships, and geometric characteristics.

Key attributes include lane type and speed limits. Lanes are grouped based on their direction and road association, forming the foundation of a lane-level network. The geometric design of lanes is articulated using splines, augmented with elevation profiles and section shapes akin to those in the OpenDRIVE format. The NDS map format also supports lane boundary types, such as lane markers, road edges, and railings.

3. Other **information:** The NDS map has detailed, high-precision data and includes information typical of traditional maps. Leveraging a comprehensive tile system, the NDS map supports various types of information, including map display, traffic data, terrain features, object names, and more. This makes the NDS map more mature than OpenDRIVE and improves its complexity, making it less simple than an XML OpenDRIVE file.

3.4.3. ADASIS [69] and LDM *[65,66]*
ADASIS is a map standard developed for ADAS applications, and it focuses on the data transmission between the cloud and the clients. The cloud provides ADAS Horizon (AH) for client subscriptions, containing information pertinent to autonomous driving map standards, including the road, junction, lanes, and reference lines. When users input the destination in real applications, the global path planner will simultaneously sort the map element information [69]. In addition, ADASIS supports the fusion of perception results in the map platform as shown in Fig. 13.

In contrast, LDM focuses on the dynamic elements in the driving environment. It is designed for the Intelligent Transportation System (ITS)
rather than only the static geographical environment. LDM contains four layers: highly dynamic, transient dynamic, transient static, and permanently static data, with dynamic information being updated by V2X.

As shown in Fig. 14, LDM contains static information from OpenDRIVE
and NDS, as well as dynamic elements. The traffic details, such as traffic lights and flow, is allocated to the third layer, while the highly dynamic elements, predominantly dynamic obstacles on the road, are slotted in the fourth layer.

![7_image_1.png](7_image_1.png)

## 3.4.4. Lanelet

In the field of automated driving, LaneLet [67,68] serves as an effective expression of high-precision maps. It specify the area where automated driving is possible with LaneLets that are connected to one another. It is capable of fully expressing both the lane topology and the lane geometry. It can also incorporate people's driving behaviours and traffic laws simultaneously. A physical, relational, and topological layer can be found in Lanelet2 [68]. Each Lanelet is bordered by left and right bounds, each composed of a sequence of points, enabling precise replication of various lane shapes. The output map of the lanelet2 software typically adopts the OSM format. This technology was notably employed during the MERCEDES BENZ S 500 INTELLIGENT DRIVE's autonomous trip over the Bertha Benz Memorial Route in the summer of 2013 [20].

The map example for a highway road and the resulting map structure, as well as for an intersection and the resulting routing graph for normal vehicles, are shown in Fig. 15. The red in the graph indicates conflicting lanelets.

## 3.4.5. Tsinghua Had Map

Generally, the basic idea of the above map standards is to find a way to better sort the information in the road environment. In contrast, the Tsinghua HAD map standard focuses on the application in autonomous driving, providing information according to the requirements of perception, positioning, and decision-making [21]. Tsinghua HAD map contains seven layers, considering the road-level and lanelevel network, high-precision static information, dynamic obstacles, and partial decision-making assistant information (See Fig. 16).

1. Road **layer:** Road-level network is the basis of the traditional map and the foundation of global path planning of autonomous vehicles.

2. Traffic information **layer:** The road-level macroscopic traffic information is provided in this layer to help global path planning. The traffic flow and temporary road closure information can be found in this layer.

3. Road-lane connection **layer:** The lane-level network is further given for the lane-level global path planning of autonomous cars based on the road-level network. The road-lane connection layer provides the topological relationship between the road and lane-level networks.

4. Lane **layer:** This layer contains high-precision, detailed static environment information. Like the OpenDRIVE map, the lane layer contains lane geometry, traffic signs, lane-level traffic rules, slope, and curvature.

5. Map feature **layer:** The map feature layer is designed for highlyaccurate self-positioning of autonomous vehicles. The map feature layer contains LiDAR point cloud and image line features. During

![8_image_1.png](8_image_1.png)

![8_image_0.png](8_image_0.png)

the operation of autonomous vehicles, comparing features extracted by onboard sensors with those in the map plays a crucial role in refining the position measurement of ego vehicles can be modified. This is useful in a complex urban environment where the GNSS signal is interrupted and occluded. This layer contains a lot of sensor feature data and, thus, needs more storage than the above four layers.

However, compared to the vector and string information in the four layers, the map feature layer can better support the self-positioning of autonomous vehicles.

6. Dynamic object container **layer:** This layer is designed for obstacle perception and local dynamic trajectory planning. With the help of V2X, the roadside infrastructure, and the connected vehicles can upload the obstacle information to the cloud, achieving the real-time update of the dynamic objects container layer. Autonomous vehicles can get this information from the map to get a non-occlusion environment perception, thus better supporting local dynamic trajectory planning.

7. Intelligent decision support **layer:** The layer can support driving decisions by providing some prior decision knowledge. In fact, the driving decisions are closely related to the local geographical features. The characteristics of driving decisions are analyzed according to every specific location. Then, these are stored in the intelligent decision support layer as prior knowledge. This data can be acquired by leveraging crowdsourced data from taxis, for example, inside a city. The vehicle can download the local driving knowledge for the most appropriate driving decision policy. This layer is a significant characteristic of the Tsinghua HAD map.

## 3.5. Summary

High-definition maps are diverse, each featuring multiple layers tailored to the information they store and their specific application scenarios. These maps can be classified into various types, including raster, point cloud, geometric feature, topological, intensity,semantic, and density maps. This section also encapsulates the standardization process of current HD maps across these classifications. As illustrated in Table 3, OpenDRIVE and NDS are geared towards static environments, whereas LDM and Tsinghua maps encompass both static and dynamic elements.

OpenDRIVE is known for its simplicity, open-source nature, and ease of use, making it popular in research settings. In contrast, NDS aims for comprehensive coverage, providing detailed static information that includes both conventional map data (e.g., GDF map standard) and additional HD details essential for autonomous driving. The LDM standard, designed for ITS, addresses static and dynamic elements. It enables updating macroscopic traffic information and microscopic dynamic obstacles via V2X communication in ITS. The Tsinghua map model, distinct from LDM, prioritizes integration with technical modules in autonomous driving, offering advanced features for positioning and decision-making.

Unlike these standards, ADASIS is more concerned with data transmission than an extensive driving environment description. It provides users with information along the globally planned path, making the "path" its sole layer or building block, with all relevant data treated as path properties. Collectively, these five standards each have their unique focal points, characteristics, and advantages.

## 4. Map Creation, Products, And Maintenance

This section will briefly discuss the mapping process, update, resulting products, and available open-source HAD map datasets.

## 4.1. Had Map Creation

HAD maps are widely used to enhance autonomous vehicle technologies, and the accuracy and quality of HAD maps are directly related to the reliability, safety, and efficiency of autonomous driving. At present, the accuracy of the HAD map is centimeter-lever, and the update should be done frequently to ensure the precision and quality of the HAD map.

HAD map mapping can be divided into four steps: data acquisition, HD
map generation, quality control, and release and maintenance [71]. The details are as follows:
1. Data **acquisition:** This task involves using multiple Mobile Mapping Systems (MMS) to gather high-precision, multi-source road data. These MMS can be seen in Fig. 17. Updating these maps promptly with each change is crucial to ensure autonomous vehicle safety.

Currently, the prevalent method employs MMS equipped with cameras, LiDAR, GPS/IMU, and other sensors [72]. The raw data of MMS
is collected from cameras, LiDAR, GPS, IMU, wheel speed sensors, and other onboard sensors for HD map generation afterward [73].

While this approach offers high accuracy, it is costly, and updates may only occur monthly at times. Although this method ensures high accuracy, it is expensive and may lead to monthly update cycles at best. To address the need for real-time updates, there is a growing trend towards crowdsourcing data from vehicles like smart cars, public buses, and taxis, all equipped with various sensors [74].

This approach significantly enriches the data sources and increases the frequency of updates. However, it presents challenges related to the variable quality of crowdsourced data, which can be affected by differences in sensor capabilities, timing of data collection, and the perspectives from which the data is acquired.

2. HD Map **Generation:** This stage can utilize MMS or SLAM (Simultaneous Localization and Mapping) technology [31,75]. MMS estimates the vehicle's pose directly through GPS and IMU [76–78],

| The characteristics of different map standards. Standard Layers Contained elements   | Characteristics                              |                                                                       |                                                                                        |
|--------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| OpenDRIVE                                                                            | 5                                            | Road network, junction, lane, traffic sign, traffic rule, station     | HD static road information, XML hierarchical format, open and free                     |
| NDS                                                                                  | 18                                           | Complete understanding of static elements                             | Abundant static HD information, quadtree storage, both HAD and traditional information |
| ADASIS                                                                               | 1                                            | Road network, junction, lane, traffic sign, and traffic rule.         | ADAS application, communication consideration                                          |
| LDM                                                                                  | 4                                            | Permanent static, transient static, transient dynamic, highly dynamic | Both static and dynamic information, designed for ITS and V2X                          |
| Tsinghua                                                                             | 7                                            | Road network, detailed static elements, static positioning features,  | Designed for autonomous driving application, decision-making                           |
| dynamic elements, decision-making knowledge                                          | support, additional features for positioning |                                                                       |                                                                                        |

while SLAM combines data from odometers, GPS, IMU, and wheel speed sensors for a more confident pose estimation and reduces error accumulation through loop closure [79–81]. After acquiring poses, an HD map can be pieced together using map elements extracted from the point clouds and images collected. The three-dimensional geometric and topological information of map elements extracted based on LiDAR [82,83] and image data [84–91], include lanes, traffic signs, traffic lights, and poles. Finally, the map elements are transformed into the coordinate system and saved in the corresponding map layers [72,92].

3. Quality **Control:** This phase involves applying predefined evaluation metrics and standards to verify the map's accuracy. Some map elements, automatically extracted by algorithms, require manual verification [93].

4. Release and **Maintenance:** After meeting accuracy requirements, the HD map is released. In this stage, map elements are compiled and issued according to set standards. HD maps undergo updates to reflect environmental changes and issues identified in use [71].

## 4.2. The Had Map Products

In the sector of automotive driving, various research institutions and leading companies have proposed map products, including Apollo HD
map, AMAP HD map, NavInfo HD map, HERE HD Live Map, Waymo HD map, and Mobileye HD map. These products of HD maps have been improved continuously, enriching their content and enhancing data accuracy to reach a level of precision within centimeters.

4.2.1. Commercialized HAD map Given the value provided by HAD map towards autonomous driving, more and more companies are now working on commercializing the HAD map data (See Table 4). Various companies are working on this aspect, such as:
1. Apollo HD map **(Baidu)** [94]: The production of Apollo HD
maps includes four links: data collection, data processing, element identification, and manual verification. Data elements of the Apollo HD map include road elements, intersection elements, traffic signal elements, logical relationship elements, and other road object elements. The data format is mainly inherited from the OPENDRIVE format.

2. AMAP HD map [104]: AMAP, formerly AutoNavi, has amassed high-precision autopilot map data over more than 320,000 kilometers. The two LiDARs and four cameras on AMAP's specialized mapping vehicle for HAD-level autonomous driving maps primarily gather road data with an accuracy of up to 10 cm. To offer a complete "autonomous driving map + high-precision positioning solution," AMAP collaborated with the provider of precise location services, Qianxun Location. The lateral and longitudinal errors are within 7 cm under normal road conditions and 6 cm and 5 cm under high-speed/urban loop conditions, according to the two parties' present lane-level positioning solutions [95].

3. NavInfo HD map [96]: NavInfo initiated its foray into the realm of autonomous driving maps with technical research and exploration starting in 2013. The company further solidified its commitment to this field in 2015 by establishing the Smart Map Division, marking the official commencement of product development and commercialization efforts for autonomous driving maps, specifically targeting Level 3 and higher autonomous driving systems. NavInfo has now achieved comprehensive proficiency in the entire product capability suite for autonomous driving maps. This suite encompasses a range of processes from data collection, automated mapping, and crowdsourcing updates to rapid iteration, demonstrating NavInfo's significant progress and expertise in this domain.

4. TomTom HD map [105]: TomTom N.V., a Dutch multinational company specializing in developing and producing consumer gadgets and location-based services. With precision down to a few centimeters, it provides TomTom HD map, a very accurate representation of the road with various features, including lane models, traffic signs, road furniture, and lane geometry. To guarantee that the automated driving system has access to the most recent road information, TomTom developed the TomTom AutoStream delivery service, which effectively distributes the most recent and pertinent HD map data.

5. HERE HD Live Map [106]: HERE was formerly known as NAVTEQ, an American mapping company. HERE's autonomous driving map is an extension of the traditional navigation map.

The accuracy of the map must be at least sub-meter level, and the information will be more abundant. Basic road information, features, and dynamic information layers are composed of different layers, which can be customized according to the needs of the OEM. In May 2018, HERE, NavInfo (China), Increment P /Pioneer
(Japan), and SK Telecom (South Korea) announced establishing the OneMap alliance to develop global map standards. Starting in 2020, we will provide uniform standard high-precision map products and services to the industry to support the implementation of global OEM autonomous driving solutions.

6. Dynamic Map and Cooperation **Area** [99]: Dynamic Map and Cooperation Area is a high-precision three-dimensional location information platform that DMP (Dynamic Map Platform Co., Ltd.)
offers. It contains both static information (High-Accuracy 3D Information) and dynamic information, such as road construction plans, accident information, and traffic light information. They can achieve centimeter-class precision for their geometric map data.

7. **Waymo** HD map [107]: Waymo's high-precision maps are developed from Google Maps and have a strong data and technical background. Currently, the high-precision maps it produces are only used for its own autonomous driving, not as a commercial product. The method of collecting maps is LiDAR, plus an integrated navigation and positioning system. They also have a large surveying and mapping fleet to create high-precision maps together by means of map fusion.

8. **Mobileye** [108]: Although Mobileye does not directly produce high-precision maps, its camera technology significantly contributes to this domain. Each Mobileye camera is capable of capturing detailed road conditions ahead. For instance, these cam-

| The comparison of various HAD Map. HD map Accuracy                                | Updating method                                 | Coverage                                                |                                                         |
|-----------------------------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Apollo HD map [94]                                                                | Centimeters                                     | Professional mapping vehicles and crowdsourced vehicles | China                                                   |
| AMAP HD map [95]                                                                  | < 10𝑐𝑚                                        | Professional mapping vehicles and crowdsourced vehicles | China                                                   |
| NavInfo HD map [96]                                                               | -                                               | Crowdsourced data, UGC, OEMs                            | China                                                   |
| HERE HD map [97]                                                                  | < 20𝑐𝑚                                        | Crowdsourced data and satellite imagery                 | North America and Western Europe                        |
| TomTom HD map [98]                                                                | 15-20 cm                                        | Professional equipped vehicles and crowdsource          | U.S., Europe and East Asia                              |
| Dynamic map and cooperation                                                       | Centimeters                                     | Professional mapping vehicles and crowdsourced vehicles | Japan and U.S.                                          |
| area [99] Waymo HD map [100]                                                      | 10 cm, low efficiency,                          | Crowdsourced vehicles                                   | U.S.                                                    |
| long cycle and high cost                                                          |                                                 |                                                         |                                                         |
| Mobileye HD map [101]                                                             | Centimeters                                     | Professional mapping vehicles                           | U.S.                                                    |
| Uber HD map [102]                                                                 | -                                               | Professional mapping vehicles                           | U.S.                                                    |
| Apple map [103]                                                                   | -                                               | Professional mapping vehicles                           | U.S.                                                    |
| Table 5 Comparative between different HD map datasets. Dataset Lyft Level 5 [109] | NAVER LABS HD map Dataset [110]                 | Argoverse[111]                                          |                                                         |
| Sensors                                                                           | 7 cameras and 3 laser scanners                  | 10 cameras and 2 laser scanners                         | 2 laser scanners, 7 cameras, and 2 front stereo cameras |
| Annotation                                                                        | 55000+ 3D manual annotation                     | contain about 130k images as well as 6DoF               | HD map with geometric shape and semantic                |
| camera poses for training and validation                                          | information                                     |                                                         |                                                         |
| Map information                                                                   | Surface map for safe driving, and               | 3D Road Layout, LiDAR Feature Data, and Visual          | Geometric lane vector map, grid map of the              |
| semantic map of the underlying                                                    | Feature Data                                    | drivable area, and grid map with actual height          |                                                         |
| high-definition space                                                             |                                                 |                                                         |                                                         |
| Map content                                                                       | More than 4000 lane sections, 197               | 3D location information, including lanes, road          | (1) Two HD maps with lane centerline, traffic           |
| crosswalks, 60 stop signs, 54 parking                                             | signs, crosswalks, intersections, and overspeed | direction, and ground height (2) An API for             |                                                         |
| areas, 8X speed bumps, 11X speed bumps                                            | stops                                           | connecting map data with sensor information             |                                                         |
| Data size                                                                         | 350+Scenes at 60-90 Minutes Long, 30K           | -                                                       | 3D tracking annotation with 113 scenes 290KM            |
| LiDAR Point Clouds, 1.3M 3D Annotations                                           |                                                 |                                                         |                                                         |

eras can accurately identify lane markings or the position of speed limit signs. They process each captured image into data, subsequently packaging it into packets for uploading. This data is then overlaid in real time onto the base map for enhanced accuracy.

The collaborative efforts between Mobileye and automotive manufacturers like Volkswagen, Nissan, and GM are leading to more vehicles being equipped with Mobileye cameras. The combination of image, intelligence, and network connection can achieve a high precision of 10cm.

9. Uber HD map [102]: They employ AI-based methods to automate and assist human-in-the-loop HD map production processes.

Machine learning and computer vision are also applied to offline map generation pipelines.

10. Apple Map [103]: It has acquired around 6 million kilometers of driving data, which has resulted in a new underlying map with a much more detailed and accurate perspective. The new map has greatly improved and updated information on highways, beaches, marinas, parks, structures, airports, and other elements. It is already accessible throughout the United States, and it was launched in a number of nations in 2020.

## 4.2.2. Opensourced Had Map

Several companies have made significant contributions by opensourcing their High-Definition (HD) map datasets to foster the advancement of autonomous driving technology. These datasets are instrumental in the development and refinement of autonomous vehicle technologies. Among these notable contributions are the NAVER LABS HD map Dataset [110], the Lyft LEVEL 5 OPEN DATA Perception Dataset [109],
and the Argoverse Dataset by Argo.ai [111], each offering unique features and data types (See Table 5):
1. NAVER LABS HD map **Dataset:** This dataset consists of three data layers. These layers can be explained as:
(a) 3D Road *Layout:* This layer comprises a detailed representation of the road's surface, including the types and positions of visual elements such as lanes, road markings, crosswalks, and speed bumps.

(b) LiDAR Feature *Data:* It includes 3D LiDAR point clouds of the static road environment, meticulously captured by MMS vehicles and enriched with semantic annotations for each data point.

(c) Visual Feature *Data:* This segment offers compact, discriminative, and invariant across various viewing situations. These features are essential for localization and matching purposes.

The dataset is exclusively accessible to Korean scholars and groups, reflecting the sensitive nature of the map data.

2. Lyft LEVEL 5 OPEN DATA Perception **Dataset:** Lyft has included human-labeled 3D bounding boxes of traffic agents and an underlying HD spatial semantic map in Lyft LEVEL 5 OPEN DATA Perception Dataset to supplement the raw camera and LiDAR data.

3. Argoverse Dataset by **Argo.ai:** This dataset is designed to enhance the capability of autonomous vehicles in environmental perception.

It includes exceptionally detailed High-Definition (HD) maps, a notable inclusion for large-scale data collection in autonomous driving.

These maps feature an array of geometric and semantic details, including lane centerlines, lane directions, and drivable areas. This dataset marks a significant advancement in providing comprehensive spatial data for free. The rich data repository offered by Argo.ai facilitates the development of refined vision algorithms which is pivotal in equipping self-driving cars with the ability to navigate complex urban scenes safely.

## 4.3. Had Map Update

Automated driving requires highly accurate and real-time updates of the HAD maps. In instances where the HAD map is not updated in a timely manner, discrepancies between the map and the actual environment can arise. Such error may lead to the erroneous decisions by the autonomous driving system, posing major safety hazards and increasing the risk of traffic accidents, thereby compromising the safety of intelligent vehicles [1]. Currently, there are two primary approaches

![11_image_0.png](11_image_0.png)

## 5. Application Of Had Map 5.1. High-Precision Localization Based On Had Map

processing units, conducting real-time change detection experiments.

Using synthetic data, [124] developed a data-driven approach to detect map changes in real scenarios. Finally, [74] conducted frequent updates based on bus and taxi data in Seoul, an extension of the method proposed in [115]. A detailed comparison of centralized versus crowdsourced map updates is presented in Table 6.

Given the quality of the HAD map's information, numerous important use case applications exist. The most common are localization, cooperative perception, and intelligent decision support. Below, the explanation of each application is elaborated.

Fig. 18. Three stages of mapping based on crowdsourced data, which consisted of (a) smoothed trajectories, (b) aligned trajectories, and (c) **learning**. This result is extracted from Liebner et al. [116] works.

A requirement for autonomous vehicle navigation, decision-making, and control is high-precision and reliable self-vehicle localization [125–
127]. Theoretically centimeter-level localization findings are theoretically possible using high-precision localization techniques, such as GNSS
based on differential RTK (D-RTK). The GNSS signal may be blocked by nearby structures and trees in practical applications, such as urban settings, leading to a significant localization divergence. When GNSS positioning is unsuccessful, the dead reckoning (DR) technology based on an IMU can offer correction, but a cumulative inaccuracy will invariably result from long-term GNSS signal loss. Moreover, the cost of the D-RTK and IMU systems prevents them from being used commercially.

Map-based localization has been quite popular as an alternative strategy since it may be used with other localization techniques [128,129].

After its initial release, HD maps have become incredibly common in the fields of intelligent vehicles, to list just a few [128,130]. Road elements on HD maps are more precisely detailed than conventional navigation maps [21]. Several map-building companies have accumulated HD map datasets on a significant scale using several standards, such as NDS [64] and LDM [65]. The common method for creating HD maps is to use MMS [73,75] that are outfitted with high-precision sensors, such as LiDAR, RTK, and IMU, with centimeter-level accuracy. The generated map, which includes localization information, can help autonomous vehicles plan their positions and trajectories. A dense point cloud feature and a sparse vector landmark feature are two ways that HD map's localization feature can be broken down; these two types of features are referred to as point cloud HD map and vector HD map, respectively.

to updating the HAD map database: the centralized update method and the crowd-sourced method [112,113]. 4.3.1. Centralized *update* The centralized method is often considered the state-of-the-art method since this method utilizes a dedicated fleet of mapping vehicles equipped with a highly accurate GPS sensor, 360-degree camera, and LiDAR sensors [73,75]. Due to the high cost of the vehicle, the number of these specialized vehicles is limited. Thus, the update frequency provided by this method is not sufficient[112,113]. For example, Google updates the map database using a street view vehicle fleet. In 2012, there were only 250 vehicles actively roaming around on streets and freeways worldwide. Another mapping company named HERE used a vehicle fleet of a little above 200 cars to do mapping by the end of 2015. These examples show that even giant companies cannot satisfy a timely map update. Therefore, the future outlook of the autonomous vehicle presented back in 2016 stated that the crowdsourcing method of the map-building framework by large fleets of autonomous vehicles equipped with onboard sensors would be the future [114,115].

4.3.2. Crowdsourced *Update* While centralized mapping methods are often favored for their quality, crowdsourced approaches are increasingly recognized for their ability to incorporate the most current information into existing maps, a key aspect of map updates. For example, research [9] performs an update by lane line merging through hierarchical clustering. Study [116] introduced a scoring system grounded in consistency, spatial fit, and coverage, refining new data integration into existing HAD maps using graph calculations (See Fig. 18). A similar graph-based method was used in [117], assuming the presence of a monocular camera and basic GPS in vehicles, to achieve cross-correlation between landmarks and centimeter-level accuracy using 1000 passing vehicle data. Research [118] focused on the semantic alignment of lane features from visual odometry, enhancing the reconstruction process through edge refinement (See Fig. 19).

Pioneering work by Aijazi et al. [119] established the pipeline where map update is not a given situation but a situation that needs to be first detected and then updated. In [12], they approach the problem by first predicting whether the change has happened through a boosted particle filter. They assess the change based on the road-edge geometry in the visual landmark layer. Pannen et al. [120] considered a broader range of road sections with crowdsourced lane feature data, prioritizing areas with the highest update probability. Jo et al. [121] introduced SLAMCU, a SLAM approach that includes change detection. Heo et al. [122] proposed a novel cross-domain deep learning framework to align map data with real-time semantic layer detections. Zhang et al. [123] envisioned crowdsourced data comprising advanced sensors and 5.1.1. Point cloud feature-based *localization* GNSS systems cannot meet the demanding requirements for autonomous vehicles' self-localization in several environments. LiDARbased localization offers a promising solution and can be divided into SLAM (simultaneous localization and mapping) and map-based techniques. SLAM methods have two main categories: feature-based
[131] and scan-based [132]. Typically, localization based on SLAM suffers from an error accumulation problem [133]. In contrast, many researchers focus on vehicle localization in urban areas using LiDAR and priori known maps due to the significance of localization accuracy for autonomous driving in complex urban scenarios.

The original point cloud scanned by a LiDAR sensor, which preserves the point cloud's raw geometric data, forms the basis of the point cloud HD map. State-of-the-art map-based localization methods use point cloud HD maps to estimate vehicle pose accurately. The vehicle has a LiDAR sensor, and the LiDAR scans match the point cloud map. Yoneda et al. [134] use the Iterative Closest Point (ICP) method to match the real-time LiDAR scan with the point cloud map. Kato et al.

[135] Kato et al. implement ICP with Normal Distribution Transformation (NDT) for matching to obtain a stable localization. Levinson
[136] built the point cloud map in a probabilistic cell representation, modeling the mean and variance of reflectivity and location of each cell. Therefore, the reflectivity feature of point cloud points on the map

 

![12_image_0.png](12_image_0.png)

JID: FMRE [m5GeSdc;July 1, 2024;10:0]
Fig. 19. The pipeline and result for crowdsourced 3D edge map **reconstruction**. The figure is obtained from Herb et al. [118] works.

| The comparison between centralized and crowdsourced approaches. Content Centralized   | Crowdsourced                                                        |                                                                               |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Equipment                                                                             | Professional mobile mapping systems, Limited quantity               | Ordinary vehicles equipped with low-cost sensors, abundant crowdsourcing data |
| Data                                                                                  | Laser point cloud, high-resolution camera, and other high-precision | Track, photo, video, and other low-cost sensing data                          |
| data obtained by MMS                                                                  |                                                                     |                                                                               |
| Precision                                                                             | high-precision centimeter level                                     | Low precision up to sub-meter or meter                                        |
| Period                                                                                | Updated quarterly/monthly                                           | Update by month/week/day                                                      |
| Cost                                                                                  | High                                                                | Low                                                                           |
| Worker                                                                                | Surveying and mapping staff with professional training              | Volunteers, public and other non-professional surveying and mapping personnel |
| Characteristic                                                                        | High-precision, low efficiency, long cycle, and high cost           | Limited precision, high efficiency, real-time update and low-cost             |
| Suitable scenarios                                                                    | Reconstruction of large-scale new roads                             | Update of a few map changes with random distribution                          |

can be utilized in the map-matching process. Ding et al. [137] makes the LiDAR intensity-based map matching algorithm better by combining intensity and altitude cues in a way that adapts to different road conditions. This makes sure that localization is accurate even when the conditions are bad. Based on it, [137] adaptively fuses the map-matching result with a tightly coupled LiDAR inertial odometry to obtain a more accurate pose estimation. Bauer et al. [138] The localization performance has been demonstrated to achieve 10 cm or less localization error by benefiting from the dense geometric feature of the point cloud. 5.1.2. Vector landmark feature-based *localization* Compared to the point cloud HD map, the lightweight vector HD
map is more adaptable and simple to use. In contrast to the original point cloud HD map [128], the vectorized HD map format is far more lightweight and consists of static vectorized semantic features like lane lines, poles, and traffic signs. For mass-produced vehicles, matching the vector HD map with the affordable camera is an engineering and business-friendly option [126]. Researchers have worked hard to align the camera and the vector HD map. The fundamental idea behind it is to find semantic HD map landmarks in the image. The vehicle position may be made as efficient as possible by lining up the 3D landmarks in the vector HD map corresponding to the recognized landmarks in the image. Pink [139] employs aerial pictures to extract lane markings and their locations to create a lane-level map. They then use a straightforward ICP method to compare the lane marking feature in the image with the pre-built map. In addition, several different methods are employed, including direct point comparison [140,141]. Later work improved the map-matching localization by adding more sensors, like GNSS and IMU,
to an Extended Kalman Filter (EKF) architecture. Tao et al. suggested integrating lost GPS, dead reckoning, and map-matching information from visual lane markings using the EKF fusion framework [142]. The video camera system uses lane markers to determine the vehicle's lateral distance and heading angle. They demonstrated the viability and potential of a vision-based map-matching approach for localization applications utilizing pre-built lane-level maps.

## 5.2. Cooperative Perception Based On Had Map

HAD map is supplementary in improving the perception's performance and accuracy, especially in cooperative perception, which has been widely applied in autonomous vehicle areas. This subsection analyzes the role the high-precision map plays in improving perception.

5.2.1. Expand the perception *range* Cooperative perception information needs temporal and partial alignment [143]. HAD map can act as a container that stores the multisource asynchronous sensing information from cooperative perception and distributes it to each vehicle, thus making over-the-horizon perception possible. Kim et al. [144] showed the demo of see-through visualization as a subfunction of over-the-horizon perception. Xiao et al. proposed a unified multi-target positioning framework that could handle the situation of occlusion perception and perception out of range [11].

![13_image_0.png](13_image_0.png)

Jiang et al. [145] creates a new map container concept that can extend the perception range to see around the corner when the connected vehicle can detect the moving obstacle, as illustrated in Fig. 20.

## 5.2.2. Provide Priori Information

Priori mapping methods have been widely adopted by state-of-theart vehicles, such as Google, Uber, and Navya Arma vehicles [146]. HAD
maps provide centimeter-accurate priori map information to AVs and continually update map information based on collected sensor data [1].

Here are some applications based on a priori map. Obstacle detection is done by observing differences between the priori map and the current sensor data [146]. Yang et al. exploited priori knowledge from HAD
map for 3D object detection [10]. Xiao et al. created a small semantic map model and a method for choosing landmarks ahead of time that can make alignment easier with onboard measurement [129]. Ghallabi double-checked the detected road sign to be valid if a correspondent road sign exists in the HAD map [147]. Many practices implement maps to store perception information. Rauch et al. modeled Car2X-based perception as a virtual sensor to integrate into a high-level sensor data architecture [148,149]. Kim et al. built a multivehicle system and explored cooperative perception, where sensing information was dealt with as a 2-D map, and cooperative perception was handled by map merging [150]. Xiao et al. extended the concept of HAD map to a map container, a theoretical model that solves the problem of cooperative perception.

It makes the driving environment space using data from various onboard sensors and the HAD map. It then estimates the vehicle's state using multi-source asynchronous redundant data and adds the HAD map's non-sensorized data on top of that. Moreover, complete estimating the state quantity in the driving environment space [11]. From the review above, the HAD map is a stable base and a powerful supplement to the cooperative perception of ICVs.

## 5.3. Intelligent Decision Support Based On Had Map

Besides perception, the HAD map also plays an important role in the decision-making process of an autonomous vehicle. This subsection focuses on the decision-making roles that HAD maps can support, such as navigation and planning.

## 5.3.1. Navigation

Navigation is an important part of autonomous driving decisionmaking and is also called mission planning [26,36,151,152]. In early autonomous driving, navigation information only used static information the route network definition file (RNDF), waypoints, and road topology for navigation. Subsequently, with the introduction and widespread use

![13_image_1.png](13_image_1.png)

of lane-level maps, road-level navigation algorithms are gradually applied to lane-level navigation [153]. Many methods often establish a special map topology based on the lane-level map for road search. At the same time, different types of costs are also considered when creating the topology map. After that, as the map contains more and more dynamic traffic information based on the distance, the navigation algorithm also considers traffic congestion, fuel consumption, and other data accordingly.

## 5.3.2. Planning

With the development of autonomous driving technology, adding semantic information in the map has further assisted the trajectory planning algorithm[154]. For example, some methods use point clouds to establish a potential field and perform trajectory planning based on the potential field, and some methods use information in a feature map to construct a cost function for trajectory planning. In recent years, with the development of learning-based planning algorithms, more and more planning methods rely on specific knowledge to make decisions [155]. Although this "knowledge" is not stored in the map for the time being, this information is related to geographic features, such as information related to cognitive state, state transition probability, and reward function. Using this information in trajectory planning also helps trajectory planning algorithms, as shown by Diaz-Diaz et al. [156] in Fig. 21.

## 6. Futures And Challenges

This section emphasizes the difficulties that will need to be overcome in the development of high-quality map technology. Here, we emphasize the significance of real-time dynamic updates, a unified map model, strong localization, map data confidence, V2X technology, and the security of map data. Furthermore, we complete this section with a future outlook on the HAD map industry as a whole.

## 6.1. Challenges

6.1.1. Real-time dynamic update of HAD map The real-time dynamic updating of automated driving maps is still challenging, especially for the crowd-sourced map update, which is mainly based on low-cost sensors. How to achieve high-precision maps based on visual data with limited accuracy? Due to the limited mapping accuracy of visual data and the lack of effective scale information, how to ensure the high accuracy and reliability of map element reconstruction based on visual data remains to be solved and broken through. Meanwhile, it is hard to combine data from multiple vehicles and sources that are accurate because the visual data collected by different vehicle ends is different in terms of angle, space-time scale, and other factors. The data from the different vehicle ends is also not always accurate because of things like positioning and matching errors, false detections, and missed detections. This makes it hard to combine data from

![14_image_0.png](14_image_0.png)

multiple vehicles that is accurate. How to ensure the accuracy, and reliability of HAD map crowd-sourced updates is worth studying and facing challenges.

## 6.1.2. Unified Multi-Layer Had Map Model

Though HAD maps have been widely considered a key technology for autonomous driving, the key challenge for HAD maps is determining the levels of geometric, semantic, and real-time information to add to the standard map. Commercial use of HD maps also differs from research use depending on the application, and characteristics such as redundancy, compatibility, modularity, and interoperability are all major considerations that factor into the model and the data size of the map.

A unified and universal multi-layer map model for automated driving maps is lacking. Currently, the existing automated driving map models are not unified in design, expression, interface, and other aspects. It is necessary to closely combine the actual needs of automated driving, especially in the face of complex road traffic scenarios in China, to establish a unified auto-mated driving map model that supports all elements, flexible expansion, and real-time updates.

6.1.3. Robust localization based on HAD map and other *sensors* Although there are some localization algorithms at present, robust positioning still has some challenges in the face of complex traffic scenarios, especially low-cost, high-precision localization at the vehicle end. In the case of loss of GNSS signals at the vehicle end, achieving stable, reliable, and low-cost high-precision positioning in various complex traffic scenarios is a big challenge. Additionally, changes in lighting, weather, and other environmental factors can affect the performance of sensors like LiDAR and cameras. HAD maps may also not accurately reflect environmental changes, such as construction or road damage.

Compounding with the first challenge, the accuracy of the HAD map is critical to achieving accurate localization in ever-changing dynamic environments as illustrated in Fig. 22.

## 6.1.4. The Confidence Level Of Map Data

Maps have been helpful in assisting in navigational tasks and localization, perception, planning, and decision. These important tasks can ensure safety in several driving scenarios. However, the reliability of the map data proposed has its limitations. For example, even though the research direction trends towards the crowdsourcing method of a map update, there remains the challenge of putting a system in place to guarantee the map data is accurate and precise in every scenario. To address this challenge, a framework to quantify the reliability factor of the map data according to the time of the update or the number of updates that have happened in a given area can be a potential solution.

In the meantime, many articles always assume map data is a reliable information source. However, there are still many uncertainties in the construction process that have not been considered. 6.1.5. The combination of V2X *technology* Through the perspective of a single vehicle, the HAD map represents a vast amount of information that must be downloaded and processed before being used to supplement sensor fusion failure scenarios. However, with the addition of vehicle-to-everything (V2X) applications, HAD
maps can be considered a cloud solution where the amount of data can be optimized. The map itself can be broken down into static elements that act as ground truth and dynamic real-time elements that could be shared amongst vehicle nodes, thus lowering both the pre-processing and transmission requirements. Real-time traffic information could be transferred from vehicular nodes to the roadside unit (RSU) infrastructure, effectively building and updating the HAD map through a fleet of autonomous vehicles. The transmission of the real-time portion of the HAD map has been considered from the power and communication efficiency perspective. Though present-day HD maps have been built with top-end professional mapping vehicles, as sensor technology and quality have progressed and the barrier cost has been lowered, the potential for autonomous vehicles to create their high-definition maps has also been explored with promising results in accuracy.

## 6.1.6. The Policy And Security Of Had Map

Accurate 3D map information is related to national defense security. Therefore, strict laws and regulations have been implemented for the HAD map industry. In autonomous driving, HAD maps contain highly detailed and accurate geographical information, making them even more important to national security than traditional navigation electronic maps. For the security of HAD maps, in the process of uploading and publishing HAD maps, it is very important to ensure the security of geographic information by introducing bias and encrypting the data processing module. It is difficult to ensure the timeliness of map data updates and the security of real-time transmission of updated data from many sources by using the traditional offline processing mode of navigation electronic map data plus bias encryption. The policy about data security on the HAD map in China is designed to ensure national security. There is a lack of standards and specifications related to key technologies involved in high-precision maps, which requires the cooperation of government, industries, universities, and research units in the industry. At the same time, laws and regulations must be further promoted to support the development of automated driving, high-precision map-related technology, and industry progress reasonably.

## 6.2. Future Outlook

The future outlook for HAD map technology in the autonomous driving space is poised for significant growth and transformation. As selfdriving cars become increasingly common on the road, the industry is shifting towards a paradigm where strong perception technology takes precedence over traditional positioning technologies. Here is the author's take on the future outlook for HD map technology in this evolving landscape:
1. Rise in Autonomous Vehicle **Deployment**: With each passing year, we can expect a substantial increase in the deployment of autonomous vehicles on the road. As more self-driving cars navigate our streets, the demand for accurate and up-to-date HD maps will grow exponentially. These maps will be a critical foundation for safe and efficient autonomous driving.

2. Enhanced Perception **Technology**: One of the most significant trends in the industry is the emphasis on advanced perception technology. Autonomous vehicles will increasingly rely on a combination of sensors, cameras, LiDAR, and radar to navigate their surroundings. HD maps will complement these sensors by providing highprecision reference data, allowing vehicles to validate their perceptions and make informed decisions.

3. Positioning Technology **Approach**: Traditional positioning technology, such as GPS, is inherently limited in terms of accuracy, especially in downtown, urban canyons, or challenging weather conditions. Autonomous vehicles will rely less on global positioning systems and more on real-time sensor fusion and perception to determine their exact location. HD maps will assist in localization by matching sensor data with known map features with high precision and accuracy.

4. Dynamic Map **Updating**: The future of HD maps will involve dynamic updating in real-time or near-real-time. Maps will no longer be static but will evolve continuously to reflect changing road conditions, construction, accidents, and other dynamic factors. This realtime map data will be essential for route planning, obstacle avoidance, and decision-making in autonomous vehicles.

5. Collaborative **Mapping**: To keep maps accurate and updated, there will be greater collaboration between automakers, tech companies, municipalities, and even individual vehicles. Crowdsourced data and vehicle-to-infrastructure communication will play a significant role in maintaining the integrity of HD maps. This collaboration will result in more comprehensive and reliable mapping datasets.

6. Safety and **Regulation**: As autonomous vehicles become more common, safety regulations and standards will evolve accordingly. HD
maps will play a crucial role in ensuring the safety of self-driving cars, as they can provide a high level of redundancy and validation for the vehicle's perception systems. Regulatory bodies will work closely with the industry to establish map accuracy, updating, and security guidelines.

## 7. Conclusion

HAD map is a necessary database for automotive driving and has become the focus of countries at home and abroad. HAD map plays an important role in automated driving perception, positioning, control, decision-making, planning, and other aspects. However, achieving real-time dynamic updates of high-precision maps is difficult, seriously affecting the safety and reliability of automotive driving. Although the crowdsourcing of high-precision map updates still faces many challenges, the increased effort from governments, industry, universities, and research centers on this domain shows a positive outlook on the future of low-cost HD map building and maintenance. The rapid development and application of automated driving will also affect the advancement of HAD map technology in terms of its technology, policy, laws, and regulations.

## Declaration Of Competing Interest

The authors declare that they have no conflicts of interest in this work.

## Acknowledgments

National Natural Science Foundation of China (U22A20104, 52102464), Beijing Natural Science Foundation (L231008), and Young Elite Scientist Sponsorship Program By BAST (BYESS2022153).

## References

[1] H.G. Seif, X. Hu, Autonomous driving in the iCity-HD maps as a key challenge of the automotive industry, Engineering 2 (2) (2016) 159–162, doi:10.1016/J.ENG.2016.02.010.

[2] Taxonomy and definitions for terms related to driving automation systems for onroad motor vehicles, 2021, 10.4271/J3016_202104.

[3] S. Kuutti, S. Fallah, K. Katsaros, et al., A survey of the state-of-the-art localization techniques and their potentials for autonomous vehicle applications, IEEE Internet Things J. 5 (2) (2018) 829–846, doi:10.1109/JIOT.2018.2812300.

[4] H. Cai, Z. Hu, G. Huang, et al., Integration of GPS, monocular vision, and high definition (HD) map for accurate vehicle localization, Sensors (Switzerland) 18
(10) (2018), doi:10.3390/s18103270.

[5] W.C. Ma, R. Urtasun, I. Tartavull, et al., Exploiting sparse semantic HD
maps for self-driving vehicle localization, in: Proceedings of IEEE International Conference on Intelligent Robots and Systems (IROS), 2019, pp. 5304–5311, doi:10.1109/IROS40897.2019.8968122.

[6] Z. Xiao, D. Yang, T. Wen, et al., Monocular localization with vector HD map
(MLVHM): a low-cost method for commercial IVs, Sensors (Switzerland) 20 (7)
(2020) 1–24, doi:10.3390/s20071870.

[7] J. Jeong, Y. Cho, A. Kim, HDMI-Loc: exploiting high definition map image for precise localization via bitwise particle filter, IEEE Rob. Autom. Lett. 5 (4) (2020)
6310–6317, doi:10.1109/LRA.2020.3013881.

[8] C. Jang, S. Cho, S. Jeong, et al., Traffic light recognition exploiting map and localization at every stage, Expert Syst. Appl. 88 (2017) 290–304, doi:10.1016/j.eswa.2017.07.003.

[9] M. Hirabayashi, A. Sujiwo, A. Monrroy, et al., Traffic light recognition using highdefinition map features, in: Robotics and Autonomous Systems, vol. 111, 2019, pp. 62–72, doi:10.1016/j.robot.2018.10.004.

[10] B. Yang, M. Liang, R. Urtasun, HDNET: Exploiting HD maps for 3D object detection, in: Proceedings of the Conference on Robot Learning, vol. 87, 2018, pp. 146–
155.

[11] Z. Xiao, D. Yang, F. Wen, et al., A unified multiple-target positioning framework for intelligent connected vehicles, Sensors (Switzerland) 19 (9) (2019) 1–22, doi:10.3390/s19091967.

[12] R. Izquierdo, I. Parra, D. Fernández-Llorca, et al., Multi-radar self-calibration method using high-definition digital maps for autonomous driving, in: Proceedings of IEEE Conference on Intelligent Transportation Systems, Proceedings (ITSC),
2018, pp. 2197–2202, doi:10.1109/ITSC.2018.8569272.

[13] B. Paden, M. Čáp, S.Z. Yong, et al., A survey of motion planning and control techniques for self-driving urban vehicles, IEEE Trans. Intell. Veh. 1 (1) (2016) 33–55, doi:10.1109/TIV.2016.2578706.

[14] Z. Jian, S. Zhang, S. Chen, et al., High-definition map combined local motion planning and obstacle avoidance for autonomous driving, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV), 2019, pp. 2180–2186, doi:10.1109/IVS.2019.8814229.

[15] Mobileye, watch how our camera-only AV handles the streets of Munich, 2020, https://www.mobileye.com/blog/munich-av-video/.

[16] Y. Liu, M. Song, Y. Guo, An incremental fusing method for high-definition map updating, in: IEEE, 2019, pp. 4251–4256, doi:10.1109/SMC.2019.8913867.

[17] J.P. Leite, A brief History of GPS In-Car Navigation, 2018, https://ndrive.com/brief-history-gps-car-navigation/.

[18] J. pandazis, Final Report, IST-1999-11206 NextMAO Project, Delierable D1, NextMAP Consortium, Technical Report, 2002.

[19] EDMap, Enhanced Digital Mapping Project Final Report, Technical Report, United States Department of Transportation, Federal Highway Administration and National Highway Traffic and Safety Administration, 2004.

[20] J. Ziegler, P. Bender, M. Schreiber, et al., Making bertha drive-an autonomous journey on a historic route, IEEE Intell. Transp. Syst. Mag. 6 (2) (2014) 8–20, doi:10.1109/MITS.2014.2306552.

[21] K. Jiang, D. Yang, C. Liu, et al., A flexible multi-layer map model designed for lanelevel route planning in autonomous vehicles, Engineering 5 (2) (2019) 305–318, doi:10.1016/j.eng.2018.11.032.

[22] Intelligent Transport Systems-Co-Operative ITS-Local Dynamic MapTechnical Report, ISO/TC 204 Intelligent Transport Systems, 2018.

https://www.iso.org/standard/69433.html
[23] M. Dannehy, 3D Maps: beyond automotive, 2016, https://goo.gl/WpwiiX.

[24] D.G. Yang, K. Jiang, D. Zhao, et al., Intelligent and connected vehicles: current status and future perspectives, Sci. China Technol. Sci. 61 (10) (2018) 1446–
1471.

[25] H. V., Solving the challenges of HD mapping for smart navigation in autonomous cars, 2020, https://www.intellias.com/solving-the-challenges-of-hdmapping-for-smart-navigation-in-autonomous-cars.

[26] R. Liu, J. Wang, B. Zhang, High definition map for automated driving: overview and analysis, J. Navig. 73 (2) (2020) 324–341, doi:10.1017/S0373463319000638.

[27] ISO/TC 204 Intelligent transport systems, ISO/TR 14825:1996 Geographic Data Files (GDF), Technical Report, 1996.

[28] Z. Pan, L. Jingnan, A generalized data model of high definition maps, Acta Geod.

Cartogr. Sin. 50 (11) (2021) 1432–1446, doi:10.11947/j.AGCS.2021.20210254.

[29] X. Zheng, Y. Li, D. Duan, et al., Multivehicle multisensor occupancy grid maps
(MVMS-OGM) for autonomous driving, IEEE Internet Things J. 9 (22) (2022) 22944–22957, doi:10.1109/JIOT.2022.3187827.

[30] A. Elfes, Occupancy grids: a stochastic spatial representation for active robot perception, 2013, http://rpg.ifi.uzh.ch/research_mav.html.

[31] H.P. Moravec, Sensor fusion in certainty grids for mobile robots, Sensor Devices Syst. Rob. 9 (2) (1989) 253–276, doi:10.1007/978-3-642-74567-6_19.

[32] H. Xue, H. Fu, R. Ren, et al., Real-time 3D grid map building for autonomous driving in dynamic environment, in: Proceedings of the 2019 IEEE International Conference on Unmanned Systems (ICUS), IEEE, 2019, pp. 40–45, doi:10.1109/ICUS48101.2019.8996066.

[33] S.J. Han, J. Kim, J. Choi, Effective height-grid map building using inverse perspective image, in: 2015 IEEE Intelligent Vehicles Symposium (IV), Proceedings, 2015, pp. 549–554, doi:10.1109/IVS.2015.7225742.

[34] C. Badue, R. Guidolini, R.V. Carneiro, et al., Self-driving cars: a survey, Expert Syst.

Appl. 165 (2021) 113816, doi:10.1016/j.eswa.2020.113816.

[35] C. Cadena, L. Carlone, H. Carrillo, et al., Past, present, and future of simultaneous localization and mapping: toward the robust-perception age, IEEE Trans. Rob. 32 (6) (2016) 1309–1332, doi:10.1109/TRO.2016.2624754.

[36] J. Liu, J. Xiao, H. Cao, et al., The status and challenges of high precision map for automated driving, in: Proceedings of China Satellite Navigation Conference (CSNC), 2019, pp. 266–276.

[37] P. Beeson, J. Modayil, B. Kuipers, Factoring the mapping problem: mobile robot map-building in the hybrid spatial semantic hierarchy, Int. J. Rob. Res. 29 (4)
(2010) 428–459, doi:10.1177/0278364909100586.

[38] K. Luo, S. Casas, R. Liao, et al., Safety-oriented pedestrian occupancy forecasting, in: Proceedings of IEEE International Conference on Intelligent Robots and Systems
(IROS), 2021, pp. 1015–1022, doi:10.1109/IROS51168.2021.9636691.

[39] F. Mutz, T. Oliveira-Santos, A. Forechi, et al., What is the best grid-map for self-driving cars localization? An evaluation under diverse types of illumination, traffic, and environment, Expert Syst. Appl. 179 (2021) 1–22, doi:10.1016/j.eswa.2021.115077.

[40] S. Mentasti, M. Matteucci, Multi-layer occupancy grid mapping for autonomous vehicles navigation, in: Proceedings of AEIT International Conference of Electrical and Electronic Technologies for Automotive (AEIT AUTOMOTIVE), 2019, doi:10.23919/EETA.2019.8804556.

[41] R.B. Rusu, S. Cousins, 3D Is here: Point cloud library (PCL), in: Proceedings of IEEE International Conference on Robotics and Automation (ICRA), 2011, pp. 1–4, doi:10.1109/ICRA.2011.5980567.

[42] J. Huang, M. Demir, T. Lian, et al., An online multi-lidar dynamic occupancy mapping method, in: 2019 IEEE Intelligent Vehicles Symposium (IV), 2019, pp. 517–
522, doi:10.1109/IVS.2019.8814006.

[43] J. Li, J. Zhao, Y. Kang, et al., DL-SLAM: direct 2.5D LiDAR SLAM for autonomous driving, in: 2019 IEEE Intelligent Vehicles Symposium (IV), IEEE, 2019, pp. 1205– 1210, doi:10.1109/IVS.2019.8813868.

[44] A. Woo, Multi-objective Mapping and Path Planning using Visual SLAM and Object Detection, University of Waterloo, 2019 Master's degree thesis.

[45] M. Mataric, Environment learning using a distributed representation, in: Proceedings of IEEE International Conference on Robotics and Automation (ICRA), vol. 1, 1990, pp. 402–406, doi:10.1109/ROBOT.1990.126009.

[46] F. Savelli, B. Kuipers, Loop-closing and planarity in topological map-building, in:
Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), vol. 2, 2004, pp. 1511–1517, doi:10.1109/IROS.2004.1389610.

[47] E. Garcia-Fidalgo, A. Ortiz, Vision-based topological mapping and localization methods: a survey, Rob. Auton. Syst. 64 (2015) 1–20, doi:10.1016/j.robot.2014.11.009.

[48] Z. Wei, M. Yang, L. Wang, et al., Customized mobile LiDAR system for manhole cover detection and identification, Sensors (Switzerland) 19 (10) (2019),
doi:10.3390/s19102422.

[49] J. Wan, A. Chan, Adaptive density map generation for crowd counting, in: Proceedings of IEEE/CVF International Conference on Computer Vision (ICCV), 2019, pp. 1130–1139, doi:10.1109/ICCV.2019.00122.

[50] I.A. Bârsan, S. Wang, A. Pokrovsky et al. Learning to localize using a LiDAR intensity map, 2020, 2012.10902
[51] B. Wijaya, K. Jiang, M. Yang, et al., Crowdsourced road semantics mapping based on pixel-wise confidence level, Automot. Innov. (0123456789) (2022),
doi:10.1007/s42154-021-00173-x.

[52] Y. Zhang, D. Zhou, S. Chen, et al., Single-image crowd counting via multicolumn convolutional neural network, in: Proceedings of IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 589–597, doi:10.1109/CVPR.2016.70.

[53] C. Zhang, H. Li, X. Wang, et al., Cross-scene crowd counting via deep convolutional neural networks, in: Proceedings of IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 833–841, doi:10.1109/CVPR.2015.7298684.

[54] H. Idrees, I. Saleemi, C. Seibert, et al., Multi-source multi-scale counting in extremely dense crowd images, in: Proceedings of IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2013, pp. 2547–2554, doi:10.1109/CVPR.2013.329.

[55] J. Wan, W. Luo, B. Wu, et al., Residual regression with semantic prior for crowd counting, in: Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2019, pp. 4031–4040, doi:10.1109/CVPR.2019.00416.

[56] D. Paz, H. Zhang, Q. Li, et al., Probabilistic semantic mapping for urban autonomous driving applications, in: IEEE International Conference on Intelligent Robots and Systems, 2020, pp. 2059–2064, doi:10.1109/IROS45743.2020.9341738.

[57] H. Wang, C. Xue, Y. Zhou, et al., Visual semantic localization based on HD
map for autonomous vehicles in urban scenarios, in: Proceedings - IEEE International Conference on Robotics and Automation ICRA, 2021, pp. 11255–11261, doi:10.1109/ICRA48506.2021.9561459.

[58] J. Gao, W. Lin, B. Zhao et al. 3 framework: An open-source pytorch code for crowd counting, 2019, 1907.02724
[59] J. Gao, Q. Wang, X. Li, PCC Net: perspective crowd counting via spatial convolutional network, IEEE Trans. Circuits Syst. Video Technol. 30 (10) (2020) 3486–
3498, doi:10.1109/TCSVT.2019.2919139.

[60] K. Jetlund, E. Onstein, L. Huang, Information exchange between GIS and geospatial its databases based on a generic model, ISPRS Int. J. Geo-Inf. 8 (3) (2019),
doi:10.3390/ijgi8030141.

[61] D. Marius, OpenDRIVE format specification, 2008, http://www.opendrive.org/
download.htm.

[62] M. Dupuis, M. Strobl, H. Grezlikowski, Opendrive 2010 and beyond -status and future of the de facto standard for the description of road networks, 2010.

[63] A. Zang, X. Chen, G. Trajcevski, High definition maps in urban context, SIGSPATIAL
Spec. 10 (1) (2018) 15–20, doi:10.1145/3231541.3231546.

[64] P. Hubertus, M. Schleicher, F. Klebert et al. NDS: the benefits of a common map data standard for autonomous driving (2019) 11.

[65] T. Eiter, H. Füreder, F. Kasslatter, et al., Towards a semantically enriched local dynamic map, Int. J. Intell. Transp.Syst. Res. 17 (1) (2019) 32–48, doi:10.1007/s13177-018-0154-x.

[66] J. Santa, F. Pereñíguez, A. Moragón, et al., Vehicle-to-infrastructure messaging proposal based on CAM/DENM specifications, in: 2013 IFIP Wireless Days (WD), 2013, pp. 1–7, doi:10.1109/WD.2013.6686514.

[67] P. Bender, J. Ziegler, C. Stiller, Lanelets: efficient map representation for autonomous driving, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV),
2014, pp. 420–425, doi:10.1109/IVS.2014.6856487.

[68] F. Poggenhans, J.H. Pauls, J. Janosovits, et al., Lanelet2: a high-definition map framework for the future of automated driving, in: Proceedings of IEEE Conference on Intelligent Transportation Systems (ITSC), 2018, pp. 1672–1679, doi:10.1109/ITSC.2018.8569929.

[69] A. Forum, http://adasis.org/. [70] AECC, Operational behavior of a high definition map application white paper
(2020).

[71] Y. Bisheng, L. Fuxun, H. Ronggang, Progress, challenges and perspectives of 3D
LiDAR point cloud processing, Acta Geod. Cartogr. Sin. 46 (2017) 1509–1516.

[72] E. D. of China Journal of Highway, Transport, Review on China's automotive engineering research progress: 2017, China J. Highway Transp. 30 (6) (2017) 1–
197.

[73] M. Yang, Y. Wan, X. Liu, et al., Laser data based automatic recognition and maintenance of road markings from MLS system, Opt. Laser Technol. 107 (2018) 192–203.

[74] M. Cho, K. Kim, S. Cho, et al., Frequent and automatic update of lane-level HD
maps with a large amount of crowdsourced data acquired from buses and taxis in Seoul, Sensors (Switzerland) 23 (438) (2023) 1–16.

[75] M. Yang, X. Liu, K. Jiang, et al., Automatic extraction of structural and non-structural road edges from mobile laser scanning data, Sensors (Basel) (2019).

[76] P. Kumar, C.P. McElhinney, P. Lewis, et al., Automated road markings extraction from mobile laser scanning data, Int. J. Appl. Earth Observation Geoinf. 32 (2014)
125–137, doi:10.1016/j.jag.2014.03.023.

[77] H. Ma, Z. Pei, Z. Wei, et al., Automatic extraction of road markings from mobile laser scanning data, Int. Arch. Photogramm.Remote Sens. Spatial Inf. Sci. XLII2/W7 (2017) 825–830, doi:10.5194/isprs-archives-XLII-2-W7-825-2017.

[78] H. Guan, J. Li, Y. Yu, et al., Using mobile laser scanning data for automated extraction of road markings, ISPRS J. Photogramm. Remote Sens. 87 (2014) 93–107, doi:10.1016/j.isprsjprs.2013.11.005.

[79] R. Mur-Artal, J.M.M. Montiel, J.D. Tardós, ORB-SLAM: a versatile and accurate monocular slam system, IEEE Trans. Rob. 31 (5) (2015) 1147–1163, doi:10.1109/TRO.2015.2463671.

[80] R. Mur-Artal, J.D. Tardós, ORB-SLAM2: an open-source slam system for monocular, stereo, and RGB-D cameras, IEEE Trans. Rob. 33 (5) (2017) 1255–1262, doi:10.1109/TRO.2017.2705103.

[81] C. Campos, R. Elvira, J.J.G. Rodríguez, et al., ORB-SLAM3: an accurate open-source library for visual, visual-inertial, and multimap slam, IEEE Trans. Rob. 37 (6)
(2021) 1874–1890, doi:10.1109/TRO.2021.3075644.

[82] N. Haala, Peter, J. Kremer, et al., Mobile LiDAR mapping for 3D point cloud collecation in urban areas: a performance test, 2008.

[83] B. Riveiro, H. González-Jorge, J. Martínez-Sánchez, et al., Automatic detection of zebra crossings from mobile LiDAR data, Opt. Laser Technol. 70 (2015) 63–70, doi:10.1016/j.optlastec.2015.01.011.

[84] M. Rezaei, M. Amiri, P. Mohajeri, et al., A new algorithm for lane detection and tracking on pulsed field gel electrophoresis images, Chemom. Intell. Lab. Syst. 157
(2016) 1–6, doi:10.1016/j.chemolab.2016.05.018.

[85] S.-C. Yi, Y.-C. Chen, C.-H. Chang, A lane detection approach based on intelligent vision, Comput. Electr. Eng. 42 (2015) 23–29, doi:10.1016/j.compeleceng.2015.01.002.

[86] Y. Tian, J. Gelernter, X. Wang, et al., Lane marking detection via deep convolutional neural network, Neurocomputing 280 (2018) 46–55, doi:10.1016/j.neucom.2017.09.098. Applications of Neural Modeling in the new era for data and IT
[87] S.L. Phung, M.C. Le, A. Bouzerdoum, Pedestrian lane detection in unstructured scenes for assistive navigation, Comput. Vis. Image Understanding 149 (2016) 186–
196, doi:10.1016/j.cviu.2016.01.011.

[88] H. Du, Z. Xu, Y. Ding, The fast lane detection of road using RANSAC algorithm, in:
J. Abawajy, K.-K. R. Choo, R. Islam (Eds.), International Conference on Applications and Techniques in Cyber Security and Intelligence, 2018, pp. 1–7.

[89] Y.Y. Ye, X.L. Hao, H.J. Chen, Lane detection method based on lane structural analysis and CNNs, IET Intell. Transp. Syst. 12 (6) (2018) 513–520, doi:10.1049/iet-its.2017.0143.

[90] C.H. Quach, V.L. Tran, D.H. Nguyen, et al., Real-time lane marker detection using template matching with RGB-D camera, in: Proceedings of International Conference on Recent Advances in Signal Processing, Telecommunications & Computing
(SigTelCom), 2018, pp. 152–157, doi:10.1109/SIGTELCOM.2018.8325781.

[91] J. Kim, J. Kim, G.-J. Jang, et al., Fast learning method for convolutional neural networks using extreme learning machine and its application to lane detection, Neural Netw. 87 (2017) 109–121, doi:10.1016/j.neunet.2016.12.002.

[92] H. Wong, X. Zhang, T. Wen, et al., HD-Map aided LiDAR-INS extrinsic calibration, in: Proceedings of IEEE International Intelligent Transportation Systems Conference (ITSC), 2021, pp. 3136–3143, doi:10.1109/ITSC48978.2021.9564813.

[93] R. Wang, Y. Jian, X.-Y. Li, et al., Designation and verification of road markings detection and guidance method, in: Proceedings of International Conference on Optical Instruments and Technology: Optoelectronic Imaging/Spectroscopy and Signal Processing Technology, 2018, p. 1062006.

[94] Apollo mapping, https://apollomapping.com/.

[95] Alibaba, AMAP's transformation from navigation positioning to high-precision positioning, 2020, https://www.alibabacloud.com/blog/amaps-transformationfrom-navigation-positioning-to -high-precision-positioning_596546.

[96] Navinfo HD map, https://navinfo.com/en/hdmap.

[97] HERE Technologies, HERE HD live map technical paper(2017).

[98] TomTom International BV, More than 5 million vehicles now rely on TomTom's maps for automated driving, 2022, https://www.globenewswire.com/en/
news-release/2022/01/06/2362115/0/en/More-than-5-million-vehicles-now-rely
-on-TomTom-s- maps-for-automated-driving.html.

[99] Dynamic map and cooperation area, https://www.dynamic-maps.co.jp/en/index.

html.

[100] Building maps for a self-driving car, 2016, https://blog.waymo.com/2019/09/
building-maps-for-self-driving-car.html.

[101] D. Silver, Deep dive on mobileye REM maps, 2021, https://medium.

com/self-driving-cars/deep-dive-on-mobileye-rem-maps-4a107d55acf0.

[102] Uber HD map, https://developer.uber.com/solutions/maps. [103] Apple map, https://www.apple.com/maps.

[104] Autonavi navigation HD, https://mobile.amap.com/.

[105] TomTom, Extending the vision of automated vehicles with HD maps and ADASIS,
https://Www.Tomtom.Com/Products/Hd-Map/(2020) 9.

[106] Here HD live map | autonomous driving system, https://www.here.com/platform/HD-live-map.

[107] Waymo, The Waymo driver handbook: how our highly-detailed maps help unlock new locations for autonomous driving, 2020, https://blog.waymo.com/2020/09/the-waymo-driver-handbook-mapping.html.

[108] Mobileye HD map, https://www.mobileye.com/technology/rem/. [109] Lyft level 5 open data dataset, https://level5.lyft.com/dataset/?source=post_page.

[110] Naver labs - open dataset, https://www.naverlabs.com/datasets.

[111] Argoverse dateset, https://www.argoverse.org. [112] M.O. TAŞ, H. Serhan YAVUZ, A. YAZICI, Updating HD-maps for autonomous transfer vehicles in smart factories, in: Proceedings of International Conference on Control Engineering and Information Technology (CEIT), 2018, pp. 1–5, doi:10.1109/CEIT.2018.8751934.

[113] C. Kim, S. Cho, M. Sunwoo, et al., Crowd-sourced mapping of new feature layer for high-definition map, Sensors (Switzerland) 18 (12) (2018) 1–17, doi:10.3390/s18124172.

[114] C. Kim, S. Cho, M. Sunwoo, et al., Updating point cloud layer of high definition (HD)
map based on crowd-sourcing of multiple vehicles installed LiDAR, IEEE Access 9
(2021) 8028–8046, doi:10.1109/ACCESS.2021.3049482.

[115] K. Kim, S. Cho, W. Chung, HD map update for autonomous driving with crowdsourced data, IEEE Rob. Autom. Lett. 6 (2) (2021) 1895–1901, doi:10.1109/LRA.2021.3060406.

[116] M. Liebner, D. Jain, J. Schauseil, et al., Crowdsourced HD map patches based on road model inference and graph-based slam, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV), 2019, pp. 1211–1218, doi:10.1109/IVS.2019.8813860.

[117] A. Stoven-Dubois, K.K. Miguel, A. Dziri, et al., A collaborative framework for highdefinition mapping, in: Proceedings of IEEE Intelligent Transportation Systems Conference (ITSC), 2019, pp. 1845–1850, doi:10.1109/ITSC.2019.8917292.

[118] M. Herb, T. Weiherer, N. Navab, et al., Crowd-sourced semantic edge mapping for autonomous vehicles, in: Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2019, pp. 7047–7053, doi:10.1109/IROS40897.2019.8968020.

[119] A.K. Aijazi, P. Checchin, L. Trassoudaine, Automatic removal of imperfections and change detection for accurate 3D urban cartography by classification and incremental updating, Remote Sens. 5 (8) (2013) 3701–3728, doi:10.3390/rs5083701.

[120] D. Pannen, M. Liebner, W. Hempel, et al., How to keep HD maps for automated driving up to date, in: Proceedings of IEEE International Conference on Robotics and Automation (ICRA), 2020, pp. 2288–2294, doi:10.1109/ICRA40945.2020.9197419.

[121] K. Jo, C. Kim, M. Sunwoo, Simultaneous localization and map change update for the high definition map-based autonomous driving car, Sensors (Switzerland) 18 (9) (2018), doi:10.3390/s18093145.

[122] M. Heo, J. Kim, S. Kim, HD map change detection with cross-domain deep metric learning, in: Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2020, pp. 10218–10224.

[123] P. Zhang, M. Zhang, J. Liu, Real-time HD map change detection for crowdsourcing update based on mid-to-high-end sensors, Sensors (Switzerland) 21 (7) (2021) 1–
12, doi:10.3390/s21072477.

[124] J. Lambert, J. Hays, Trust, but verify: cross-modality fusion for HD map change detection, in: Proceedings of Conference on Neural Information Processing Systems
(NeurIPS), 2021, pp. 1–14.

[125] T. Wen, Z. Xiao, K. Jiang, et al., High precision target positioning method for RSU in cooperative perception, in: Proceedings of IEEE International Workshop on Multimedia Signal Processing (MMSP), 2019, pp. 1–6, doi:10.1109/MMSP.2019.8901755.

[126] T. Wen, Z. Xiao, B. Wijaya, et al., High precision vehicle localization based on tightly-coupled visual odometry and vector HD map, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV), 2020, pp. 672–679, doi:10.1109/IV47402.2020.9304659.

[127] K. Jiang, X. Zhang, B. Qin, et al., Feature-based loop closure detection and optimization for LiDAR mapping, in: Proceedings of International Forum on Connected Automated Vehicle Highway System through the China Highway & Transportation Society, 2020, doi:10.4271/2020-01-5225.

[128] T. Wen, K. Jiang, B. Wijaya, et al., TM3Loc: Tightly-coupled monocular map matching for high precision vehicle localization, IEEE Trans. Intell. Transp.Syst. 23 (11)
(2022) 20268–20281, doi:10.1109/TITS.2022.3176914.

[129] Z. Xiao, K. Jiang, S. Xie, et al., Monocular vehicle self-localization method based on compact semantic map, in: Proceedings of International Conference on Intelligent Transportation Systems (ITSC), 2018, pp. 3083–3090, doi:10.1109/ITSC.2018.8569274.

[130] R.P.D. Vivacqua, M. Bertozzi, P. Cerri, et al., Self-localization based on visual lane marking maps: an accurate low-cost approach for autonomous driving, IEEE Trans. Intell. Transp.Syst. 19 (2) (2018) 582–597, doi:10.1109/TITS.2017.

2752461.

[131] J. Cheng, Z. Wang, H. Zhou, et al., DM-SLAM: a feature-based slam system for rigid dynamic scenes, ISPRS Int. J. Geo-Inf. 9 (4) (2020), doi:10.3390/ijgi9040202.

https://www.mdpi.com/2220-9964/9/4/202
[132] J.-E. Deschaud, IMLS-SLAM: scan-to-model matching based on 3D data, in: Proceedings of IEEE International Conference on Robotics and Automation (ICRA),
2018, pp. 2480–2485, doi:10.1109/ICRA.2018.8460653.

[133] A.R. Khairuddin, M.S. Talib, H. Haron, Review on simultaneous localization and mapping (slam), in: Proceedings of IEEE International Conference on Control System, Computing and Engineering (ICCSCE), 2015, pp. 85–90, doi:10.1109/ICCSCE.2015.7482163.

[134] K. Yoneda, H. Tehrani, T. Ogawa, et al., Lidar scan feature for localization with highly precise 3-D map, in: Proceedings of IEEE Intelligent Vehicles Symposium
(IV), 2014, pp. 1345–1350, doi:10.1109/IVS.2014.6856596.

[135] S. Kato, E. Takeuchi, Y. Ishiguro, et al., An open approach to autonomous vehicles, IEEE Micro 35 (6) (2015) 60–68, doi:10.1109/MM.2015.133.

[136] J. Levinson, S. Thrun, Robust vehicle localization in urban environments using probabilistic maps, in: Proceedings of IEEE International Conference on Robotics and Automation (ICRA), 2010, pp. 4372–4378, doi:10.1109/ROBOT.2010.5509700.

[137] W. Ding, S. Hou, H. Gao, et al., LiDAR inertial odometry aided robust LiDAR
localization system in changing city scenes, in: Proceedings of IEEE International Conference on Robotics and Automation (ICRA), 2020, pp. 4322–4328, doi:10.1109/ICRA40945.2020.9196698.

[138] S. Bauer, Y. Alkhorshid, G. Wanielik, Using high-definition maps for precise urban vehicle localization, in: Proceedings of IEEE International Conference on Intelligent Transportation Systems (ITSC), 2016, pp. 492–497, doi:10.1109/ITSC.2016.7795600.

[139] O. Pink, Visual map matching and localization using a global feature map, in:
2008 IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops, CVPR Workshops, 2008, pp. 1–7, doi:10.1109/CVPRW.2008.

4563135.

[140] M. Schreiber, C. Knöppel, U. Franke, LaneLoc: lane marking based localization using highly accurate maps, in: Proceedings of IEEE Intelligent Vehicles Symposium
(IV), 2013, pp. 449–454, doi:10.1109/IVS.2013.6629509.

[141] H. Deusch, J. Wiest, S. Reuter, et al., Multi-sensor self-localization based on maximally stable extremal regions, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV), 2014, pp. 555–560, doi:10.1109/IVS.2014.6856413.

[142] Z. Tao, P. Bonnifait, V. Frémont, et al., Mapping and localization using GPS,
lane markings and proprioceptive sensors, in: Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2013, pp. 406–412, doi:10.1109/IROS.2013.6696383.

[143] C. Allig, G. Wanielik, Alignment of perception information for cooperative perception, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV), 2019, pp. 1849–
1854, doi:10.1109/IVS.2019.8814108.

[144] S.-W. Kim, B. Qin, Z.J. Chong, et al., Multivehicle cooperative driving using cooperative perception: design and experimental validation, IEEE Trans. Intell.

Transp.Syst. 16 (2) (2015) 663–680, doi:10.1109/TITS.2014.2337316.

[145] K. Jiang, Y. Shi, B. Wijaya et al. Map container: a map-based framework for cooperative perception, 2022, 2208.13226
[146] J. Van Brummelen, M. O'Brien, D. Gruyer, et al., Autonomous vehicle perception:
the technology of today and tomorrow, Transp. Res. Part C Emerg.Technol. 89 (2018) 384–406, doi:10.1016/j.trc.2018.02.012.

[147] F. Ghallabi, M.-A. Mittet, G. EL-HAJ-SHHADE, et al., LIDAR-based high reflective landmarks (HRL)s for vehicle localization in an HD map, in: Proceedings of IEEE Intelligent Transportation Systems Conference (ITSC), 2019, pp. 4412–4418, doi:10.1109/ITSC.2019.8917057.

[148] S.-W. Kim, B. Qin, Z.J. Chong, et al., Multivehicle cooperative driving using cooperative perception: design and experimental validation, IEEE Trans. Intell. Transp.Syst. 16 (2) (2015) 663–680, doi:10.1109/TITS.2014.2337316.

[149] A. Rauch, F. Klanner, R. Rasshofer, et al., Car2X-based perception in a high-level fusion architecture for cooperative perception systems, in: Proceedings of IEEE Intelligent Vehicles Symposium (IV), 2012, pp. 270–275, doi:10.1109/IVS.2012.6232130.

[150] S.-W. Kim, W. Liu, Cooperative autonomous driving: a mirror neuron inspired intention awareness and cooperative perception approach, IEEE Intell. Transp. Syst.

Mag. 8 (3) (2016) 23–32, doi:10.1109/MITS.2016.2573339.

[151] P. Fankhauser, M. Hutter, A universal grid map library: implementation and use case for rough terrain navigation, 2016, pp. 99–120. Cham
[152] P. Groves, Principles of GNSS, Inertial, and Multisensor Integrated Navigation Systems, Artech House, 2007, p. 800.

[153] M. Elsheikh, A. Noureldin, M. Korenberg, Integration of GNSS precise point positioning and reduced inertial sensor system for lane-level car navigation, IEEE Trans.

Intell. Transp.Syst. 23 (3) (2022) 2246–2261, doi:10.1109/TITS.2020.3040955.

[154] J. Choi, Kinodynamic motion planning for autonomous vehicles, Int. J. Adv. Rob.

![18_image_1.png](18_image_1.png)

Syst. 11 (6) (2014) 90, doi:10.5772/58683.

[155] H. Song, D. Luan, W. Ding, et al., Learning to predict vehicle trajectories with model-based planning, in: Proceedings of the Conference on Robot Learning, vol. 164, 2022, pp. 1035–1045.

[156] A. Diaz-Diaz, M. Ocana, A. Llamazares et al. HD maps: exploiting OpenDRIVE potential for path planning and map monitoring, IEEE Intelligent Vehicles Symposium
(IV), Proceedings(2022) 1211–1217. 10.1109/IV51971.2022.9827297
[157] S. Zheng, J. Wang, High definition map-based vehicle localization for highly automated driving: Geometric analysis, in: Proceedings of International Conference on Localization and GNSS (ICL-GNSS), 2018, pp. 1–8, doi:10.1109/ICL-GNSS.2017.8376252.

Mengmeng **Yang** received the PhD degree in Photogrammetry and Remote Sensing from Wuhan University, Wuhan,China in 2018. She is currently an assistant research professor at Tsinghua University, Beijing, China. Her research interests include autonomous vehicles, high precision digital map, and sensor fusion.

Kun **Jiang** received the BS degree in mechanical and automation engineering from Shanghai Jiao Tong University, Shanghai, China in 2011. Then he received the Master degree in mechatronics system and the PhD degree in information and systems technologies from University of Technology of Compiegne (UTC), Compiegne, France, in 2013 and 2016, respectively. He is currently an assistant research professor at Tsinghua University, Beijing, China. His research interests include autonomous vehicles, high precision digital map, and sensor fusion.

Benny **Wijaya** received the BS degree in mechanical engineering from University of Newcastle, Newcastle, Australia in 2015. Then he received the Master degree in mechanical engineering from Tsinghua University, Beijing, China in 2020. He is currently working toward the PhD degree at the School of Vehicle and Mobility in Tsinghua University, Beijing, China. His research interests include, sensor fusion, confidence modelling, and high definition mapping and update for autonomous driving.

Tuopu Wen received the BS degree from Electronic Engineering, Tsinghua University, Beijing, China in 2018. He is currently working toward the PhD degree at the School of Vehicle

![18_image_0.png](18_image_0.png)

and Mobility of Tsinghua University, Beijing, China. His research interests include computer vision, high definition map, and high precision localization for autonomous driving.

Jinyu **Miao** received the BS degree in Automation from Beihang University, Beijing, China in 2019. Then he received the MSc degree in Control Science and Engineering from Beihang University, Beijing, China in 2022. He is currently pursuing the PhD degree at the School of Vehicle and Mobility in Tsinghua University, Beijing, China. His research interests include highprecision localization and mapping for autonomous driving.

Jin **Huang** received his PhD and BE degrees from the College of Mechanical and Vehicle Engineering, Hunan University, China, in 2012 and 2006. He is also a joint PhD in the George W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, Atlanta, Georgia, USA, during 2009–2011.

He started his career at School of Software, Tsinghua University, Beijing, China, since 2013. He is now serve as an Associate Professor at School of Vehicle and Mobility, Tsinghua University. His research interests include artificial intelligence in Intelligent Transportation Systems, dynamics control, fuzzy engineering, etc.

Diange **Yang** received his PhD in Automotive Engineering from Tsinghua University in 2001. He is now a Professor at the school of vehicle and mobility at Tsinghua University. He currently serves as the director of the Tsinghua University Development & Planning Division. His research interests include autonomous driving, environment perception, and HD map. He has more than 180 technical publications and 100 patents.

He received the National Technology Invention Award and Science and Technology Progress Award in 2010, 2013, 2018, and the Special Prize for Progress in Science and Technology of China Automobile Industry in 2019.