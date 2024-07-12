

![0_image_0.png](0_image_0.png)

![0_image_2.png](0_image_2.png)

![0_image_3.png](0_image_3.png)

![0_image_4.png](0_image_4.png)

Contents lists available at ScienceDirect Physica A: Statistical Mechanics and its Applications 

![0_image_1.png](0_image_1.png)

journal homepage: www.elsevier.com/locate/physa 

## The Impacts Of Connected Autonomous Vehicles On Mixed Traffic Flow: A Comprehensive Review

Yuchen Pan a, Yu Wu a, Lu Xu a,*, Chengyi Xia b, David L. Olson c a School of Information Resource Management, Renmin University of China, Beijing 100872, China b School of Artificial Intelligence, Tiangong University, Tianjin 300387, China c *College of Business Administration, University of Nebraska-Lincoln, Lincoln, NE 68588-4114, United States* ARTICLE INFO 

| Keywords:  Automated vehicles  Mixed traffic flow  Connected vehicles  Energy usage  Safety   |
|-----------------------------------------------------------------------------------------------|

## Abstract

The rapid improvements in communication and self-driving technology in recent years have made connected autonomous cars an essential component of urban road transit. Connected autonomous vehicles excel in eliminating uncertainties arising from human driving behaviors. Consequently, they alleviate the issue of 'phantom congestion', a phenomenon that significantly impacts traffic efficiency, safety and sustainability while simultaneously enhancing overall traffic flow stability and safety. Moreover, the increasing adoption of connected autonomous vehicles has led to improved driving efficiency, resulting in reduced energy emissions and decreased environmental pollution. This paper endeavors to conduct an extensive review concerning the effects of CAVs on mixed traffic flows, with a primary emphasis on their impact on traffic efficiency and congestion. 

Additionally, secondary aspects such as stability, safety, and environmental repercussions will be addressed. The article begins with a concise historical account of connected autonomous vehicles and their related technologies. Subsequently, an investigation was conducted into their impact on the mixed traffic environment, along with corresponding policy recommendations. Finally, potential avenues for future research were identified. 

## 1. **Introduction**

In the past few years, substantial progress in communication technology, artificial intelligence, and autonomous driving tech has spurred the emergence of self-driving automobiles, connected vehicles, and associated breakthroughs. Autonomous vehicles (AVs) 
constitute a novel category of automobiles that rely on internal sensors and computing systems to autonomously make driving decisions. AVs can be considered as computer-controlled entities [1] or defined as vehicles equipped with integrated computers [2]. The origins of autonomous driving technique can be traced back to the early 1900 s. The fundamental concept involves the substitution of certain or all human driving tasks with electronic and mechanical systems [3]. During that era, technological progress primarily revolved around basic cruise control systems, including autonomous speed regulation, braking mechanisms, and lane control [4]. 

During the period of rapid development of connected self-driving cars, V2X real-time communication technology can better optimize the traffic flow and enable a new phase of self-driving research [1]. 

Human driving behavior often exhibits uncertainty and instability, resulting in traffic flow characterized by unpredictability [5]. 

This behavior frequently leads to abrupt starts and stops, congestion, and traffic accidents, collectively contributing to the 
* Corresponding author. 

E-mail address: rzxulu@ruc.edu.cn (L. Xu). 

https://doi.org/10.1016/j.physa.2023.129454 Received 19 September 2023; Received in revised form 6 December 2023; Accepted 20 December 2023 Available online 3 January 2024 0378-4371/© 2024 Elsevier B.V. All rights reserved.

phenomenon known as "phantom congestion" [6]. The congestion we face on today's roads is a major challenge when it comes to controlling and managing traffic flow. Connected autonomous driving shows its potential in optimizing traffic flow [3]. However, the real-time communication system in these vehicles, while highly accessible, also exposes them to risks like cyber-attacks and information leaks. Examples include potential attacks on external systems leading to communication failures or manipulation of critical data, which can result in unsafe driving behaviors [7]. 

Compared to traditional human-driven cars, connected autonomous vehicles can exchange data between vehicles and infrastructure in real-time and without delays. This exchange greatly enhances reliable support for driving decisions, countering potential threats stemming from the instability of human driving behavior. Consequently, these vehicles can swiftly respond to traffic conditions, improving driving efficiency and to some extent, reducing congestion and the occurrence of accidents [8]. The improvement in traffic capacity and communication speed also positively impacts the resource utilization of autonomous driving, which also aids in decreasing unnecessary energy emissions, promoting environmental sustainability [9]. 

Currently, connected autonomous vehicles (CAVs) have gained significant prominence in research. While numerous articles have explored the technological advancements and potential impacts of CAVs, there remains a limited body of literature comprehensively addressing their potential effects on mixed traffic flow, and corresponding integrated policy recommendations. Thus, the paper focuses primarily on the current state of CAV, its implications on hybrid traffic flow, particularly emphasizing the core issue of CAVs' impact on traffic efficiency. It also offers fundamental policy recommendations for the development of CAV. Finally, potential future research directions are proposed. 

The primary contribution of this paper lies in shifting focus away from solely examining specific subsets of CAVs' impact on mixed traffic flow. Instead, it simultaneously considers traffic efficiency, traffic flow stability, safety, environmental friendliness, and energy consumption from an integrated perspective, comprehending their interconnections. This comprehensive assessment of the collective performance of hybrid traffic flow facilitates the delivery of thorough and dependable data to policymakers. Such an approach is beneficial for the strategic deployment of CAV implementation. 

The paper follows this structure: Section 2 gives an overview of the developmental history of AVs and CAVs, along with relevant technological foundations. Section 3 explores the core implications of CAV on hybrid traffic flow—traffic Productivity—covering measurement factors and vehicle control. Section 4 discusses other impacts of CAVs on hybrid traffic flow, emphasizing stability, security, and environmental factors. Section 5 presents policy recommendations associated with CAV development and compares policies from representative countries. Section 6 outlines potential future research directions. Section 7 provides a concise summary of the entire document. 

## 2. **Overview Of Connected Autonomous Vehicles** 2.1. History Background

The earliest recorded accounts of autonomous automobiles date back to the early 1920 s [10], with General Motors introducing the concept in 1939 [3]. During the 1980 s, researchers directed their efforts towards developing an automated highway system [11,12], which laid the foundation for integrating self-driving cars with highway infrastructure. From the 1980 s to the early 2000 s, the U.S. 

Department of Defense's Advanced Research Projects Agency (DARPA) contributes to the developments of advancing autonomous vehicle technology. DARPA launched the "Grand Challenges Program," expanding autonomous vehicle competitions from desert environments to simulated urban settings, significantly expediting the progress of autonomous vehicles, as detailed by Pendleton [10] 
and Shladover [3]. 

Currently, numerous enterprises are actively engaged in the realm of autonomous driving, primarily categorized into traditional automobile manufacturers, internet technology firms, and emerging startups specializing in autonomous driving. In the United States, Google initiated its self-driving project back in 2009, garnering significant attention within the industry. By 2016, Waymo emerged as an autonomous driving technology entity independent of Alphabet, introducing the Waymo One autonomous ride-hailing application. Over recent years, Waymo has consistently expanded its suite of services. Tesla, on the other hand, concentrates on the holistic 

| Table 1  Development of representative autonomous car companies.  Firms Competitive landscapes   | Major developments                                                             |                                                                                           |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Waymo[13]                                                                                        | Autonomous driving network about car travel services,                          | Received its driverless deployment permit from the California Public Utilities            |
| autonomous driving technology                                                                    | Commission (CPUC) in In August 2023                                            |                                                                                           |
| Tesla[14]                                                                                        | Design, development, manufacture and sales of electric                         | Announced a $1 billion investment in 2023 to develop a Doj project designed               |
| autonomous vehicles and power transmission components                                            | to manage large amounts of data, especially video data from Tesla              |                                                                                           |
| Nissan[15]                                                                                       | Advanced autonomous driving assistance system,                                 | Tried a driverless taxi service in parts of Suzhou, China in 2023, with technical         |
| autonomous vehicle manufacturing                                                                 | support from Wenyuan Zhixing (WeRide)                                          |                                                                                           |
| Pony ai[16]                                                                                      | Autonomous mobility services, autonomous trucks,                               | Pony.ai, in partnership with Toyota and using the startup's self-driving                  |
| intelligent driving of passenger cars                                                            | technology and ride-hailing services, plans to mass-produce robotaxis in China |                                                                                           |
| Mercedes-Benz                                                                                    | Advanced electric vehicle manufacturing, autonomous                            | Launch of independently developed operating system MB.OS to enhance                       |
| [17]                                                                                             | driving software system                                                        | intelligent driver assistance features or L3 conditional autonomous driving  capabilities |
| Volkswagen                                                                                       | Autonomous vehicle manufacturing, autonomous driving                           | It plans to roll out roughly ten ID Buzz electric vehicles with an autonomous             |
| Group[18]                                                                                        | technology                                                                     | driving system created in collaboration with Mobileye by the end of 2023.                 |

development cycle of electric autonomous vehicles and their power transmission components. 

In China, both Apollo and Pony.ai direct their efforts toward advancing autonomous driving technology and manufacturing autonomous vehicles, concurrently propelling the growth of autonomous ride-hailing platforms. In Japan, traditional automotive giants like Nissan and Toyota have commenced their foray into autonomous driving operations. Their approach primarily revolves around a blend of collaborations with technology companies and self-directed research to advance their autonomous driving technology. 

Across Europe, Mercedes-Benz, renowned for its advanced automobile manufacturing, has recently begun prioritizing its autonomous driving initiatives. Their latest independent development, the MB.OS operating system, aims to augment intelligent driving assistance functions and Level 3 conditional autonomous driving capabilities. The following table offers a more lucid representation of the current developmental landscape of key autonomous driving companies from various regions.. 

According to reports, it is predicted that self-driving cars will make up about 50% of all road trips by 2045 [19,20]. The transportation landscape is rapidly changing due to new technologies, for example, smartphones, social networks and AI-equipped autonomous vehicles [21–23]. Car automation is one of the top ten disruptive technologies of the future, according to Manyika [24]. 

In 2020, the autonomous driving car industry reached a significant milestone in its commercial integration into a broader market, largely driven by the intensifying competition among enterprises within the autonomous driving sector [25,26]. Various studies indicate that the AV market is moving towards a state of maturity by the middle of this century. Based on previous developments and deployments in intelligent vehicle technologies, it is anticipated that by 2040, self-driving cars will constitute approximately 50% of the total car sales and contribute to around 40% of automotive travel. Report does, however, also highlight the fact that major advantages like reduced traffic, autonomous travel options for low-income populations, improved safety, and lower emissions can only be felt to the fullest extent when the number of AV reaches a critical mass and their prices are affordable for most people [20]. At this juncture, there might even be a need to impose restrictions on the utilization of specific human-driven vehicles. Therefore, comprehending future challenges and promptly capitalizing on the opportunities they present is paramount for the prospective advancement of intelligent urban transportation [27]. 

## 2.2. Autonomous Technology

After continuous development, self-driving cars have been classified into different levels based on various standards. According to the National Highway Traffic Safety Administration (NHTSA) standards, self-driving cars can be categorized into five levels [28]. Fig. 1 shows the five levels of autonomous vehicles. Level 0 signifies a car with no self-driving capability, requiring the driver to fully control the vehicle. Level 1 indicates some degree of assistance, such as assisted braking or cruise control. Level 2 represents "partially automated" vehicles. Level 3 is termed "conditionally automated", allowing the automated system to operate relatively independently under certain conditions. Level 4 signifies a high level of automation, indicating that under suitable environmental conditions, a self-driving car can autonomously execute predetermined driving tasks without requiring human intervention or manual operation. 

Finally, Level 5 represents "fully automated" vehicles, capable of taking over all driving responsibilities from a human driver. However, it's worth noting that while this classification serves as one criterion for assessing self-driving cars' levels, academia has yet to establish a strict definition. As a result, any level of "automation" is considered an attribute of self-driving cars [27]. 

Irrespective of the degree of autonomy, achieving autonomous driving entails a spectrum of functionalities, including positioning, sensing, planning, controlling, and management [30]. Positioning and sensing rely on information gathering and acquisition. When an autonomous vehicle can communicate with other vehicle infrastructures to coordinate its operations, it is referred to as a connected automated vehicle [3]. In contrast, when a manually-driven vehicle communicates with other cars and infrastructures to gather data and coordinate operations, it is regarded as a connected vehicle (CV) [30]. Consequently, connected vehicle technologies complement, advance, and synergize with the implementation of autonomous vehicle technologies to a certain extent [3]. 

Thus, connected drive technologies are integral parts of self-driving car program [28]. It improves driving efficiency by allowing CV 
to communicate in real time with infrastructure and other CV. This communication can be categorized into several modes, including vehicle-to-vehicle communication (V2V), vehicle-to-infrastructure communication (V2I), and vehicle-to-cloud communication (V2C). Additionally, Fang et al. [31] have suggested that vehicle-to-pedestrian (V2P) and vehicle-to-network (V2N) communication can also be considered part of this networked Intelligent Transportation System (ITS). All these communication mechanisms collectively fall under the term "vehicle-to-everything" (V2X), which is synonymous with the Internet of Vehicles [32]. Autonomous vehicles and 

| Study on traffic efficiency of mixed traffic flow.  Study Model / Framework Conclusion  [44] Car follower model Self-stabilizing effect can enhance the stability of heterogeneous traffic flow and alleviate traffic congestion.  Increasing the proportion of autonomous vehicles could also help stabilize heterogeneous traffic flows  [46] Mixed traffic flow model Demonstrate that self-driving cars can improve traffic efficiency and reduce energy consumption using three  metrics-traffic assessment  [48] Synergistic drive strategies CDS-L  Networked autonomous driving reduces traffic fluctuations and improves traffic efficiency  and CDS-G  [54] General vehicles follow the frame The permeability and spatial distribution of connected vehicles are intimately related to traffic stability. Connected  vehicles can significantly enhance the stability of traffic flow and improve traffic efficiency  [55] Cellular automata model As autonomous vehicle penetration and fleet size increase, overall capacity increases, reducing congestion   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Table 3  metrics of mixed traffic flow efficiency.  Study Index   | Conclusion                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [46]                                                              | Traffic flow, average speed and quantity of vehicles                                                                                                                                                                     | The outcomes of simulations demonstrate that self-driving cars can lower energy usage  and increase traffic efficiency. Elevated degrees of automation and an increased  quantity of autonomous vehicles have the potential to enhance transportation  effectiveness and minimize energy usage. |
| [47]                                                              | 19 factors, divided into 4 categories: vehicle characteristics,                                                                                                                                                          | Policymakers should be aware of the variables that may affect how autonomous                                                                                                                                                                                                                    |
| travel behavior, network characteristics, and policies            | vehicles affect traffic flow, as the impact of these vehicles varies depending on a  number of metropolitan characteristics. Additionally, different scenarios for linked  autonomous driving exist in different cities. |                                                                                                                                                                                                                                                                                                 |
| [56]                                                              | Uniform performance indicators composed of traffic                                                                                                                                                                       | Overall traffic performance, including single-vehicle and multi-vehicle safety as well as                                                                                                                                                                                                       |
| efficiency, multi-vehicle safety and single-vehicle safety        | traffic efficiency, has improved with increased market penetration. Furthermore, selfdriving cars have a bigger effect on traffic performance overall on cloudy days than on  bright ones.                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                 |
| [57]                                                              | Automation level, penetration, and kind of vehicle                                                                                                                                                                       | CAVs have a gradual and non-linear influence on traffic efficiency and safety, with the  greatest benefits occurring at MPR ranges of 20 to 40%.                                                                                                                                                |
| [59]                                                              | Permeability, vehicle connectivity, road capacity and speed                                                                                                                                                              | The road capacity is significantly increased by the high permeability. Furthermore,  vehicle connectivity allows for quick travel times while preserving a small gap between  vehicles.                                                                                                         |

interconnected vehicles overlap in certain technological aspects [1]. Vehicular Ad hoc Network (VANET) technology is used in connected vehicles, which need the installation of an On-Board Unit (OBU) within the car. Vehicles within its communication range can communicate with one another using the Dedicated Short Range Communication (DSRC) standard protocol [33,34]. VANET 
technology can support both safety-related and infotainment applications, with the main distinction between the two being the level of security measures employed; safety-related applications typically adhere to more stringent security standards [1]. 

Communication in CAVs relies on wireless technologies [32]. DSRC facilitates communication between autonomous vehicles and infrastructure through On-Board Units (OBUs) in vehicles that receive signals and Roadside Units (RSUs) exchanging information with OBUs from various sources [31]. DSRC deployment can help mitigate traffic congestion and accidents caused by human driving, playing a crucial role in accident prevention on roadways. Huang and Lin [35] suggests that DSRC is particularly suitable for early collision estimation and avoidance in highway scenarios. However, DSRC-based V2X communication has limited scalability and cannot provide satisfactory probabilistic characteristics as vehicle density increases [36,37]. Furthermore, the limited transmission range inherent in DSRC renders it inadequate for delivering high-capacity, low-latency communication channels essential for sophisticated V2X applications like autonomous driving. Consequently, V2X technology amplifies the advantages of autonomous driving and promotes the application of autonomous vehicles in actual traffic [38,39]. 

In the field of communication methods among CAVs, cellular connectivity plays an important role. Specifically, Cellular Vehicle-toEverything (C-V2X) communication stands as a crucial foundational technology, contributing significantly to the establishment of interconnected and automated traffic systems. Inter-vehicle communication enables more precise and efficient autonomous driving behavior, allowing vehicles to exchange driving intentions (such as lane changes, braking) and provide perception beyond the capabilities of AV sensors, ensuring more reliable navigation. Consequently, vehicle data has become a critical resource, occupying a significant position in the driving network, requiring new network architectures to support this growth [40]. Despite the advancements in 3GPP LTE and 4 G V2X (version 14 C-V2X), their incapability to deliver high throughput and low latency for advanced applications falls short of meeting the practical demands of CAVs. As a result, 5 G C-V2X emerges as a more promising and viable choice [32]. The millimeter-wave frequency band, edge computing, network slicing, virtualization, and advanced antenna systems within 5 G C-V2X 
technology have the potential to offer more reliable low-latency communication and higher data rates, enabling the realization of more 

| Nation                                                                                                   | Year                                                                                                                                                                                                                    | Document   | Content   |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------|
| Automated Vehicles Comprehensive Plan[18]                                                                | Identify three goals for the development of the U.S. autonomous vehicle  industry: promoting cooperation and transparency, modernizing the regulatory  environment, and preparing the transportation system             |            |           |
| Occupant Protection Safety Standards for Autonomous                                                      | Emphasizes that autonomous vehicles must provide the same level of occupant                                                                                                                                             |            |           |
| Vehicles[139]                                                                                            | protection as traditional vehicles driven by humans, and makes it clear that  fully autonomous vehicles may no longer need manual equipment                                                                             |            |           |
| Regulations on Administration of Intelligent  Connected Vehicles in Shenzhen Special Economic  Zone[140] | Allow L3 AV to be tested on open roads in administrative areas with relatively  complete CVIS infrastructure                                                                                                            |            |           |
| Autonomous Driving Law (Draft)[141]                                                                      | Supplements to the existing Road Traffic Law and Compulsory Insurance Law  have established a legal framework for L4-level autonomous driving, allowing  it to operate normally on public roads throughout the country. |            |           |
| Autonomous Driving Law (Draft)[142]                                                                      | A legal framework has been established for level 4 autonomous driving to  enable it to operate normally on prescribed public roads across the country                                                                   |            |           |

![4_image_0.png](4_image_0.png)

advanced CAV functionalities. The sensitivity of connected autonomous driving to network security makes security a critical attribute within C-V2X, including specific elements such as authentication identification, integrity, user privacy, and availability [40] . However, most information within C-V2X is disseminated in a temporary broadcast form, posing certain risks in such communication methods, necessitating the formulation of further standards and specifications to achieve communication security in C-V2X.

The connectivity and autonomy offered by connected autonomous driving are poised to revolutionize the transportation paradigm in several ways, with profound social and economic impacts. These include enhanced safety, increased stability and comfort, time savings, more efficient road utilization [41] .

3. Impacts of connected autonomous vehicles on alleviating congestion and traffic efficiency Connected autonomous vehicles (CAVs) constitute a profoundly transformative technology with vast potential across multiple domains. This potential includes a substantial reduction in traffic accidents, particularly those involving pedestrians or cyclists, the improvement of traffic flow stability and fluidity to enhance overall traffic system efficiency, and a reduction in pollution emissions [32] . Currently, extensive research has focused on exploring the efficiency, congestion alleviation, safety, pollution and stability of CAVs within their operating environment.

However, based on the most recent findings, CAVs will comprise 75% of global automobiles before the mid-21st century [42] . The escalating adoption of CAVs is shaping a landscape where road traffic will comprise a diverse mix of HDVs and CAVs [43] . The homogeneous traffic flow composed solely of human-driven vehicles will gradually evolve into heterogeneous traffic flow, coexisting with both connected autonomous vehicles and human-driven vehicles [44]. Due to differences in driving logic and technology, their interactions with each other and the external environment are dissimilar, making heterogeneous traffic flow more complex than homogeneous traffic flow, where uncertainties, unobservability, and uncontrollability in HDVs make it difficult to estimate traffic states. The reaction time and compliance with changes in driving states due to the development level of CAV technology also contribute to this complexity [45]. Fig. 2 illustrates a connected system of mixed traffic flow, showcasing the interconnections between networked autonomous vehicles themselves, pedestrians, infrastructure, and networks. 

Therefore, how CAVs influence heterogeneous traffic flows has garnered attention from a group of scholars. Scholars have specifically focused on the role of CAVs in enhancing traffic efficiency within mixed traffic flows. Traffic efficiency correlates with various factors, such as velocity, transit time, and traffic volume [46]. CAVs influence traffic efficiency in multiple ways, including CAV penetration rates, vehicle control, dedicated lane design, and road planning [47]. By optimizing traffic flow from different aspects, they elevate traffic efficiency. The advantage of connected autonomous driving lies in its real-time interaction with infrastructure and other networked vehicles, engaging in cooperative driving [48]. Powerful networked autonomous systems can intelligently plan lane changes, braking, acceleration, and deceleration, reducing traffic fluctuations caused by uncertainties and sudden changes inherent in human driving—a state of inefficient stop-and-go movement [49]. Systematic planning and vehicle collaboration effectively enhance traffic efficiency, alleviating traffic congestion. 

## 3.1. Research Models And Measurement Indicators Of Connected Autonomous Vehicles

The real-time communication and precision computing of connected autonomous driving enable shorter response delays and increased travel speeds, minimizing the influence of human drivers' personality traits, preferences, and skills, thereby allowing for enhanced vehicle throughput [2]. To evaluate the effect of CAV on traffic efficiency, numerous scholars have suggested a variety of metrics and study approaches, including as network models, cellular automata, following models, reinforcement learning algorithms, and more. The cellular automata model, with its unique advantage of discrete grid-based dynamics in time and space, evaluates various vehicles and speeds based on cells within the model [50]. Zhang et al., for instance, introduced an advanced cellular automata model based on the classical NS model. This enhanced model integrates the physical characteristics of vehicles and simulates mixed traffic flow involving both electric and fuel-based vehicles. Their research analyzed how the presence of electric vehicles affects traffic flow safety across different penetration rates [51]. Based on three-phase traffic theory framework and the traditional three-phase traffic flow theory KKW model, Zeng et al. created a cellular automaton model for highway ramp systems under accident conditions, which was used to analyze the effects of traffic accidents on traffic flow and comprehend the patterns of congestion propagation [52]. Additionally, the Lagrangian-based multi-valued cellular automaton model has been utilized to analyze multi-lane traffic flow. Lower density coupled with a higher number of lanes results in increased traffic volume [53]. 

Xie et al. derived, using a general vehicle-following framework, that the stability of heterogeneous traffic is closely linked to the penetration rate and spatial distribution of connected vehicles, emphasizing how interconnected vehicles enhance traffic flow stability and efficiency. Furthermore, they proposed a distributed feedback control-based driver assistance strategy that positively influences traffic flow stability and efficiency [54]. However, most existing studies on heterogeneous traffic flow models have not adequately considered the self-stabilizing effects. Gong and Zhu introduced a car-following model considering the self-stabilizing effects of AV in heterogeneous traffic flow. They verified using both linear and nonlinear techniques that self-stabilizing effects may improve heterogeneous traffic flow stability and reduce traffic congestion. Additionally, a higher percentage of autonomous cars helps to stabilize 

![5_image_0.png](5_image_0.png)

the flow of diverse traffic [44]. The local strategy CDS-L and global strategy CDS-G, which are based on shared CV information, have also been confirmed to dampen traffic fluctuations and enhance traffic efficiency [48]. Zeng et al. simulated the effects of intelligent networked vehicles on energy consumption and traffic congestion using a cellular automaton model of heterogeneous traffic flow on a dual-lane roadway. The results showed that as CAV penetration rates and convoy sizes rise, so does total traffic capacity, which reduces congestion [55]. 

In Chen's study, a mixed traffic flow model was established using three metrics—traffic volume, average speed, and vehicle count—to assess traffic efficiency. The simulation results indicated that autonomous driving vehicles could enhance traffic efficiency and reduce energy consumption [46]. Narayanan outlined 19 factors influencing the traffic flow efficiency of connected autonomous driving vehicles, categorized as vehicle characteristics, travel behavior, network features, and policies. Noteworthy factors included CAV dedicated lanes, CAV market penetration rates (MPR), and intersection control [47]. Hou proposed a comprehensive performance assessment framework for CAV in mixed traffic and a unified performance metric reflecting the overall traffic performance, demonstrating significant CAV-induced improvements in overall traffic efficiency and safety [56]. 

Gu´eriau and Dusparic [57] investigated CAV's impact on three networks (urban, national, and highways) regarding traffic efficiency and safety, concurrently evaluating three CAV indicators: automation level, penetration rate, and vehicle type. Their findings indicated a progressive and nonlinear impact of CAV on traffic efficiency and safety, achieving maximum benefits at MPRs ranging from 20% to 40% [56]. Overall, in heterogeneous traffic flow composed of CAVs and HDVs, most studies have focused on traffic performance itself, with few reviews addressing policy-related indicators. Consequently, a significant portion of research has concentrated solely on subsets of traffic efficiency, failing to comprehensively summarize related influencing factors. There is a need for a more inclusive set of metrics to provide decision-making support for the development and regulation of CAVs. 

When studying the traffic efficiency of mixed traffic flow, the market penetration rate (MPR) of CAVs stands as a crucial influencing factor. Different MPRs may result in varied impacts on traffic efficiency. In scenarios with lower market penetration rates, the positive benefits of CAVs may be challenging to realize [58]. Do et al. reviewed CAV simulation studies and found that higher penetration rates greatly enhance road capacity. Moreover, vehicular connectivity enables rapid passage while maintaining minimal inter-vehicle distances, where road capacity and speed serve as critical metrics for traffic efficiency [59]. Houshmand, using actual traffic data from Boston, examined the effect of allocating system central routes under different CAV penetration rates in mixed traffic flow. The results indicated that even at low CAV penetration rates, traffic congestion can be alleviated [60]. Hou suggested in their study that variations in MPR exert diverse impacts on the efficiency of mixed traffic flow. When MPR is below 20%, its effect on traffic efficiency is minor, yet it significantly enhances traffic safety. Therefore, in researching the influence of CAVs on mixed traffic flow, it's essential to consider these various factors together [56]. 

## 3.2. Vehicle Control And Traffic Efficiency Enhancement Strategies In Connected Autonomous Vehicles

Vehicle control can be categorized into two aspects: longitudinal control, aimed at maintaining the desired speed and following distance, and lateral control, focused on directing lane changes [61]. Networked autonomous driving, through real-time communication and coordinated cooperation, reduces response time and precisely plans actions to enhance vehicle control. While considerable research has been conducted on the longitudinal control of CAVs in this domain, studies on lateral control are relatively dispersed. 

However, reasonable lane changes show promise in enhancing traffic efficiency and alleviating congestion in dense traffic scenarios, despite connected CAVs having a limited spatial impact by improving speed within traffic flow. Therefore, investigating CAVs' coordinated behaviors such as lane-changing, overtaking, and merging is important. Strategies for CAV longitudinal control can be approached through linear or nonlinear [62,63], model prediction [61,64], and deep reinforcement learning [49,65,66]. Automated lane-changing strategies for CAVs involve reinforcement learning [67–69], model simulation [70,71], and partially observable Markov decision processes [72]. Although some strategies are tailored for AVs, the authors assert that representative techniques and practices have significant reference value for CAVs as well. 

Liu et al. conducted a comprehensive review of vehicle control technologies for both AVs and CAVs, particularly emphasizing AVs' micro-level vehicle state estimation and trajectory tracking control, alongside CAVs' evolution in macro-level coordinated control. 

They discussed non-predictive feedback, predictive model forecasting, and learning-based vehicle control technologies, which significantly enhance traffic efficiency, safety, and sustainability [73]. Wang et al. delved into the impact of CAV autonomous lane changing on mixed traffic flow, demonstrating, from the perspectives of micro-traffic simulation and reinforcement learning, the positive effects of lane-changing strategies at 50% or 100% market penetration rates [61]. Shi et al. proposed a distributed longitudinal control strategy based on Deep Reinforcement Learning (DRL), integrating interference signals and noise into machine learning to simulate real environments. Their approach involved a multi-agent system receiving real-time information to address signal failures, effectively mitigating traffic oscillations and thus improving traffic efficiency [49]. 

Apart from direct vehicle control, scholars have also focused on the impact of autonomous vehicle intersection control and the implementation of dedicated lanes on traffic efficiency and congestion relief [74]. Traffic density and the number of lanes significantly impact traffic flow, where lower density and more lanes result in higher traffic volume [50]. Similar to dedicated lanes for rapid transit, toll roads, and HOV lanes, specialized lanes play a crucial role in enhancing traffic efficiency, contingent upon the overall penetration rate of CAVs. He explored the implications of CAV lane policies on highway traffic efficiency in terms of capacity and throughput. Experimental combinations of different lane policies and traffic conditions revealed that at lower CAV Market Penetration Rates (MPR), CAV-dedicated lanes had no significant effect on traffic efficiency, suggesting a recommendation for implementing a "mandatory use" policy instead of setting multiple dedicated lanes [8]. Ye conducted a modeling study to assess the advantages and disadvantages of setting exclusive lanes for CAVs. The findings indicated that at lower CAV penetration rates, Exclusive lanes of CAV decreased the overall traffic flow throughput. However, under moderate penetration rates, dedicating lanes was more favorable for optimizing CAV advantages in traffic efficiency [75]. 

## 4. **Impacts Of Connected Self-Driving Cars On Stability, Safety And Environment**

Although connected autonomous vehicles are developing rapidly, achieving a 100% adoption rate will require a lengthy process. 

Therefore, HV and CAV will coexist for an extended period, forming a complex mixed traffic flow system. In response to this shift, some scholars have begun to focus on the security and stability implications of CAVs within hybrid traffic flows rather than exclusively within a fully CAVs environment [58,76,77]. For instance, Yao considered situations in mixed CAV environments where CACC-equipped vehicles degrade into ACC-equipped vehicles and studied the security and stability within hybrid traffic flows using various security assessment metrics [78]. Furthermore, advancements in vehicle design and engine efficiency of Connected Autonomous Vehicles have effectively reduced fuel consumption and emissions [28]. Research estimates indicate that fuel consumption has nearly halved compared to figures from 30 years ago [79], resulting in reduced energy emissions and contributing to environmental sustainability. 

The earlier discussion focused on the impact of CAVs on enhancing traffic efficiency and alleviating traffic congestion. Traffic efficiency serves as a crucial intermediary and focal point, enabling an exploration into the potential correlations and influences associated with the enhancement of traffic efficiency and its implications on other aspects. In this section, we will review the influence of CAVs on hybrid traffic flows, specifically examining their effects on stability, safety, and environmental conservation. 

## 4.1. Stability Implications Of Connected Autonomous Vehicles

V2X communication, cloud technology, positioning and sensing will enable CAV systems to work better together. CAVs achieve this by gathering diverse data from sources like infrastructure, nearby vehicles, and cloud servers. This multi-source data acquisition significantly improves the safety and stability of autonomous driving [80]. CAVs communicate with other connected vehicles (V2V), with infrastructure (V2I), with networks (V2N), as well as with pedestrians (V2P). Collectively, these communication modes are termed V2X [5]. 

Zheng points out in his research that a significant characteristic of traffic flow primarily consisted of HDV is its inherent instability 
[6]. Sudden events and decisions can easily result in the stop-and-go nature of traffic flow. This is also applicable to connected autonomous vehicles. This chain reaction amplifies and propagates through traffic, leading to a wave-like pattern of congestion [81]. 

This fluctuating traffic condition is often referred to as "phantom traffic"[82] or "traffic oscillations." It is typically caused by various factors, including lane changes resulting from diverging and merging [83–85], lane height variations [86], changes in road geometry 
[87], and fluctuations in traffic volume, among others. Additionally, driver personality [88] and stochastic behavior can also contribute to the instability of traffic flow. 

Numerous studies have explored traffic flow stability in CAV environments [89–91]. Talebpour and Mahmassani, for instance, employed a microsimulation framework with diverse vehicle types to assess string stability across various CAV penetration rates. They found that CAVs notably improved mixed traffic flow stability and mitigated the formation and propagation of traffic disruption [58]. 

Yao conducted a microsimulation experiment showing that a 25% penetration of ACC vehicles effectively enhanced traffic flow stability and road capacity [78]. Lu and Aakre introduced a stability criterion for homogeneous traffic flow, establishing its stability [92]. 

Ye and Yamamoto observed that the integration of self-driving cars significantly bolsters traffic flow stability. To investigate this, they simulated mixed traffic flow scenarios using a meta-cellular automata model. Their analysis scrutinized collision event distributions, acceleration patterns, and speed differences across various CAV penetration levels [93]. 

Zheng employed the Lagrangian coordinate system and six performance metrics to measure how autonomous cars affect system stability. The findings revealed that increasing the AV penetration rate from 5% to 50% positively impacts the stability of mixed traffic flow and human-driven vehicles [6]. In parallel research, Jin investigated the stability of mixed traffic flow under various conditions, including diverse CAV penetration rates, driver reaction times, and the number of CAVs, employing a deterministic model of mixed traffic flow. It was observed that appropriate control of CAVs significantly enhances the stability of mixed traffic flow [94]. In addition, Ghiasi et al. introduced an analytical stochastic model to scrutinize the stability and throughput of mixed traffic flow under diverse conditions, including CAV penetration rates, CAV platoon intensity, and mixed traffic headway settings [95]. 

In various traffic scenarios, urban roads often pose dynamic challenges, such as sudden accidents and frequent congestion. 

Consequently, many scholars have expressed significant interest in evaluating CAV performance at urban intersections. Some researchers have even proposed that CAV deployment could potentially replace traditional traffic signal lights [96], leading to improved stability in mixed traffic flow. An essential aspect of achieving this enhancement involves optimizing the travel times of all vehicles within the intersection radius. This optimization ultimately increases intersection throughput and enables optimal CAV control at intersections. Consequently, recent research in this area has focused on minimizing vehicle travel times [97–100]. Zohdy [101] 
introduced a Cooperative Adaptive Cruise Control-based method to minimize intersection delays and maximize traffic throughput. 

Miculescu [99] employed a polling system approach to allocate time sequences to vehicles on each road, ensuring expected travel times. Additionally, some studies [102,103] established a decentralized optimal control framework to assist CAVs in navigating intersections without explicit signal lights, considering left and right turns. Zhang [104] introduced a decentralized optimization control framework based on Malikopoulos [103], achieving optimal acceleration/deceleration, maximizing throughput, and maintaining mixed traffic flow stability. 

8

## 4.2. Safety Implications Of Connected Self-Driving Cars

The information connectivity and communication capabilities of connected autonomous vehicles construct an open network environment. Through V2X communication, CAVs engage in real-time information exchange, allowing them to 'see' beyond their immediate line of sight [105]. This extended perception range further enhances driving safety. With real-time communication data updates and precise decision-making, CAVs can make more reasoned judgments when faced with changing driving conditions, such as turns, inclines, obstacle avoidance, and emergency braking, thereby ensuring the safety of both drivers and passengers. However, autonomous vehicles operating in platoons are also susceptible to cyberattacks [7]. This not only poses risks of compromising user privacy but may also directly jeopardize traffic safety, such as increasing collision risks and causing traffic disruptions [106,107]. Consequently, connected autonomous vehicles exert two distinct influences on the security of heterogeneous traffic flow and other vehicle types. 

Concerns about CAV's own security can be categorized into two areas [32]: attacks from active and attacks from passive. Among them, passive attacks refer to an attacker eavesdropping on the CAV's position, speed, and planning information transmitted via broadcasts, which can be re-observed and stolen by the attacker after the broadcasted data is delivered to the RSU [108], adding another layer of risk to the security of the connected self-driving cars. Kang [109] explained a passive attack method in their study, where a unique and accurate information about the target vehicle is obtained from the roadside localization unit (RLU), and the information about the target vehicle is obtained from the roadside localization unit (RLU). Cheng [7] proposed a novel intelligent driving model that takes into account network attacks and heterogeneous vehicles while integrating a dynamic communication topology. Validation revealed that under network attacks, low penetration rates and high latency times lead to hazardous traffic behaviors. 

Active attacks may include incorrect data, spoofing of data, retransmission of previous messages to obtain a valid system key, modification of information about the data in question, or denial of service to prevent the transmission of data on a server where it is vital [32]. For instance, failures or interference with GPS signals could lead to drivers or assisted driving systems receiving incorrect information, resulting in erroneous judgments. Ghanavati discovered that fine-tuning the speeds between vehicles or exercising spatial control among them can result in traffic congestion and shockwaves of traffic flows [110]. Using a collaborative intelligent driver drive model, Wang illustrates the adverse effects of different cyber-attacks on connected autonomous driving, such as delays, sudden braking, and destruction of safety distances [111]. 

The capacity of interconnected autonomous vehicles to manage driving via real-time data transfer and sensing mechanisms significantly diminishes traffic conflicts and elevates the overall safety of traffic flow. This underscores their substantial influence on the safety of hybrid traffic configurations [56,93,112,113]. Hou proposed that an increase in MPR enhances the overall traffic performance in terms of safety for both multiple vehicles and individual vehicles, especially demonstrating a more pronounced improvement in safety performance with increased CAV penetration rates under adverse weather conditions [56]. Papadoulis et al. developed CAV decision control algorithms to explore CAV safety performance, revealing a significant positive effect of CAVs on traffic safety even at lower penetration rates [114]. Karbasi and O'Hern, utilizing the urban mobility simulator (SUMO) for traffic simulation, investigated the impact of CAVs on road safety, demonstrating that real CAVs potentially reduce the number of traffic conflicts and collisions, with vehicles equipped with collision avoidance systems offering additional safety benefits [115]. Ye and Yamamoto discovered that an increase in MPR contributes to the enhancement of safety in mixed traffic flows [115]. 

## 4.3. Environmental Impacts Of Connected Self-Driving Cars

According to UN-Habitat in the newly released State of the World's Cities Report 2022, urbanization has always been an unstoppable world trend, and although the COVID-19 pandemic that erupted in late 2019 has temporarily put some obstacles in the way of urban development, urbanization is poised for a resurgence, as estimates indicate a rise of 2.2 billion in the global urban population by 2050, accounting for 68% of the total world population [116]. The inevitable result of the development of urbanization is the problem of inter-city and urban-rural road traffic, which in turn affects the sustainable development of the environment. Unsuitable modes of transport development will greatly undermine the living environment and well-being of human beings, such as the increasing urban congestion, traffic accidents and energy waste in recent years. Although energy emissions and losses are not central to the design and manufacture of CAVs, the development of CAVs has had a significant impact on energy emissions and environmental friendliness. In the course of research on urban transportation, many researchers have found that connected self-driving cars can effectively respond to this problem. 

CAV is not only a new kind of traffic unit, but also an optimization tool to improve traffic operation by suppressing or even eliminating the negative impacts of traffic oscillations, and at the same time, it holds the potential to significantly reduce greenhouse effect [117]. The combination of CAV's communication mechanism and autonomous driving technology can effectively reduce the instability of the traffic flow, create enough buffer time, and improve the traffic efficiency [81,118], which was also verified by Wang M and Milanes et al. through field experiments [119,120]. Qu and Yu et al. created a reinforcement learning-driven model for car-following, this model focuses on the present driving state, enhancing human driver behavior and ensuring precise vehicle control to minimize energy usage and diminish greenhouse effect. The trained model demonstrates increased capability in mitigating the impact of abrupt traffic disruptions when controlling the CAV, resulting in enhanced traffic flow efficiency and a consequent decline in energy usage [117]. 

Scholars have highlighted the varying environmental and energy emission impacts of CAVs, with both positive and negative effects noted [121,122]. Simon and Alexander-Kearns contend that the outcomes hinge on different policy approaches [123,124]. Greenblatt and Shaheen stated that the overall impact of autonomous driving and on-demand mobility on energy and the environment could be positive, but these effects may vary based on policy directions [125]. Research by Wadud et al. [121] indicates that enhancing eco-driving, traffic coordination, lightweighting risk reduction, size adjustments based on occupancy, carpooling promotion, and reduced emphasis on vehicle performance all contribute to enhanced energy efficiency. Nonetheless, the identical study posits that the escalated incorporation of CAVs, propelled by reduced travel expenses, a broadening user base (comprising youth, seniors, and individuals with disabilities), increased highway velocities, and supplementary vehicle functionalities, could markedly elevate the energy impact of vehicle automation. 

Expanding on this foundation, some scholars have further explored the potential energy-saving benefits of networked automated driving grounded in motion principles and optimal control theory. They argue that automation enables vehicles to anticipate road conditions accurately and adjust their driving strategies, resulting in energy savings [41]. In other words, Cooperative driving enhances vehicle energy efficiency through coordinated interactions. The environmental effects of connected and self-driving automobiles were explored using the CMEM model, which demonstrated that increasing MPR of connected cars had a positive impact on reducing emissions and traffic [126]. 

Furthermore, scholars have also focused on how intersection traffic lights influence the depletion of resources. They have proposed various methods to investigate trajectory-smoothing strategies for single vehicles [127,128], multiple vehicles [129–131], and platoons of vehicles [132,133] at intersections, aiming to reduce energy consumption. For instance, He et al. devised an optimal control model to offer eco-driving advice for Heterogeneous traffic comprised of electric cars and gasoline cars [133]. Building on these studies, Han et al. proposed the PTO-GFC, a trajectory optimization method that considers all vehicles within a platoon and extends to multiple platoons. This method aims to reduce energy emissions of CAVs fleets driving through signal-controlled junctions, demonstrating the significant influence of CAV in enhancing transportation efficiency and mitigating adverse impacts of environment [134]. 

However, it's crucial to note that the current focus on CAV and AV emissions primarily centers on their short-term effects, and the long-term net implications on fuel consumption remains uncertain. 

## 5. **Policy Recommendations Of Cav**

AVs and CAVs constitute a dynamic and emerging field. Currently, studies related to connected autonomous driving vehicles primarily concentrate on automation technology [135]. Starting from 2015, there has been a progressive pivot towards non-technical facets, such as governance and the sustainable advancement of vehicle automation. A central concern is finding the optimal balance between deploying connected autonomous vehicles and realizing their societal benefits [136]. 

While some countries initially approached CAV development with caution and observation, the majority have now begun to respond to the inevitable wave of CAV development and the foreseeable impacts. They are addressing various issues and conflicts that arise during this process [137]. Planning and regulation by the public sector have become indispensable. While extensive research underscores the substantial influence of CAVs on traffic dynamics, road security, and environmental factors, it's important to note that this doesn't advocate for a laissez-faire approach, as it could yield further adverse repercussions [138]. A requisite is a coherent, succinct policy that ensures mutual benefits, including favorable socio-economic outcomes while duly addressing public apprehensions. The following table shows the current policies and regulations on CAV in major countries: 
Based on the contents of policy documents, it's evident that various countries have released publications advocating the development of their respective autonomous driving vehicle industries. These publications encompass visions, plans, legal frameworks, and regulatory measures aimed at fostering the advancement of autonomous driving. For instance, these initiatives involve deploying L4level autonomous driving vehicles, expanding areas for testing and operating a larger number of autonomous vehicles, and introducing comprehensive legal frameworks to oversee and regulate the operation of autonomous driving vehicles. However, owing to varying levels of development among countries, these policies exhibit differing degrees of preference and emphasis. 

The efficiency of traffic flow has historically not been the responsibility of automotive manufacturers whose primary aim is profitmaking; rather, achieving traffic efficiency falls under the purview of governments and operators [143]. However, with increased automation, automotive companies also need to consider the objectives of autonomous driving systems [144]. Presently, there exist regulations that demand stability and traffic flow efficiency for CAVs [145]. Nonetheless, as evidenced in the preceding overview, the confirmed impact of CAVs on traffic efficiency necessitates policymakers' attention. Integrating traffic efficiency into policy guidance is crucial, encouraging innovation while maximizing the positive impact of CAVs. Without policy intervention, manufacturers might lean toward designing products more inclined to attract customers rather than optimizing network performance [146]. Apart from constraints placed on automotive manufacturers, policymakers should also prioritize factors affecting CAVs implication on the efficiency of hybrid traffic flows, such as CAVs proliferation, dedicated lane setups, and considerations for integrating them with shared mobility options [47]. 

Currently, numerous studies have explored the influence of CAVs on safety and stability of hybrid traffic flows, with much of the research focusing on the technological advancements of CAVs and infrastructure development. Therefore, the progress in technology and infrastructure upgrades are crucial for enhancing the safety and stability of mixed traffic flows, the government should proactively take measures to regulate the adoption of new technologies like AVs, with a particular focus on areas such as testing and deployment of CAVs, network security and privacy, liability and insurance, environmental monitoring, and more. Meanwhile, establishing stringent safety and security standards [147], focusing on data encryption, preventing network attacks, and real-time threat detection systems, as well as defining clear responsible entities and penalty criteria, are crucial. 

Policymakers should prioritize exploring energy-efficient, environmentally-friendly, and sustainable strategies for the deployment of CAVs concerning their environmental impact. Emphasizing the interconnectedness of CAVs' environmental effects with other relevant impacts is crucial in identifying a balanced beneficial point within their network of effects. Although there may be benefits to autonomous vehicles' effects on pollution and energy economy, it is yet unclear how to balance these short- and long-term effects 
[144]. Therefore, the establishment of a continuous framework for evaluating the long-term impacts of CAVs on energy usage and exhaust emission is crucial. Regular policy updates based on scientific research findings and technological advancements are necessary to explore the interactions between their short-term and long-term benefits. 

Future research can delve deeper into societal awareness and acceptance of CAVs, as well as their effects on public health, environmental sustainability, and the advancement of smart cities [136]. Understanding the perspectives of pedestrians and cyclists in automated driving environments is crucial as they fall under vulnerable road users. Their views are integral to the development and application of CAVs. Positive interactions with automated driving technology can influence their perception of its safety and acceptance. Hence, governments should facilitate constructive engagements between these groups and automated driving [148], enhancing their acceptance of this technology. Conducting comprehensive studies on CAVs from interdisciplinary perspectives will facilitate both horizontal and vertical analyses of their overall impact. 

## 6. **Future Research Directions**

The realm of connectivity and autonomous driving is no longer an unattainable fantasy but is instead rapidly advancing at an unpredictable pace. CAVs rely on a variety of software and hardware technologies to achieve extensive perception, intercommunication, and driver assistance. They alleviate traffic congestion, reduce traffic accidents, lower energy emissions, enhance environmental friendliness, and have the potential to alter future transportation patterns and people's modes of travel [121]. However, achieving widespread adoption of connected autonomous driving and reaching high penetration rates still requires significant investments in technology and funding, as well as strategic government planning. Currently, there are still substantial obstacles to overcome in this regard. 

When studying the implications of CAVs on the efficiency of hybrid traffic flows, expanding the control framework becomes imperative for further investigating and optimizing the intricate characteristics of mixed traffic flows. Emphasis should be placed on scrutinizing the predictive processes of advanced supervised machine learning algorithms [49]. Beyond examining singular subsets of CAV vehicle control, leveraging multimodal technologies and control architectures [73] integrating GPS, LiDAR, cameras, V2X, etc., 
within the research framework becomes essential. This integration counters potential omissions and failure risks from singular information sources, enabling efficient CAV driving and better adaptation to the complexities inherent in heterogeneous traffic flows. 

Given the susceptibility of CAV communications to disruptions, attention must be directed towards vehicle control technologies in scenarios involving network attacks, communication failures, and human-induced operations. Integrating real-world elements such as noise, signal interference, adverse weather, among others, into the control framework is vital, facilitating the development of a simulation environment conducive to learning and modeling. 

It is essential to prioritize safety and stability during the transitional phase from HVs to CAVs within mixed traffic flow. This involves investigating the types of network attacks that target connected vehicles, understanding their potential impacts on traffic safety, assessing the inherent safety risks associated with CAVs, and analyzing the road implications resulting from their interactions with HVs. Furthermore, the influence of vehicle automation on emissions and fuel efficiency has been thoroughly investigated. Nonetheless, further testing is needed to determine the extent of its impact under various automation levels and penetration rates. As discussed earlier, forthcoming research endeavors may focus on exploring the lasting implications of autonomous vehicles on energy usage and emissions, thereby evaluating the balance between the immediate and enduring benefits of autonomous vehicles concerning energy. 

A thorough evaluation of the economic, public health, and societal effects of CAVs is still lacking in the research, in addition to the four areas covered in this article. For instance, there is a shortage of thorough exploration regarding the potential effects of deploying CAVs on the traditional automotive industry and the varying impacts on developed and developing countries. Furthermore, the implications of CAVs on public health presents a novel and noteworthy area of study. It prompts questions about how vehicle automation will influence human physical activity levels and the potential associated public health issues. 

The public's perception of CAV technology is crucial [149]. It significantly influences the adoption of innovative technologies such as CAV and potential societal benefits they can bring [150]. Thus, it is imperative to examine whether the public, especially disadvantaged groups, will benefits economically and socially from the development of connected autonomous vehicles. For instance, Xing et al. analyzed Pittsburgh BikePGH survey data from 2017 and 2019, revealing an increase in positive interactions between vulnerable road users and autonomous vehicles, which can positively affect their perceived safety and acceptance of this technology. Hence, government support of positive interactions between these groups and AVs is crucial to enhance their acceptance of autonomous driving technologies [148]. Conducting a more comprehensive and multi-dimensional study of CAVs can further enhance our understanding of the economic impacts and societal benefits associated with their development, ultimately promoting their sustainable and health-conscious growth. 

## 7. **Conclusions**

The remarkable advancement of CAV technology has prompted numerous automobile manufacturers and internet technology companies to seize this new momentum. Governments worldwide are closely monitoring these cutting-edge developments, ensuring support for the progress of their own nation's connected autonomous driving initiatives. This study emphasizes various effects of CAVs on mixed traffic flows, highlighting the fundamental problem of traffic efficiency and congestion. It could be asserted that enhanced efficiency of hybrid traffic flow due to CAVs has multifaceted implications, such as alleviating congestion, boosting driving speeds, increasing traffic capacity, enhancing flow, and reducing pollution emissions. Building upon this foundation, the implications of CAVs on the environment, safety, and stability of hybrid traffic flows are also reviewed in this study. Traffic efficiency, stability, safety, and environment impact are intricately interlinked, necessitating careful attention to their interconnectedness when formulating policy recommendations. Neglecting any aspect might lead to suboptimal policy outcomes. Finally, the paper distills the comprehensive findings and suggests potential avenues for future research. We hope this study makes a modest contribution to understanding the systemic impacts of CAVs. 

## Credit Authorship Contribution Statement

Xia Chengyi: Conceptualization, Supervision, Validation. **Olson David L.:** Conceptualization, Supervision, Writing - review & 
editing. **Pan Yuchen:** Conceptualization, Supervision, Writing - review & editing, Funding acquisition, Resources. **Wu Yu:** Writing - original draft, Writing - review & editing. **Xu Lu:** Conceptualization, Funding acquisition, Methodology, Supervision, Validation. 

## Declaration Of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## Data Availability

No data was used for the research described in the article. 

## Acknowledgments

This work was supported by the National Natural Science Foundation of China [Grants 72101258], the Fundamental Research Funds for the Central Universities, and the Research Funds of Renmin University of China [No. 23XNA033]. 

## References

[1] Rasheed Hussain, Zeadally Sherali, Autonomous cars: Research results, issues, and future challenges, IEEE Communications Surveys & Tutorials, 21 (2) (2018) 

1275–1313. 

[2] Hani S. Mahmassani, 50th anniversary invited article—Autonomous vehicles and connected vehicle systems: Flow and operations considerations, 

Transportation Science 50 (4) (2016) 1140–1162. 

[3] Steven E. Shladover, Connected and automated vehicle systems: Introduction and overview, Journal of Intelligent Transportation Systems 22 (3) (2018) 

190–200. 

[4] Steven E. Shladover, Dongyan Su, Lu Xiao-Yun, Impacts of cooperative adaptive cruise control on freeway traffic flow, Transportation Research Record, 2324 

(1) (2012) 63–70. 

[5] Na Lin, Changfu Zong, Masayoshi Tomizuka, Pan Song, Zexing Zhang, An overview on study of identification of driver behavior characteristics for automotive 

control, Mathematical Problems in Engineering, 2014 (2014). 

[6] Fangfang Zheng, Can Liu, Xiaobo Liu, Saif Eddin Jabari, Liang Lu, Analyzing the impact of automated vehicles on uncertainty and stability of the mixed traffic 

flow, Transportation Research Part C: Emerging Technologies, 112 (2020) 203–219. 

[7] Rongjun Cheng, Hao Lyu, Yaxing Zheng, Ge Hongxia, Modeling and stability analysis of cyberattack effects on heterogeneous intelligent traffic flow, Physica 

A: Statistical Mechanics and its Applications, 604 (2022) 127941. 

[8] Shanglu He, Fan Ding, Chaoru Lu, Qi Yong, Impact of connected and autonomous vehicle dedicated lane on the freeway traffic efficiency, European Transport 

Research Review 14 (1) (2022) 12. 

[9] Haokun Song, Fuquan Zhao, Guangyu Zhu, Liu Zongwei, Impacts of Connected and Autonomous Vehicles with Level 2 Automation on Traffic Efficiency and 

Energy Consumption, Journal of Advanced Transportation, 2023 (2023). 

[10] Drew Scott Pendleton, Hans Andersen, Xinxin Du, Xiaotong Shen, Malika Meghjani, Eng You Hong, Daniela Rus, H. Ang Marcelo, Perception, planning, 

control, and coordination for autonomous vehicles, Machines, 5 (1) (2017) 6. 

[11] Ioannou, Petros, ed. Automated highway systems. Springer Science & Business Media, 1997. 

[12] B´ela Lantos, Marton ´ Lorinc. ˝ *Nonlinear control of vehicles and robots*, Springer Science & Business Media, 2010. 

[13] Waymo One, Waymo's next chapter in San Francisco, https://waymo.com/blog/2023/08/waymos-next-chapter-in-san-francisco.html (accessed 29 November 

2023). 

[14] Bloomberg, Elon Musk says Tesla will spend US$1 billion on Dojo supercomputer over next year, https://www.scmp.com/tech/big-tech/article/3228285/ 

elon-musk-says-tesla-will-spend-us1-billion-dojo-supercomputer-over-next-year?campaign=3228285&module=perpetual_scroll_0&pgtype=article (accessed 

29 November 2023). 

[15] Shicong Dou, YICAI, Nissan Launches Trial Robotaxi Service in China's Suzhou, https://www.yicaiglobal.com/news/nissan-launches-trial-robotaxi-service-inchina-suzhou (accessed 29 November 2023). 

[16] Reuters, Toyota, Pony.ai Plan to Mass Produce Robotaxis in China, https://www.usnews.com/news/technology/articles/2023-08-04/toyota-chinas-pony-aito-set-up-jv-with-139-million-investment (accessed 29 November 2023). [17] Mercedes-Benz, Software architects: Mercedes-Benz previews its operating system MB.OS, https://media.mbusa.com/releases/software-architects-mercedesbenz-previews-its-operating-system-mbos (accessed 29 November 2023). 

[18] Latane Montague, Joanne Rotondi, Susan McAuliffe, Hannah Grace, Hillary Neger, DOT releases comprehensive plan regarding autonomous vehicles, https:// 

www.engage.hoganlovells.com/knowledgeservices/news/department-of-transportation-releases-comprehensive-plan-regarding-autonomous-vehicles (accessed 22 November 2023). 

[19] Prateek Bansal, and Kara M. Kockelman, Forecasting Americans' long-term adoption of connected and autonomous vehicle technologies, *Transportation* 

Research Part A: Policy and Practice, 95 (2017) 49-63. 

[20] Litman, Todd, TRID, Autonomous vehicle implementation predictions: Implications for transport planning, https://trid.trb.org/View/1678741 (accessed 12 

November 2023). 

[21] Anderson, James M., Kalra Nidhi, Karlyn D. Stanley, Paul Sorensen, Constantine Samaras, and Oluwatobi A. Oluwatola, Autonomous vehicle technology: A 

guide for policymakers, Rand Corporation, 2014. 

[22] Jinan Piao, McDonald Mike, Advanced driver assistance systems from autonomous to cooperative approach, Transport reviews, 28 (5) (2008) 659–684. 

[23] Folsom, Tyler C, Social ramifications of autonomous urban land vehicles, In 2011 IEEE International Symposium on Technology and Society (ISTAS), pp. 1-6. 

IEEE, 2011. 

[24] James Manyika, Michael Chui, Jacques Bughin, Richard Dobbs, Peter Bisson, Alex Marrs, Disruptive technologies: Advances that will transform life, business, and the global economy, https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/disruptive-technologies (accessed 12 November 2023). 

[25] Petit, Jonathan, and Steven E. Shladover, Potential cyberattacks on automated vehicles. *IEEE Transactions on Intelligent Transportation Systems*, 16 (2) (2014) 
546-556. 

[26] Fagnant J. Daniel, Kara Kockelman, Preparing a nation for autonomous vehicles: opportunities, barriers and policy recommendations, Transportation Research Part A: Policy and Practice, 77 (2015) 167–181. 

[27] Asif Faisal, Md Kamruzzaman, Tan Yigitcanlar, Graham Currie, Understanding autonomous vehicles, Journal of transport and land use, 12 (1) (2019) 45–72. 

[28] Bagloee, Saeed Asadi, Madjid Tavana, Mohsen Asadi, and Tracey Oliver, Autonomous vehicles: challenges, opportunities, and future implications for transportation policies, *Journal of Modern Transportation,* 24 (2016) 284-303. 

[29] Adrija Ghansiyal, Mamta Mittal, Arpan Kumar Kar, Information management challenges in autonomous vehicles: A systematic literature review, Journal of Cases on Information Technology (JCIT), 23 (3) (2021) 58–77. 

[30] Riccardo Coppola, Maurizio Morisio, Connected car: technologies, issues, future trends, ACM Computing Surveys (CSUR), 49 (3) (2016) 1–36. 

[31] Fang, Ji, Ruichen Xu, Yuan Yang, Xiaofan Li, Sha Zhang, Xiao Peng, and Xiaoyong Liu, Introduction and simulation of dedicated short range communication, In 2017 IEEE 5th International Symposium on Electromagnetic Compatibility (EMC-Beijing), pp. 1-10. IEEE, 2017. 

[32] David Elliott, Keen Walter, Lei Miao, Recent advances in connected and automated vehicles, Journal of Traffic and Transportation Engineering 6 (2) (2019) 
109–131 (English edition). 

[33] Sherali Zeadally, Ray Hunt, Yuh-Shyan Chen, Angela Irwin, Aamir Hassan, Vehicular ad hoc networks (VANETS): status, results, and challenges, Telecommunication Systems 50 (2012) 217–241. 

[34] Kenney, John B, Dedicated short-range communications (DSRC) standards in the United States, *Proceedings of the IEEE*, 99 (7) (2011) 1162-1182. [35] Chung-Ming Huang, Shih-Yang Lin, Cooperative vehicle collision warning system using the vector-based approach with dedicated short range communication data transmission, IET intelligent Transport Systems, 8 (2) (2014) 124–134. 

[36] Claudia Campolo, Alexey Vinel, Antonella Molinaro, Yevgeni Koucheryavy, Modeling broadcasting in IEEE 802.11 p/WAVE vehicular networks, IEEE 
Communications Letters 15 (2) (2010) 199–201. 

[37] Van Eenennaam, Martijn, Wouter Klein Wolterink, Georgios Karagiannis, and Geert Heijenk, Exploring the solution space of beaconing in VANETs, In 2009 IEEE vehicular networking conference (VNC), pp. 1-8. IEEE, 2009. 

[38] E. Steven Shladover, Christopher Nowakowski, Xiao-Yun Lu, Robert Ferlis, Cooperative adaptive cruise control: Definitions and operating concepts, Transportation Research Record 2489 (1) (2015) 145–152. 

[39] Yangsheng Jiang, Fangyi Zhu, Qiufan Gu, Yunxia Wu, Xuguang Wen, Zhihong Yao, Influence of CAVs platoon characteristics on fundamental diagram of mixed traffic flow, Physica A: Statistical Mechanics and its Applications (2023) 128906. 

[40] Hatem Abou-Zeid, Farhan Pervez, Abdulkareem Adinoyi, Mohammed Aljlayl, Halim Yanikomeroglu, Cellular V2X transmission for connected and autonomous vehicles standardization, applications, and enabling technologies, IEEE Consumer Electronics Magazine 8 (6) (2019) 91–98. 

[41] Ardalan Vahidi, Antonio Sciarretta, Energy saving potentials of connected and automated vehicles, Transportation Research Part C: Emerging Technologies 95 
(2018) 822–843. 

[42] Ahmadreza Talebian, Sabyasachee Mishra, Predicting the adoption of connected autonomous vehicles: A new approach based on the theory of diffusion of innovations, Transportation Research Part C: Emerging Technologies, 95 (2018) 363–380. 

[43] Zhihong Yao, Taorang Xu, Yangsheng Jiang, Rong Hu, Linear stability analysis of heterogeneous traffic flow considering degradations of connected automated vehicles and reaction time, Physica A: Statistical Mechanics and Its Applications 561 (2021) 125218. 

[44] Yuan Gong, Wen-Xing Zhu, Modeling the heterogeneous traffic flow considering the effect of self-stabilizing and autonomous vehicles, Chinese Physics B 31 (2) 
(2022) 024502. 

[45] Jinjue Li, Chunhui Yu, Zilin Shen, Zicheng Su, Wanjing Ma, A survey on urban traffic control under mixed traffic environment with connected automated vehicles, Transportation Research Part C: Emerging Technologies 154 (2023) 104258. 

[46] Bokui Chen, Yaohui Chen, Yao Wu, Xiao Fu, Kai Zhang, The effects of autonomous vehicles on traffic efficiency and energy consumption, Systems 11 (7) 
(2023) 347. 

[47] Santhanakrishnan Narayanan, Emmanouil Chaniotakis, Constantinos Antoniou, Factors affecting traffic flow efficiency implications of connected and autonomous vehicles: A review and policy recommendations, Advances in Transport Policy and Planning (2020) 1–50. 

[48] Dong-Fan Xie, Yong-Qi Wen, Xiao-Mei Zhao, Xin-Gang Li, Zhengbing He, Cooperative driving strategies of connected vehicles for stabilizing traffic flow, Transportmetrica B: Transport Dynamics 8 (1) (2020) 166–181. 

[49] Haotian Shi, Yang Zhou, Xin Wang, Sicheng Fu, Siyuan Gong, Bin Ran, A deep reinforcement learning-based distributed connected automated vehicle control under communication failure, Computer-Aided Civil and Infrastructure Engineering 37 (15) (2022) 2033–2051. 

[50] Yongsheng Qian, Cheng Da, Junwei Zeng, Xuexin Wang, Yongzhi Zhang, Dejie Xu, A bidirectional quasi-moving block cellular automaton model for singletrack railways, Physica A: Statistical Mechanics and its Applications 598 (2022) 127327. 

[51] Jiahe Zhang, Yongsheng Qian, Junwei Zeng, Xuting Wei, Haijun Li, Hybrid characteristics of heterogeneous traffic flow mixed with electric vehicles considering the amplitude of acceleration and deceleration, Physica A: Statistical Mechanics and its Applications 614 (2023) 128556. 

[52] Junwei Zeng, Yongsheng Qian, Ziwen Lv, Fan Yin, Leipeng Zhu, Yongzhi Zhang, Dejie Xu, Expressway traffic flow under the combined bottleneck of accident and on-ramp in framework of Kerner's three-phase traffic theory, Physica A: Statistical Mechanics and its Applications 574 (2021) 125918. 

[53] Junwei Zeng, Yongsheng Qian, Fan Yin, Leipeng Zhu, Dejie Xu, A multi-value cellular automata model for multi-lane traffic flow under lagrange coordinate, Computational and Mathematical Organization Theory (2022) 1–15. 

[54] Dong-Fan Xie, Xiao-Mei Zhao, Zhengbing He, Heterogeneous traffic mixing regular and connected vehicles: Modeling and stabilization, IEEE Transactions on Intelligent Transportation Systems 20 (6) (2018) 2060–2071. 

[55] Junwei Zeng, Yongsheng Qian, Jiao Li, Yongzhi Zhang, Dejie Xu, Congestion and energy consumption of heterogeneous traffic flow mixed with intelligent connected vehicles and platoons, Physica A: Statistical Mechanics and its Applications 609 (2023) 128331. 

[56] Guangyang Hou, Evaluating efficiency and safety of mixed traffic with connected and autonomous vehicles in adverse weather, Sustainability 15 (4) (2023) 
3138. 

[57] Maxime Gu´eriau and Ivana Dusparic, Quantifying the impact of connected and autonomous vehicles on traffic efficiency and safety in mixed traffic, in 2020 IEEE 23rd International Conference on Intelligent Transportation Systems (ITSC), pp. 1-8. IEEE, 2020. 

[58] Talebpour Alireza, Hani S. Mahmassani, Influence of connected and autonomous vehicles on traffic flow stability and throughput, Transportation Research Part C: Emerging Technologies 71 (2016) 143–163. 

[59] Do Wooseok, Omid M. Rouhani, Luis Miranda-Moreno, Simulation-based connected and automated vehicle models on highway sections: a literature review, Journal of Advanced Transportation 2019 (2019). 

[60] Arian Houshmand, Salomon ´ Wollenstein-Betech, and Christos G. Cassandras, The penetration rate effect of connected and automated vehicles in mixed traffic routing, in 2019 IEEE Intelligent Transportation Systems Conference (ITSC), pp. 1755-1760. IEEE, 2019. 

[61] Yibing Wang, Long Wang, Jingqiu Guo, Papamichail Ioannis, Markos Papageorgiou, Fei-Yue Wang, Robert Bertini, Wei Hua, Qinmin Yang, Ego-efficient lane changes of connected and automated vehicles with impacts on traffic flow, Transportation Research Part C: Emerging Technologies 138, 138 (2022) 103478. 

[62] Hongyan Guo, Jun Liu, Qikun Dai, Hong Chen, Yulei Wang, Wanzhong Zhao, A distributed adaptive triple-step nonlinear control for a connected automated vehicle platoon with dynamic uncertainty, IEEE Internet of Things Journal 7 (5) (2020) 3861–3871. 

[63] Anye Zhou, Siyuan Gong, Chaojie Wang, Srinivas Peeta, Smooth-switching control-based cooperative adaptive cruise control by considering dynamic information flow topology, Transportation Research Record 2674 (4) (2020) 444–458. 

[64] Yang Zhou, Meng Wang, Soyoung Ahn, Distributed model predictive control approach for cooperative car-following with guaranteed local and string stability, Transportation Research Part B: Methodological, 128 (2019) 69–86. 

[65] Sikai Chen, Jiqian Dong, Paul Ha, Yujie Li, Samuel Labi, Graph neural network and reinforcement learning for multi-agent cooperative control of connected autonomous vehicles, Computer-Aided Civil and Infrastructure Engineering 36 (7) (2021) 838–857. 

[66] Yipei Wang, Shuaikun Hou, Xin Wang, Reinforcement learning-based bird-view automated vehicle control to avoid crossing traffic, Computer-Aided Civil and Infrastructure Engineering 36 (7) (2021) 890–901. 

[67] Yingjun Ye, Xiaohui Zhang, Jian Sun, Automated vehicle's behavior decision making using deep reinforcement learning and high-fidelity simulation environment, Transportation Research Part C: Emerging Technologies 107 (2019) 155–170. 

[68] Daofei Li, Ao Liu, Personalized lane change decision algorithm using deep reinforcement learning approach, Applied Intelligence 53 (11) (2023) 
13192–13205. 

[69] Wei Zhou, Dong Chen, Jun Yan, Zhaojian Li, Huilin Yin, Wanchen Ge, Multi-agent reinforcement learning for cooperative lane changing of connected and autonomous vehicles in mixed traffic, Autonomous Intelligent Systems 2 (1) (2022) 5. 

[70] Hui Song, Dayi Qu, Haibing Guo, Kekun Zhang, Tao Wang, Lane-changing trajectory tracking and simulation of autonomous vehicles based on model predictive control, Sustainability 14 (20) (2022) 13272. 

[71] Seongjin Choi, Hwasoo Yeo, Framework for simulation-based lane change control for autonomous vehicles, in 2017 IEEE intelligent vehicles symposium (IV), 
IEEE, 2017, pp. 699–704. 

[72] Simon Ulbrich and Markus Maurer, Towards tactical lane change behavior planning for automated vehicles, in 2015 IEEE 18th International Conference on Intelligent Transportation Systems, pp. 989-995. IEEE, 2015. 

[73] Wei Liu, Min Hua, Zhiyun Deng, Meng Zonglin, Yanjun Huang, Chuan Hu, Shunhui Song, et al., A systematic survey of control techniques and applications in connected and automated vehicles, IEEE Internet of Things Journal (2023). 

[74] Solmaz Razmi Rad, Haneen Farah, Henk Taale, Bart van Arem, Serge P. Hoogendoorn, Design and operation of dedicated lanes for connected and automated vehicles on motorways: A conceptual framework and research agenda, Transportation Research Part C: Emerging Technologies 117 (2020) 102664. 

[75] Lanhang Ye, Toshiyuki Yamamoto, Impact of dedicated lanes for connected and autonomous vehicle on traffic flow throughput, Physica A: Statistical Mechanics and its Applications 512 (2018) 588–597. 

[76] Seungwuk Moon, Ilki Moon, Kyongsu Yi, Design, tuning, and evaluation of a full-range adaptive cruise control system with collision avoidance, Control Engineering Practice 17 (4) (2009) 442–455. 

[77] Hyunjin Park, Cheol Oh, A vehicle speed harmonization strategy for minimizing inter-vehicle crash risks, Accident Analysis & Prevention 128 (2019) 230–239. 

[78] Zhihong Yao, Rong Hu, Yangsheng Jiang, Taorang Xu, Stability and safety evaluation of mixed traffic flow with connected automated vehicles on expressways, Journal of Safety Research 75 (2020) 262–274. 

[79] Aaron Hula, Amy Bunker, Jeff Alson, Light-Duty Automotive Technology, Carbon Dioxide Emissions, and Fuel Economy Trends: 1975 Through 2015 (accessed 2 September 2023). 

[80] Scott Drew Pendleton, Hans Andersen, Xinxin Du, Xiaotong Shen, Malika Meghjani, You Hong Eng, Daniela Rus, Marcelo H. Ang, Perception, planning, control, and coordination for autonomous vehicles, Machines 5 (1) (2017) 6. 

[81] Raphael E. Stern, Shumo Cui, Maria Laura Delle Monache, Rahul Bhadani, Matt Bunting, Miles Churchill, Nathaniel Hamilton et al, Dissipation of stop-and-go waves via control of autonomous vehicles: Field experiments, *Transportation Research Part C: Emerging Technologies*, 89 (2018) 205-221. 

[82] Denos C. Gazis, Robert Herman, The moving and "phantom" bottlenecks, Transportation Science 26 (3) (1992) 223–229. 

[83] Soyoung Ahn and Michael J. Cassidy, Freeway traffic oscillations and vehicle lane-change maneuvers, *Transportation and Traffic Theory*, 1 (2007) 691-710. 

[84] Jorge A. Laval and Carlos F. Daganzo, Lane-changing in traffic streams, *Transportation Research Part B: Methodological*, 40 (3) (2006) 251-264. 

[85] Zuduo Zheng, Soyoung Ahn, Danjue Chen, Jorge Laval, Applications of wavelet transform for analysis of freeway traffic: Bottlenecks, transient traffic, and traffic oscillations, Transportation Research Part B: Methodological 45 (2) (2011) 372–384. 

[86] Robert L. Bertini, Monica T. Leal, Empirical study of traffic features at a freeway lane drop, Journal of Transportation Engineering 131 (6) (2005) 397–407. [87] Wen-Long Jin, Yu Zhang, Paramics simulation of periodic oscillations caused by network geometry, Transportation Research Record 1934 (1) (2005) 188–196. [88] H.B. Zhu, Y.J. Zhou, W.J. Wu, Modeling traffic flow mixed with automated vehicles considering drivers' character difference, Physica A: Statistical Mechanics and its Applications 549 (2020) 124337. 

[89] L.C Davis, The effects of mechanical response on the dynamics and string stability of a platoon of adaptive cruise control vehicles, Physica A: Statistical Mechanics and its Applications 392 (17) (2013) 3798–3805. 

[90] Chi-Ying Liang, Huei Peng, String stability analysis of adaptive cruise controlled vehicles, JSME International Journal Series C Mechanical Systems Machine Elements and Manufacturing 43 (3) (2000) 671–677. 

[91] Zhihong Yao, Rong Hu, Yi Wang, Yangsheng Jiang, Bin Ran, Yanru Chen, Stability analysis and the fundamental diagram for mixed connected automated and human-driven vehicles, Physica A: Statistical Mechanics and Its Applications 533 (2019) 121931. 

[92] Chaoru Lu, Arvid Aakre, A new adaptive cruise control strategy and its stabilization effect on traffic flow, European Transport Research Review 10 (2018) 
1–11. 

[93] Lanhang Ye, Toshiyuki Yamamoto, Evaluating the impact of connected and autonomous vehicles on traffic safety, Physica A: Statistical Mechanics and its Applications 526 (2019) 121009. 

[94] Shuang Jin, Di-Hua Sun, Min Zhao, Yang Li, Jin Chen, Modeling and stability analysis of mixed traffic with conventional and connected automated vehicles from cyber physical perspective, Physica A: Statistical Mechanics and its Applications 551 (2020) 124217. 

[95] Amir Ghiasi, Xiaopeng Li, Jiaqi Ma, A mixed traffic speed harmonization model with connected autonomous vehicles, Transportation Research Part C: 
Emerging Technologies 104 (2019) 210–233. 

[96] Falko Dressler, Hannes Hartenstein, Onur Altintas, and Ozan K. Tonguz, Inter-vehicle communication: Quo vadis, *IEEE Communications Magazine*, 52 (6) (2014) 
170-177. 

[97] Joyoung Lee, Byungkyu Park, Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment, IEEE Transactions on Intelligent Transportation Systems 13 (1) (2012) 81–90. 

[98] Li Li, Fei-Yue Wang, Cooperative driving at blind crossings using intervehicle communication, IEEE Transactions on Vehicular Technology 55 (6) (2006) 
1712–1724. 

[99] David Miculescu and Sertac Karaman, Polling-systems-based control of high-performance provably-safe autonomous intersections, in 53rd IEEE conference on decision and control, pp. 1417-1423. IEEE, 2014. 

[100] Feng Zhu and Satish V. Ukkusuri, A linear programming formulation for autonomous intersection control within a dynamic traffic assignment and connected vehicle environment, *Transportation Research Part C: Emerging Technologies,* 55 (2015) 363-378. 

[101] Ismail H. Zohdy, Raj Kishore Kamalanathsharma, and Hesham Rakha, Intersection management for autonomous vehicles using iCACC, in 2012 15th international IEEE conference on intelligent transportation systems, pp. 1109-1114. IEEE, 2012. 

[102] Yue J. Zhang, Andreas A. Malikopoulos, and Christos G. Cassandras, Optimal control and coordination of connected and automated vehicles at urban traffic intersections, in 2016 American Control Conference (ACC), pp. 6227-6232. IEEE, 2016. 

[103] Andreas A. Malikopoulos, Christos G. Cassandras, and Yue J. Zhang, A decentralized energy-optimal control framework for connected automated vehicles at signal-free intersections, *Automatica*, 93 (2018), 244-256. 

[104] Yue Zhang and Christos G. Cassandras, An impact study of integrating connected automated vehicles with conventional traffic, *Annual Reviews in Control*, 48 
(2019) 347-356. 

[105] Seong-Woo Kim, Zhuang Jie Chong, Baoxing Qin, Xiaotong Shen, Zhuoqi Cheng, Wei Liu, and Marcelo H. Ang, Cooperative perception for autonomous vehicle control on the road: Motivation and experimental results, in 2013 IEEE/RSJ International Conference on Intelligent Robots and Systems, pp. 5059-5066. IEEE, 
2013. 

[106] Skanda Vivek, David Yanni, Peter J. Yunker, and Jesse L. Silverberg, Cyberphysical risks of hacked internet-connected vehicles, *Physical Review E*, 100 (1) 
(2019) 012316. 

[107] Axelrod, C. Warren, Cybersecurity in the age of autonomous vehicles, intelligent traffic controls and pervasive transportation networks, in 2017 IEEE Long Island Systems, Applications and Technology Conference (LISAT), pp. 1-6. IEEE, 2017. 

[108] Rong Yu, Yan Zhang, Gjessing Stein, Wenlong Xia, Kun Yang, Toward cloud-based vehicular networks with efficient resource management, IEEE Network 27 
(5) (2013) 48–55. 

[109] Jiawen Kang, Rong Yu, Xumin Huang, Magnus Jonsson, Hanna Bogucka, Stein Gjessing, Yan Zhang, Location privacy attacks and defenses in cloud-enabled internet of vehicles, IEEE Wireless Communications 23 (5) (2016) 52–59. 

[110] Meysam Ghanavati, Animesh Chakravarthy, Prathyush P. Menon, Analysis of automotive cyber-attacks on highways using partial differential equation models, IEEE Transactions on Control of Network Systems 5 (4) (2017) 1775–1786. 

[111] Pengcheng Wang, Xinkai Wu, Xiaozheng He, Modeling and analyzing cyberattack effects on connected automated vehicular platoons, Transportation Research Part C: Emerging Technologies 115 (2020) 102625. 

[112] Jian Zhang, Kunrun Wu, Min Cheng, Min Yang, Yang Cheng, Shen Li, Safety evaluation for connected and autonomous vehicles' exclusive lanes considering penetrate ratios and impact of trucks using surrogate safety measures, Journal of Advanced Transportation 2020 (2020) 1–16. 

[113] Amolika Sinha, Sai Chand, Kasun P. Wijayaratna, Navreet Virdi, and Vinayak Dixit, Comprehensive safety assessment in mixed fleets with connected and automated vehicles: A crash severity and rate evaluation of conventional vehicles, *Accident Analysis & Prevention*, 142 (2020) 105567. 

[114] Alkis Papadoulis, Mohammed Quddus, Marianna Imprialou, Evaluating the safety impact of connected and autonomous vehicles on motorways, Accident Analysis & Prevention 124 (2019) 12–22. 

[115] Amirhosein Karbasi, Steve O'Hern, Investigating the impact of connected and automated vehicles on signalized and unsignalized intersections safety in mixed traffic, Future Transportation 2 (1) (2022) 24–40. 

[116] UN-Habitat, World Cities Report 2022: Envisaging the Future of Cities seeks, https://unhabitat.org/wcr/ (accessed 10 September 2023). 

[117] Xiaobo Qu, Yang Yu, Mofan Zhou, Chin-Teng Lin, Xiangyu Wang, Jointly dampening traffic oscillations and improving energy consumption with electric, connected and automated vehicles: a reinforcement learning based approach, Applied Energy 257 (2020) 114030. 

[118] Cui, Shumo, Benjamin Seibold, Raphael Stern, and Daniel B. Work, Stabilizing traffic flow via a single autonomous vehicle: Possibilities and limitations, in 2017 IEEE Intelligent Vehicles Symposium (IV), pp. 1336-1341. IEEE, 2017. 

[119] Meng Wang, Winnie Daamen, Serge P. Hoogendoorn, Bart van Arem, Rolling horizon control framework for driver assistance systems. Part II: Cooperative sensing and cooperative control, Transportation Research Part C: Emerging Technologies 40 (2014) 290–311. 

[120] Vicente Milan´es, Steven E. Shladover, John Spring, Christopher Nowakowski, Hiroshi Kawazoe, Masahide Nakamura, Cooperative adaptive cruise control in real traffic situations, IEEE Transactions on Intelligent Transportation Systems 15 (1) (2013) 296–305. 

[121] Zia Wadud, Don MacKenzie, Paul Leiby, Help or hindrance? The travel, energy and carbon impacts of highly automated vehicles, Transportation Research Part A: Policy and Practice 86 (2016) 1–18. 

[122] Austin Brown, Jeffrey Gonder, Brittany Repac, An analysis of possible energy impacts of automated vehicles, Road Vehicle Automation (2014) 137–153. [123] Karl Simon, Jeff Alson, Lisa Snapp, Aaron Hula. Can transportation emission reductions be achieved autonomously?, 2015, pp. 13910–13911. 

[124] Myriam Alexander-Kearns, Miranda Peterson, A. Cassady. The impact of vehicle automation on carbon emissions, Center for American Progress, 2016. [125] Jeffery B. Greenblatt, Susan Shaheen, Automated vehicles, on-demand mobility, and environmental impacts, Current Sustainable/Renewable Energy Reports 2 
(2015) 74–81. 

[126] Arash Olia, Hossam Abdelgawad, Baher Abdulhai, and Saiedeh N. Razavi, Assessing the potential impacts of connected vehicles: mobility, environmental, and safety perspectives, *Journal of Intelligent Transportation Systems*, 20 (3) (2016) 229-243. 

[127] Handong Yao, Jianxun Cui, Xiaopeng Li, Yu Wang, Shi An, A trajectory smoothing method at signalized intersection based on individualized variable speed limits with location optimization, Transportation Research Part D: Transport and Environment 62 (2018) 456–473. 

[128] Huifu Jiang, Jia Hu, An Shi, Meng Wang, Byungkyu Brian Park, Eco approaching at an isolated signalized intersection under partially connected and automated vehicles environment, Transportation Research Part C: Emerging Technologies 79 (2017) 290–307. 

[129] Fang Zhou, Xiaopeng Li, Jiaqi Ma, Parsimonious shooting heuristic for trajectory design of connected automated traffic part I: Theoretical analysis with generalized time geography, Transportation Research Part B: Methodological 95 (2017) 394–420. 

[130] Pangwei Wang, Jiang Yilun, Xiao Lin, Yi Zhao, Yinghong Li, A joint control model for connected vehicle platoon and arterial signal coordination, Journal of Intelligent Transportation Systems 24 (1) (2020) 81–92. 

[131] Qiu Jin, Guoyuan Wu, Kanok Boriboonsomsin, Matthew J. Barth, Power-based optimal longitudinal control for a connected eco-driving system, IEEE 
Transactions on Intelligent Transportation Systems 17 (10) (2016) 2900–2910. 

[132] Simon Stebbins, Mark Hickman, Jiwon Kim, and Hai L. Vu, Characterising green light optimal speed advisory trajectories for platoon-based optimisation, Transportation Research Part C: Emerging Technologies, 82 (2017) 43-62. 

[133] Xiaozheng He, Xinkai Wu, Eco-driving advisory strategies for a platoon of mixed gasoline and electric vehicles in a connected vehicle system, Transportation Research Part D: Transport and Environment 63 (2018) 907–922. 

[134] Xiao Han, Rui Ma, H. Michael Zhang, Energy-aware trajectory optimization of CAV platoons through a signalized intersection, Transportation Research Part C: 
Emerging Technologies 118 (2020) 102652. 

[135] Rodrigo Marçal Gandia, Fabio Antonialli, Bruna Habib Cavazza, Arthur Miranda Neto, Danilo Alves de Lima, Joel Yutaka Sugano, Isabelle Nicolai, and Andre Luiz Zambalde, Autonomous vehicles: scientometric and bibliometric review, *Transport Reviews*, 39 (1) (2019) 9–28. 

[136] Dimitris Milakis, Long-term implications of automated vehicles: An introduction, Transport Reviews 39 (1) (2019) 1–8. [137] Crystal Legacy, David Ashmore, Jan Scheurer, John Stone, Carey Curtis, Planning the driverless city, Transport Reviews 39 (1) (2019) 84–102. 

[138] Tom Cohen, Cl´emence Cavoli, Automated vehicles: Exploring possible consequences of government (non) intervention for congestion and accessibility, Transport Reviews 39 (1) (2019) 129–151. 

[139] Latane Montague, Joanne Rotondi, Lance Bultena, Susan McAuliffe, Hannah Graae, and Christina Bassick, NHTSA issues occupant protection safety standards for automated driving system equipped vehicles, https://www.engage.hoganlovells.com/knowledgeservices/news/nhtsa-issues-occupant-protection-safetystandards-for-automated-driving-system-equipped-vehicles (accessed 22 November 2023). 

[140] Telematics Wire, Global overseas ADAS and autonomous driving Tier 1 suppliers market to 2025, https://www.telematicswire.net/global-overseas-adas-andautonomous-driving-tier-1-suppliers-market-to-2025-germany-has-become-the-first-country-in-the-world-to-allow-l4-autonomous-vehicles-onto-public-roads 
(accessed 22 November 2023). 

[141] The Japan Times, Fully automated driving under certain conditions allowed in Japan, https://www.japantimes.co.jp/news/2023/04/02/national/level-4fully-automated-driving-allowed-japan (accessed 22 November 2023). 

[142] Andreas Neumann, Germany: German Government introduces bill for "Level-4" highly automated driving, https://www.globalcompliancenews.com/2021/ 
03/30/germany-german-government-introduces-bill-for-level-4-highly-automated-driving-23032021 (accessed 22 November 2023). 

[143] Iman Mahdinia, Amin Mohammadnazar, Ramin Arvin, and Asad J. Khattak, Integration of automated vehicles in mixed traffic: Evaluating changes in performance of following human-driven vehicles, Accident Analysis & *Prevention*, 152 (2021) 106006. 

[144] Elina Aittoniemi, Evidence on impacts of automated vehicles on traffic flow efficiency and emissions: Systematic review, IET Intelligent Transport Systems 16 
(10) (2022) 1306–1327. 

[145] Biagio Ciuffo, Konstantinos Mattas, Michail Makridis, Giovanni Albano, Aikaterini Anesiadou, Yinglong He, Szil´ard Josvai, et al., Requiem on the positive effects of commercial adaptive cruise control on motorway traffic and recommendations for future automated driving systems, Transportation Research Part C: 
Emerging Technologies 130 (2021) 103305. 

[146] Xiaopeng Li, Trade-off between safety, mobility and stability in automated vehicle following control: An analytical method, Transportation Research Part B: 
Methodological, 166 (2022) 1–18. 

[147] Christopher Nowakowski, Steven E. Shladover, Ching-Yao Chan, and Han-Shue Tan, Development of California regulations to govern testing and operation of automated driving systems, *Transportation Research Record*, 2489 (1) (2015) 137-144. 

[148] Yingying Xing, Huiyu Zhou, Xiao Han, Meng Zhang, Jian Lu, What influences vulnerable road users' perceptions of autonomous vehicles? A comparative analysis of the 2017 and 2019 Pittsburgh surveys, Technological Forecasting and Social Change 176 (2022) 121454. 

[149] Roger Bennett, Rohini Vijaygopal, Rita Kottasz, Attitudes towards autonomous vehicles among people with physical disabilities, Transportation Research Part A: Policy and Practice 127 (2019) 1–17. 

[150] Teresa Brell, Ralf Philipsen, Martina Ziefle, Suspicious minds?–users' perceptions of autonomous and connected driving, Theoretical Issues in Ergonomics Science 20 (3) (2019) 301–331. 