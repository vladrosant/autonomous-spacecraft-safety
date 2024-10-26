# Spacecraft Autonomous Debris Avoidance System

**Author**: Pedro H. F. Santana  
**Institution**: Universidade Paulista  
**Date**: 07/11/2024

## Introduction
As space exploration and travel rise, there is a growing need for advanced, efficient, and foolproof software to enhance the safety of both manned and unmanned missions. Existing Debris Collision Avoidance Systems (DCAS) have limitations that need to be addressed for future missions, ranging from simple orbiting satellites to Lunar or Martian expeditions.

This project explores the combination of image processing and artificial intelligence (AI) to develop a real-time, autonomous debris avoidance system for spacecraft. Unlike traditional reactive systems that depend on Earth-based interventions, our approach leverages onboard AI to process visual data, make predictive decisions, and autonomously adjust the spacecraft's trajectory.

## Key Features
- **Edge Detection**: Utilizes Canny or Sobel algorithms to detect object boundaries, differentiating debris from the space background.
- **Object Detection and Classification**: Employs Convolutional Neural Networks (CNNs) to classify objects based on shape, size, and velocity.
- **Optical Flow**: Analyzes pixel movement across sequential images to track debris motion, predicting future paths.

## Artificial Intelligence Approaches
- **Convolutional Neural Networks (CNNs)**: High accuracy and speed in classifying space debris.
- **Recurrent Neural Networks (RNNs)**: Predict future positions of debris based on current trajectories.
- **Reinforcement Learning (RL)**: Optimal avoidance strategies through simulation of various scenarios, enhancing energy-efficient and safe maneuvers.

## Redundancy and Failure Handling
To ensure robustness, the system incorporates a fault-tolerant control strategy that adjusts movements based on operational thrusters. AI models trained with simulated failures ensure that the spacecraft can safely maneuver even with partial system failures.

## Comparison of Approaches
| Method                  | Advantages                                  | Disadvantages                     |
|-------------------------|---------------------------------------------|-----------------------------------|
| DCAS (Radar-based)      | Real-time updates for larger debris         | Requires Earth-based intervention |
| AI + Image Processing   | Autonomous operation, tracks all sizes      | Computationally intensive onboard |
| Lidar-based             | Works in low-light or obscured environments | Expensive and complex             |

## Simulation and Testing
Validation of the proposed system is conducted through simulations using OpenCV for real-time image processing and TensorFlow for AI modeling. A test environment in Gazebo simulates various debris fields, spacecraft trajectories, and failure modes.

### Simulation Details
- Varying densities and velocities of debris fields.
- Measurements of response time, energy efficiency, and collision avoidance accuracy.
- Redundancy tests by disabling thrusters and sensors to observe AI adaptation.

## References
- [ESA Space Debris Office](https://www.esa.int/Enabling_Support/Operations/Ground_Systems_Engineering/ESA_Space_Debris_Office)
- [Phys.org: Algorithms for Autonomous Spacecraft Safety](https://phys.org/news/2024-08-algorithms-autonomous-spacecraft-safety.html)
- [Science.org: SciRobotics](https://www.science.org/doi/10.1126/scirobotics.adn4722)

## Repository Structure
`/Spacecraft-Autonomous-Debris-Avoidance-System
│
├── /src
│   ├── image_processing.py
│   ├── ai_models.py
│   ├── simulation.py
│   └── utils.py
│
├── /data
│   ├── training_data/
│   └── test_data/
│
├── /docs
│   └── project_report.pdf
│
└── README.md`

## Installation and Usage
To run the simulations and models, follow these steps:
1. Clone the repository.
2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
3. Execute the main script:
    ```sh
    python src/simulation.py
    ```
