import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(page_title="Brugada AI", page_icon="🫀", layout="wide")
st.title("🫀 Brugada Syndrome Real-Time AI Diagnosis")
st.markdown("---")

# 2. Load the AI Model
@st.cache_resource
def load_my_ai():
    try:
        # Try to load the trained pipeline model
        return joblib.load('brugada_model.pkl')
    except Exception as e:
        return None

model = load_my_ai()

# 3. Sidebar: Upload CSV Dataset
st.sidebar.header("📁 Step 1: Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your CSV dataset", type=['csv'])

if model is None:
    st.error("❌ Error: 'brugada_model.pkl' not found! Please make sure it is saved in the exact same folder as this app.py file.")
elif uploaded_file is not None:
    # Load the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Dataset loaded successfully!")
    
    # 4. Sidebar: Select a Patient
    st.sidebar.header("👤 Step 2: Choose Patient")
    patient_id = st.sidebar.selectbox("Select Patient Row:", df.index)
    
    # Extract the specific patient's data
    current_patient = df.iloc[[patient_id]]
    
    # Remove labels/IDs before feeding to the AI (AI must not see the answer!)
    X_input = current_patient.drop(columns=['Label', 'Patient_ID'], errors='ignore')
    
    # Display extracted features
    st.subheader(f"📊 Extracted Features for Patient #{patient_id}")
    st.dataframe(X_input)

    # 5. Run AI Prediction
    st.divider()
    if st.button("🚀 Run AI Analysis", use_container_width=True):
        
        # Predict probability using the pipeline
        prob = model.predict_proba(X_input)[0][1]
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("### AI Prediction Result")
            if prob > 0.5:
                st.error(f"### ⚠️ HIGH RISK\nConfidence: {prob*100:.1f}%")
            else:
                st.success(f"### ✅ LOW RISK\nConfidence: {(1-prob)*100:.1f}%")
        
        with col2:
            st.write("### Analysis Breakdown")
            st.info(f"The model successfully analyzed **{len(X_input.columns)} features** extracted from ECG Leads V1-V3. This real-time prediction is powered by the customized machine learning pipeline trained on clinical biomarkers.")
else:
    st.warning("👈 Please upload your `brugada_features_V1_to_V3.csv` on the left sidebar to start the analysis.")