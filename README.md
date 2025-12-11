# Autonomous Spacecraft Safety

**this is an ever work in progress**

## Introduction
Autonomous Spacecraft Safety, or ASS for short, is a study created to developed to control spacecrafts autonomously. Safely.
The project is a combination of image processing and AI.

## Key Features
- **Edge Detection**: Compares the utilization of Canny, Laplacian of Gaussian and Sobel algorithms to detect object boundaries, differentiating obstacles from the space background.
- **Object Detection and Classification**: Employs Convolutional Neural Networks (CNNs) to classify objects based on shape, size, and velocity.
- **Optical Flow**: Analyzes pixel movement across sequential images to track debris motion, predicting future paths.

## Artificial Intelligence Approaches
- **Convolutional Neural Networks (CNNs)**: High accuracy and speed in classifying space debris.
- **Recurrent Neural Networks (RNNs)**: Predict future positions of debris based on current trajectories.
- **Reinforcement Learning (RL)**: Optimal avoidance strategies through simulation of various scenarios, enhancing energy-efficient and safe maneuvers.

## Redundancy and Failure Handling
To ensure robustness, the system incorporates a fault-tolerant control strategy that adjusts movements based on operational thrusters. AI models trained with simulated failures ensure that the spacecraft can safely maneuver even with partial system failures.

## Comparison of Approaches
| Method                  |
|-------------------------|
| DCAS (Radar-based)      |
| AI + Image Processing   |
| Lidar-based             |

## Simulation and Testing
Validation of the proposed system is conducted through simulations using OpenCV for real-time image processing and TensorFlow for AI modeling. A test environment in Gazebo simulates various debris fields, spacecraft trajectories, and failure modes.

### Planned Simulation Details
- Varying densities and velocities of debris.
- Measurements of response time, energy efficiency, and collision avoidance accuracy.
- Redundancy tests by disabling thrusters and sensors to observe AI adaptation.

## References
- [ESA Space Debris Office](https://www.esa.int/Enabling_Support/Operations/Ground_Systems_Engineering/ESA_Space_Debris_Office)
- [Phys.org: Algorithms for Autonomous Spacecraft Safety](https://phys.org/news/2024-08-algorithms-autonomous-spacecraft-safety.html)
- [Science.org: SciRobotics](https://www.science.org/doi/10.1126/scirobotics.adn4722)

