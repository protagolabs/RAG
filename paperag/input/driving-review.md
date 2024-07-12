

![0_image_0.png](0_image_0.png)

![0_image_1.png](0_image_1.png)

![0_image_3.png](0_image_3.png)

![0_image_4.png](0_image_4.png)

Review 

![0_image_2.png](0_image_2.png)

| Contents lists available at ScienceDirect                                        |
|----------------------------------------------------------------------------------|
| Expert Systems With Applications  journal homepage: www.elsevier.com/locate/eswa |

Autonomous driving system: A comprehensive survey Jingyuan Zhao a,*, Wenyi Zhao b, Bo Deng b, Zhenghong Wang c, Feng Zhang b, Wenxiang Zheng b, Wanke Cao b, Jinrui Nan b,*, Yubo Lian d, Andrew F. Burke a a Institute of Transportation Studies, University of California Davis, Davis, CA 95616, USA b Shenzhen Automotive Research Institute, Beijing Institute of Technology, Beijing 100811, China c Hubei Longzhong Laboratory, Hubei University of Arts and Science, Xiangyang 441000, China d *BYD Automotive Engineering Research Institute, Shenzhen 518118, China* 

| ARTICLE INFO  Keywords:  Autonomous driving  Deep learning  Scene perception  Localization  Motion planning  Decision-making   |
|--------------------------------------------------------------------------------------------------------------------------------|

## Abstract

Automation is increasingly at the forefront of transportation research, with the potential to bring fully autonomous vehicles to our roads in the coming years. This comprehensive survey provides a holistic look at the essential components and cutting-edge technologies that are driving the development and implementation of autonomous driving. It starts by evaluating two critical system architectures that are fundamental to the operation of autonomous vehicles: the layered and end-to-end structures. It then examines the critical areas of scene perception and localization, emphasizing the importance of sensor technologies. These technologies are vital for tasks such as object detection and semantic segmentation, which allow vehicles to understand and navigate their environment. A special focus is given to the complex topic of object detection, along with suggestions for how it can be enhanced. The survey then proceeds to provide detailed discussions on path planning, trajectory prediction, and decision-making processes. These elements are crucial for the smooth navigation of autonomous vehicles, and the survey highlights the role of artificial intelligence (AI) and machine learning in these processes. 

Overall, the survey presents the rapid progress in the field of autonomous driving, offering a comprehensive assessment of the technologies and innovations that are essential for moving toward a safe and efficient autonomous future. 

Abbreviations: AI, Artificial intelligence; ALV, Autonomous land vehicle; ADs, Autonomous driving systems; ALVINNs, Autonomous land vehicles in systems based on neural networks; BC, Behavior cloning; CNNs, Convolutional neural networks; CIL, Controlled imitation learning; CVAT, Computer vision annotation tool; CRFs, Conditional random fields; DDQN, Dueling deep q-network; DDP, Differential dynamic programming; DNNs, Deep neural networks; DRL, Deep reinforcement learning; DGMs, Deep generative models; DARPA, Defense advanced research projects agency; E-RPN, Euler-region-proposal network; FCN, Fully convolutional network; FNNs, Feedforward neural networks; FSM, Finite state machine; GRUs, Gated recurrent units; GANs, Generative adversarial networks; GCN, Graph convolutional network; GMF, Gaussian mean field; GPU, Graphic processing unit; GAIL, Generative adversarial imitation learning; GPS, Global positioning system; HD, 
High-definition; IL, Imitate learning; IMU, Inertial measurement unit; IoV, Internet of vehicles; IRL, Inverse reinforcement learning; IMLS, Implicit moving least squares; ILC, Iterative learning control; JPDA, Joint probabilistic data association; LFA, Local feature aggregation; LaneRoI, Lane-graph region-of-interest; LQR, 
Linear quadratic regulator; LSTM, Long short-term memory; MIT, Massachusetts institute of technology; MV3D, Multi-view 3d networks; MOT, Multi-object tracking; MHT, Multi-hypothesis tracking; MDP, Markov decision process; MARL, Multi-agent reinforcement learning; MPC, Model predictive control; NMS, Non-maximum suppression; MFRL, Multi-fidelity reinforcement learning; POMDP, Partially observable Markov decision process; RCNNs, Region-based convolutional neural networks; RNNs, Recurrent neural networks; RGBD, Red-green–blue-depth; RCNN, Region-based CNN; RPN, Region proposal network; RRL, Road research laboratory; SAE, Society of automobile engineers; SVO, Semi-direct visual odometry; SLAM, Simultaneous localization and mapping; SSD, Single shot detector; SVM, Support vector machine; STGCNNs, Spatio-temporal graph cnns; SSGP, Sparse spectral gaussian process; TPCN, Temporal point cloud networks; VFE, Voxel feature encoding; V2X, Vehicle to everything; V2I, Vehicle to infrastructure; V2N, Vehicle to network; V2P, Vehicle to pedestrian; V2V, Vehicle to vehicle; VO, Visual odometry; YOLO, You only look once. 

* Corresponding authors. 

E-mail addresses: jyzhao@ucdavis.edu (J. Zhao), 3220210332@bit.edu.cn (W. Zhao), db98@bit.edu.cn (B. Deng), 202208551062@hbuas.edu.cn (Z. Wang), 
zhangfeng@szari.ac.cn (F. Zhang), zhengwenxiang@szari.ac.cn (W. Zheng), caowanke@bit.edu.cn (W. Cao), nanjinrui@bit.edu.cn (J. Nan), lian.yubo@byd.com 
(Y. Lian), afburke@ucdavis.edu (A.F. Burke). https://doi.org/10.1016/j.eswa.2023.122836 Received 17 August 2023; Received in revised form 14 November 2023; Accepted 1 December 2023 Available online 2 December 2023 0957-4174/© 2023 Elsevier Ltd. All rights reserved.

## 1. **Introduction**

Over the past decade, self-driving/driverless cars have gained increasing popularity worldwide, promoting the autonomous driving revolution (Baruch, 2016). The use of autonomous driving technology can improve mobility in crowded cities, reduce traffic congestion, and improve travel safety (Nunes & Axhausen, 2021). The British Road Research Laboratory showed a video of autonomous driving, in the early 1970 s, which aroused huge interest in both academia and industry. Since then, huge efforts have been devoted worldwide by researchers and engineers from around the world to improve the autonomous technology. In 1984, the U.S. Defense Advanced Research Projects Agency (DARPA) partnered with the army to launch the Autonomous Land Vehicle (ALV) program. Since the 1980 s, many famous universities such as Carnegie Mellon University (CMU), Stanford University, and Massachusetts Institute of Technology (MIT) etc., have successively joined the research on autonomous driving. Good examples include the NavLab series of intelligent vehicles developed by Carnegie Mellon University in the United States (Thorpe et al., 1988) and the ARGO test vehicle developed by the VisLab Laboratory of the University of Parma in Italy (Bertozzi et al., 2006). In addition to active research in the field of unmanned driving underpinned by scientific and research institutions, many automobile manufacturers such as Audi, BMW, Ford, General Motors, Mercedes, Tesla, Volvo and so on also began to deploy in the field of unmanned vehicles since the start of the decade of the 2010 s (Greenblatt, 2016). Some companies even adopt the "one-stop" SAE Level 4 + development route for designing commercial autonomous driving. Since the DARPA Grand Challenge in 2004 and 2005, datadriven, machine learning-based techniques have been widely used in autonomous driving and is translating into a world of computercontrolled vehicles with autonomy and intelligence. 

In order to eliminate the inconsistency and confusion in the terminology used in the autonomous industry, Society of Automobile Engineers (SAE) proposed to define an accurate and consistent vocabulary, launched as an official document named SAE-J3016 in 2014, which clearly classified Levels of Driving Automation on a scale of 0 to 5 (International, 2023), as shown in Fig. 1. The higher the level, the higher the degree of automation. However, the current autonomous driving is still not a fully stable technology per se, and has been at the level 2 for years. The jump from Level 2 to Level 3 require craftsmanship, complex formulations and elaborate implementations, which presents severe challenges and introduces excessive cost and uncertainty to the autonomous process. Safety and robust security operation remain major factors in the market for the foreseeable future. Careful consideration should be given to how to transform autonomous driving from niche to widespread commercial viability. Moreover, the accuracy and sensitivity of hardware seriously affect the safety of autonomous driving during the daily operation. Various high-cost sensors are difficult to put into use on a large scale. Deep learning has brought about a paradigm shift in the field of AI, empowering computational models with the ability to learn intricate data representations through multiple layers of processing (LeCun et al., 2015). These state-of-the-art methods have made significant advancements across various domains, such as enhancing speech recognition accuracy, achieving remarkable success in visual object recognition tasks, enabling precise object detection, and impacting numerous other areas of research and application. The remarkable achievements of deep learning algorithms have propelled the boundaries of what was previously thought possible in the realm of AI. Deep learning methods offer opportunity to perceive, make predictions about future scenarios, and take decisions that are rational/ 
optimal given these predictions (Ghahramani, 2015). In the realm of autonomous driving, machine learning and deep learning have permeated various domains (Bachute & Subhedar, 2021). However, the blackbox and inexplicable nature of neural networks have a huge impact on the perception, decision, and execution, which makes autonomous driving vulnerable to environmental influences and external interference (Van Brummelen et al., 2018). The current decision planning is mainly based on the planner and lattice state algorithms using vehicle and road models. Therefore, we must carefully consider the security and robustness of deep learning, which has been an unsolved problem for several years. In cloud services, unstable vehicle-to-vehicle (V2V) links and centralized resource allocation methods with high signaling overhead become bottlenecks for safety–critical applications. This can be described as an NP-hard problem that is expected to be solved by specialized network architectures (Tkatek et al., 2020). 

## 2. **Scope Of The Survey**

To extract insights into the structure and patterns embedded within 

![1_image_0.png](1_image_0.png)

the scientific literature pertaining to autonomous driving, bibliometric networks are constructed (Fig. 2), through the application of VOSviewer 
(VOSviewer, 2023). The visualization and subsequent analysis of cooccurrence networks, comprised of significant terms, allow for the identification of influential works, notable initiatives, and emergent research directions in the domain. The blueprint not only facilitates a holistic understanding of the intellectual landscape of autonomous driving 

![2_image_0.png](2_image_0.png)

research but also aids in uncovering pivotal trends and collaborations that are integral to the field. With a focus on burgeoning and promising research avenues, this survey offers a succinct yet thorough overview of the dynamic landscape within the realm of autonomous driving.

In this survey, Section 3 initiates our summary with a succinct outline of system architectures pertinent to autonomous driving. It then disaggregates autonomous driving into three cardinal layers delineated in subsequent sections: perception and localization ( Section 4 ), motion

![2_image_1.png](2_image_1.png)

planning and decision-making (Section 5). A crucial facet of autonomous driving development—simulators and scenario generation tools—receive a methodical examination in Section 6. The survey culminates with Section 7 spotlighting prevailing challenges, followed by Section 8 which canvasses promising trajectories for impending research in this dynamic field. 

## 3. **System Architectures For Autonomous Driving**

The architectural framework underpinning the functionality of autonomous driving systems plays an indispensable role in fortifying their robustness and prognosticating their capacity for prospective expansion (Fig. 3). Herein, we provide an overview of the system architecture essential for autonomous driving. This includes the layered and end-to-end architectures, with the goal of giving readers a foundational understanding of the architectural principles that operate at the systemic level in the field of autonomous driving. These driving systems exemplify autonomous decision-making agents, necessitating the realtime processing of voluminous data streams emanating from a constellation of diverse sensors. It is imperative to acknowledge that architectural variances among different autonomous driving systems induce disparities in data processing flows and decision-making trajectories, thereby engendering a spectrum of operational dynamics. 

## 3.1. Layered Architecture

The layered architecture is a widely used architecture (Fig. 4). Unmanned driving systems can be divided into three levels: perception and simultaneous localization and mapping (SLAM) layer, planning layer, and control layer (Grigorescu et al., 2020). Commencing with the perception system, this layer harnesses data derived from an array of sensors, encompassing GPS, inertial measurement units (IMUs) and so on. This data fusion is pivotal for establishing dynamic information and generating a coherent internal environmental representation, utilizing additional sensors such as cameras, radar, and lidar. The localization subsystem, which is part of the SLAM system, is responsible for estimating the state of the vehicle (attitude, linear velocity, angular velocity, etc.) to construct the environment map. The first-order mapping subsystem, also part of the SLAM system, receives offline maps and the vehicle's state as input and produces online maps as output, which can improve the information available to the decision-making system. The motion planning system is responsible for navigating the vehicle from its starting position to a user-defined final position, while considering the vehicle's current state, an internal representation of the environment, traffic rules, and passenger safety and comfort. The motion controller system receives the motion decision, and the obstacle avoidance subsystem modifies and calculates steering wheel angle, accelerator opening, brake force, and other signals, sending instructions to the actuator to execute the modified motion as efficiently as possible (Badue et al., 
2021). 

## 3.2. End-To-End

The "end-to-end" approach is a method of learning driving policies directly from raw sensor data (e.g., images, point clouds, outputs brake, accelerator, and steering operations) without the need for manual feature engineering or modules. This paradigm first appeared in the 1990 s and established autonomous land vehicles in systems based on neural networks (ALVINN) (Pomerleau, 1988). At the time, ALVINN was designed to drive along predefined roads. In the mid-2000 s, research on end-to-end driving reached a climax again as Darpa's Autonomous Vehicle (DAV) successfully navigated a road full of obstacles (H. Xu et al., 2017). The development of computing hardware is also the basis for the use of the end-to-end model. Compared to layered architectures, end-to-end architectures are less demanding for sensor data annotation, so they are becoming more and more popular(Janai et al., 2020; Tampuu et al., 2020). Next, this paper briefly introduces some of the development of end-to-end autonomous driving technology in recent years, and the specific content is introduced in the following chapters. 

In the past few years, end-to-end control methods based on CNNs, RNNs, and reinforcement learning have been continuously proposed. NVIDIA and Comma AI developed an unmanned demonstration system using end-to-end deep learning (George et al., 2018). REF. (Innocenti et al., 2017) applied vision-based end-to-end steering angle prediction to the lane keeping task. Using lidar data, REF. (Rhinehart et al., 2018) 
made expert vehicle trajectory prediction based on imitation learning 
(IL) and model-based reinforcement learning. However, the driving policy of IL training may appear uncontrollable during testing. REF. (Codevilla et al., 2018) proposed a conditional IL method: conditioning IL into high-level command input, which enables IL to be effective in complex urban environments. In the other hand, REF. (D. Chen et al., 2021) assumed that neither the agent nor its operations will affect the environment, the model is simplified. Although there is little true independence, it does improve the training efficiency, simplifies the 

![3_image_0.png](3_image_0.png)

reward function, and performs better than the previous IL. In some complex urban traffic, REF. (Toromanoff et al., 2020) used a model-free DRL method Rainbow-IQN-Apex, which introduces end-to-end autonomous driving is much larger networks than in previous reinforcement learning work, enabling autonomous driving to handle tasks such as intersection management and traffic light detection. REF. (Chitta et al., 
2021) proposed the neural attention field, NEAT, a continuous function that maps the location of BEV scene coordinates to waypoints and semantics, and iteratively compresses high-dimensional 2D image features into a compact representation with an intermediate attention map. This approach allows the model to selectively focus on relevant input regions while ignoring information irrelevant to the driving task, effectively associating images with BEV representations. 

There are many kinds of sensors on autonomous driving. For the endto-end architecture, if only one kind of sensor data (such as RGB image) 
is used for driving control of the vehicle, it is difficult to guarantee the accuracy and safety. Therefore, multi-modal end-to-end autonomous driving based on the fusion of multiple sensors is also one of the key directions of current research (Xiao et al., 2020). The multi-modal controlled imitation learning (CIL) model is obtained by fusing the camera (RGB) and lidar (depth information). Compared with the singlemodal CIL model, the multi-modal CIL model has better driving performance, especially in the early stage. Fusion shows better performance relative to other epoch fusions. REF. (Prakash et al., 2021) used an attention mechanism to integrate image and LiDAR representations, and proposes a new multimodal fusion Transformer. The Transformer's selfattention mechanism fuses the global context about the 3D scene into the feature extraction layers of different modalities and integrate different modal information for vehicle autoregressive waypoint prediction. 

## 3.3. Merits Of The Two Architectures

The choice of system architecture plays a critical role in determining the performance and reliability of vehicle systems. One can distinguish between two main approaches: layered and end-to-end architectures based on their fundamental operational paradigms, each offering distinct benefits. Layered architectures are highly regarded for their modular design and reliability. This design approach results from their sophisticated structure, which, unfortunately, can also lead to increased complexity and the possibility of delays in system responses. These architectures typically involve separate modules for perception, decision making, and control, which communicate in a sequential manner. On the other hand, end-to-end architectures offer a more streamlined approach, enhancing efficiency by processing input data through a single neural network that outputs control commands directly. This architecture is often implemented with deep learning techniques that can learn complex representations of the data. However, this comes at the cost of a heavy reliance on the quality of the training data and challenges in understanding how the system makes decisions, often referred to as the "black box" problem. End-to-end systems require extensive and diverse datasets to learn effectively and are only as good as the data they are trained on. The decision to opt for one architecture style over the other is greatly influenced by the specific requirements and constraints of the autonomous driving application in question, as summarized in Table 1. 

## 4. **Scene Perception And Localization**

Machine learning play a pivotal role, providing a powerful tool to simplify the complexities of environmental perception and spatial referencing in autonomous driving. This, in turn, promotes a paradigm deeply rooted in data analysis and algorithmic functionalities. This part of the text explores the application of machine learning, with a particular focus on its ability to address challenges related to hardware deployments, especially sensors. Sensors are crucial for tasks such as object 

| Table 1  Comparing layered and end-to-end architectures in autonomous systems.  Aspect Layered Architecture End-to-End Architecture  Advantages Modular design facilitates easier  Simplified structure reduces  updates and development.  system complexity.  Structured approach simplifies  Reduced latency as data  debugging and testing.  processing occurs in a single  pass.  Allows specialized optimization at  each layer for improved  performance.  Strengths Independent layer development  leads to increased system  reliability.  Adaptable to changes and new  environments with adequate  training.  Compatible with a wide range of  sensors and algorithms for better  integration.  Can achieve high performance  levels through advanced  learning.  Challenges Processing across multiple layers  Requires extensive, welllabeled datasets for effective  can introduce latency.  training.  Complex inter-layer  Debugging can be challenging;  communication maintenance.  low interpretability of  decisions.  Outlook Focus on reducing latency to  Efforts to enhance model  increase efficiency.  interpretability.  Incorporating learning-based  methods for greater adaptivity and  responsiveness.  Developing more efficient  training methods to improve  learning.   |
|---|

recognition and semantic segmentation. Through this concise but rigorous exploration, our goal is to establish a clear connection between the fields of AI and autonomous vehicle technology. We want to highlight the potential for synergistic development and mutual evolution in these intricate and technologically advanced domains (Fig. 5). 

## 4.1. Characteristics Of Sensor Technologies In Autonomous Driving

In the intricate tapestry of technologies that undergird the functionalities of autonomous driving, three sensor technologies stand prominent: camera, lidar, and radar, each bringing to the fore unique strengths and facing distinct challenges, outlined in Table 2. The camera, a cornerstone in this triad, is unparalleled in its capability to interpret the subtle nuances of textures and colors with finesse. This ability renders it indispensable for critical tasks inherent to autonomous navigation, such as lane detection and traffic sign recognition, along with distilling insights crucial to comprehending the driving milieu. 

However, it is imperative to acknowledge that these advantageous attributes come tethered to the demand for significant computational resources requisite for processing high-definition imagery. In contrast, lidar sensors are lauded for their precision, a trait quintessential for executing tasks pivotal to autonomous driving, ranging from object and pedestrian detection to meticulous mapping, thereby playing an indispensable role in navigation and obstacle avoidance. Nevertheless, lidar sensors, despite their acknowledged precision, are not without their challenges; they exhibit sensitivity to meteorological conditions and have been burdened by issues related to bulkiness and high cost—although the relentless tide of technological advancement is gradually alleviating these constraints. Radar technology demonstrates robust performance under adverse weather, providing reliable data on the distance and velocity of nearby objects. With a wide field of view and the capability to detect entities at considerable distances, radar is crucial for adaptive cruise control and collision avoidance applications. However, while beneficial, radar has limitations, including lower spatial resolution than lidar and challenges in angular accuracy. 

## 4.2. Object Detection

Object detection serves as the bedrock upon which autonomous driving systems construct their perceptive understanding of surrounding 

![5_image_0.png](5_image_0.png)

| Aspect                                                                                                                         | Camera                                                                                                    | Lidar                                                                                             | Radar   |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------|
| detection and  traffic sign  recognition. Can  be used for visual  SLAM. Often  combined with  other sensors for  data fusion. | - Commonly used  in adaptive cruise  control, blindspot warning,  collision warning, and collision  prevention. Wellsuited for velocity  estimation of surrounding objects.                                                                                                           |                                                                                                   |         |
| perspective  Excellent  texture  interpretation  Cost-effective  Easily  accessible                                            | - Utilized for highprecision localization. Used for  obstacle avoidance and detection  of pedestrians.  Critical for HD  map creation.                                                                                                           | - Robust against  adverse weather.  Wide field of  view  Precise speed  and distance  information |         |
| significant  computational  resources  Vast data  generation                                                                   | - High spatial  resolution  Detailed 3D  point clouds  Excellent for  object  identification and  mapping | - Lower angular  accuracy  compared to  Lidar  Limited  resolution,  especially  vertically       |         |
| - Sensitive to  weather  conditions  Traditionally  high-priced and  large-sized  Requires substantial processing                                                                                                                                |                                                                                                           |                                                                                                   |         |

![5_image_1.png](5_image_1.png)

- Lower angular 

accuracy 

compared to 

Lidar 

Limited 

resolution, 

especially 

vertically 

Lower data 

volume 

Prospects - Integration with 

deep learning for 

advanced perception 

Humanmachine 

interaction 

Applications in 

segmentation and 

end-to-end 

driving 

environments, standing as a paramount facet of autonomous driving technologies. The fundamental objective steering object detection mechanisms is the astute identification, meticulous classification, and precise localization of objects that punctuate the environmental landscape within which these autonomous entities navigate. In the landscape of recent technological advancements, there has been a discernible acceleration in the refinement and deployment of deep learning algorithms specifically tailored for object detection tasks. This swift paradigmatic shift has precipitated enhancements in the performance metrics of detection systems. These advanced algorithms leverage the foundational structure of neural networks as their computational backbone, utilizing these sophisticated networks to effectuate the extraction of salient features from image data with enhanced accuracy and efficiency. Through the systematic application of these evolved algorithms, the field has witnessed a substantial elevation in the reliability and functionality of autonomous driving systems in real-world, dynamically shifting environments. 

| deep learning for  advanced  perception  Humanmachine  interaction  Applications in  segmentation and  end-to-end  driving   | - Becoming more  compact and  affordable  Enhanced  performance in  diverse conditions  Integration with  other sensors for  better mapping   |
|---|-----------------------------------------------------------------------------------------------------------------------------------------------|

| autonomous  driving  Integration  with other  sensors for better  perception  Improved  resolution and  data processing   |
|---------------------------------------------------------------------------------------------------------------------------|

4.2.1. *Image object detection* Two techniques dedicated to image object detection are investigated in this section (Table 3), both of which enjoy extensive application within the domain of autonomous driving. The techniques under examination include region-based convolutional neural networks (RegionBased CNNs) and single-stage detection methods, with particular reference to you only look once (YOLO) and single shot detector (SSD). These methodologies have garnered popularity for their efficacy and reliability in facilitating object detection, thereby contributing significantly to the operational proficiency of autonomous driving systems. 

4.2.1.1. *Region-based CNNs.* Region-based CNNs (RCNNs) revolutionized object detection by initially generating around 2000 bottom-up region proposals through selective search, and subsequently extracting features for each region using CNNs, followed by classification via linear support vector machines (SVMs) (Girshick et al., 2015). The advent of Fast RCNN (Ren et al., 2015) and Faster RCNN (Mansour et al., 2021) 
brought significant improvements. Fast RCNN introduced ROI Pooling to circumvent the issue in RCNN where pre-convolution image 

| Characteristics of different image object detection techniques.  Method Description Key Features   | Limitations                                                                    | Applications                                    |                     |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------|---------------------|
| Region  Based  CNNs                                                                                | - High precision in localization and                                           |                                                 |                     |
| Utilizes a two-step process for object  detection with CNNs.                                       | classification  Two-stage process: region proposal and  refinement             | - Slower inference speed Higher                 | Fine-grained object |
| computational resources needed                                                                     | detection, complex scenes                                                      |                                                 |                     |
| YOLO and                                                                                           | Single-stage models predicting object                                          | - High detection speed                          |                     |
| SSD                                                                                                | classes and bounding boxes directly.                                           | Single-stage process: simultaneous              |                     |
| prediction of class labels and bounding  boxes                                                     | - Slightly compromised localization  accuracy  Less effective on small objects | Real-time object detection,  video surveillance |                     |

segmentation led to deformation or feature loss. By leveraging fast RCNN and region proposal network (RPN), the attention-based detection framework shows promise in addressing the challenge of detecting small objects in large, high-resolution images (Fig. 6). 

4.2.1.2. *YOLO and SSD.* YOLO's swift, single-pass image processing is 

![6_image_0.png](6_image_0.png)

pivotal for real-time object detection, a necessity for responding to dynamic traffic situations. Complex-YOLO (Simony et al., 2018), a variant specifically crafted for 3D object detection within Lidar point clouds 
(Fig. 7a), facilitates real-time environmental perception—critical for decision-making and navigation in autonomous vehicles. Unlike traditional YOLO, it employs Euler-region-proposal network (E-RPN) using complex numbers for regression, enhancing orientation estimation's robustness and avoiding singularities. This innovative approach, effective especially during training, distinguishes Complex-YOLO for its unparalleled speed and efficiency. According to KITTI benchmark tests, Complex-YOLO outstrips other techniques, processing at a rate five times faster than its closest counterpart and simultaneously estimating various object classes, including cars, vans, and pedestrians. Remarkably, Complex-YOLO operates on Lidar data, bolstering its efficiency and making it apt for deployment on embedded platforms such as NVIDIA 
TX2 without reliance on additional sensors. 

Future enhancements for Complex-YOLO envision the incorporation of height data into the regression, laying the foundation for genuine 3D 
object detection. By tapping into tempo-spatial dependencies, there is potential to further boost class differentiation and elevate accuracy levels. Complex-YOLO stands as a monumental stride in the domain of 3D object detection for autonomous driving. By harnessing the agility of YOLO and pioneering with complex number-driven regression via ERPN, it achieves a commendable blend of speed and efficiency. 

SSD (W. Liu et al., 2016), on the other hand, belongs to the category of one-stage object detection algorithms that circumvent the region proposal phase. SSD can directly generate category probabilities and positional coordinates for objects (Y. Zhang et al., 2020). This streamlined approach allows for faster detection speeds as the final detection results are acquired through a single forward pass of the network. As depicted in Fig. 7b, the structure of the SSD algorithm is twofold: (1) The Backbone network, which is constituted by segments of the VGG16 convolutional layers. Notably, the last two layers, conv6 and conv7, are substituted by fully connected layers for image classification purposes. 

(2) The SSD testing framework comprises two parts: the frontend employing the VGG16 model for preliminary feature extraction from the image, and the backend multi-scale feature detection network, which operates at varying scales to extract features from different layers. This allows the SSD to detect both large and small objects by examining shallow feature maps with larger receptive fields and deeper feature maps with finer details. SSD's emphasis on multi-scale features allows it to detect objects of varying sizes, which is essential for recognizing 

![7_image_0.png](7_image_0.png)

Fig. 7. The framework of (a) SSD and (b) YOLO. 
pedestrians, vehicles, and traffic signs at varying distances. SSD stand as a powerful tool in the autonomous driving domain, especially in scenarios where speed and real-time processing are of importance. 

representational capacity, and data handling (Table 4). Exploring these approaches' principles and characteristics offers valuable insights into their applications and the challenges they navigate within autonomous driving, robotics, and augmented reality. 

4.2.2. *Point cloud object detection* Point cloud object detection, a field within computer vision, facilitates three-dimensional environmental perception. Point clouds, aggregations of spatial coordinates and attributes such as color or intensity, offer rich scene information. Enhanced sensor technologies, notably LiDAR, enable the acquisition of dense, high-resolution point cloud data, whose unique qualities, such as representing complex geometries and detailed structures, are invaluable for object detection. 

These point clouds' spatial and geometric features have been leveraged to craft various object detection methodologies in 3D space. This section introduces three leading approaches in point cloud object detection: 
point-based, voxel-based, and 2D-projection-based methods, each presenting distinct advantages and challenges in computational efficiency, 4.2.2.1. *Point-based.* PointNet offers a unified architecture, leveraging point methods, that processes point clouds directly for either holistic input classification or segment-specific labeling. Meanwhile, Grid-GCN 
(Q. Xu et al., 2020), a variant employing point convolutions, utilizes graph convolution networks for point cloud learning, aggregating feature information of points through Fourier transforms within its various GridConv layers. Each layer consists of two steps: central node sampling and neighboring node selection, followed by information aggregation from queried nodes to the center. In this process, each point generates a local graph, and then GCN aggregates the information of the points according to the local graph (Z. Liu et al., 2019; Zarzar et al., 2019). However, the efficacy of these models is somewhat constrained 

| Method                     | Description                                                                | Features                | Advantages                                                  |
|----------------------------|----------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------|
| Point-based                | Operates directly on raw point clouds, preserving spatial and geometric    | Raw point cloud         | Preserves complete information, handles complex point       |
| characteristics.           | operation                                                                  | cloud data effectively. |                                                             |
| Voxel-based                | Converts point clouds into 3D voxel grids, enabling the use of traditional | 3D voxel grid           | Utilizes traditional CNN structures, simplifies analysis of |
| CNNs for object detection. | conversion                                                                 | structured data.        |                                                             |
| 2D-Projectionbased                            | Projects 3D point clouds onto 2D planes, creating simplified views while   | 3D to 2D projection     | Simplifies data processing, retains significant object      |
| retaining object details.  | details.                                                                   |                         |                                                             |

by the farthest sampling process, even though it enhances memory efficiency and operational speed. To mitigate this, KPConv (Thomas et al., 
2019) employs a learnable radius neighborhood input method to formulate kernel points, offering a flexible and robust local neighborhood representation. RandLA-Net (Hu et al., 2020) introduces a random sampling strategy paired with a local feature aggregation (LFA) module to counteract feature loss, expanding the receptive field layer by layer to accommodate complex local structures efficiently. For detecting 3D 
objects from raw point clouds, REF. (Shi et al., 2019) designed a network based on RCNN, which generates high-quality 3D proposals directly from point clouds. The introduced KCA module, incorporating a selfattention mechanism, selectively highlights key points and features, minimizing redundancy (H. Wang et al., 2021). However, Point-based methods see computational complexity increasing linearly with point numbers, with data structure construction costs, such as for KD trees, becoming a technical bottleneck. 

4.2.2.2. *Voxel-based.* VoxeNet (Maturana & Scherer, 2015) and VoxelNet (Y. Zhou & Tuzel, 2018) both take raw point cloud data as input partitions the space into voxels and input voxels into a 3D neural network for detection. Occupancy grid reduces the amount of data and preserves the shape of the point cloud, the representation is more informative than that of the point cloud, since the distinction between free space and unknown space can be a valuable piece of information. 

VoxNet just feeds the voxels into the neural network, convolves and pools the output point cloud fragments. VoxelNet designs a novel voxel feature encoding (VFE) layer and via stacked VFE layers, which enables inter-point interaction within a voxel. Finally, a volume representation is output by the RPN network as the detection result. Recently, researchers have proposed different voxel structures to represent point clouds. PointPillars (Lang et al., 2019) converts the raw point cloud into a stacked pillar tensor and pillar index tensor. It uses a novel encoder that learns features on pillars (vertical columns) of the point cloud to predict 3D oriented boxes for objects. There are several advantages of this approach. Firstly, PointPillars can exploit the full information of point clouds by learning point cloud features instead of relying on fixed encoders. Secondly, the operation of the column does not require manual adjustment of the vertical bins, which simplifies the operation process. Finally, since all key operations can be performed by 2D 
convolution, it is very fast to compute on CPU. Another benefit of the learning function is that PointPillars can use different point cloud configurations, such as multiple lidar scans or even radar point clouds, without manual tuning. PolarNet, represents the point cloud as a ringbased structure and proposes a ring CNN to extract special data distribution characteristics. Compared with conventional voxelization methods, this representation can reduce the effects of non-uniform distribution of point clouds. PolarNet (Y. Zhang et al., 2020) represents the point cloud as a ring-based structure and proposes a ring CNN to extract special data distribution characteristics. Compared with conventional voxelization methods, this representation can reduce the effects of nonuniform distribution of point clouds. Cylinder3D uses 3D polar voxels instead of 2D polar voxels. In future development, there will be more and more shaped voxels that can be used to process point cloud data. 4.2.3. *Challenges and prospects: Object detection* Object detection is crucial for interpreting the contours of external environments, which is fundamental to the decision-making processes inherent in various systems. Despite the critical role of object detection, it frequently encounters challenges arising from the unpredictable and complex nature of real-world driving scenarios. These challenges are manifold, marked by variable environmental conditions and the inherent complexity found within the dynamics of driving conditions. 

Nevertheless, it is essential to recognize that the direction of technological advancement and methodological innovation in this field is decidedly positive. With a consistent flow of developments emerging in both the technological and theoretical domains, there is a clear vision of promise and potential. The technologies and strategies signal a future where the capabilities of object detection systems are not only enhanced but also refined. This progress is set to facilitate more sophisticated, reliable, and effective implementations in autonomous navigation and driving systems. Table 5 succinctly summarizes the challenges and prospects in object detection, providing a critical overview necessary for understanding and advancement in this arena. Despite the formidable challenges, the encouraging prospects provide avenues for future enhancements and applications in the realm of object detection. 

## 4.3. Semantic Segmentation

In autonomous driving, semantic segmentation offers pixel-level environmental discernment, a computer vision task that classifies image pixels into distinct classes, thus mapping the scene intricately. However, its application faces challenges, given the dynamic driving landscapes. The algorithm must handle diverse lighting, object occlusions, varied appearances, and unforeseen incidents. 

4.3.1. *Annotation for semantic segmentation* In the domain of semantic segmentation, there is a necessity for precision in annotations. This precision demands a process where each pixel within an image is accurately labeled, identified with the class of its encompassing object or region. The requirement for such fine-grained precision inherently renders the annotation task for semantic segmentation as time-intensive and laborious. Nevertheless, this challenge can be mitigated and the process expedited through the adoption of specialized annotation methodologies and tools, purposefully crafted to aid in this detailed endeavor. Subsequently, a succinct introduction to a selection of four annotation tools, including (i) Labelbox (Labelbox, 2023), (ii) Roboflow (Roboflow, 2023), (iii) Encord (Encord, 2023) and 
(iv) CVAT (CVAT, 2023), are provided, aiming to shed light on their functionalities and afford the insightful considerations regarding their application in the field of semantic segmentation. 

## (1) Labelbox

Table 5 

Challenges and prospects of object detection. 

Challenges Prospects 

Variation in Object Appearance: 

Diverse shapes, colors, textures, sizes, 

and poses, along with changing 

lighting and perspectives, complicate 

the detection process. 

Contextual Information Utilization: 

Future models are expected to better understand scene context, aiding in more 

accurate object detection. 

Training Data Scarcity: The collection 

and labeling of extensive datasets, 

especially for rare or variable 

scenarios, is a significant hurdle. 

Explainable AI (XAI): The move towards AI explain ability is driving the 

development of models that are not only 

more interpretable but also more 

trustworthy. 

Contextual Information: The 

challenge of interpreting the context 

to accurately identify relationships 

between objects persists. 

Transfer Learning & Few-Shot 

Learning: These techniques are 

enhancing the ability of models to 

quickly adapt to new tasks with limited 

data, essential for detecting uncommon 

objects. 

Scale Variance: Detecting objects of 

varying sizes within the same scene is difficult, especially smaller objects in 

wide shots. 

Hardware Technological 

Advancements: Improvements in GPUs and TPUs are enabling more 

sophisticated real-time object detection 

by providing greater processing power. 

Occlusion & Overlapping: Partially 

hidden or overlapping objects are problematic, often leading to detection errors. 

3D Object Detection: The adoption of 

3D sensors such as Lidar is improving spatial detection accuracy beyond traditional 2D methods. 

Real-time Detection Constraints: 

There is a need for faster processing to enable real-time detection in video 

analysis within current hardware 

limitations. 

AI Regulations: The anticipation of 

stricter AI regulations could lead to the 

development of more fair, private, and 

robust detection systems. 

Labelbox provides an efficient milieu for the data labeling. This datacentric tool is engineered, not solely as a crucible for the genesis of pristine-quality data but also as a robust platform fostering the processes of training, fine-tuning, and human-centric evaluations - elements for the execution of semantic segmentation tasks. With features enabling users to visualize, peruse, classify, and disseminate data subsets with precision, Labelbox provides support for the processing of datasets through AI mechanisms. Furthermore, it facilitates insights through workflows assisted by both human intellect and mechanized algorithms, enhancing efficiency in data preparation for AI model training. Its suite, with model-assisted labeling and collaborative annotation capabilities, has been enabling enterprises to institute standardized protocols for data creation and management, culminating in savings in time and financial resources. 

## (2) Roboflow

Its AI-assisted labeling feature supports various annotation types, allowing teams to work collaboratively and securely in real-time. This not only speeds up the process but also ensures accurate annotations, thanks to pre-trained models that automatically detect and label common objects in your dataset. Roboflow is designed for effective teamwork, providing a smooth platform for managing annotation projects where tasks such as uploading, searching, assigning, reviewing, and approving annotations are streamlined. With features facilitating easy communication and project management, and secure, role-based access, it supports safe collaboration both within and outside your organization. It supports a range of labeling tools for various use cases and allows for importing or exporting to over 26 formats, supporting model building with any architecture without the need for relabeling. Its fully managed labeling services are scalable and cost-effective, ensuring high-quality annotations by skilled, expert labelers. 

## (3) Encord

Encord emerges as an advanced platform, offering tools for enterprises committed to advancing in semantic segmentation. The integration of AI-assisted labeling methodologies not only underscores its innovation but also accelerates the intricate processes of data annotation. This functionality proves important for segmenting various computer vision modalities. With its intuitive interface, Encord not only good at operational efficiency but also fosters a conducive environment for collaboration among other annotators, catering to expansive projects. Recognizing the diverse needs of businesses, Encord provides the option to engage with annotators possessing domain-specific expertise, thereby assuring impeccable accuracy and reliability of AI training datasets. 

## (4) Computer Vision Annotation Tool (Cvat)

CVAT offers a flexible tool for or semantic segmentation annotation, crafted meticulously using machine learning. Its intuitive, fast interface addresses diverse annotation needs. CVAT's versatility is evident in its ability to manage tasks ranging from image classification and object detection to point clouds/Lidar and video annotation, adapting to different data types and delivering results that professionals can rely on. The tool facilitates a smoother, more accurate annotation process with features such as auto-annotation and AI integration. With a vibrant, collaborative community of users and contributors, CVAT continuously evolves and improves. Whether you're embarking on a small project or a substantial annotation task, CVAT stands ready to assist, committed to supporting users in achieving excellence in semantic segmentation and a variety of computer vision projects. 

4.3.2. *Decoder variants* At present, most of the advanced deep learning methods for semantic segmentation trace their roots to a shared progenitor: the fully convolutional network (FCN) (Long et al., 2015). The genius behind this approach was to harness the capabilities of existing CNNs as potent visual models capable of learning feature hierarchies. Aside from the FCN 
structure, the segmentation model arena has witnessed the rise of numerous alternative strategies that strive to adapt classification networks for segmentation tasks, such as VGG16, into segmentationfriendly architectures. These methodologies generally involve stripping away fully connected layers from the classification network to form what is often termed an "encoder." This modified component of the segmentation network then generates low-resolution feature maps or image representations. The principal challenge, however, is the translation of these low-resolution images into pixel-wise predictions that are essential for segmentation. This decoding task is often where these architectures show their distinct approaches. 

Take, for example, SegNet, an innovative deep FCN model tailored for semantic pixel-wise segmentation (Badrinarayanan et al., 2017). The architecture of SegNet is underpinned by a core segmentation engine, consisting of an encoder network and a corresponding decoder network, topped off with a pixel-wise classification layer. The encoder network is structurally identical to the 13 convolutional layers found in the VGG16 network. The role of the decoder network, on the other hand, is to transform the low-resolution feature maps from the encoder into full input resolution feature maps suitable for pixel-wise classification. In assessing SegNet's performance, it is compared against other renowned architectures such as FCN, DeepLab-LargeFOV, and DeconvNet. This comparative analysis underscores the balancing act between memory utilization and accuracy to secure robust segmentation performance. SegNet was primarily conceived with scene understanding applications in mind; hence, its design prioritizes efficiency in both memory use and computation time during inference. Furthermore, SegNet stands out for having markedly fewer trainable parameters compared to its competitors, while also offering support for end-to-end training via stochastic gradient descent. 4.3.3. *Integration of information across spatial scales* Semantic segmentation integrates data across various spatial scales, requiring a balance between local details and global context. Strategies examined in this section include post-processing refinement via conditional random fields (CRFs), the utilization of dilated convolutions, and the application of RNNs. 

(1) CRFs: It offer a structured framework facilitating the integration of low-level image information (for instance, pixel interactions) with the outputs produced by multi-class inference systems that yield per-pixel class scores (Sutton & McCallum, 2012). This integration process is pivotal, serving to encapsulate long-range dependencies and subtle local details effectively, elements often not adequately addressed by conventional CNNs. To secure a representation that is not only adaptable but also continuous, reflecting the probability distribution inherent in image data, a novel deep network dubbed the Gaussian Mean Field (GMF) 
network was introduced (Vemulapalli et al., 2016). This innovative Gaussian CRF network is architecturally segmented into three distinct sub-networks. The initial sub-network, grounded in CNNs, is assigned the function of generating unary potentials. Sequentially, the second sub-network, also reliant on CNNs, is entrusted with the generation of pairwise potentials. The concluding segment, the GMF network, undertakes the task of Gaussian CRF inference. Within this architectural configuration, the GMF network sustains a continuous model, systematically refining its outputs to approximate the maximum a posteriori solution intrinsic to the Gaussian CRF. Intriguingly, empirical evidence indicates that the Gaussian CRF network, despite sustaining a continuous model, exhibits proficiency in tackling discrete labeling tasks effectively. This observed performance underscores the network's potential as a robust instrument for semantic segmentation, enhancing its ability to discern and interpret both global and local contextual elements within images. 

(2) Dilated Convolutions: Dilated Convolutions serve as a variant of Kronecker-factored convolutional filters, adept at facilitating the exponential expansion of receptive fields without concurrent loss of resolution. Noteworthy contributions employing dilated convolutions encompass the multi-scale context aggregation module 
(F. Yu & Koltun, 2015), the expedient network ENet (Paszke et al., 2016), and a refined iteration of DeepLab (L.-C. Chen et al., 2017). The aforementioned multi-scale context aggregation module (F. Yu & Koltun, 2015) ingeniously incorporates dilated convolutions, a strategic integration aiming at the accrual of contextual information spanning multiple scales. This incorporation fosters an enhanced comprehension of the global context, executed without relinquishing the granularity of local information. ENet (Paszke et al., 2016), architecturally crafted to suit real-time applications, strategically deploys dilated convolutions for the efficient processing of images manifesting diverse resolutions. Through the application of dilated convolutions, ENet demonstrates a commendable capability to capture both local and global features, thereby facilitating image analysis that is both swift and precise. Furthermore, an advanced version of the DeepLab model (L.-C. Chen et al., 2017) operationalizes dilated convolutions to address and surmount challenges related to the capture of minute details pivotal for semantic segmentation tasks. The model, by broadening the receptive field through the use of dilated convolutions, attains a deeper understanding of both object boundaries and the contextual information, culminating in enhanced accuracy in segmentation. 

(3) RNNs: RNNs, celebrated for their specialized topology, are proficient in modeling sequences across diverse temporal spans, thus skillfully capturing global contexts and enhancing semantic segmentation. However, the challenges materialize due to the intrinsic lack of sequential structure in images and the predisposition of traditional RNN architectures toward onedimensional inputs. A novel architecture, ReSeg (Visin et al., 
2016), which draws upon the ReNet model, navigates through these challenges. The methodology embarks with an initial processing of the input image through the primordial layers of the VGG-16 network, subsequently extracting feature maps which are refined by one or several ReNet layers to envelop global contexts. These polished maps are then upsampled to their original resolution using transposed convolutions. Within the ReNet layers, gated recurrent units (GRUs) are employed, esteemed for their equilibrium between memory usage and computational power. To manage challenges associated with modeling longterm dependencies and the vanishing gradients issue, innovations such as long short-term memory (LSTM) (Y. Yu et al., 
2019) and GRUs (Kanai et al., 2017) are incorporated. These networks, fashioned to preserve pivotal information across lengthy sequences, augment the ability to model intricate dependencies vital for semantic segmentation tasks. Architectures like ReSeg combine the strengths of various neural network designs, enhancing semantic segmentation by considering the bigger picture in images and addressing challenges to improve the system's performance." 
4.3.4. *Challenges and prospects: Semantic segmentation* Semantic segmentation occupies a critical role in the realm of autonomous driving systems, serving as an indispensable tool for the extraction and interpretation of environmental data. This process is central to the functionality of these systems, facilitating judicious and strategic decision-making that underpins autonomous navigation models. The domain of semantic segmentation presents a labyrinth of complexities, mirroring the unpredictable and vibrant dynamics of the real-world environment. Despite the inherent challenges, this field is characterized by considerable potential. The collaborative energies of academia and industry are fueling a dynamic cycle of innovation and enhancement, reflecting the dedication of researchers and practitioners in this specialty. Their collective endeavors are progressively establishing robust capabilities, providing avenues for advancement and opportunity within the landscape of semantic segmentation. The challenges inherent in this field are not prohibitive; rather, they serve as benchmarks guiding us towards a future where the capabilities of semantic segmentation are ever-increasing. Table 6 offers a detailed overview of the challenges and prospects in the scope of semantic segmentation. 

## 4.4. Multi-Object Tracking

Multi-Object Tracking (MOT) is like the sharp eyes and keen senses of autonomous vehicles as they navigate the ever-changing city traffic scene (Ravindran et al., 2020). Urban streets are a bustling canvas, with vehicles and pedestrians moving in their own unique ways, speeds, and paths. In general, MOT doesn't work in isolation; it teams up with SLAM 
techniques in a smooth partnership (Bescos et al., 2021). These advanced technologies work together, allowing vehicles not only to see and track what's happening around them but also to build a detailed, responsive map of their surroundings at the same time. 

## 4.4.1. Framework Of Mot

MOT bears the responsibility of detecting multiple objects within its purview, retaining the unique identity assigned to each and charting their respective trajectories over time, all while assimilating a steady stream of incoming video data. Whether the object in question is a pedestrian or another vehicle, it is duly recognized, identified, and monitored, with its trajectory outlined and updated upon the virtual canvas of the roadmap. MOT can be classified into two distinct modalities: online tracking and offline tracking. Each modality shares foundational principles but diverges in approach and application, enriching the broader MOT framework with multifaceted capabilities. 

| Challenges                                                                                                                                                                                       | Prospects                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quality and Quantity of Annotations:  High-quality, extensive annotations  are essential for training semantic  segmentation algorithms but are costly  and error-prone when produced  manually. | Deep Learning Enhancements:  Advances in deep learning, particularly  convolutional neural networks, are  expected to boost the accuracy and  resilience of semantic segmentation  techniques.  |
| Real-time Processing: Algorithms must  process high-resolution images swiftly  for autonomous vehicles to make  immediate decisions.                                                             | Transfer Learning and Data  Augmentation: Employing pre-trained  models and expanding dataset  variability can reduce the need for large  annotated datasets and enhance  algorithm efficiency. |
| Environmental Robustness:  Algorithms must perform reliably  under various conditions such as fog,  rain, nighttime, or direct sunlight.                                                         | Edge Computing and Hardware  Acceleration: New developments in  edge computing and specialized  hardware aim to reduce latency,  facilitating real-time processing.                             |
| Class Imbalance: Disproportionate  representation of object classes in  training data can bias predictions  toward more common classes.                                                          | Active Learning and Unsupervised  Learning: These methodologies can  minimize the need for large annotated  datasets by focusing annotation efforts  and utilizing unlabeled data.              |
| Computational Resources: The  significant computational power  required for high-resolution image  processing in semantic segmentation  poses training and real-time  application challenges.    | Multi-modal Sensor Fusion:  Combining data from various sensors  such as cameras, LIDAR, and radar can  enhance environmental adaptability and  segmentation precision.                         |

(i) Online Tracking: This method stands out for its timely and stepby-step handling of image frames (Bescos et al., 2021; Xiang et al., 2015). It creates a real-time picture of motion, tracing the paths of objects as they move and interact in traffic (Z. Wang et al., 2020). Past movements are shown with arrows, forming a visual story of their paths. This visual representation is essential for online tracking, capturing the dynamic journey of each object. 

These objects aren't passive; they are actively highlighted, pinpointed, and given unique identifiers. Their paths are continuously updated as the scene unfolds, showcasing adaptability in response to changing traffic conditions. By tuning into the realtime flow of traffic and skillfully understanding its intricate patterns, it plays a crucial role in safely and efficiently guiding autonomous vehicles through the varied and ever-changing urban traffic landscape. Built upon its dedication to up-to-theminute data, Online tracking lays the foundation for the advancing story of autonomous driving technologies. 

(ii) Offline Tracking: It presents a holistic approach to data analysis, diverging from the frame-by-frame scrutiny characteristic of other techniques. Rather than evaluating frames in isolation, this method aggregates requisite data prior to initiating analysis, fostering a comprehensive examination where individual frames are analyzed collectively, thereby amalgamating diverse data into a coherent result. However, this simultaneous processing of frames encounters constraints, notably computational power and memory capacity limitations. A pragmatic resolution to these constraints is the segmentation of extensive data into smaller, manageable portions or abbreviated video clips. These truncated segments are individually analyzed, adhering to either a hierarchical or sequential methodology as necessitated by the specific task. Subsequently, the analytical outcomes of these discrete segments are meticulously integrated, yielding a coherent and precise depiction of the intricate environment under observation, effectively synthesizing the individual analyses into a unified and accurate representation that encapsulates the complexity of the observed scenario. 

MOT for autonomous driving unfolds as a refined system with crucial components, each contributing to efficient tracking of multiple objects. 

Object detection, the system's bedrock, identifies and pinpoints objects within the vehicle's perception using pre-trained algorithms such as YOLO, Faster R-CNN, or SSD, as discussed earlier. These tools discern and distinguish between various objects with precision. Feature extraction follows detection, distilling the essence of each detected object and carving out distinctive features pivotal for tracking algorithms. 

This process ensures each object is identified and tracked through frame sequences. 

Data association matches detected objects across sequential frames with precision. The matching process considers appearance and motion, employing cost functions and techniques such as the Hungarian algorithm (Weng et al., 2020), joint probabilistic data association (JPDA) 
(Shenoi et al., 2020), or multi-hypothesis tracking (MHT) (Xie et al., 2021) to solve assignment problems, associating current detections with pre-existing tracks accurately. Motion models predict future object locations, with models embodying constant velocity or acceleration providing essential foresight into object movements. Filtering techniques, such as Kalman filters (G. Guo & Zhao, 2022) or particle filters 
(Xia et al., 2021), estimate an object's state, providing accurate and reliable tracking output. Finally, the system manages and updates tracks, initiating new tracks for newly detected objects and terminating old tracks for irrelevant objects. Mechanisms for handling occlusions are integrated, ensuring accurate tracking even in complex driving environments. 

In the world of traffic, especially in the realm of autonomous driving, every part of MOT has its role, working diligently and precisely. 

Together, they weave a story that prioritizes safety and responsiveness. 

Each piece in this MOT system adds to the smooth and secure experience of autonomous driving, bringing technology and safety together in the name of innovation. 4.4.2. *Challenges and prospects: Multi-object tracking* Within the technological framework, MOT emerges as a crucial focus, navigating through sequential frames with precision, thereby becoming essential for applications crucial to the areas of traffic control and oversight. The ability to understand the subtle trajectories and directions of multiple concurrently moving objects unfolds as a source of valuable insights, highlighting ways to alleviate traffic bottlenecks and efficiently manage the rerouting of vehicles through areas of lesser congestion. For scholars, practitioners, and policymakers deeply engaged in the complex field of autonomous driving and traffic management, developing a deep, subtle understanding of the challenges and prospects (Table 7) within MOT is essential. The journey through this terrain is filled with challenges; however, the prospects appearing on the horizon are enticing. Advanced MOT techniques offer the promise of a future where the movement and flow of traffic are not only efficient but also intelligent and responsive, moving gracefully in response to the dynamic and constantly changing urban environment. This narrative serves as a concise, yet insightful introduction, leading the reader into a deeper, more subtle exploration and consideration of the complex challenges and bright prospects closely connected to the practice of MOT within the context of autonomous driving. 

## 4.5. Localization And Mapping

At present, the most widely used positioning method is based on communication positioning, such as GNSS (Joubert et al., 2020) and Internet of Vehicles (IoV) (Ji et al., 2020). However, Under the conditions of high buildings, underground garages, indoor or mountainous terrain, GNSS signals will be blocked and have multi-channel effect, which will lead to decreased positioning accuracy or even errors. GNSS is susceptible to interference from electromagnetic wave, atmosphere, and other factors, with long transmission delay and low update frequency (1 Hz ~ 50 Hz). IoV positioning is currently expensive. So SLAM 
has the potential to become a mainstream location approach. This section will introduce several commonly used SLAM systems, including the 

| Challenges                                                                                                                                               | Prospects                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Association Challenges:  Associating data from various sensors  and timeframes introduces ambiguity  and uncertainty, especially in multiobject tracking.                                                                                                                                                          | Advanced Algorithms: Emerging  algorithms specialized in data  association promise to resolve  ambiguities and enhance the precision of  multi-object tracking.         |
| Real-time Processing: Ensuring realtime performance with high accuracy  is difficult due to the complexity of  tracking algorithms.                                                                                                                                                          | Hardware Improvements: Cutting-edge  computing hardware is expected to boost  real-time processing capabilities,  enabling more accurate and faster  tracking.          |
| Occlusion Handling: Accurately  tracking multiple objects in scenarios  where they may obscure each other is  particularly challenging in dense  scenes. | Deep Learning Techniques: Advanced  deep learning and AI techniques are  being developed to improve occlusion  handling, thereby enhancing tracking in  complex scenes. |
| Variable Illumination and  Appearance: Variations in lighting  and object appearance add complexity  to tracking, affecting reliability.                 | Adaptive Methods: Research into  adaptive techniques aims to better cope  with environmental variations,  improving tracking reliability under  changing conditions.    |
| Limited Resources: Computational,  energy, and memory constraints in  embedded systems pose challenges for  the deployment of tracking  algorithms.      | Optimization Techniques: Ongoing  research focuses on optimizing  algorithms to be resource-efficient  without compromising accuracy,  enabling effective tracking in limitedresource settings.                                                                                                                                                                         |

architecture and development of visual SLAM, lidar SLAM and fusion SLAM. 

## 4.5.1. Visual Slam

Visual SLAM, a cornerstone of autonomous navigation, discerns a vehicle's precise location and its environment through a four-part system: front-end or Visual Odometry (VO), back-end, loop closure detection, and mapping (Sun et al., 2021). This process primarily uses vehicleinstalled sensors and GPS. While VO estimates sensor motion using either feature point or direct methods, its data requires optimization to prevent error accumulation and resultant drift. The back-end enhances this data for globally consistent trajectories and maps. Loop closure detection aids in drift reduction, while mapping establishes critical navigational and obstacle avoidance features. Based on image information use, visual SLAM methods fall into direct, indirect, and semidirect categories (Table 8), each explored in depth in subsequent sections. 

4.5.1.1. *Direct methods.* The direct method estimates the motion of the camera according to the brightness information of the pixels, and can eliminate the calculation of key points and descriptors. Therefore, it not only avoids the calculation time of features, but also avoids the situation of missing features. The direct method works if there are light and dark changes in the scene (which can be gradients, without forming local image gradients). The direct sparse mapping (Zubizarreta et al., 2020) 
scheme is a complete monocular SLAM system based on the direct method. The direct method SLAM system usually uses the photometric error for BA optimization, but the direct method cannot rely on itself to solve the reobservation problem of the same scene and the fusion problem of the same point (so the loop closure detection of the direct method relies on feature points to solve, such as LSD-SLAM). DSM solves this problem and is the first SLAM system based entirely on the direct method to achieve loop closure detection and map reuse, and achieves the highest accuracy in the direct method SLAM on the EuRoC dataset. 

DL-SLAM (Li et al., 2019) solves the problem that the map cannot perform efficient loop detection by extracting segment features from the 2.5D heightmap and integrated the 2.5D segment-based loop closure to DLO. 

Another approach grabbed attention since the advent of deep learning with focus on CNNs. Quite interesting results were observed especially with the work on CNN-SLAM (Tateno et al., 2017). It was shown through experiments that robot pose or localization could be achieved from a pair of images acquired by a moving robot through deep learning or CNN. Even though the CNN-SLAM approach is promising, this approach has invited few challenges that needs to be addressed. Deep learning requires high-end Graphic Processing Unit (GPU) systems, which is still a challenge for robotic embedded systems. Moreover, SLAM systems are seen to be directed on continuous open-world scenes where the environment keeps changing. These changes need to be learned on a continuous basis for a deep learning system. From the various techniques introduced in SLAM, one can observe that SLAM is inclined to combine various fields such as signal processing, deep learning (CNN-SLAM) and more significantly computer vision. CubeSLAM (Yang & Scherer, 2019) demonstrates that object detection and SLAM benefit each other. This also shows that neural networks can be used for feature extraction of SLAM instead of geometrically extracting features. DROID-SLAM (Teed & Deng, 2021) is an end-to-end system, which builds a neural network into the SfM pipeline to improve keypoint localization accuracy. Since neural network eliminates the manually designed feature extraction link, more and more researchers begin to introduce it into SLAM object recognition and segmentation, and even the pose estimation and loop detection of SLAM itself. At present, some papers based on Gaussian process regression and deviation correction are expected to be replaced by neural networks (Oliveira et al., 2020; Tang et al., 2018). 4.5.1.2. *Indirect method.* The indirect method uses the features (points or lines) in the image for matching, and then solves it according to the matching relationship. Its optimization objective function is the reprojection error of the feature, and the optimized variable is generally the relative pose. SLAM has the problem of being difficult to start in unknown locations in unknown environments. ORB-SLAM is a system built on PTAM that is robust to severe motion clutter, allows wide baseline loop closure and repositioning, and includes fully automatic initialization. Due to the use of ORB feature extraction, feature matching between image frames is very easy, reducing the phenomenon of feature point loss and mismatching, and the speed of image feature extraction is greatly improved. REF. (Mur-Artal & Tardos, ´ 2017) built ORB-SLAM2 based on ORB-SLAM that can be used on monocular, stereo and RGBD cameras. ORB-SLAM3 (Campos et al., 2021) supports more devices and functions, supporting monocular, binocular, RGB-D cameras, pinhole, fisheye, visual inertial odometry, multi-map SLAM, etc., covering almost all branches of visual SLAM. In general, the basic framework and code structure of ORB-SLAM3 are extensions of ORBSLAM2, but many new methods have been added to achieve better results, which are reflected in the following three aspects: the construction of a feature-based highly integrated vision -Inertial navigation SLAM 
system, more robust, suitable for indoor/outdoor large/small scenes, and the accuracy is improved simultaneously. 

4.5.1.3. *Semi-direct method.* The realm of autonomous navigation has witnessed remarkable strides with the advent of Semi-Direct Visual Odometry (SVO-SLAM) (Engel et al., 2014; Forster et al., 2014), presenting an approach to camera pose estimation that deviates notably from conventional strategies. SVO-SLAM introduces a semi-direct method wherein the camera pose is determined not by directly matching an entire image, but through identifying and aligning feature points within specific image blocks. This divergence proffers an alternative to the prevailing direct matching methodologies commonly associated with red–green–blue-depth (RGBD) sensors, which innately have the ability to procure depth data for an entire image, thereby facilitating the direct matching process. Opting for a distinct pathway, the semi-direct 

| Table 8  Classification and characteristics of simultaneous localization and mapping techniques.  Techniques Direct SLAM Indirect SLAM   | Semi-Indirect SLAM                                        |                                           |                                              |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|----------------------------------------------|
| Definition                                                                                                                               | Using pixel-level intensity information for feature       | By extracting and matching feature points | Combines pixel-level information and feature |
| extraction and matching                                                                                                                  | or descriptors                                            | points                                    |                                              |
| Map Representation                                                                                                                       | Dense or sparse point cloud                               | Sparse feature-based map                  | Sparse feature-based map                     |
| Feature Tracking                                                                                                                         | No explicit requirement                                   | Needed for operation                      | Necessary for operation                      |
| Camera Motion                                                                                                                            | Simultaneous estimation of camera poses and 3D points     | Sequential estimation of camera poses and | Simultaneous estimation of camera poses and  |
| Estimation                                                                                                                               | feature depths                                            | feature depths                            |                                              |
| Computational                                                                                                                            | High computational complexity                             | Efficient computational requirements      | Moderate computational requirements          |
| Efficiency  Robustness                                                                                                                   | Less robust to feature occlusions and repetitive patterns | More robust to feature occlusions and     | Moderately robust to feature occlusions and  |
| repetitive patterns                                                                                                                      | repetitive patterns                                       |                                           |                                              |
| Scale Drift                                                                                                                              | Prone to scale drift                                      | Less prone to scale drift                 | Less prone to scale drift                    |

13 method, rather than strictly adhering to a feature-based method—which can be computationally intensive and potentially fallible in texturedeficient environments—amalgamates the merits of the direct method. 

Consequently, it employs pixel intensity information intrinsic to images to establish correspondences, engendering more astute and efficient pose estimation. The adeptness and scalability of SVO-SLAM are illuminated through this approach, capacitating it to accommodate a wide spectrum of scenarios, from feature-rich environments to those characterized by sparse or poor textural features, while maintaining impeccable performance and precision. 

## 4.5.2. Laser Slam

Hector_SLAM (Kohlbrecher et al., 2011) uses the optimization method for the laser SLAM algorithm for inter-frame matching. The search space is not large, odometer information is not required, and the code is short. And only the endpoints of the scan are processed (the laser scan structure is not used), so the IMU can be used to adjust the laser scan attitude. The disadvantage is that the effect is not good on devices with insufficient radar frequency, and it is easy to match incorrectly when turning quickly; there is no loop closure, so if the cumulative error is too large, HectorSLAM has no map adjustment ability, and the optimization and matching between frames is also performed on the global map, cpu resources. consumes a lot. Karto is graph-optimized SLAM, including loopback detection, is suitable for large-area mapping. The VO frame matching adopts the method of correlative scan matcher to perform rough and fine matching. Karto does not have the concept of submap in loopback detection, and it is all stored in the Mapper-sensorManager in the form of keyScan. The window generates a localMap for matching. The loop closures of local and global store the assigned ID 
information sequentially according to the graph structure and Mappersensor-Managerss, select candidates to generate localMap for matching, and further determine the closed loop according to the score. 

Cooperation of the two algorithms allows accurate motion estimation and mapping in real-time. Compared with LOAM, LeGO-LOAM 
(Shan & Englot, 2018) changed the extraction form of feature points and added back-end optimization, so that the constructed map is more perfect. IMLS-SLAM (Deschaud, 2018) uses 3D data directly by scan-tomodel matching from 3D radar and representing them with implicit moving least squares (IMLS) and achieves the effect of reducing drift. 

This is a solution for mapping and positioning based on the extraction of line segments in 3D point clouds (Y. Guo et al., 2020). The 3D point cloud is segmented, and different environmental objects are divided into different segments, thus a new map representation method is proposed: 
Segmap. Compared with existing feature extractors that are only used for localization, Segmap uses data-driven (deep learning) descriptors to extract semantic feature information. Data processing at the semantic information layer greatly reduces the amount of computation, and the semantic feature descriptor with smaller dimensions solves the real-time data compression problem of single-robot and multi-robot systems. This 3D laser SLAM framework utilizing CNN semantic information has more advantages than traditional SLAM in multi-robot global path planning scenarios (Dub´e, Cramariuc, et al., 2018; Dub´e et al., 2017; Dub´e, Gollub, et al., 2018). 

## 4.5.3. Fusion Slam

Navigating the multifaceted domain of high-precision positioning, modern vehicles adroitly utilize a spectrum of sensors, synchronizing their operations to secure enhanced locational accuracy. BAD SLAM (Schops et al., 2019), for instance, presents a calibration benchmark that harmonizes synchronized global shutter RGB cameras with depth sensors, assuring a tightly knit and calibrated interaction among assorted sensors. LIC-Fusion (Zuo et al., 2019) strategically employs an algorithm that melds Inertial Measurement Unit (IMU) measurements with sparse visual features and extracted lidar points, enhancing multimodal sensor fusion. This integration notably improves accuracy and robustness, especially in contexts involving aggressive motions. DM-VIO, 
introduced in (Von Stumberg & Cremers, 2022), navigates through monocular visual-inertial odometry, wielding two pioneering techniques: delayed marginalization and pose graph bundle adjustment. It gracefully manages visual data, weaving dynamic weight into visual residuals and solidly embracing photometric uncertainties. The 
"delayed marginalization" strategy allows for a meticulous approach where marginalization is postponed, facilitating subsequent graph updates and enabling the creation of a fresh, consistently linearized marginalization prior. This permits the intertwining of IMU data into already marginalized states, forming the bedrock for the innovative pose graph bundle adjustment and assisting IMU initialization. When put to the test across various scenarios and datasets, DM-VIO not only outperforms existing methodologies in visual-inertial odometry but also surpasses stereo-inertial methods using a singular camera and IMU, 
marking a notable advancement in visual-inertial navigation. Both initiatives underscore the continual evolution of algorithmic approaches aiming to refine the precision of sensor data integration in complex environments. ORB-SLAM3 (Campos et al., 2021), on the other hand, expands support for fish-eye cameras and integrates visual and IMU systems, enabling the capture of a more generous field of view and thus, becoming valuable in restricted environments. The scrupulous integration and fusion of various sensors, along with the perpetual progression of algorithms, are pivotal in augmenting the precision and robustness of SLAM systems in automotive applications. 

Maps hold a pivotal position in SLAM applications, embodying various forms—ranging from point cloud maps, octree maps, and grid maps to topological maps—each serving distinctive purposes. The selection of both map type and associated algorithm is inherently tethered to the unique requirements and specifications of the given SLAM 
application. Broadly speaking, maps within this context can be compartmentalized into three primary categories: metric maps, topological maps, and semantic maps. Point cloud-based mapping and localization emerge as prevalent methodologies within this spectrum of mapping techniques, garnering widespread acclaim and utilization. However, it is imperative to acknowledge the inherent limitations of these methods; the expansive scale of point cloud maps, coupled with their constraints in accommodating dynamic objects, presents tangible challenges. In light of these limitations, octree maps—which boast superior compressibility—have been identified and employed as viable alternatives for diverse SLAM applications (Vespa et al., 2018). When navigating the process of map type selection for SLAM, a multitude of factors warrant careful consideration, including the requisite spatial accuracy, inherent complexity, overall scale of the application, and the imperative for semantic information. These considerations are instrumental in aligning the selected map type with the demands and expectations of the specific SLAM application in focus. 

SLAM is experiencing robust advancements. In environments with low texture, where salient features are scarce, SLAM's efficacy diminishes. Radar-based SLAM is hindered by the substantial cost of radar and its struggle with low texture and dynamic environments. Fusion SLAM, integrating data from various sensors, is progressing rapidly; however, it necessitates uniform processing of data types, timestamps, and coordinate systems. Deep learning-based Semantic SLAM holds promise for high-precision, real-time positioning in extensive settings, and is likely to supersede traditional geometric SLAM, excelling in global optimization, loop closure, and relocalization. Additionally, deep neural networks (DNNs) are being employed in self-supervised motion estimation to mitigate multimodal data discrepancies, thereby enhancing the accuracy and dependability of all-weather autonomous driving (Fig. 8). 

4.5.4. *Challenges and prospects: Localization and mapping* Advancements in sensor technology, artificial intelligence, and computational power are continually reshaping the domain of localization and mapping for autonomous driving systems. High-definition mapping, combined with sophisticated algorithms for SLAM, is empowering vehicles 

![14_image_0.png](14_image_0.png)

with unprecedented spatial awareness. The integration of real-time kinematic positioning with IMUs and advancements in machine learning for sensor fusion contribute to an ever-improving accuracy in vehicle localization. Furthermore, the proliferation of 5G connectivity and edge computing offers the prospect of cloud-assisted driving, where vehicles can access updated maps and localization data with minimal latency. As these technologies mature, they promise to mitigate current limitations, such as the dependency on high-visibility conditions and the need for intensive computational resources. The anticipated synergy between these technological developments is poised to significantly elevate the robustness and reliability of localization and mapping systems, reinforcing them as pivotal components in the autonomous driving stack, which are meticulously summarized in Table 9. 

## 5. **Motion Planning And Decision-Making**

Deep learning has profoundly reshaped the field of autonomous driving, particularly in the facets of motion planning and decisionmaking, thereby drastically boosting both the performance and safety standards of such vehicles. Motion planning is the process of devising an optimal route from a starting point to a destination, while skirting around obstacles and abiding by a set of constraints. Conversely, decision-making and behavior arbitration involve the intelligent processing of decisions, leveraging real-time environmental perceptions, sensor data, and established rules to enable vehicles to suitably respond to dynamic traffic conditions. Key elements in these domains, such as path planning, trajectory prediction, and behavior arbitration, witness 

## 5.1. Path Planning

Motion planning includes path planning and trajectory planning, both of which belong to the planning layer. The path planning is to move the autonomous driving from the starting position to the ending position according to a certain path strategy. Path planning is one of the main research contents of motion planning. Global path planning requires all environmental information to be mastered, and global path planning can be performed based on high-definition (HD) maps. Local path planning requires the real-time information of sensors to understand the environment, and then determine the distribution information such as obstacles, so as to select the local optimal path. Traditional path planning methods can be divided into search-based path planning algorithms, such as Dijkstra (Daniel et al., 2010; T. Zhang et al., 2021), 
which are also raster map-based search algorithms. Probability-based path planning algorithms, such as the RRT series (Karaman et al., 
2011) of algorithms. This section focuses on the neural network algorithms most relevant to AI. 

For autonomous driving, AI can imitate and reproduce human reasoning and learning behavior. This requires autonomous driving to think like humans in order to adapt to the environment and predict future trajectory behaviors. From this aspect, AI is of great significance 

| Challenges and prospects of localization and mapping.  Research Area Challenges Prospects for Improvement  Dynamic  Rapid environmental  Environments  changes, such as construction  and weather variations, make  it difficult to maintain up-todate maps.  Sensor fusion integrating  data from diverse sensors to  improve localization  accuracy and adapt to  changes, ensuring effective  navigation.  GPS  In urban areas or tunnels, GPS  Dependability  signals can be unreliable or  unavailable, affecting  localization.  Advanced AI and machine  learning techniques to  predict and compensate for  GPS loss, using historical   |
|---|

Advanced AI and machine 

learning techniques to predict and compensate for GPS loss, using historical 

data for smarter navigation 

decisions. 

![15_image_0.png](15_image_0.png)

High computational demand for real-time mapping and localization can hinder 

performance, particularly 

when quick decisions are 

needed. 

Collaborative updates via 

vehicle-to-vehicle (V2V) 

networks to share real-time 

data, continuously refining maps for long-term accuracy. 

Sensor Precision Inaccuracies in sensor data 

and drift over time can 

degrade the quality of 

localization and mapping. 

Edge computing solutions to reduce latency, enabling faster data processing close to data sources, and lessening the burden on central systems. 

Map Accuracy Keeping maps accurate over time is difficult due to constant environmental changes, leading to potential obsolescence. 

Quantum sensors and technologies that provide higher precision to overcome drift and inaccuracies, boosting localization and mapping reliability. 

to the decision-making system of autonomous driving. As stated by 

![15_image_1.png](15_image_1.png) (Claussmann et al., 2017), the period of flexibility and adaptability of AI methods is perfectly adapted to the upper-level decision-making of the agent. Compared with other methods, AI can generally solve decisionmaking problems, and can learn without modifying algorithms in new and unknown environments. The following subsections will introduce the application of AI in motion planning. 

## 5.2. Trajectory Prediction

5.2.1. *Generative models* Generative models have shown good results in tasks such as imageto-image translation and image synthesis, super-resolution, which have multiple possibilities for a given input and output. The authors of 
(Petrovich et al., 2021) introduce a Deep Stochastic IOC1 RNN encoderdecoder framework that uses a conditional variational autoencoder to obtain a set of different hypothetical future prediction samples for future prediction tasks on multiple interacting agents in dynamic scenes. 

However, they lack the simulation of human interaction in crowded scenes. An alternative approach, generative adversarial networks (GANs) offers a promising tool that contains two models, one is a generative model and the other is a discriminative model. The task of a generative model is to generate instances that look natural and real, similar to the original data. The task of a discriminative model is to judge whether a given instance appears to be naturally real or artificial, where the training process is a minimax game between a generative model and a discriminative model; this overcomes the difficulty of approximating intractable probability calculations (G. Zhang et al., 2021). A generative adversarial pipeline for crowd trajectory prediction and group membership identification in a crowd was proposed by REF. (Fernando et al., 2018a). Dimension extracts the most discriminative features and reduces them by DBSCAN clustering. They model the local neighborhood of a pedestrian of interest with a soft and hard attention framework (Fernando et al., 2018b), where the soft attention context vector is used to embed trajectory information from the pedestrian of interest, and the hardwired attention context vector is used for adjacent trajectories. The method exhibits encouraging results on learning complex real-world human navigation behaviors on multiple public benchmarks. REF. (Gupta et al., 2018) integrated the extraction and dimensionality reduction of crowd trajectory features into the same framework, in which the encoding module is responsible for trajectory feature extraction, and the pooling module replaces clustering for feature dimensionality reduction. The authors also propose a simple diversity loss function, coupled with pooling layers to encourage the network to produce globally consistent, socially compatible diversity samples. In addition to the generative models of the above methods, some researchers use the generative model of flow-base to predict the agent 
(Rhinehart et al., 2019). 

## 5.2.2. Gnn-Based Models

Aggregation of feature states in aggregation layers of earlier recurrent architectures is neither intuitive nor straightforward, and may not correctly model interactions between pedestrians. In recent years, variants of GNNs (J. Zhou et al., 2020), such as graph convolutional network (GCN) (S. Zhang et al., 2019) have demonstrated groundbreaking performances across a wide range of tasks. A social spatiotemporal graph CNNs (STGCNNs) (Mohamed et al., 2020) pedestrian trajectories as a spatiotemporal graph, the edges of the graph represent the interactions between pedestrians, and an adjacency matrix with a kernel function measures pedestrians influence between. The STGCNN 
and time-extrapolator (TXP)–CNN in the model operate on the spatiotemporal graph, so that the model can be in one shot to predict the entire sequence. Experiments show that Social-STGCNN outperforms previous models in both prediction accuracy and inference speed. Like SocialSTGCNN, temporal point cloud networks (TPCN) (Ye et al., 2021) also divides trace prediction into spatial and temporal dimensions to capture spatial and temporal information, but the author believes that it is difficult to deal with large-scale scenes containing a large number of nodes and vertices based on GCN, so a point cloud learning strategy is adopted. The prediction task is accomplished through joint learning between spatial and temporal modules. The spatial module takes advantage of the complementary information between voxel and point representations, preserving the geometric information of the graph. The temporal module utilizes the proposed dynamic temporal learning method: multi-interval learning and instance pooling to capture more fine-grained sequential information. 

## 5.2.3. Multimodal Deep Learning Fusion

In the realm of trajectory prediction, the extrapolation of observed motion patterns from historical data into future estimates is paramount. Sequence models rooted in deep learning, especially RNNs, have demonstrated proficiency in navigating such challenges due to their capacity to articulate temporal dependencies. In a discernible trend towards amplifying accuracy and extending the predictive time horizon in recent endeavors, there is an incorporation of multimodal models. This synthesis enables the intelligent models that not only project trajectories across temporal horizons but also capture the intricate spatial relationships and temporal patterns, thereby enhancing the model's predictive acumen and reliability in trajectory forecasting. 

The combination of RNN and DRL to predict the behavior of pedestrians and vehicles is a hotspot. RNNs can encode the motion information of pedestrians of interest and other surrounding pedestrians, and map these encoded dynamics into feature maps, maintaining the structural integrity of neighbors. A DRL model will choose the best predictive strategy. REF. (Fernando et al., 2019) proposed an inverse reinforcement learning (D-IRL) method based on an attention framework together with LSTMs to predict human trajectories in the far future. The reward prediction network of this architecture is a FCN, ensuring that the learned reward map covers all regions of the environment, incorporates structural factors such as buildings and paths that affect pedestrian behavior, and utilizes a combination of soft and hardconnected attention to embed features from the agent's local neighborhood. The method achieves encouraging results in predicting pedestrian behavior in the far future. To validate the effectiveness of DIRL, the authors of (Fernando et al., 2020) quantitatively and qualitatively evaluate these frameworks on two public driver benchmark datasets and demonstrate the utility of D-IRL, especially when predicting longer trajectories. good performance. Nowadays, reinforcement learning is also widely used in navigation and vehicle following (Cai et al., 2019; Gao et al., 2018) proposes a CIL end-to-end model that receives camera images, high-level commands, and the autonomous driving's previous trajectory, and learns to output a collision-free trajectory 3 s later. The network consists of 3 sub-networks for performing 3 basic driving tasks: going straight, turning left and turning right. These sub-networks are then fed into the LSTM/FCC network to output trajectories. (Everett et al., 2018) proposes a collision avoidance algorithm, GA3C-CADRL (GPU/CPU Asynchronous Advantage Actor-Critic for Collision Avoidance with Deep RL), which does not require any other agents Simulation training with DRL with knowledge of dynamics, and a strategy borrowed from LSTM networks in natural language processing, which enables the algorithm to use the observations of any number of other agents, rather than Previous methods with fixed observation size. 

## 5.3. Decision-Making 5.3.1. Ai Logic-Based Approach

Introducing inference into motion planning for intelligent driving is a reasonable choice. An inference engine is a component of an AI system that applies logical rules to a knowledge graph (or foundation) to reveal new facts and relationships. The inference engine can be implemented inductively or deductively. Among all reasoning engines, the rule-based reasoning algorithm (expert system) is the most famous, with the statement: "if observe, then act". Expert systems rely on a knowledge base and an inference engine to automate the inference system and solve specific complex tasks. When the knowledge base is updated, a recursive mechanism must be used to ensure the convergence of the new rule system. The recursive mechanism can transform a big problem into many small problems and solve it conveniently. The advantages of this system are clear semantics, intuitive performance, and the ability to clearly describe the objective laws or domain concepts implicit in data distribution. However, the disadvantage is that designing a large number of rules and circular reasoning is necessary, which prolongs calculation time, requires expert guidance in the field, and has poor portability and learning ability. 

The emergence of finite state machine (FSM) (Y. Chen et al., 2019) 
solves the problem of infinite exhaustive rules. FSM describes states and transitions between states that are triggered in response to changes in the environment. Logical assertions and conditions contribute to reasoning explanatory power. The system is simple and controllable, easy to develop, and can describe complex state relationships. The main disadvantages are the acquisition, maintenance and storage of knowledge bases, the expert generation of engines, the discretization of a large number of environmental variables, and due to the determinism based on knowledge, it cannot be generalized to unknown situations. 

In the realm of autonomous driving, decision-making tools are critical for assessing various scenarios and making informed choices. The Decision Tree is one such tool that elucidates the mechanics of rulebased decision-making (Charbuty & Abdulazeez, 2021). It comprehensively enumerates possible strategies, making it well-suited for applications such as vehicle lane-change predictions (C. Wang et al., 2019), 
collision predictions in autonomous driving (Osman et al., 2019), and pedestrian behavior predictions (Xin et al., 2022) in relatively simple scenarios. In scenarios characterized by dynamic uncertainty, more sophisticated models come into play. For instance, REF. (Luque & Straub, 2019) employed a Dynamic Bayesian Network which hinges on a statistical representation of causality based on probability transitions. 

Moreover, REF. (X. Liu et al., 2022) tackled the problem of tentacle trajectory selection by modeling it as a markov decision process (MDP), wherein among navigable trajectories, a tentacle acts as the local reference trajectory for the vehicle (Lin et al., 2021). 

When dealing with environments that are both dynamic and uncertain, the partially observable markov decision process (POMDP) offers a mathematically sound model that links perception and planning. This is particularly useful for decision-making problems involving interdependent behaviors of multiple agents. REF. (Cubuktepe et al., 2021) utilized a robust convex optimization technique amenable to computing solutions for multi-state, uncertain, and partially observable problems. However, solving POMDPs in complex scenarios is computationally challenging due to the iterative nature of the solutions. This has led to the coupling of POMDPs with DRL (G. Singh et al., 2021; Song et al., 2022). Notably, advancements in time-series models have further bolstered the synthesis of POMDPs and DRL, circumventing the intricate solution process (S. Kumar et al., 2020; Parisotto et al., 2020). 

The way autonomous driving systems make decisions is varied and complex. They use everything from simple decision trees to more advanced systems like dynamic Bayesian networks and partially observable Markov decision processes (POMDPs). The choice of which method to use depends on how complicated and unpredictable the driving environment is. As these decision-making systems get better, they are becoming more capable of making the precise and critical decisions needed for safe and smart self-driving. We're entering a time when these systems can adapt and respond with incredible accuracy, which is a big step forward for the reliability and independence of autonomous vehicles in the real world. 

## 5.3.2. Ai Heuristic Algorithms

Heuristic algorithms are proposed relative to optimization algorithms. A heuristic algorithm (Goli et al., 2021) can be defined as follows: an algorithm based on intuition or empirical construction that gives a feasible solution for each instance of the combinatorial optimization problem to be solved at an acceptable cost (referring to computing time and space), and the feasible solution is the same as the optimal solution. The degree of deviation of the solution cannot generally be predicted. When faced with complex problems, the heuristic algorithm has lower complexity and faster calculation speed than the traditional exhaustive method, but cannot guarantee the convergence to the global optimal solution. The basic idea in motion planning is to discretize the state space into a graph in a certain way, and then use various heuristic search algorithms to search for feasible solutions or even optimal solutions. This kind of algorithm has analytical completeness and even analytical optimality, and this kind of algorithm is relatively mature now. A support vector machine (SVM) is a statistical learning classifier that relies on information search for the intent of an agent. The literature (Vallon et al., 2017) proposes a classifier autonomous lane changing algorithm based SVM. Several SVMs are trained using data from human drivers' actual lane changing and lane keeping demonstrations. 

Metaheuristic algorithms are widely used heuristic algorithms, which include the tabu search algorithm, simulated annealing algorithm, genetic algorithm, ant colony optimization algorithm, particle swarm optimization algorithm, artificial fish swarm algorithm, artificial bee colony algorithm, and artificial neural network algorithm (Osaba et al., 2021). This paper mainly focuses on the research status of the artificial neural network algorithm. An artificial neural network is an information processing system designed to mimic the structure and function of the human brain. Like the multilayer perceptron, neural networks learn based on misguided, constantly adjusting weights. 

Neural networks can handle supervised learning, unsupervised learning, and reinforcement learning, and their main advantage in autonomous driving is their ability to learn through training on multi-dimensional data with strong learning capabilities. However, the reasons for their decisions lack interpretability and are not as intuitive as rule-based learning. Many researchers treat neural networks as black boxes. If the training method is incorrect, they may make poor decisions due to the variety of vehicle states. Specifically, the system must learn the rules to apply in each environment, and large amounts of human-labeled data are required to improve accuracy. 

5.3.3. *Reinforcement learning* Deep reinforcement learning has gained significant popularity in the field of motion planning for autonomous vehicles (Aradi, 2020). Modelbased methods generally provide better data efficiency and can employ models for various purposes, including planning and data augmentation. 

For example, an explicit model of the environment's dynamics, including a transition function and a reward function, is constructed. The model is then leveraged to derive a policy that aims to maximize cumulative rewards through these functions (Deisenroth & Rasmussen, 2011). In contrast, model-free reinforcement learning does not incorporate a known model of the environment. Instead, it estimates the action-value function Q(s, a) or the state-value function V(s) directly and selects actions based on these estimates. In essence, model-free methods learn from interactions with the environment without a predefined model, often using neural networks for approximation. For example, REF. (Kendall et al., 2019) represents a pioneering attempt to apply deep reinforcement learning to autonomous driving. The authors used a model-free deep reinforcement learning algorithm for lane-keeping, one of the fundamental tasks in autonomous driving. The salient feature of this study is the simplicity and generality of the reward function; the distance travelled without intervention from a safety driver. This is an ingenious approach as it doesn't require meticulously crafted reward functions. The study uses a single monocular image, which signifies a minimalist approach. The research puts forward a new paradigm in autonomous driving by minimizing the dependency on predefined rules, mapping, and direct supervision. The reliance on on-vehicle exploration and optimization is noteworthy, but it may also imply challenges regarding safety during training. 

To tackle a specific scenario in autonomous driving: overtaking on highways, one research presents a hierarchical control framework 
(Fig. 10), where the upper level is responsible for making driving decisions, and the lower level supervises vehicle speed and acceleration 
(Liao et al., 2020). This division mimics how human drivers operate, with cognitive decision-making coupled with fine motor control, which adds intuitiveness and logic to the system design. The study incorporates dueling deep Q-network (DDQN) for decision-making, an advanced algorithm variant known for its efficiency in learning value functions. The in-depth mathematical exploration and the comparison between DQN and DDQN in the study offer valuable insights into the decision-making algorithm's workings. However, it is crucial to strike a balance between reacting to unforeseen behavior and maintaining fluidity in driving without being excessively cautious, as this can hinder traffic flow. 

The infusion of multi-agent reinforcement learning (MARL) casts a deliberate lens on the interactions amongst various agents—vehicles, pedestrians, and more—mirroring the complexity intrinsic to real-world scenarios. A wave of recent research (Bhalla et al., 2020; Palanisamy, 2020; Wachi, 2019; C. Yu et al., 2019) has navigated through the challenges of autonomous driving with a focus on MARL, attracted by its ability to adapt to the dynamic interactions and inherent unpredictability commonplace in traffic environments. Diverging from singleagent systems, MARL respects the non-static nature of various agents, each potentially adhering to their unique objectives and policies. Moreover, it can orchestrate coordination and negotiation amongst autonomous vehicles, proving indispensable in scenarios such as traffic merging, lane-changing, and intersection navigation—enabling more fluid traffic flows and augmenting safety and efficiency. Nonetheless, autonomous vehicles navigate through perpetually evolving environments, often interacting with a vast number of agents, posing a formidable scalability challenge. Additionally, the non-stationarity of agents' policies compounds the complexity of learning within MARL settings when juxtaposed with single-agent reinforcement learning. Thus, as MARL research in the context of autonomous driving propels forward, a pivotal focus on scalability, real-time adaptation, and sturdy coordination mechanisms becomes imperative, steering toward the realization of resilient and efficient autonomous driving systems that adeptly weave into the multifaceted fabric of contemporary traffic environments. 

5.4. *Challenges and prospects: Motion planning and behavior arbitration* Motion planning and behavior arbitration collectively constitute the 

![18_image_0.png](18_image_0.png)

![18_image_1.png](18_image_1.png)

intellectual core essential for the effective operation of autonomous vehicles, playing a crucial role in facilitating intelligent decision-making processes and meticulous planning corresponding to diverse environmental contexts. The significance of these elements extends beyond their central role, as they are indispensable in ensuring safety and enhancing operational efficiency - both fundamental to the practical application of autonomous driving. Nevertheless, the domains of motion planning and behavior arbitration are laden with multifarious challenges demanding urgent resolution and thoughtful consideration. Such challenges encompass issues related to real-time decision-making amidst uncertainties and the necessity for behavior optimization in the everchanging landscape of traffic scenarios. These existing obstacles inevitably hinder the unobstructed deployment of autonomous driving technologies. Nevertheless, the present technological milieu is characterized by a series of remarkable advancements and innovations, providing a canvas of opportunity that has the potential to substantially impact the future direction of autonomous driving. These developments, ranging from advanced algorithms with learning and adaptive capabilities in complex environments to hardware innovations offering increased computational power, signal a future where challenges within motion planning and behavior arbitration are not merely addressed but also converted into opportunities for improved functionality and performance. This delicate balance between challenges and opportunities as outlined in Table 10 provides a fertile ground for the ongoing refinement of processes related to motion planning and behavior arbitration, vital for the development of autonomous vehicles. 

## 6. **Simulator & Scenario Generation**

Given that deep learning involves a process of trial and error along with data sampling, it is typically essential to initially assess algorithms within a simulated environment before evaluating their performance in a real-world setting (Fig. 11). Hence, the creation of a simulation environment is indispensable for training models, especially in reinforcement learning (Kiran et al., 2021). State-action pairs used for learning can be acquired through the interaction of autonomous driving systems with their simulated surroundings. Currently, various autonomous driving task simulators are used to train and validate reinforcement learning algorithms. Such as Motion Planning, Intersections, Table 10 Challenges and prospects of motion planning and decision-making. 

Research Area Challenges Prospects for Improvement Complex Traffic Scenarios The unpredictability in traffic due to variable driver behavior and dynamic conditions creates substantial challenges for autonomous vehicle motion planning. 

Advanced AI and machine learning techniques can enhance vehicles' ability to make adaptive decisions, effectively managing the unpredictability of complex traffic scenarios. 

Real-time Decision Making Developing cutting-edge algorithms that model human behavior can lead to more responsive and socially acceptable autonomous driving, streamlining realtime decision-making. 

Human-like Driving Behavior Autonomous vehicles must make immediate, safe, and efficient decisions in constantly changing environments with numerous moving variables. 

Emulating a natural human driving style, crucial for seamless traffic integration and public trust, is difficult while maintaining high safety standards. Dealing with inaccuracies and the unpredictability of sensory data is crucial for the consistent and reliable performance of autonomous driving systems. 

Simulations and the use of digital twins for exhaustive testing can advance the safety and reliability of driving algorithms, promoting human-like behavior without compromising safety. 

Legal and Ethical Constraints Autonomous vehicles face complex ethical decisions and legal issues, especially in situations with potential safety risks, requiring careful consideration and compliance. 

Implementing V2X communication and developing consistent ethical guidelines can help navigate these challenges, improving vehicles' predictive responses and adherence to regulations. 

Robustness to Sensor Noise and Uncertainty Incorporating robust ethical standards and sophisticated risk assessment methodologies can bolster the reliability of algorithms, ensuring robust performance amid sensor noise and uncertainties. 

![19_image_0.png](19_image_0.png)

Overtaking, Lane Change, Lane Keep and more. Some simulators also incorporate vehicle state dynamics. REF. (Beard & Baheri, 2022) proposed a Multi-Fidelity Reinforcement Learning (MFRL) framework available for multiple simulators. Enables training and validation of RL algorithms by representing state dynamics (and thus computational cost) using a cascade of simulators with increasing fidelity, while using RC cars to find real-world examples in fewer expensive real-world samples close to the optimal strategy. Experiments on RC cars (Abbeel et al., 2006) demonstrate the reliability of the MFPL framework and the possibility of porting reinforcement learning algorithms to real vehicles. 

Carla Simulator is currently a popular open simulator for urban autonomous driving (research, 2023). The competition evaluates autonomous driving systems in a variety of special scenarios based on the National Highway Traffic Safety Administration report (Najm et al., 2007), such as: vehicle loss of control, vehicle reacting to invisible obstacles, lane changing to avoid slow preceding vehicles, etc. 

Since online reinforcement learning needs to interact with the environment in the process of finding the optimal strategy, the construction of simulators or simulators increases the learning cost, so many researchers now start research on offline reinforcement learning to achieve real data-driven This will be of great significance for the reinforcement learning decision-making experiment of unmanned driving. The current main problem of offline reinforcement learning is nondistribution operation guidance and overfitting (Prudencio et al., 
2023). The main research methods are policy constraints (Fujimoto et al., 2019; Kumar et al., 2019; Nair et al., 2020), regularization (A. 

Kumar et al., 2020; A. Singh et al., 2020), trajectory optimization (L. 

Chen et al., 2021; Janner et al., 2021) and model-based policy optimization (T. Yu et al., 2021). 

A crucial impediment to the progression and implementation of autonomous driving technology lies in the formidable costs—both temporal and financial—necessary for verifying the safety of these systems within the intricate tapestry of real-world driving scenarios. This verification challenge is intensified by the rarity of safety–critical events. In response, scholars and practitioners have collaboratively fashioned an intricate testing ecosystem, which ingeniously employs AIbased background agents (Feng et al., 2023). These agents, meticulously trained through a dense deep-reinforcement-learning (D2RL) methodology applied to a corpus of naturalistic driving data, are pivotal in impartially and efficiently assessing the safety functionalities inherent to autonomous driving systems (Fig. 12). The D2RL methodology is characterized by a judicious manipulation of Markov decision processes, encompassing the excision of non-crucial states and the linkage of critical ones, culminating in a data set enriched with densified, safety–critical information. This enhancement in turn facilitates the acquisition of invaluable knowledge by neural networks during safety–critical events, enabling the accomplishment of tasks previously deemed unfeasible through conventional deep-reinforcement learning techniques. To illuminate the efficacy of this approach, experimental trials were orchestrated utilizing a highly automated vehicle within the controlled environments of both highway and urban testing tracks. This innovative approach presents a viable pathway for harnessing AI in the verification of other safety–critical autonomous systems, offering a significant enhancement over existing methodologies by overcoming their limitations in real-world applications. 

## 7. **Current Challenges And Limitations**

Autonomous mobility is not just about innovating sophisticated systems; it requires the seamless integration of complex subsystems. 

While both academia and industry are working diligently, the success of autonomous driving systems remains deeply intertwined with the performance of its individual subsystems. This interdependence introduces certain challenges and limitations (Fig. 13): 
(1) **Higher Safety Standards**: While autonomous driving systems leverage cutting-edge technology to improve safety, achieving and maintaining higher safety standards presents significant challenges. Advanced sensors and AI algorithms must perform flawlessly in real-time, necessitating relentless testing and validation to ensure reliability. The integration of lidar, radar, and cameras, despite providing a comprehensive sensory network, introduces intricate interdependencies and potential points of failure that must be meticulously managed. The need for robust 

![20_image_0.png](20_image_0.png)

![20_image_1.png](20_image_1.png)

backup systems and fail-safes adds layers of complexity and requires stringent safety measures that are often difficult to standardize across varying traffic and weather conditions. 

Additionally, ensuring that these systems can handle unexpected scenarios without human intervention continues to be a formidable challenge that the industry must overcome to fully realize reliable autonomous driving. 

(2) **Complexity of Urban Environments**: The urban environment poses one of the most intricate challenges for autonomous vehicles, where a high density of dynamic and unpredictable elements exists. Advanced mapping systems and data-driven machine learning algorithms are pivotal in these settings; however, they must contend with the constant variability and unpredictability of city landscapes. Real-time data processing must be incredibly fast and accurate to interpret the actions of pedestrians, cyclists, and other vehicles—tasks that humans perform intuitively but are highly complex for machines. There are also challenges related to the scalability of these systems in different urban areas with their own unique traffic patterns and infrastructure. Ensuring consistent performance across the various of scenarios encountered in urban settings underscores the monumental task facing developers of autonomous vehicle systems. Achieving a seamless and safe integration of autonomous vehicles into the already complex tapestry of urban traffic is not only a technological hurdle but also a regulatory and infrastructural one. 

(3) **Robust Performance in Adverse Weather**: The aspiration for autonomous vehicles to perform robustly in adverse weather conditions introduces a gamut of challenges that significantly complicate research and development. Sensors such as lidar and cameras, which are critical for navigation and obstacle detection, can be severely impaired by rain, snow, fog, or extreme temperature fluctuations. The attenuation of signals and distortion of data in such conditions can lead to reduced visibility and sensor reliability, necessitating the creation of more resilient sensor systems. Despite ongoing research into novel sensing techniques, enhancing sensor fusion, and crafting adaptive algorithms, achieving consistent performance in all weather conditions remains an elusive target. The difficulty lies not only in developing technologies that can withstand such environmental stresses but also in ensuring these systems can make safe and accurate decisions in the face of rapidly changing or extreme weather phenomena. 

(4) **Dynamic and Unpredictable Scenarios**: Dynamic and unpredictable scenarios present a thicket of challenges for autonomous vehicles. Navigating through construction zones, reacting to sudden obstacles, managing complex traffic dynamics, and safely interacting with pedestrians and cyclists require a level of situational awareness and decision-making sophistication that current technology struggles to achieve. Beyond the technical complexities, there are additional layers of challenges involving legal frameworks, ethical considerations, data privacy concerns, and the imperative for continuous learning and adaptation of the AI systems. Crafting algorithms that can make split-second decisions in such scenarios, implementing redundant sensor systems to cover potential failures, updating legal regulations, and establishing clear ethical guidelines are monumental tasks that researchers and policymakers must address. Ensuring that autonomous vehicles can not only cope with but excel in handling these various unpredictable elements is critical to their acceptance and success in the real world, where every day brings a new set of variables. 

(5) **Interpreting and Reacting to Human Behavior**: Autonomous vehicles must be adept at interpreting human behavior—a challenge that remains one of the most formidable hurdles to widespread adoption. Human actions are often situationally dependent, with subtle cues such as eye contact or hand gestures being key indicators of intent, particularly in shared spaces. Machines must be trained to not only recognize these cues but also understand their context, which can vary widely across different cultures and social norms. The individuality of human behavior adds another layer of complexity, making it difficult for machine learning models to predict and adapt to every potential scenario. This challenge calls for advancements in artificial intelligence that go beyond mere pattern recognition, requiring a sophistication that allows for an almost empathic understanding of human behaviors and intentions within an infinitely variable range of situations. 

(6) **Ethical Concerns**: The deployment of autonomous vehicles transcends technical challenges and delves into profound ethical considerations. Decisions made by these systems in split-second scenarios—often referred to as "moral dilemmas"—evoke questions about the value of life and the prioritization of safety. 

Establishing ethical guidelines for autonomous driving systems is as crucial as it is complex, involving multifaceted issues that intersect with our deepest values, legal systems, and societal norms. This domain of ethics is not just about programming a set of rules but about how these machines can embody ethical principles that are universally accepted and understood. It necessitates a collaborative approach involving ethicists, engineers, legal experts, and the broader public to ensure that the moral compass guiding autonomous vehicles aligns with societal expectations and preserves the fabric of trust and safety in our communities. 

(7) **Legal and Regulatory Frameworks**: Establishing legal and regulatory frameworks for autonomous driving is a complex task that has to accommodate a diverse range of traffic environments and conditions. The intricate interplay between software and hardware in autonomous vehicles, compounded by the unpredictability of external factors, creates a tangle of liability issues. 

Determining responsibility in the event of malfunctions or accidents is a contentious and unresolved issue. Furthermore, these vehicles generate vast amounts of data, which introduces substantial privacy concerns. The imperative to secure this sensitive information against various threats, and the necessity to comply with stringent data protection laws, adds to the regulatory maze. 

The evolving nature of this technology means that legal systems are perpetually playing catch-up, striving to create regulations that balance innovation with public safety, privacy, and security. 

(8) **High-Definition Mapping and Localization**: Creating and continuously updating high-definition maps for autonomous vehicles is a task of herculean proportions. These maps must reflect the real-time dynamics of the driving environment, capturing changes such as road works, temporary obstructions, and shifts in traffic patterns. To achieve the required level of detail and accuracy, there is a need to synthesize an enormous volume of data from a variety of sources. This synthesis must be both rapid and reliable, presenting substantial technical and computational challenges. Moreover, the storage, processing, and dissemination of this high-fidelity mapping data demand robust infrastructure and significant computational resources. Keeping these maps current is a relentless endeavor that necessitates constant data collection and processing, highlighting the formidable challenge of ensuring that the virtual representations used for navigation are always an accurate reflection of the physical world. 

(9) **Cybersecurity**: As autonomous vehicles become more interconnected, they are increasingly vulnerable to sophisticated cyber threats that could compromise passenger safety and privacy. The complexity of these systems, with their various sensors, actuators, and communication modules, presents a broad attack surface for potential hackers. Developing comprehensive cybersecurity measures for these vehicles is a monumental challenge. It involves not only safeguarding the communication channels with robust encryption and secure protocols but also ensuring the integrity of the software and hardware against tampering and intrusions. Regular vulnerability assessments and penetration testing are crucial to identify and address security gaps. However, the evolving nature of cyber threats means that these measures must be continually updated and adapted. Moreover, building resilient systems that can detect, isolate, and respond to cyberattacks in real time is critical to maintaining safety and functionality, thereby creating multiple layers of security that can adapt as quickly as new threats emerge. 

(10) **Public Trust and Confidence**: Earning public trust and confidence in autonomous driving technology is an ongoing challenge that hinges not just on demonstrating technical competence but also on addressing deeper concerns around safety, reliability, and privacy. These concerns are rooted in a natural apprehension towards surrendering control to machines, compounded by highprofile mishaps and privacy breaches. Overcoming this skepticism requires transparent communication about the capabilities and limitations of autonomous vehicles, as well as clear demonstrations of their benefits in improving traffic efficiency, reducing accidents, and enhancing mobility for the disabled and elderly. Moreover, it calls for a consistent track record of performance that stands up to public scrutiny. Education campaigns and the involvement of community stakeholders in testing and development can further bridge the gap between technology and public sentiment. Ultimately, building trust is a process that encompasses not only technical excellence but also an empathetic understanding of the public's concerns and a commitment to addressing them. 

## 8. **Outlook And Future Directions**

To truly advance autonomous driving, we need to encourage research partnerships between various industries and academic institutions. The main goal is to make these systems safer and more reliable, ultimately changing how we view and experience travel. Some critical areas to focus on are: 
(i) **Tech Innovation Growth**: The horizon of autonomous driving is linked to the pace of technological innovation. Progress in sensor technology, artificial intelligence, processing capabilities, and network connectivity is vital for advancing the sophistication of self-driving vehicles. Enhanced sensors are being developed to provide greater precision and range, while AI is evolving to make more nuanced decisions. Increased processing speed will allow for quicker response times and more complex scenario analysis, and stable, high-speed connectivity is essential for real-time data exchange and vehicle to everything (V2X) communications. Additionally, augmented reality (AR) and virtual reality (VR) are emerging as pivotal tools in creating highly detailed simulations for training autonomous systems, allowing them to navigate virtual environments that closely mirror the real world. These advancements in simulation technology will lead to higher levels of accuracy and reliability in autonomous driving systems, fostering greater trust in their ability to operate safely and efficiently in the real world. 

(ii) **Elevating Road Safety Paradigms**: The transformative potential of autonomous driving in the domain of road safety is profound. 

By removing human error—a significant factor in road mishaps—autonomous vehicles offer the promise of substantially reducing accidents caused by distractions, fatigue, impaired driving, and other human-related issues. The shift towards more autonomous systems on the roads is expected to usher in a new era of safety standards, with vehicles equipped to consistently adhere to traffic rules, maintain safe distances, and execute defensive maneuvers. The ripple effects of this technological shift could be extensive, not only improving individual passenger safety but also revolutionizing transportation systems at large. 

The overall safety of roadways could be improved, and emergency response services might be able to operate more efficiently. 

In the broader context, the enhancement of road safety through autonomous driving technologies contributes significantly to the global vision of creating safer living environments, potentially saving thousands of lives annually and leading to a paradigm shift in how safety is perceived and achieved on the roads of the future. 

(iii) **Optimizing Traffic Flow**: Future developments in autonomous driving are set to revolutionize the way traffic flows on our roads. 

With the integration of advanced navigation systems and vehicleto-vehicle (V2V) communication, autonomous vehicles can travel in harmonized swarms, seamlessly negotiating intersections and adapting to the ebb and flow of traffic. This synergy allows for the minimization of bottlenecks and the mitigation of the start-stop rhythm that characterizes congested roadways. In effect, it is anticipated that traffic will become more fluid, reducing commute times and enhancing the predictability of travel schedules. This orchestrated vehicular ballet not only benefits individual commuters but also has the potential to elevate the efficiency of the entire transportation ecosystem, cutting down on fuel consumption and reducing the environmental footprint of road travel. 

(iv) **Enhancing Mobility and Accessibility**: One of the most impactful prospects of autonomous driving is its potential to greatly enhance mobility and accessibility for individuals who have traditionally faced transportation challenges. By removing the need for a human driver, self-driving technology can grant newfound autonomy to the elderly, people with disabilities, and those who do not drive for various reasons. This advancement could profoundly enhance the quality of life for these groups by providing them with reliable transportation options. Beyond mere mobility, autonomous vehicles can facilitate better access to essential services, employment opportunities, and social interactions. This inclusivity extends the benefits of autonomous technology far beyond the individual, fostering a more connected, engaged, and equitable society. As this technology matures and becomes more integrated into our daily lives, it promises to reshape our communities into more inclusive spaces, where transportation barriers are significantly diminished, allowing everyone to contribute to and participate in the community more fully. 

(v) **Promoting Sustainable Transportation**: As we navigate towards a more environmentally conscious future, autonomous driving stands at the forefront of promoting sustainable transportation. These vehicles are engineered for optimal route efficiency, smoother acceleration, and braking patterns that contribute to lower fuel consumption and reduced greenhouse gas emissions. In electric vehicle (EV) formats, autonomous technologies complement the shift away from fossil fuels, leading to a cleaner transportation sector. Additionally, the potential for autonomous vehicles to function within shared mobility services can lead to a decrease in the number of vehicles on the road, further diminishing the transportation sector's carbon footprint. 

The ripple effect of such innovation is significant, aligning with international goals for sustainability and the mitigation of climate change, and it accelerates our journey towards achieving a low-carbon future. 

(vi) **Transforming Logistics and Delivery Services**: The domain of logistics and delivery services stands on the cusp of a major transformation powered by autonomous driving technology. 

Autonomous delivery vehicles and drones are carving out a path towards round-the-clock operations, enabling a level of precision and reliability previously unattainable. These technologies are set to streamline supply chains, drastically reducing delivery times, cutting costs, and minimizing human error. The capacity for continuous operation without the constraints of driver work hours will drive the efficiency of these systems to unprecedented levels. The prospect of a more optimized logistics infrastructure holds promise for both urban and rural areas, enhancing accessibility to goods and services. As a result, we can anticipate a future where the delivery of packages, groceries, and even medical supplies is more efficient, reliable, and accessible, propelling the logistics sector into a new era of innovation and performance. 

(vii) **Synchronizing with Smart City Infrastructure**: Autonomous driving is set to become an integral part of the smart city revolution, converging with other technological advancements to create highly efficient urban ecosystems. Vehicles capable of communicating with traffic signals, road sensors, and other infrastructural elements will usher in an age of synchronized mobility, reducing congestion and enhancing safety. Smart city infrastructure is poised to provide real-time data that will enable autonomous vehicles to navigate optimally, adjust to varying traffic conditions, and integrate with public transportation systems. This harmony between autonomous vehicles and urban design has the potential to enhance the livability of cities by making transportation more adaptive and responsive to the needs of the residents, and by extension, transforming the urban landscapes to be more sustainable and resilient. 

(viii) **Navigating the Regulatory and Legal Frameworks**: As autonomous driving technologies progress, there is an increasing need for updated regulatory and legal frameworks to guide their deployment and integration into public roadways. Ensuring the safety and reliability of these systems is paramount, necessitating regulations that can keep pace with technological advancements. 

Policymakers are called upon to establish clear guidelines addressing liability in the event of an accident, standards for data privacy to protect user information, and ethical codes to manage the decision-making algorithms within autonomous systems. 

Effective policy will need to balance safety and innovation, provide clear directives for manufacturers and users, and consider the societal implications of widespread autonomous vehicle adoption. The evolution of these frameworks is crucial for building public trust and facilitating the responsible introduction of autonomous vehicles into society. 

(ix) **Building Public Confidence and Trust**: The trajectory of autonomous driving technologies towards mainstream acceptance is contingent upon building a foundation of public confidence and trust. This process involves not just demonstrating the capabilities of such systems, but also actively engaging in transparent discussions about their limitations and the measures in place to address them. It is essential that the public is wellinformed about how autonomous vehicles work, the benefits they offer, and the safety protocols they follow. Moreover, rigorous testing and validation must be communicated and observed, with a clear emphasis on the meticulousness of safety standards. Public policy debates and educational initiatives can play a pivotal role in demystifying the technology, addressing concerns, and shaping a positive public perception. By fostering an environment where the dialogue between technology providers, regulators, and the public is open and ongoing, there can be a gradual building of trust which is critical for the successful integration of autonomous driving into societal norms and daily routines. 

## 9. **Conclusions**

The evolution of autonomous driving technology signifies a transformative juncture in transportation history and societal norms. This survey methodically examines the foundations of autonomous driving, covering system design methodologies, environmental perception, localization, path planning and decision-making. In terms of environmental perception, we underscore the pivotal role of sensors—such as cameras, Lidar, and radar—in object detection and semantic segmentation. The survey also navigates through the inherent challenges and opportunities in these areas, shedding light on various localization and mapping strategies, particularly emphasizing SLAM variations. Our exploration of motion planning and decision-making underscores key components, including trajectory forecasting, decision-making protocols, and behavioral regulation. In conclusion, we outline the prospective future trajectories and opportunities in the autonomous driving landscape, underscoring its potential to redefine transport. Autonomous driving represents more than just a technological leap; it marks a fundamental shift in our understanding of mobility. Our aspiration is that this detailed, comprehensive survey provides an overview of autonomous vehicle technology for researchers, industry frontrunners, and all stakeholders in the autonomous driving sector, towards the development of safer, more intelligent, and efficient transportation systems. 

## Competing Interests The Authors Declare No Competing Interests. Credit Authorship Contribution Statement

Jingyuan Zhao: Conceptualization, Methodology, Formal analysis, Investigation, Writing - original draft, Writing - review & editing, Project administration, Funding acquisition, Supervision. **Wenyi Zhao:** 
Methodology, Formal analysis, Investigation, Writing - original draft. 

Bo Deng: Methodology, Formal analysis, Investigation. **Zhenghong** Wang: Formal analysis, Investigation, Visualization. **Feng Zhang:** 
Methodology, Investigation. **Wenxiang Zheng:** Methodology, Investigation. **Wanke Cao:** Project administration, Supervision. **Jinrui Nan:** 
Project administration, Funding acquisition, Supervision. **Yubo Lian:** 
Project administration, Resources. **Andrew F. Burke:** Writing - review 
& editing. 

## Declaration Of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## Data Availability

No data was used for the research described in the article. 

## Acknowledgements

This research was supported by the Key Research and Development Program of Shanxi Province, China under Grant No. 202202070301005. 

## References

Abbeel, P., Quigley, M., & Ng, A. Y. (2006, June). Using inaccurate models in reinforcement learning. Proceedings of the 23rd international conference on Machine learning, Pittsburgh, Pennsylvania, USA. 

Almalioglu, Y., Turan, M., Trigoni, N., & Markham, A. (2022). Deep learning-based robust positioning for all-weather autonomous driving. Nature Machine Intelligence, 4, 749–760. https://doi.org/10.1038/s42256-022-00520-5 Aradi, S. (2020). Survey of deep reinforcement learning for motion planning of autonomous vehicles. *IEEE Transactions on Intelligent Transportation Systems, 23*, 
740–759. https://doi.org/10.1109/TITS.2020.3024655 Bachute, M. R., & Subhedar, J. M. (2021). Autonomous driving architectures: Insights of machine learning and deep learning algorithms. *Machine Learning with Applications,* 6, Article 100164. https://doi.org/10.1016/j.mlwa.2021.100164 Badrinarayanan, V., Kendall, A., & Cipolla, R. (2017). Segnet: A deep convolutional encoder-decoder architecture for image segmentation. IEEE Transactions on Pattern 
Analysis Machine Intelligence, 39, 2481–2495. https://doi.org/10.1109/ 
TPAMI.2016.2644615 Badue, C., Guidolini, R., Carneiro, R. V., Azevedo, P., Cardoso, V. B., Forechi, A., … 
Mutz, F. (2021). Self-driving cars: A survey. *Expert Systems with Applications, 165*, 
Article 113816. https://doi.org/10.1016/j.eswa.2020.113816 Baruch, J. (2016). Steer driverless cars towards full automation. *Nature, 536*, 127. 

https://doi.org/10.1038/536127a Beard, J. J., & Baheri, A. (2022). Black-Box Safety Validation of Autonomous Systems: A 
Multi-Fidelity Reinforcement Learning Approach. *arXiv preprint arXiv:2203.03451,* 
https://doi.org/10.48550/arXiv.2203.03451. 

Bertozzi, M., Broggi, A., & Fascioli, A. (2006). VisLab and the evolution of vision-based UGVs. *Computer, 39*, 31–38. https://doi.org/10.1109/MC.2006.448 Bescos, B., Campos, C., Tardos, ´ J. D., & Neira, J. (2021). DynaSLAM II: Tightly-coupled multi-object tracking and SLAM. *IEEE Robotics Automation Letters, 6*, 5191–5198. 

https://doi.org/10.1109/LRA.2021.3068640 Bhalla, S., Ganapathi Subramanian, S., & Crowley, M. (2020, May). Deep multi agent reinforcement learning for autonomous driving. Canadian Conference on Artificial Intelligence, Ottawa, ON, Canada. 

Cai, P., Sun, Y., Chen, Y., & Liu, M. (2019, October). Vision-based trajectory planning via imitation learning for autonomous vehicles. 2019 IEEE Intelligent Transportation Systems Conference (ITSC), Auckland, New Zealand. 

Campos, C., Elvira, R., Rodríguez, J. J. G., Montiel, J. M., & Tardos, ´ J. D. (2021). Orbslam3: An accurate open-source library for visual, visual–inertial, and multimap slam. *IEEE Transactions on Robotics, 37*, 1874–1890. https://doi.org/10.1109/ 
TRO.2021.3075644 Charbuty, B., & Abdulazeez, A. (2021). Classification based on decision tree algorithm for machine learning. *Journal of Applied Science Technology Trends, 2*, 20–28. https:// 
doi.org/10.38094/jastt20165 Chen, D., Koltun, V., & Kr¨ahenbühl, P. (2021, October). Learning to drive from a world on rails. Proceedings of the IEEE/CVF International Conference on Computer Vision, Montreal, QC, Canada. 

Chen, L.-C., Papandreou, G., Kokkinos, I., Murphy, K., & Yuille, A. L. (2017). Deeplab: 
Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected crfs. *IEEE Transactions on Pattern Analysis Machine Intelligence, 40*, 
834–848. https://doi.org/10.48550/arXiv.1606.02147 Chen, L., Lu, K., Rajeswaran, A., Lee, K., Grover, A., Laskin, M., Abbeel, P., Srinivas, A., & 
Mordatch, I. (2021, December). Decision transformer: Reinforcement learning via sequence modeling. Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, Online. 

Chen, Y., Zha, J., & Wang, J. (2019). An autonomous T-intersection driving strategy considering oncoming vehicles based on connected vehicle technology. IEEE/ASME 
Transactions on Mechatronics, 24, 2779–2790. https://doi.org/10.1109/ 
TMECH.2019.2942769 Chitta, K., Prakash, A., & Geiger, A. (2021, October). Neat: Neural attention fields for end-to-end autonomous driving. Proceedings of the IEEE/CVF International Conference on Computer Vision, Montreal, QC, Canada. 

Claussmann, L., Revilloud, M., Glaser, S., & Gruyer, D. (2017, October). A study on albased approaches for high-level decision making in highway autonomous driving. 

2017 IEEE international conference on systems, man, and cybernetics (SMC), Banff, AB, Canada. 

Codevilla, F., Müller, M., Lopez, ´ A., Koltun, V., Dosovitskiy, A., & 2018, May). End-to-end driving via conditional imitation learning.. (2018). IEEE international conference on robotics and automation (ICRA). QLD, Australia: Brisbane. 

Cubuktepe, M., Jansen, N., Junges, S., Marandi, A., Suilen, M., & Topcu, U. (2021, February). Robust finite-state controllers for uncertain POMDPs. Proceedings of the AAAI Conference on Artificial Intelligence, Online. 

CVAT. (2023). Retrieved from https://www.cvat.ai/. Accessed July 6, 2023. 

Daniel, K., Nash, A., Koenig, S., & Felner, A. (2010). Theta*: Any-angle path planning on grids. *Journal of Artificial Intelligence Research, 39*, 533–579. https://doi.org/ 
10.1613/jair.2994 Deisenroth, M., & Rasmussen, C. E. (2011, June-July). PILCO: A model-based and dataefficient approach to policy search. Proceedings of the 28th International Conference on machine learning (ICML-11), Bellevue, Washington, USA. 

Deschaud, J.-E. (2018, May). IMLS-SLAM: Scan-to-model matching based on 3D data. 

2018 IEEE International Conference on Robotics and Automation (ICRA), Brisbane, QLD, Australia. 

Dub´e, R., Cramariuc, A., Dugas, D., Nieto, J., Siegwart, R., & Cadena, C. (2018). SegMap: 
3d segment mapping using data-driven descriptors. *arXiv preprint arXiv:1804.09557,* 
https://doi.org/10.48550/arXiv.1804.09557. 

Dub´e, R., Dugas, D., Stumm, E., Nieto, J., Siegwart, R., & Cadena, C. (2017, May). 

Segmatch: Segment based place recognition in 3d point clouds. 2017 IEEE International Conference on Robotics and Automation (ICRA), Singapore. 

Dub´e, R., Gollub, M. G., Sommer, H., Gilitschenski, I., Siegwart, R., Cadena, C., & 
Nieto, J. (2018). Incremental-segment-based localization in 3-d point clouds. IEEE 
Robotics Automation Letters, 3, 1832–1839. https://doi.org/10.1109/ 
LRA.2018.2803213 Encord. (2023). Retrieved from https://encord.com/annotate/. Accessed July 6, 2023. 

Engel, J., Schops, ¨ T., & Cremers, D. (2014, September). LSD-SLAM: Large-scale direct monocular SLAM. European conference on computer vision. 

Everett, M., Chen, Y. F., & How, J. P. (2018, October). Motion planning among dynamic, decision-making agents with deep reinforcement learning. 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Madrid, Spain. 

Feng, S., Sun, H., Yan, X., Zhu, H., Zou, Z., Shen, S., & Liu, H. X. (2023). Dense reinforcement learning for safety validation of autonomous vehicles. *Nature, 615*, 
620–627. https://doi.org/10.1038/s41586-023-05732-2 Fernando, T., Denman, S., Sridharan, S., & Fookes, C. (2018a, December). Gd-gan: 
Generative adversarial networks for trajectory prediction and group detection in crowds. Computer Vision–ACCV 2018: 14th Asian Conference on Computer Vision, Perth, Australia, December 2–6, 2018, Revised Selected Papers, Part I 14, Perth, Australia. 

Fernando, T., Denman, S., Sridharan, S., & Fookes, C. (2018). Soft+ hardwired attention: 
An lstm framework for human trajectory prediction and abnormal event detection. 

Neural Networks, 108, 466–478. https://doi.org/10.1016/j.neunet.2018.09.002 Fernando, T., Denman, S., Sridharan, S., & Fookes, C. (2019, October). Neighbourhood context embeddings in deep inverse reinforcement learning for predicting pedestrian motion over long time horizons. Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops, Seoul, Korea (South). 

Fernando, T., Denman, S., Sridharan, S., & Fookes, C. (2020). Deep inverse reinforcement learning for behavior prediction in autonomous driving: Accurate forecasts of vehicle motion. *IEEE Signal Processing Magazine, 38*, 87–96. https://doi.org/ 
10.1109/MSP.2020.2988287 Forster, C., Pizzoli, M., & Scaramuzza, D. (2014, May). SVO: Fast semi-direct monocular visual odometry. 2014 IEEE international conference on robotics and automation (ICRA), Hong Kong, China. 

Fujimoto, S., Meger, D., & Precup, D. (2019, June). Off-policy deep reinforcement learning without exploration. International conference on machine learning, Long Beach, California, USA. 

Gao, H., Shi, G., Xie, G., & Cheng, B. (2018). Car-following method based on inverse reinforcement learning for autonomous vehicle decision-making. International Journal of Advanced Robotic Systems, 15, 1729881418817162. https://doi.org/ 10.1177/1729881418817162. 

George, L., Buhet, T., Wirbel, E., ´ Le-Gall, G., & Perrotton, X. (2018). Imitation learning for end to end vehicle longitudinal control with forward camera. *arXiv preprint arXiv:* 1812.05841, https://doi.org/10.48550/arXiv.1812.05841. 

Ghahramani, Z. (2015). Probabilistic machine learning and artificial intelligence. Nature, 521, 452–459. https://doi.org/10.1038/nature14541 Girshick, R., Donahue, J., Darrell, T., & Malik, J. (2015). Region-based convolutional networks for accurate object detection and segmentation. *IEEE Transactions on* Pattern Analysis Machine Intelligence, 38, 142–158. https://doi.org/10.1109/ 
TPAMI.2015.2437384 Goli, A., Khademi-Zare, H., Tavakkoli-Moghaddam, R., Sadeghieh, A., Sasanian, M., & 
Malekalipour Kordestanizadeh, R. (2021). An integrated approach based on artificial intelligence and novel meta-heuristic algorithms to predict demand for dairy products: A case study. *Network: Computation in Neural Systems, 32*, 1–35. https:// 
doi.org/10.1080/0954898X.2020.1849841 Greenblatt, N. A. (2016). Self-driving cars and the law. *IEEE Spectrum, 53*, 46–51. https:// 
doi.org/10.1109/MSPEC.2016.7419800 Grigorescu, S., Trasnea, B., Cocias, T., & Macesanu, G. (2020). A survey of deep learning techniques for autonomous driving. *Journal of Field Robotics, 37*, 362–386. https:// 
doi.org/10.1002/rob.21918 Guo, G., & Zhao, S. (2022). 3D multi-object tracking with adaptive cubature Kalman filter for autonomous driving. *IEEE Transactions on Intelligent Vehicles, 8*, 512–519. 

https://doi.org/10.1109/TIV.2022.3158419 Guo, Y., Wang, H., Hu, Q., Liu, H., Liu, L., & Bennamoun, M. (2020). Deep learning for 3d point clouds: A survey. *IEEE Transactions on Pattern Analysis Machine Intelligence, 43*, 
4338–4364. https://doi.org/10.1109/TPAMI.2020.3005434 Gupta, A., Johnson, J., Fei-Fei, L., Savarese, S., & Alahi, A. (2018, June). Social gan: 
Socially acceptable trajectories with generative adversarial networks. Proceedings of the IEEE conference on computer vision and pattern recognition, Salt Lake City, UT, USA. 

Hu, Q., Yang, B., Xie, L., Rosa, S., Guo, Y., Wang, Z., Trigoni, N., & Markham, A. (2020, June). Randla-net: Efficient semantic segmentation of large-scale point clouds. 

Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, Seattle, WA, USA. 

Innocenti, C., Lind´en, H., Panahandeh, G., Svensson, L., Mohammadiha, N., & (2017, October). Imitation learning for vision-based lane keeping assistance.. (2017). IEEE 20th International Conference on Intelligent Transportation Systems (ITSC). Japan: Yokohama. 

International, S. (2023). *SAE Standards News: J3016 automated-driving graphic update*, 
Retrieved from https://www.sae.org/news/2019/01/sae-updates-j3016-automateddriving-graphic. Accessed July 6, 2023. 

Janai, J., Güney, F., Behl, A., & Geiger, A. (2020). Computer vision for autonomous vehicles: 
Problems, datasets and state of the art. Now Foundations and Trends (Chapter 12). 

Janner, M., Li, Q., & Levine, S. (2021, December). Offline reinforcement learning as one big sequence modeling problem. Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, Online. 

Ji, B., Zhang, X., Mumtaz, S., Han, C., Li, C., Wen, H., & Wang, D. (2020). Survey on the internet of vehicles: Network architectures and applications. IEEE Communications Standards Magazine, 4, 34–41. https://doi.org/10.1109/MCOMSTD.001.1900053 Joubert, N., Reid, T. G., & Noble, F. (2020, October). Developments in modern GNSS and its impact on autonomous vehicle architectures. 2020 IEEE Intelligent Vehicles Symposium (IV), Las Vegas, NV, USA. 

Kanai, S., Fujiwara, Y., & Iwamura, S. (2017). Preventing gradient explosions in gated recurrent units. *Advances in Neural Information Processing Systems, 30*. https://doi. org/10.5555/3294771.3294813 Karaman, S., Walter, M. R., Perez, A., Frazzoli, E., & Teller, S. (2011, May). Anytime motion planning using the RRT. 2011 IEEE international conference on robotics and automation, Shanghai, China. 

Kendall, A., Hawke, J., Janz, D., Mazur, P., Reda, D., Allen, J.-M., Lam, V.-D., Bewley, A., 
& Shah, A. (2019, May). Learning to drive in a day. 2019 International Conference on Robotics and Automation (ICRA), Montreal, QC, Canada. 

Kiran, B. R., Sobh, I., Talpaert, V., Mannion, P., Al Sallab, A. A., Yogamani, S., & P´erez, P. 

(2021). Deep reinforcement learning for autonomous driving: A survey. IEEE 
Transactions on Intelligent Transportation Systems, 23, 4909–4926. https://doi.org/ 
10.48550/arXiv.2002.00444 Kohlbrecher, S., Von Stryk, O., Meyer, J., & Klingauf, U. (2011, November). A flexible and scalable SLAM system with full 3D motion estimation. 2011 IEEE international symposium on safety, security, and rescue robotics, Kyoto, Japan. 

Kumar, A., Fu, J., Soh, M., Tucker, G., & Levine, S. (2019). Stabilizing off-policy qlearning via bootstrapping error reduction. Advances in Neural Information Processing Systems, 32. https://doi.org/10.1145/3452296.3472936 Kumar, A., Zhou, A., Tucker, G., & Levine, S. (2020, December). Conservative q-learning for offline reinforcement learning. Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, Online. 

Kumar, S., Parker, J., & Naderian, P. (2020). Adaptive transformers in RL. *arXiv preprint* arXiv:2004.03761, https://doi.org/10.48550/arXiv.2004.03761. 

Labelbox. (2023). Retrieved from https://labelbox.com/. Accessed July 6, 2023. 

Lang, A. H., Vora, S., Caesar, H., Zhou, L., Yang, J., & Beijbom, O. (2019, June). 

Pointpillars: Fast encoders for object detection from point clouds. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, Long Beach, CA, USA. 

LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature, 521*, 436–444. https:// 
doi.org/10.1038/nature14539 Li, J., Zhao, J., Kang, Y., He, X., Ye, C., & Sun, L. (2019, June). Dl-slam: Direct 2.5 d lidar slam for autonomous driving. 2019 IEEE Intelligent Vehicles Symposium (IV), Paris, France. 

Liao, J., Liu, T., Tang, X., Mu, X., Huang, B., & Cao, D. (2020). Decision-making strategy on highway for autonomous vehicles using deep reinforcement learning. *IEEE Access,* 
8, 177804–177814. https://doi.org/10.1109/ACCESS.2020.3022755 Lin, H., Lin, X., Labiod, H., & Chen, L. (2021). Toward multiple-phase MDP model for charging station recommendation. IEEE Transactions on Intelligent Transportation Systems, 23, 10583–10595. https://doi.org/10.1109/TITS.2021.3094926 Liu, W., Anguelov, D., Erhan, D., Szegedy, C., Reed, S., Fu, C.-Y., & Berg, A. C. (2016, October). Ssd: Single shot multibox detector. Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part I 14, Amsterdam, The Netherlands. 

Liu, X., Masoud, N., Zhu, Q., & Khojandi, A. (2022). A markov decision process framework to incorporate network-level data in motion planning for connected and automated vehicles. *Transportation Research Part C: Emerging Technologies, 136*, Article 103550. https://doi.org/10.1016/j.trc.2021.103550 Liu, Z., Zhou, S., Suo, C., Yin, P., Chen, W., Wang, H., Li, H., & Liu, Y.-H. (2019, October). 

Lpd-net: 3d point cloud learning for large-scale place recognition and environment analysis. Proceedings of the IEEE/CVF International Conference on Computer Vision, Seoul, Korea (South). 

Long, J., Shelhamer, E., & Darrell, T. (2015, June). Fully convolutional networks for semantic segmentation. Proceedings of the IEEE conference on computer vision and pattern recognition, Boston, MA, USA. 

Lu, Y., Lu, J., Zhang, S., & Hall, P. (2018). Traffic signal detection and classification in street views using an attention model. *Computational Visual Media, 4*, 253–266. 

https://doi.org/10.1007/s41095-018-0116-x Luque, J., & Straub, D. (2019). Risk-based optimal inspection strategies for structural systems using dynamic Bayesian networks. *Structural Safety, 76*, 68–80. https://doi. org/10.1016/j.strusafe.2018.08.002 Mansour, R. F., Escorcia-Gutierrez, J., Gamarra, M., Villanueva, J. A., & Leal, N. (2021). 

Intelligent video anomaly detection and classification using faster RCNN with deep reinforcement learning model. *Image Vision Computing, 112*, Article 104229. https:// doi.org/10.1016/j.imavis.2021.104229 Maturana, D., & Scherer, S. (2015, September). Voxnet: A 3d convolutional neural network for real-time object recognition. 2015 IEEE/RSJ international conference on intelligent robots and systems (IROS), Hamburg, Germany. 

Mohamed, A., Qian, K., Elhoseiny, M., & Claudel, C. (2020, June). Social-stgcnn: A social spatio-temporal graph convolutional neural network for human trajectory prediction. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, Seattle, WA, USA. 

Mur-Artal, R., & Tardos, ´ J. D. (2017). Orb-slam2: An open-source slam system for monocular, stereo, and rgb-d cameras. *IEEE Transactions on Robotics, 33*, 1255–1262. 

https://doi.org/10.1109/TRO.2017.2705103 Nair, A., Gupta, A., Dalal, M., & Levine, S. (2020). Awac: Accelerating online reinforcement learning with offline datasets. *arXiv preprint arXiv:2006.09359,* 
https://doi.org/10.48550/arXiv.2006.09359. 

Najm, W. G., Smith, J. D., & Yanagisawa, M. (2007). *Pre-crash scenario typology for crash* avoidance research. United States: National Highway Traffic Safety Administration. 

Nunes, A., & Axhausen, K. W. (2021). Road safety, health inequity and the imminence of autonomous vehicles. *Nature Machine Intelligence, 3*, 654–655. https://doi.org/ 
10.1038/s42256-021-00382-3 Oliveira, G. L., Radwan, N., Burgard, W., & Brox, T. (2020, November). Topometric localization with deep learning. Robotics Research: The 18th International Symposium ISRR. 

Osaba, E., Villar-Rodriguez, E., Del Ser, J., Nebro, A. J., Molina, D., LaTorre, A., … 
Herrera, F. (2021). A tutorial on the design, experimentation and application of metaheuristic algorithms to real-world optimization problems. Swarm Evolutionary Computation, 64, Article 100888. https://doi.org/10.1016/j.swevo.2021.100888 Osman, O. A., Hajij, M., Bakhit, P. R., & Ishak, S. (2019). Prediction of near-crashes from observed vehicle kinematics using machine learning. Transportation Research Record, 2673, 463–473. https://doi.org/10.1177/0361198119862629 Palanisamy, P. (2020, July). Multi-agent connected autonomous driving using deep reinforcement learning. 2020 International Joint Conference on Neural Networks 
(IJCNN), Glasgow, UK. 

Parisotto, E., Song, F., Rae, J., Pascanu, R., Gulcehre, C., Jayakumar, S., Jaderberg, M., 
Kaufman, R. L., Clark, A., & Noury, S. (2020, July). Stabilizing transformers for reinforcement learning. International conference on machine learning, Vienna, AUSTRIA. 

Paszke, A., Chaurasia, A., Kim, S., & Culurciello, E. (2016). Enet: A deep neural network architecture for real-time semantic segmentation. *arXiv preprint arXiv:1606.02147,* 
https://arxiv.org/abs/1606.02147\#:~:text=https%3A//doi.org/10.48550/ 
arXiv.1606.02147. 

Petrovich, M., Black, M. J., & Varol, G. (2021, October). Action-conditioned 3D human motion synthesis with transformer VAE. Proceedings of the IEEE/CVF International Conference on Computer Vision, Montreal, QC, Canada. 

Pomerleau, D. A. (1988). Alvinn: An autonomous land vehicle in a neural network. 

Advances in neural information processing systems, 1. 

Prakash, A., Chitta, K., & Geiger, A. (2021, June). Multi-modal fusion transformer for end-to-end autonomous driving. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Nashville, TN, USA. 

Prudencio, R. F., Maximo, M. R., & Colombini, E. L. (2023). A survey on offline reinforcement learning: Taxonomy, review, and open problems. arXiv preprint arXiv: 
2203.01387, https://doi.org/10.48550/arXiv.2203.01387. 

Ravindran, R., Santora, M. J., & Jamali, M. M. (2020). Multi-object detection and tracking, based on DNN, for autonomous vehicles: A review. *IEEE Sensors Journal, 21*, 5668–5677. https://doi.org/10.1109/JSEN.2020.3041615 Ren, S., He, K., Girshick, R., & Sun, J. (2015). Faster r-cnn: Towards real-time object detection with region proposal networks. *Advances in Neural Information Processing* Systems, 28. https://doi.org/10.1109/TPAMI.2016.2577031 research, C. O.-s. s. f. a. d. (2023). Retrieved from https://carla.org/. Accessed July, 6, 2023. 

Rhinehart, N., McAllister, R., Kitani, K., & Levine, S. (2019, October-November). Precog: 
Prediction conditioned on goals in visual multi-agent settings. Proceedings of the IEEE/CVF International Conference on Computer Vision, Seoul, Korea (South). 

Rhinehart, N., McAllister, R., & Levine, S. (2018). Deep imitative models for flexible inference, planning, and control. *arXiv preprint arXiv:1810.06544,* https://doi.org/ 10.48550/arXiv.1810.06544. 

Roboflow. (2023). Retrieved from https://roboflow.com/. Accessed July 6, 2023. 

Rosique, F., Navarro, P. J., Fernandez, ´ C., & Padilla, A. (2019). A systematic review of perception system and simulators for autonomous vehicles research. *Sensors, 19*, 648. https://doi.org/10.3390/s19030648 Schops, T., Sattler, T., & Pollefeys, M. (2019, June). Bad slam: Bundle adjusted direct rgb-d slam. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Long Beach, CA, USA. 

Shan, T., & Englot, B. (2018, October). Lego-loam: Lightweight and ground-optimized lidar odometry and mapping on variable terrain. 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Madrid, Spain. 

Shenoi, A., Patel, M., Gwak, J., Goebel, P., Sadeghian, A., Rezatofighi, H., Martin-Martin, R., & Savarese, S. (2020, October). Jrmot: A real-time 3d multi-object tracker and a new large-scale dataset. 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Las Vegas, NV, USA. 

Shi, S., Wang, X., & Li, H. (2019, June). Pointrcnn: 3d object proposal generation and detection from point cloud. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, Beach, CA, USA. 

Simony, M., Milzy, S., Amendey, K., & Gross, H.-M. (2018, September). Complex-yolo: 
An euler-region-proposal for real-time 3d object detection on point clouds. 

Proceedings of the European conference on computer vision (ECCV) workshops, Munich, Germany. 

Singh, A., Yu, A., Yang, J., Zhang, J., Kumar, A., & Levine, S. (2020). Cog: Connecting new skills to past experience with offline reinforcement learning. arXiv preprint arXiv: 2010.14500, https://doi.org/10.48550/arXiv.2010.14500. 

Singh, G., Peri, S., Kim, J., Kim, H., & Ahn, S. (2021, July). Structured world belief for reinforcement learning in pomdp. International Conference on Machine Learning, Online. 

Song, C., Zhang, C., Shafieezadeh, A., & Xiao, R. (2022). Value of information analysis in non-stationary stochastic decision environments: A reliability-assisted POMDP approach. *Reliability Engineering System Safety, 217*, Article 108034. https://doi.org/ 10.1016/j.ress.2021.108034 Sun, C.-Z., Zhang, B., Wang, J.-K., & Zhang, C.-S. (2021, June). A review of visual SLAM 
based on unmanned systems. 2021 2nd International Conference on Artificial Intelligence and Education (ICAIE), Dali, China. 

Sutton, C., & McCallum, A. (2012). An introduction to conditional random fields. 

Foundations and Trends® *in Machine Learning, 4*, 267-373. https://doi.org/10.1561/ 
2200000013. 

Tampuu, A., Matiisen, T., Semikin, M., Fishman, D., & Muhammad, N. (2020). A survey of end-to-end driving: Architectures and training methods. IEEE Transactions on Neural Networks and Learning Systems, 33, 1364–1384. https://doi.org/10.1109/ 
TNNLS.2020.3043505 Tang, T. Y., Yoon, D. J., Pomerleau, F., & Barfoot, T. D. (2018, May). Learning a bias correction for lidar-only motion estimation. 2018 15th Conference on Computer and Robot Vision (CRV), Toronto, ON, Canada. 

Tateno, K., Tombari, F., Laina, I., & Navab, N. (2017, July). Cnn-slam: Real-time dense monocular slam with learned depth prediction. Proceedings of the IEEE conference on computer vision and pattern recognition, Honolulu, HI, USA. 

Teed, Z., & Deng, J. (2021, December). Droid-slam: Deep visual slam for monocular, stereo, and rgb-d cameras. 35th Conference on Neural Information Processing Systems, NeurIPS 2021, Online. 

Thomas, H., Qi, C. R., Deschaud, J.-E., Marcotegui, B., Goulette, F., & Guibas, L. J. (2019, October). Kpconv: Flexible and deformable convolution for point clouds. 

Proceedings of the IEEE/CVF international conference on computer vision, Seoul, Korea (South). 

Thorpe, C., Hebert, M. H., Kanade, T., & Shafer, S. A. (1988). Vision and navigation for the Carnegie-Mellon Navlab. IEEE Transactions on Pattern Analysis Machine Intelligence, 10, 362–373. https://doi.org/10.1109/34.3900 Tkatek, S., Bahti, O., Lmzouari, Y., & Abouchabaka, J. (2020). Artificial intelligence for improving the optimization of NP-hard problems: a review. *International Journal of* Advanced Trends Computer Science, 9, https://doi.org/10.30534/ijatcse/2020/ 73952020. 

Toromanoff, M., Wirbel, E., & Moutarde, F. (2020, Jun). End-to-end model-free reinforcement learning for urban driving using implicit affordances. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, Seattle, United States. 

Vallon, C., Ercan, Z., Carvalho, A., & Borrelli, F. (2017, June). A machine learning approach for personalized autonomous lane change initiation and control. 2017 IEEE Intelligent vehicles symposium (IV), Los Angeles, CA, USA. 

Van Brummelen, J., O'Brien, M., Gruyer, D., & Najjaran, H. (2018). Autonomous vehicle perception: The technology of today and tomorrow. Transportation Research Part C: 
Emerging Technologies, 89, 384–406. https://doi.org/10.1016/j.trc.2018.02.012 Vemulapalli, R., Tuzel, O., Liu, M.-Y., & Chellapa, R. (2016, June). Gaussian conditional random field network for semantic segmentation. Proceedings of the IEEE conference on computer vision and pattern recognition, Las Vegas, NV, USA. 

Vespa, E., Nikolov, N., Grimm, M., Nardi, L., Kelly, P. H., & Leutenegger, S. (2018). 

Efficient octree-based volumetric SLAM supporting signed-distance and occupancy mapping. *IEEE Robotics Automation Letters, 3*, 1144–1151. https://doi.org/10.1109/ 
LRA.2018.2792537 Visin, F., Ciccone, M., Romero, A., Kastner, K., Cho, K., Bengio, Y., Matteucci, M., & 
Courville, A. (2016, June-July). Reseg: A recurrent neural network-based model for semantic segmentation. Proceedings of the IEEE conference on computer vision and pattern recognition workshops, Las Vegas, NV, USA. 

Von Stumberg, L., & Cremers, D. (2022). Dm-vio: Delayed marginalization visual-inertial odometry. *IEEE Robotics Automation Letters, 7*, 1408–1415. https://doi.org/10.1109/ 
LRA.2021.3140129 VOSviewer. (2023). *Visualizing scientific landscapes*, Retrieved from Accessed July 6, 2023. 

Wachi, A. (2019). Failure-scenario maker for rule-based agent using multi-agent adversarial reinforcement learning and its application to autonomous driving. arXiv preprint arXiv:1903.10654, https://doi.org/10.48550/arXiv.1903.10654. 

Wang, C., Delport, J., & Wang, Y. (2019). Lateral motion prediction of on-road preceding vehicles: A data-driven approach. *Sensors, 19*, 2111. https://doi.org/10.3390/ s19092111 Wang, H., Xu, H., Zhao, C., & Liu, Y. (2021, October). KC-PointNet: attentional network for 3D point cloud processing. 2021 China Automation Congress (CAC), Beijing, China. 

Wang, Z., Zheng, L., Liu, Y., Li, Y., & Wang, S. (2020, August). Towards real-time multiobject tracking. European Conference on Computer Vision, Glasgow, UK. 

Weng, X., Wang, J., Held, D., & Kitani, K. (2020). Ab3dmot: A baseline for 3d multiobject tracking and new evaluation metrics. *arXiv preprint arXiv:2008.08063,* https:// 
doi.org/10.48550/arXiv.2008.08063. 

Xia, Y., Qu, S., Goudos, S., Bai, Y., & Wan, S. (2021). Multi-object tracking by mutual supervision of CNN and particle filter. *Personal Ubiquitous Computing, 1–10*. https:// 
doi.org/10.1007/s00779-019-01278-1 Xiang, Y., Alahi, A., & Savarese, S. (2015, December). Learning to track: Online multiobject tracking by decision making. Proceedings of the IEEE international conference on computer vision, Santiago, Chile. 

Xiao, Y., Codevilla, F., Gurram, A., Urfalioglu, O., & Lopez, ´ A. M. (2020). Multimodal end-to-end autonomous driving. IEEE Transactions on Intelligent Transportation Systems, 23, 537–547. https://doi.org/10.1109/TITS.2020.3013234 Xie, W., Ide, J., Izadi, D., Banger, S., Walker, T., Ceresani, R., Spagnuolo, D., Guagliano, C., Diaz, H., & Twedt, J. (2021, September). Multi-object tracking with deep learning ensemble for unmanned aerial system applications. Artificial Intelligence and Machine Learning in Defense Applications III, Online. 

Xin, X., Jia, N., Ling, S., & He, Z. (2022). Prediction of pedestrians' wait-or-go decision using trajectory data based on gradient boosting decision tree. Transportmetrica B: 
Transport Dynamics, 10, 693–717. https://doi.org/10.1080/ 
21680566.2022.2027294 Xu, H., Gao, Y., Yu, F., & Darrell, T. (2017, July). End-to-end learning of driving models from large-scale video datasets. Proceedings of the IEEE conference on computer vision and pattern recognition, Honolulu, HI, USA. 

Xu, Q., Sun, X., Wu, C.-Y., Wang, P., & Neumann, U. (2020, June). Grid-gcn for fast and scalable point cloud learning. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Seattle, WA, USA. 

Yang, S., & Scherer, S. (2019). Cubeslam: Monocular 3-d object slam. IEEE Transactions on Robotics, 35, 925–938. https://doi.org/10.1109/TRO.2019.2909168 Ye, M., Cao, T., & Chen, Q. (2021, June). Tpcn: Temporal point cloud networks for motion forecasting. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Nashville, TN, USA. 

Yu, C., Wang, X., Xu, X., Zhang, M., Ge, H., Ren, J., … Tan, G. (2019). Distributed multiagent coordinated learning for autonomous driving in highways based on dynamic coordination graphs. IEEE Transactions on Intelligent Transportation Systems, 21, 735–748. https://doi.org/10.1109/TITS.2019.2893683 Yu, F., & Koltun, V. (2015). Multi-scale context aggregation by dilated convolutions. 

arXiv preprint arXiv:1511.07122, https://doi.org/10.48550/arXiv.1511.07122. 

Yu, T., Kumar, A., Rafailov, R., Rajeswaran, A., Levine, S., & Finn, C. (2021, December). 

Combo: Conservative offline model-based policy optimization. Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, Online. 

Yu, Y., Si, X., Hu, C., & Zhang, J. (2019). A review of recurrent neural networks: LSTM 
cells and network architectures. *Neural Computation, 31*, 1235–1270. https://doi. 

org/10.1162/neco_a_01199 Zarzar, J., Giancola, S., & Ghanem, B. (2019). PointRGCN: Graph convolution networks for 3D vehicles detection refinement. *arXiv preprint arXiv:1911.12236,* https://doi. org/10.48550/arXiv.1911.12236. 

Zhang, G., Pan, Y., & Zhang, L. (2021). Semi-supervised learning with GAN for automatic defect detection from images. *Automation in Construction, 128*, Article 103764. https://doi.org/10.1109/TIM.2021.3087826 Zhang, S., Tong, H., Xu, J., & Maciejewski, R. (2019). Graph convolutional networks: A 
comprehensive review. *Computational Social Networks, 6*, 1–23. https://doi.org/ 
10.1186/s40649-019-0069-y Zhang, T., Song, W., Fu, M., Yang, Y., Tian, X., & Wang, M. (2021). A unified framework integrating decision making and trajectory planning based on spatio-temporal voxels for highway autonomous driving. IEEE Transactions on Intelligent Transportation Systems, 23, 10365–10379. https://doi.org/10.1109/TITS.2021.3093548 Zhang, Y., Zhou, Z., David, P., Yue, X., Xi, Z., Gong, B., & Foroosh, H. (2020, June). 

Polarnet: An improved grid representation for online lidar point clouds semantic segmentation. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Seattle, WA, USA. 

Zhou, J., Cui, G., Hu, S., Zhang, Z., Yang, C., Liu, Z., … Sun, M. (2020). Graph neural networks: A review of methods and applications. *AI Open, 1*, 57–81. https://doi.org/ 
10.1016/j.aiopen.2021.01.001 Zhou, Y., & Tuzel, O. (2018, June). Voxelnet: End-to-end learning for point cloud based 3d object detection. Proceedings of the IEEE conference on computer vision and pattern recognition, Salt Lake City, UT, USA. 

Zubizarreta, J., Aguinaga, I., & Montiel, J. M. M. (2020). Direct sparse mapping. IEEE 
Transactions on Robotics, 36, 1363–1370. https://doi.org/10.1109/ 
TRO.2020.2991614 Zuo, X., Geneva, P., Lee, W., Liu, Y., & Huang, G. (2019, November). Lic-fusion: Lidarinertial-camera odometry. 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Macau, China. 