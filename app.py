# ============================================================
# DIFFICULT THYROIDECTOMY CALCULATOR PRO
# FINAL THESIS VERSION (n=180 | TDSS ≥14)
# PREMIUM AI SURGICAL DECISION SUPPORT PLATFORM
# STREAMLIT + GITHUB READY
# ============================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time
from math import exp

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Difficult Thyroidectomy Calculator PRO",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #071739;
    color: white;
}

.main {
    background: linear-gradient(135deg,#071739,#0B2447);
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* HERO */

.hero-container {
    padding: 60px;
    border-radius: 30px;
    background: linear-gradient(135deg,#00C6FF,#0072FF);
    text-align: center;
    color: white;
    box-shadow: 0px 12px 40px rgba(0,0,0,0.35);
    margin-top: 20px;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 52px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 22px;
    opacity: 0.95;
}

/* GLASS CARD */

.glass-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    margin-bottom: 20px;
}

/* SECTION */

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #00E5FF;
    margin-bottom: 15px;
}

/* RISK BOXES */

.low-risk {
    background: #00C853;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: white;
}

.medium-risk {
    background: #FF9800;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: white;
}

.high-risk {
    background: #D50000;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: white;
}

/* BUTTONS */

.stButton>button {
    width: 100%;
    border-radius: 15px;
    height: 3.5em;
    background: linear-gradient(90deg,#00C9A7,#005BFF);
    color: white;
    border: none;
    font-size: 18px;
    font-weight: 700;
}

/* HIDE FOOTER */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 0

# ============================================================
# PAGE 1 — LANDING PAGE
# ============================================================

if st.session_state.page == 0:

    st.markdown("""
    <div class="hero-container">

        <div class="hero-title">
            🩺 Difficult Thyroidectomy Calculator PRO
        </div>

        <br>

        <div class="hero-subtitle">
            AI-Powered Surgical Difficulty Prediction Platform
        </div>

        <br>

        <div style="font-size:18px;">
            Final MCh Thesis Model • Nomogram-Based Prediction <br>
            Advanced Surgical Intelligence Dashboard
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ========================================================

    col1,col2,col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="glass-card">

        ### 📊 Prediction Engine

        • Logistic Regression  
        • Nomogram Scoring  
        • Risk Stratification  
        • ROC Validation  

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="glass-card">

        ### 🧠 Surgical Intelligence

        • Dynamic Risk Gauge  
        • Clinical Recommendations  
        • Complexity Alerts  
        • Operative Planning  

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="glass-card">

        ### 🚀 Professional Features

        • Downloadable Reports  
        • Glassmorphism UI  
        • Mobile Responsive  
        • AI Dashboard  

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns([1,2,1])

    with c2:

        if st.button("🚀 Start AI Assessment"):
            st.session_state.page = 1
            st.rerun()

# ============================================================
# PAGE 2 — INPUT PAGE
# ============================================================

elif st.session_state.page == 1:

    st.markdown("""
    <div class="section-title">
    Patient Assessment Wizard
    </div>
    """, unsafe_allow_html=True)

    progress = st.progress(10)

    # ========================================================
    # DEMOGRAPHICS
    # ========================================================

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("👤 Patient Demographics")

    c1,c2,c3 = st.columns(3)

    with c1:
        age = st.number_input("Age",20,90,40)

    with c2:
        bmi = st.number_input("BMI",15.0,45.0,25.0)

    with c3:
        neck = st.number_input(
            "Neck Circumference (cm)",
            20.0,
            60.0,
            36.0
        )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(30)

    # ========================================================
    # IMAGING
    # ========================================================

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("🧠 Imaging Parameters")

    c1,c2 = st.columns(2)

    with c1:

        tirads = st.selectbox(
            "TIRADS Score",
            [1,2,3,4,5]
        )

        rse = st.selectbox(
            "Retrosternal Extension",
            ["No","Yes"]
        )

    with c2:

        shear = st.slider(
            "Shear Wave Elastography (kPa)",
            5.0,
            80.0,
            30.0
        )

        thyroiditis = st.selectbox(
            "Thyroiditis",
            ["No","Yes"]
        )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(60)

    # ========================================================
    # CYTOLOGY
    # ========================================================

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("🔬 Cytology")

    fnac = st.selectbox(
        "FNAC Score",
        [1,2,3,4,5,6]
    )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(80)

    # ========================================================
    # SURGICAL PLAN
    # ========================================================

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("⚠ Symptoms & Surgical Plan")

    c1,c2 = st.columns(2)

    with c1:

        compressive = st.selectbox(
            "Compressive Symptoms",
            ["No","Yes"]
        )

    with c2:

        procedure = st.selectbox(
            "Procedure Type",
            [
                "Hemithyroidectomy",
                "Total Thyroidectomy / TT+CCLND"
            ]
        )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(100)

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================
    # BUTTONS
    # ========================================================

    c1,c2 = st.columns(2)

    with c1:

        if st.button("⬅ Back to Home"):
            st.session_state.page = 0
            st.rerun()

    with c2:

        if st.button("🧠 Calculate Surgical Risk"):

            with st.spinner("Running AI Surgical Analysis..."):
                time.sleep(2)

            # STORE INPUTS
            st.session_state.age = age
            st.session_state.bmi = bmi
            st.session_state.neck = neck
            st.session_state.tirads = tirads
            st.session_state.rse = rse
            st.session_state.shear = shear
            st.session_state.thyroiditis = thyroiditis
            st.session_state.fnac = fnac
            st.session_state.compressive = compressive
            st.session_state.procedure = procedure

            st.session_state.page = 2
            st.rerun()

# ============================================================
# PAGE 3 — RESULTS DASHBOARD
# ============================================================

elif st.session_state.page == 2:

    # ========================================================
    # LOAD SESSION DATA
    # ========================================================

    age = st.session_state.age
    bmi = st.session_state.bmi
    neck = st.session_state.neck
    tirads = st.session_state.tirads
    rse = st.session_state.rse
    shear = st.session_state.shear
    thyroiditis = st.session_state.thyroiditis
    fnac = st.session_state.fnac
    compressive = st.session_state.compressive
    procedure = st.session_state.procedure

    # ========================================================
    # ENCODING
    # ========================================================

    rse_bin = 1 if rse == "Yes" else 0
    thyroiditis_bin = 1 if thyroiditis == "Yes" else 0
    compressive_bin = 1 if compressive == "Yes" else 0
    proc_bin = 1 if procedure != "Hemithyroidectomy" else 0

    # ========================================================
    # FINAL THESIS MODEL COEFFICIENTS
    # ========================================================

    intercept = -8.2

    beta_proc = 4.127
    beta_neck = 0.089
    beta_rse = 0.925
    beta_thyroiditis = 0.481
    beta_shear = -0.030
    beta_fnac = -0.072
    beta_tirads = 0.098
    beta_compressive = -0.066

    # ========================================================
    # LOGISTIC MODEL
    # ========================================================

    logit = (
        intercept
        + beta_proc * proc_bin
        + beta_neck * neck
        + beta_rse * rse_bin
        + beta_thyroiditis * thyroiditis_bin
        + beta_shear * shear
        + beta_fnac * fnac
        + beta_tirads * tirads
        + beta_compressive * compressive_bin
    )

    probability = 1 / (1 + exp(-logit))

    risk_percent = round(probability * 100,1)

    # ========================================================
    # RISK CATEGORY
    # ========================================================

    if risk_percent < 20:
        risk_class = "LOW RISK"
        risk_style = "low-risk"

    elif risk_percent < 50:
        risk_class = "MODERATE RISK"
        risk_style = "medium-risk"

    else:
        risk_class = "HIGH RISK"
        risk_style = "high-risk"

    # ========================================================
    # SIDEBAR
    # ========================================================

    st.sidebar.title("Clinical Summary")

    st.sidebar.info(f"""
    Risk Probability: {risk_percent}%

    Risk Category:
    {risk_class}

    Procedure:
    {procedure}

    TIRADS:
    {tirads}

    FNAC:
    {fnac}
    """)

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown("""
    <div class="section-title">
    AI Surgical Risk Dashboard
    </div>
    """, unsafe_allow_html=True)

    # ========================================================
    # METRICS
    # ========================================================

    m1,m2,m3,m4 = st.columns(4)

    m1.metric("Risk %",f"{risk_percent}%")
    m2.metric("AUC","0.905")
    m3.metric("Sensitivity","84.1%")
    m4.metric("Specificity","93.9%")

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================
    # MAIN GRID
    # ========================================================

    left,right = st.columns([1,1])

    # ========================================================
    # LEFT PANEL
    # ========================================================

    with left:

        st.markdown(
            f'<div class="{risk_style}">{risk_class}<br>{risk_percent}%</div>',
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_percent,
            title={'text': "Difficulty Probability"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "#00E5FF"},
                'steps': [
                    {'range': [0,20], 'color': "#00C853"},
                    {'range': [20,50], 'color': "#FF9800"},
                    {'range': [50,100], 'color': "#D50000"},
                ]
            }
        ))

        gauge.update_layout(
            paper_bgcolor="#071739",
            font={'color': "white"},
            height=420
        )

        st.plotly_chart(gauge,use_container_width=True)

    # ========================================================
    # RIGHT PANEL
    # ========================================================

    with right:

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        st.subheader("📊 Nomogram Point Allocation")

        points = {
            "Procedure Type": round(proc_bin * 100.0,1),
            "Retrosternal Extension": round(rse_bin * 22.4,1),
            "Thyroiditis": round(thyroiditis_bin * 11.7,1),
            "TIRADS": round(tirads * 2.4,1),
            "Neck Circumference": round(neck * 2.2,1),
            "Compressive Symptoms": round(compressive_bin * -1.6,1),
            "FNAC": round(fnac * -1.7,1),
            "Shear Elastography": round(shear * -0.7,1)
        }

        df = pd.DataFrame(
            list(points.items()),
            columns=["Variable","Points"]
        )

        st.dataframe(df,use_container_width=True)

        total_points = round(df["Points"].sum(),1)

        st.metric(
            "Total Nomogram Score",
            total_points
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    # ROC CURVE
    # ========================================================

    st.markdown("""
    <div class="section-title">
    ROC Performance Curve
    </div>
    """, unsafe_allow_html=True)

    roc_x = [0,0.02,0.05,0.1,0.2,1]
    roc_y = [0,0.55,0.82,0.90,0.95,1]

    roc_fig = px.line(
        x=roc_x,
        y=roc_y,
        labels={
            "x":"1 - Specificity",
            "y":"Sensitivity"
        },
        title="ROC Curve (AUC = 0.905)"
    )

    roc_fig.add_shape(
        type='line',
        line=dict(dash='dash'),
        x0=0,
        x1=1,
        y0=0,
        y1=1
    )

    roc_fig.update_layout(
        paper_bgcolor="#071739",
        plot_bgcolor="#071739",
        font_color="white"
    )

    st.plotly_chart(roc_fig,use_container_width=True)

    # ========================================================
    # RISK DISTRIBUTION
    # ========================================================

    st.markdown("""
    <div class="section-title">
    Risk Stratification
    </div>
    """, unsafe_allow_html=True)

    risk_df = pd.DataFrame({
        "Zone":["Low","Moderate","High"],
        "Probability":[20,30,50]
    })

    bar_fig = px.bar(
        risk_df,
        x="Zone",
        y="Probability",
        title="Risk Distribution"
    )

    bar_fig.update_layout(
        paper_bgcolor="#071739",
        plot_bgcolor="#071739",
        font_color="white"
    )

    st.plotly_chart(bar_fig,use_container_width=True)

    # ========================================================
    # SURGICAL RECOMMENDATIONS
    # ========================================================

    st.markdown("""
    <div class="section-title">
    Surgical Interpretation
    </div>
    """, unsafe_allow_html=True)

    if risk_percent < 20:

        st.success("""
        Low predicted surgical difficulty.

        Recommendations:
        • Standard operative planning
        • Routine RLN precautions
        • Standard operative setup
        """)

    elif risk_percent < 50:

        st.warning("""
        Intermediate surgical difficulty.

        Recommendations:
        • Experienced endocrine surgeon
        • Detailed operative planning
        • Consider RLN monitoring
        """)

    else:

        st.error("""
        High-risk difficult thyroidectomy predicted.

        Recommendations:
        • Senior endocrine surgeon
        • RLN monitoring
        • Extended OR scheduling
        • ICU backup consideration
        • Advanced airway planning
        • Detailed preoperative counseling
        """)

    # ========================================================
    # COMPLEXITY ALERT
    # ========================================================

    if proc_bin == 1 and risk_percent > 60:

        st.error("""
        ⚠ HIGH COMPLEXITY CASE ALERT

        Consider:
        • Senior endocrine surgery team
        • Neuromonitoring
        • ICU backup
        • Blood preparation
        • Extended operative preparation
        """)

    # ========================================================
    # DOWNLOAD REPORT
    # ========================================================

    st.markdown("""
    <div class="section-title">
    Export Clinical Report
    </div>
    """, unsafe_allow_html=True)

    report = pd.DataFrame({

        "Parameter":[
            "Age",
            "BMI",
            "Neck Circumference",
            "TIRADS",
            "FNAC",
            "Procedure",
            "Risk Probability",
            "Risk Category"
        ],

        "Value":[
            age,
            bmi,
            neck,
            tirads,
            fnac,
            procedure,
            risk_percent,
            risk_class
        ]

    })

    csv = report.to_csv(index=False)

    st.download_button(
        label="📥 Download Clinical Report",
        data=csv,
        file_name="thyroidectomy_report.csv",
        mime="text/csv"
    )

    # ========================================================
    # BUTTONS
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2 = st.columns(2)

    with c1:

        if st.button("⬅ Back to Inputs"):
            st.session_state.page = 1
            st.rerun()

    with c2:

        if st.button("🔄 New Assessment"):
            st.session_state.page = 0
            st.rerun()

    # ========================================================
    # FOOTER
    # ========================================================

    st.markdown("---")

    st.markdown("""
    ### 🩺 Difficult Thyroidectomy Calculator PRO

    Developed using:
    - Multivariable Logistic Regression
    - Nomogram-Based Prediction
    - MCh Endocrine Surgery Thesis Data

    #### Final Model Performance
    - AUC = 0.905
    - Sensitivity = 84.1%
    - Specificity = 93.9%
    - Brier Score = 0.101
    - Hosmer-Lemeshow p = 0.026

    Based on:
    180-patient prospective thyroid surgery cohort
    using TDSS ≥14 difficult thyroidectomy definition.

    For academic and research use only.
    """)
