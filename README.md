# 2025 MCM/ICM Problem B - Juneau Tourism Sustainability Analysis

[![Competition](https://img.shields.io/badge/Competition-MCM%2FICM%202025-blue)](https://www.comap.com/contests/mcm-icm)
[![Award](https://img.shields.io/badge/Award-Honorable%20Mention-green)](https://www.comap.com/contests/mcm-icm)
[![Problem](https://img.shields.io/badge/Problem-B-orange)](https://www.comap.com/contests/mcm-icm)

> **English** | [中文](README_CN.md)

## Project Overview

This repository contains the code and materials for our team's participation in **MCM/ICM 2025 - Problem B**. Our team received an **Honorable Mention**.

### Problem Description

Problem B focuses on **tourism sustainability in Juneau, Alaska**, especially the impact of cruise tourism on the local economy, environment, and society. The goal is to balance economic benefits with environmental protection and community well-being.

## Project Structure

```
.
|-- 2025_MCM-ICM_Problems/          # Official problem statements & policies
|   |-- 2025_MCM_Problem_B.pdf
|   `-- Contest_AI_Policy.pdf
|-- Data/                            # Data files
|   |-- glacier_data.xlsx
|   |-- tourism_data.xlsx
|   |-- Juneau_field_data.xlsx
|   `-- Juneau_city_tourism_data/
|-- Analysis.py                      # Sensitivity analysis
|-- pareto_2.py                      # Pareto frontier optimization
|-- moudle.ipynb                     # Main modeling notebook
`-- Time_forecast.ipynb              # Time series forecasting
```

For Chinese translations, references, and paper materials, please see `README_CN.md`.

## Main Models and Methods

### 1. Multi-Objective Optimization Model

- **Algorithm**: NSGA-II (Non-dominated Sorting Genetic Algorithm II)
- **Objectives**:
  - Maximize economic benefits
  - Maximize resident satisfaction
  - Minimize carbon emissions
  - Minimize hidden costs
- **File**: `pareto_2.py`

### 2. Time Series Forecasting

- **Methods**:
  - Prophet
  - LSTM
- **Predicted variables**:
  - Air Quality Index
  - Greenhouse gas emissions
  - Glacier area
  - Carbon emissions
- **File**: `Time_forecast.ipynb`

### 3. Decision Optimization

- **Methods**:
  - Genetic Algorithm (GA)
  - Direct Search
  - Linear regression modeling
- **File**: `moudle.ipynb`

### 4. Sensitivity Analysis

- Studies how changes in tourist volume and cruise ship numbers affect economic, social, and environmental indicators
- **File**: `Analysis.py`

## Tech Stack

- **Python 3.9+**
- **Libraries**:
  - `numpy`, `pandas`, `matplotlib`, `scikit-learn`
  - `tensorflow/keras`
  - `prophet`
  - `pymoo`, `deap`

## Installation and Usage

### Environment Setup

```bash
git clone https://github.com/Caria-Tarnished/2025-MCM-ICM-B.git
cd 2025-MCM-ICM-B

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install numpy pandas matplotlib scikit-learn
pip install tensorflow prophet pymoo deap
```

### Running the Code

```bash
python pareto_2.py
python Analysis.py

jupyter notebook moudle.ipynb
jupyter notebook Time_forecast.ipynb
```

## Data Description

- **Data/glacier_data.xlsx**: Historical glacier data
- **Data/tourism_data.xlsx**: Tourism-related data
- **Data/Juneau_field_data.xlsx**: Juneau field/regional data
- **Data/Juneau_city_tourism_data/**: Detailed city-level statistics

## License

For academic exchange and learning purposes only.

## Contact

- Email: [your-email@example.com]
- GitHub Issues: [Project Issues Page]

---

**Note**: The code and data in this repository are for reference and learning only. Please do not use them directly in other competitions.
