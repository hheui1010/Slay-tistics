#  Brugada Syndrome Detection: Explainable AI for Emergency Triage

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Model-Logistic%20Regression-success)
![License](https://img.shields.io/badge/License-MIT-green)

##  Overview
An interpretable machine learning pipeline designed for early Brugada Syndrome detection from multi-lead ECGs. By transitioning from "black-box" models to a highly calibrated, regularized Logistic Regression pipeline, this tool empowers clinicians with transparent risk assessments to prevent sudden cardiac death.

##  The "Hope" Impact & Clinical Value
In emergency medicine, a "black box" AI is unacceptable. Doctors need to understand *why* a prediction is made. 
Our solution provides **Absolute Clinical Transparency**:
* **Prioritizing Patient Safety:** Achieved a **0.8000 Recall** (Sensitivity), prioritizing the detection of true Brugada patients to minimize fatal missed diagnoses.
* **Explainable Risk:** The model identified `V1_J_point_amp` as the top predictor, perfectly mirroring the diagnostic reasoning of expert cardiologists.
* **Open Science:** Released under the MIT License to ensure global medical researchers can audit and build upon this screening baseline.

##  Methodology & Reproducibility
Our entire research and development process is fully documented in the provided Jupyter Notebooks:

### 1. Signal Processing & Feature Engineering
Detailed in `Extract_features_from_ECG.ipynb`:
* Applied a 3rd-order Butterworth bandpass filter (0.5–45 Hz) to eliminate noise without distorting the QRS complex.
* Extracted **18 morphological features** (J-point, ST-segment) across leads V1, V2, and V3.
* Statistical validation using **Bonferroni correction** to identify significant clinical indicators.

### 2. Model Training & Evaluation
Detailed in `brugada_(v1_3).ipynb`:
* Trained an **L2 Regularized Logistic Regression** model to ensure interpretability.
* **AUC:** 0.8586 | **Accuracy:** 0.8082 | **Recall:** 0.8000.

##  Quick Start & Installation

**1. Clone the repository & install dependencies:**
```bash
git clone [https://github.com/hheui1010/Brugada-Syndrome-Detection.git](https://github.com/hheui1010/Brugada-Syndrome-Detection.git)
cd Brugada-Syndrome-Detection
pip install -r requirements.txt
```

**2.Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Launch the Diagnostic Dashboard:**
```bash
streamlit run app.py
```
