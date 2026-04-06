# 🚗 Car Mileage Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  A Machine Learning web application that predicts the fuel efficiency (MPG) of a car based on its engine specifications and vehicle characteristics — built with Random Forest and deployed using Streamlit.
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [ML Pipeline](#-ml-pipeline)
- [Model Performance](#-model-performance)
- [Installation & Usage](#-installation--usage)
- [Screenshots](#-screenshots)
- [Author](#-author)
- [License](#-license)

---

## 🧠 Overview

Car Mileage Predictor is an end-to-end Machine Learning project that takes a user's car specifications as input and predicts the **combined fuel efficiency in MPG (Miles Per Gallon)** — also converted to **km/litre** for Indian users.

The model was trained on 11,000+ real vehicle records from the **Car Features and MSRP Dataset (1990–2018)** available on Kaggle, using a **Random Forest Regressor** that achieved an R² score of **0.9586** and a Mean Absolute Error of just **0.61 MPG**.

---

## 🌐 Live Demo

# > 🚀 **[Click here to try the app](https://car-mpg-prediction.streamlit.app/)**

---

## ✨ Features

- 🔢 Accepts real car specs as input — Engine CC, Horsepower, Fuel Type, Transmission, Drive Type, Vehicle Size and Style
- ⚡ Instant MPG prediction powered by a trained Random Forest model
- 🇮🇳 Converts MPG to km/litre for Indian context
- 🟢🟡🔴 Colour-coded result — Excellent / Average / Low fuel efficiency
- 📊 Displays feature importance so users understand what drives the prediction
- 💾 Model loaded from saved `.pkl` file — no retraining on every run

---

## 📊 Dataset

| Property | Details |
|---|---|
| **Source** | [Car Features and MSRP — Kaggle (CooperUnion)](https://www.kaggle.com/datasets/CooperUnion/cardataset) |
| **Original Rows** | 11,914 |
| **Rows after cleaning** | ~11,800 |
| **Features used** | 7 |
| **Target variable** | Combined MPG `(highway MPG + city mpg) / 2` |
| **Year range** | 1990 – 2018 |

### Features Used for Training

| Feature | Type | Description |
|---|---|---|
| `Engine_CC` | Numeric | Engineered from cylinders × 500 |
| `Engine HP` | Numeric | Horsepower of the engine |
| `Engine Fuel Type` | Categorical | Petrol / Premium / Diesel / Flex |
| `Transmission Type` | Categorical | Automatic / Manual / Direct Drive |
| `Driven_Wheels` | Categorical | FWD / RWD / AWD / 4WD |
| `Vehicle Size` | Categorical | Compact / Midsize / Large |
| `Vehicle Style` | Categorical | Sedan / SUV / Coupe etc. |

---

## 📁 Project Structure

```
CarMileagePredictor/
│
├── app.py                  # Streamlit web application
├── data.csv                # Cleaned dataset
├── rf_model.pkl            # Trained Random Forest model
├── encoders.pkl            # Saved LabelEncoders for all categorical features
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| Pandas | Data manipulation and cleaning |
| Scikit-learn | Model training and evaluation |
| Matplotlib / Seaborn | EDA and visualizations |
| Streamlit | Web app deployment |
| Pickle | Model serialization |

---

## 🔬 ML Pipeline

```
Raw Data (11,914 rows)
        ↓
Data Cleaning
  • Drop irrelevant columns (MSRP, Popularity, Make, Model, Year)
  • Handle nulls — grouped median imputation by fuel type / cylinders
  • Remove electric vehicles (MPGe scale incompatible with ICE cars)
  • Drop rows with UNKNOWN transmission (19 rows)
        ↓
Feature Engineering
  • Create combined_mpg = (highway MPG + city mpg) / 2  ← Target
  • Create Engine_CC = Engine Cylinders × 500
  • Simplify Engine Fuel Type into 4 groups
        ↓
EDA
  • MPG distribution — right skewed, electric outliers identified
  • Correlation heatmap — Engine_CC (-0.63) and HP (-0.44) with MPG
  • Boxplot — MPG by Fuel Type
        ↓
Encoding
  • LabelEncoder for all 5 categorical features
  • Encoders saved separately for consistent inference
        ↓
Model Training
  • Algorithm: Random Forest Regressor (n_estimators=100)
  • Train/Test split: 80/20, random_state=42
  • No feature scaling needed (tree-based model)
        ↓
Evaluation
  • R² Score: 0.9586
  • MAE: 0.61 MPG
        ↓
Deployment
  • Streamlit app with user-friendly inputs
  • Loads saved model and encoders via pickle
  • Outputs MPG + km/litre conversion
```

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| **R² Score** | 0.9586 |
| **Mean Absolute Error** | 0.61 MPG |
| **Algorithm** | Random Forest Regressor |
| **Training samples** | ~9,500 |
| **Test samples** | ~2,300 |

### Feature Importance

| Rank | Feature | Importance |
|---|---|---|
| 1 | Engine_CC | 78.8% |
| 2 | Engine HP | 10.1% |
| 3 | Driven Wheels | 3.7% |
| 4 | Vehicle Style | 2.9% |
| 5 | Fuel Type | 1.8% |
| 6 | Vehicle Size | 1.4% |
| 7 | Transmission | 1.3% |

---

## 💻 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/adityabobade7900/CarMileagePredictor.git
cd CarMileagePredictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## 🧪 Sample Test Case

| Input | Value |
|---|---|
| Engine CC | 1500 |
| Horsepower | 143 |
| Fuel Type | Petrol |
| Transmission | MANUAL |
| Driven Wheels | Front Wheel Drive |
| Vehicle Size | Compact |
| Vehicle Style | Sedan |
| **Predicted MPG** | **35.9 MPG** |
| **Real-world MPG** | **32–35 MPG (Honda Civic 2015)** |

---

## 📸 Screenshots

> *(Add screenshot of your running Streamlit app here)*
> Drag and drop your app screenshot into this section after uploading to GitHub.

---

## 👨‍💻 Author

**Aditya Bobade**
Data Analyst | Python | MySQL | Power BI | Machine Learning

[![GitHub](https://img.shields.io/badge/GitHub-adityabobade7900-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/adityabobade7900)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aditya%20Bobade-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adityabobade7900)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit%20Here-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://adityabobade7900.github.io/adityabobade/)

---

## 📞 Need Help?

If you have any questions, suggestions, or run into any issues, feel free to reach out:

| Platform | Link |
|---|---|
| 💼 LinkedIn | [linkedin.com/in/adityabobade7900](https://www.linkedin.com/in/adityabobade7900) |
| 📧 Email | [bobade1436@gmail.com](mailto:bobade1436@gmail.com) |
| 🐙 GitHub | [github.com/adityabobade7900](https://github.com/adityabobade7900) |

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify and distribute.

---

> ⭐ **If you found this project helpful, please give it a star on GitHub!** ⭐
