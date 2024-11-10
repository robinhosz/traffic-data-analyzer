# 🚦 **Urban Traffic Optimization with Reinforcement Learning** 🚗

This repository presents a project for **urban traffic signal optimization** using **Reinforcement Learning (RL)** to improve traffic flow, increase safety at intersections, and promote energy efficiency in cities. Using the "Traffic Volume Counts" dataset from Kaggle, the simulation aims to adjust traffic signals based on traffic volume to reduce congestion and waiting times.

---

## 📋 **Table of Contents**

1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Simulation Goal](#simulation-goal)
4. [Technologies Used](#technologies-used)
5. [Dataset](#dataset)
6. [How to Run the Project](#how-to-run-the-project)
7. [Expected Results](#expected-results)
8. [Contributions](#contributions)
9. [License](#license)

---

## 🚀 **Overview**

This project applies **artificial intelligence** to optimize **traffic signal control**, using **reinforcement learning** to adjust the timing of each signal based on real-time traffic conditions. The system continuously learns from traffic data, adjusting its actions to improve flow and reduce waiting times.

---

## 🤖 **How It Works**

The project simulates the behavior of a **traffic signal system** at different urban locations. Reinforcement learning is used to adjust the signal timings based on the following criteria:

- **Actions**: Adjusting the traffic signals (Green, Yellow, Red).
- **Rewards**: Given based on the effectiveness of the decisions, considering reduced congestion and improved traffic flow.
- **State**: The system observes real-time traffic volume to make decisions.

---

## 🎯 **Simulation Goal**

The primary goal of this project is to reduce congestion and optimize waiting times at intersections. The simulation uses reinforcement learning to adjust the signal durations and improve traffic efficiency based on observed conditions.

---

## 🛠 **Technologies Used**

- **Python**: The main language for developing the simulation.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For mathematical calculations and operations.
- **ReportLab**: For generating PDF reports.
- **Kaggle**: Source of the traffic volume dataset.

---

## 📊 **Dataset**

This project uses the **"Traffic Volume Counts"** dataset from Kaggle. The dataset includes detailed information about traffic volume at various intersections in New York, including:

- Vehicle count per hour and location.
- Weather data and special events.
- Historical congestion data.

You can access the full dataset [here](https://www.kaggle.com/datasets/aadimator/nyc-automated-traffic-volume-counts/data).

---

## 🚀 **How to Run the Project**

### Prerequisites

Before running the project, make sure you have Python 3.6+ installed and the project dependencies:

```bash
pip install pandas numpy reportlab
```

### Running the Simulation
- Download the Automated_Traffic_Volume_Counts.csv file from Kaggle and place it in the same folder as the script.
- Run the Python script to start the simulation and generate a PDF report with the results:
```bash
python traffic_simulation.py
```
The script will generate a PDF file named traffic_report.pdf with a summary and details of the simulation steps.

## 📈 **Expected Results**

The simulation aims to optimize the signal timings and improve the following aspects:

- **Traffic Flow**: Reducing average waiting time at intersections.
- **Safety**: Fewer accidents at traffic lights.
- **Energy Efficiency**: Lower fuel consumption with fewer stops and starts.

---

## 🤝 **Contributions**

Contributions are welcome! If you’d like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   git commit -am 'Adding new feature'
   git push origin feature-name
   ```
## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
