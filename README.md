# Advanced Analytics Python Exercise  
### FH Südwestfalen — Advanced Analytics Course  

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Exercises](https://img.shields.io/badge/Exercises-1--7-green.svg)
![Forecasting](https://img.shields.io/badge/Forecasting-Moving%20Average-orange.svg)
![License](https://img.shields.io/badge/License-Academic-lightgrey.svg)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)

---

# Project Overview

This repository contains Python implementations of Exercises 1–7 from the **Advanced Analytics course at FH Südwestfalen**.

The exercises focus on:

- Data processing
- Demand analysis
- Statistical computation
- Forecasting techniques
- Moving Average demand forecasting

---

# Repository Structure

```mermaid
flowchart TD

A[Repository Root]
B[src folder]
C[data folder]
D[material.xlsx]
E[Exercises 1-7 Python Scripts]
F[Forecasting Implementation]
G[README.md Documentation]

A --> B
A --> C
A --> G

C --> D

B --> E
E --> F
```
---

| Exercise   | Topic                | Description                   |
| ---------- | -------------------- | ----------------------------- |
| Exercise 1 | Data Loading         | Read Excel dataset            |
| Exercise 2 | Data Analysis        | Explore demand structure      |
| Exercise 3 | Statistical Metrics  | Mean, variance, std deviation |
| Exercise 4 | Demand Aggregation   | Total demand per material     |
| Exercise 5 | Period Analysis      | Time-based analysis           |
| Exercise 6 | Demand Visualization | Demand patterns               |
| Exercise 7 | Forecasting          | Moving Average Forecast       |

Moving Average Forecast   
Forecast(t+1) =
(Demand(t) + Demand(t-1) + Demand(t-2)) / 3

```mermaid
flowchart LR

A[Historical Demand]
B[Select Window Size]
C[Calculate Average]
D[Generate Forecast]
E[Store Results]

A --> B
B --> C
C --> D
D --> E
```
# Dataset Description

Dataset file:

[dataset/material.xlsx](https://github.com/nomanmridha/Advanced-Analytics-Python-Exercise/blob/main/dataset/material.xlsx)

Dataset characteristics:

• 1000 materials\
• 32 time periods\
• Historical demand values\
• Structured time series data

This dataset is used to implement forecasting models.

---

# Forecast Preview

Example demand input:

| Period | Demand |
| ------ | ------ |
| 28     | 105    |
| 29     | 110    |
| 30     | 95     |
| 31     | 120    |
| 32     | 115    |

Forecast(33) =
(120 + 115 + 95) / 3

Forecast(33) = 110

| Material | Last Demand | Forecast |
| -------- | ----------- | -------- |
| MAT001   | 115         | 110      |
| MAT002   | 84          | 89       |
| MAT003   | 152         | 147      |

```mermaid
flowchart TD

A[Excel Dataset]
B[Python Script]
C[Data Processing]
D[Moving Average Algorithm]
E[Forecast Output]

A --> B
B --> C
C --> D
D --> E

```

# Technologies Used
| Tool          | Purpose               |
| ------------- | --------------------- |
| Python 3.12   | Programming language  |
| Pandas        | Data processing       |
| NumPy         | Numerical computation |
| Excel Dataset | Input data            |
| GitHub        | Version control       |

# How to run
* Clone Repository
  ```
  git clone https://github.com/nomanmridha/Advanced-Analytics-Python-Exercise.git
  ```

* Navigate
  ```
  cd Advanced-Analytics-Python-Exercise
  ```
* Run Exercise
  ```
  python src/exercise7.py
  ```

---

# Learning Outcomes
This project demonstrates:

  - Data processing using Python
  - Statistical analysis
  - Demand analysis techniques
  - Forecasting implementation
  - Moving average model development
  - Analytical thinking and implementation

# Future Improvements
Potential enhancements:

  - Exponential smoothing
  - ARIMA forecasting
  - Forecast accuracy metrics
  - Visualization dashboard
  - Machine learning forecasting

---

## 👤 Author
**Course:** Advance Analytics (WiSe26)  
**University:** Fachhochschule Südwestfalen  
**Supervisor:** Prof. Dr. Christian Leubner  
**Project Type:** Individual Research Project

![FH Südwestfalen](https://img.shields.io/badge/FH-S%C3%BCdwestfalen-0083CC?style=for-the-badge&logo=university&logoColor=white)
![Research Project](https://img.shields.io/badge/Research-Project-6A1B9A?style=for-the-badge&logo=graduation-cap&logoColor=white)

## 🤝 Connect & Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/md-abdullah-al-noman-333aa4155/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nomanmridha/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:noman.hr.18@gmail.com)
* **University:** FH Südwestfalen – Advanced Analytics

---

📌 *This repository demonstrates how academic projects can be elevated to industry-ready analytics portfolios through strong documentation, business framing, and technical rigor.*
