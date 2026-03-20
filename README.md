# 🫀 Brugada Syndrome Detection: Explainable AI for Emergency Triage

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Model-Logistic%20Regression-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
An interpretable machine learning pipeline designed for early Brugada Syndrome detection from multi-lead ECGs. By transitioning from "black-box" models to a highly calibrated, regularized Logistic Regression pipeline, this tool empowers clinicians with transparent risk assessments to prevent sudden cardiac death.

## 🌟 The "Hope" Impact & Clinical Value
In emergency medicine, a "black box" AI is unacceptable. Doctors need to understand *why* a prediction is made. 
Our solution provides **Absolute Clinical Transparency**:
* **Prioritizing Patient Safety:** Achieved a **0.8000 Recall** (Sensitivity), deliberately prioritizing the detection of true Brugada patients to minimize fatal missed diagnoses.
* **Explainable Risk:** The model independently identified the `V1_J_point_amp` as the top predictor, perfectly mirroring the real-world diagnostic reasoning of expert cardiologists.
* **Open Science:** Released under the MIT License to ensure global medical researchers can audit, trust, and build upon this life-saving screening baseline.

## ⚙️ Methodology & Reproducibility
To ensure absolute reproducibility, our entire data pipeline is documented and open-sourced. 

### 1. Signal Processing
* Decoded raw `.dat` and `.hea` files using the `wfdb` library.
* Applied a 3rd-order Butterworth bandpass filter (0.5–45 Hz) to eliminate baseline wander and high-frequency muscle noise **without distorting the critical QRS complex**.

### 2. Feature Engineering & Statistical Rigor
* Utilized `find_peaks` (100 Hz sampling) to anchor R-waves and define consistent windows for the J-point (50ms post-R) and ST-segment.
* Extracted **18 morphological features** across leads V1, V2, and V3.
* Applied independent t-tests with strict **Bonferroni correction** to mathematically filter out noise and prevent false positives, successfully identifying 6 highly significant clinical indicators.

### 3. Model Deployment Performance
Strategically retained all 18 features for our final **L2 Regularized Logistic Regression** model to capture complex multivariate patterns, achieving:
* **AUC:** 0.8586
* **Accuracy:** 0.8082
* **F1-Score:** 0.6316
* **Recall:** 0.8000

## ⚖️ License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
