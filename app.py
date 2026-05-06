import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from math import exp

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Difficult Thyroidectomy Calculator PRO",
    page_icon="🩺",
    layout="wide",
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0B132B;
    color: white;
}

.stButton>button {
    background: linear-gradient(90deg,#00C9A7,#005BFF);
    color:white;
    border-radius:12px;
    height:3em;
    width:100%;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.metric-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding:20px;
    border-radius:20px;
    box-shadow:0 8px 32px rgba(0,0,0,0.2);
    margin-bottom:20px;
}

.risk-low {
    background:#00C853;
    padding:15px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}

.risk-medium {
    background:#FFAB00;
    padding:15px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}

.risk-high {
    background:#D50000;
    padding:15px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}

.title {
    font-size:42px;
    font-weight:800;
    color:#00E5FF;
}

.subtitle {
    font-size:18px;
    color:#B0BEC5;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown('<div class="title">🩺 Difficult Thyroidectomy Calculator PRO</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI-driven Surgical Difficulty Prediction using Nomogram-Based Logistic Regression</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("Patient Parameters")

neck = st.sidebar.slider(
    "Neck Circumference (cm)",
    25.0,
    55.0,
    36.0,
    0.1
)

tirads = st.sidebar.selectbox(
    "TIRADS Score",
    [1,2,3,4,5]
)

fnac = st.sidebar.selectbox(
    "FNAC Score",
    [1,2,3,4,5,6]
)

shear = st.sidebar.slider(
    "Shear Wave Elastography",
    5.0,
    80.0,
    30.0,
    0.1
)

rse = st.sidebar.selectbox(
    "Retrosternal Extension",
    ["No","Yes"]
)

thyroiditis = st.sidebar.selectbox(
    "Thyroiditis",
    ["No","Yes"]
)

compressive = st.sidebar.selectbox(
    "Compressive Symptoms",
    ["No","Yes"]
)

procedure = st.sidebar.selectbox(
    "Procedure Type",
    ["Hemithyroidectomy","Total Thyroidectomy/ND"]
)

# ---------------- BINARY ENCODING ---------------- #

rse_bin = 1 if rse == "Yes" else 0
thyroiditis_bin = 1 if thyroiditis == "Yes" else 0
compressive_bin = 1 if compressive == "Yes" else 0
proc_bin = 1 if procedure == "Total Thyroidectomy/ND" else 0

# ---------------- MODEL COEFFICIENTS ---------------- #

intercept = -8.5

beta_neck = 0.1089
beta_rse = 1.2002
beta_thyroiditis = 0.2992
beta_shear = -0.0279
beta_fnac = -0.0637
beta_tirads = 0.0418
beta_compressive = 0.1124
beta_proc = 4.302

# ---------------- PREDICTION ---------------- #

logit = (
    intercept
    + beta_neck * neck
    + beta_rse * rse_bin
    + beta_thyroiditis * thyroiditis_bin
    + beta_shear * shear
    + beta_fnac * fnac
    + beta_tirads * tirads
    + beta_compressive * compressive_bin
    + beta_proc * proc_bin
)

probability = 1 / (1 + exp(-logit))
risk_percent = round(probability * 100, 1)

# ---------------- RISK CATEGORY ---------------- #

if risk_percent < 20:
    risk_class = "LOW RISK"
    risk_style = "risk-low"

elif risk_percent < 50:
    risk_class = "MODERATE RISK"
    risk_style = "risk-medium"

else:
    risk_class = "HIGH RISK"
    risk_style = "risk-high"

# ---------------- MAIN LAYOUT ---------------- #

col1, col2 = st.columns([1,1])

# ---------------- LEFT PANEL ---------------- #

with col1:

    st.markdown("## 📊 Predicted Surgical Difficulty")

    st.markdown(
        f'<div class="{risk_style}">{risk_class}<br>{risk_percent}%</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_percent,
        title={'text': "Risk Probability"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "#00E5FF"},
            'steps': [
                {'range': [0,20], 'color': "#00C853"},
                {'range': [20,50], 'color': "#FFAB00"},
                {'range': [50,100], 'color': "#D50000"},
            ]
        }
    ))

    gauge.update_layout(
        paper_bgcolor="#0B132B",
        font={'color': "white"}
    )

    st.plotly_chart(gauge, use_container_width=True)

# ---------------- RIGHT PANEL ---------------- #

with col2:

    st.markdown("## 🧠 Nomogram Contribution")

    points = {
        "Neck Circumference": round(neck * 2.53,1),
        "Retrosternal Extension": round(rse_bin * 27.9,1),
        "Thyroiditis": round(thyroiditis_bin * 6.95,1),
        "Shear Elastography": round(shear * -0.65,1),
        "FNAC": round(fnac * -1.48,1),
        "TIRADS": round(tirads * 0.97,1),
        "Compressive Symptoms": round(compressive_bin * 2.61,1),
        "Procedure": round(proc_bin * 100,1)
    }

    df = pd.DataFrame(
        list(points.items()),
        columns=["Variable","Points"]
    )

    st.dataframe(df, use_container_width=True)

    total_points = round(df["Points"].sum(),1)

    st.metric(
        label="Total Nomogram Points",
        value=total_points
    )

# ---------------- ROC PERFORMANCE ---------------- #

st.markdown("---")
st.markdown("## 📈 Model Performance")

m1, m2, m3 = st.columns(3)

m1.metric("AUC", "0.915")
m2.metric("Brier Score", "0.091")
m3.metric("Hosmer-Lemeshow p", "0.011")

# ---------------- INTERPRETATION ---------------- #

st.markdown("---")
st.markdown("## 🩺 Clinical Interpretation")

if risk_percent < 20:
    st.success("""
    Low predicted probability of difficult thyroidectomy.
    
    Expected operative course is favorable.
    """)

elif risk_percent < 50:
    st.warning("""
    Intermediate surgical difficulty predicted.
    
    Careful operative planning recommended.
    """)

else:
    st.error("""
    High likelihood of difficult thyroidectomy.
    
    Consider:
    - Senior endocrine surgeon
    - Advanced airway planning
    - Extended operative time
    - RLN monitoring
    - Preoperative counseling
    """)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption("""
Developed using multivariable logistic regression and nomogram modeling.
For academic and clinical research use only.
""")
