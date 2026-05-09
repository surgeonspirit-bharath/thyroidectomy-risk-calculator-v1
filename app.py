# ============================================================
# DIFFICULT THYROIDECTOMY RISK CALCULATOR PRO
# CLEAN PROFESSIONAL UI VERSION
# STREAMLIT + GITHUB READY
# ============================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from math import exp
import time

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Difficult Thyroidectomy Risk Calculator PRO",
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
    background:
    radial-gradient(circle at top left, #0B2447 0%, #071739 60%);
}

/* HERO */

.hero {

    padding: 65px;

    border-radius: 30px;

    background:
    linear-gradient(
    135deg,
    #00C6FF,
    #0072FF,
    #7F00FF
    );

    background-size: 300% 300%;

    animation: gradient 12s ease infinite;

    text-align: center;

    color: white;

    margin-bottom: 30px;

    box-shadow:
    0px 10px 40px rgba(0,0,0,0.35);
}

@keyframes gradient {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.hero-title {
    font-size: 56px;
    font-weight: 900;
}

.hero-sub {
    font-size: 22px;
    opacity: 0.95;
}

/* CARDS */

.card {

    background:
    rgba(255,255,255,0.08);

    backdrop-filter:
    blur(12px);

    border-radius: 22px;

    padding: 25px;

    margin-bottom: 20px;

    box-shadow:
    0px 8px 30px rgba(0,0,0,0.25);

    transition: 0.4s;
}

.card:hover {

    transform:
    translateY(-6px);

    box-shadow:
    0px 12px 35px rgba(0,229,255,0.35);
}

/* TITLES */

.section-title {

    font-size: 30px;

    font-weight: 800;

    color: #00E5FF;

    margin-bottom: 20px;
}

/* RISK BOXES */

.low {

    background: #00C853;

    padding: 22px;

    border-radius: 18px;

    text-align: center;

    font-size: 30px;

    font-weight: bold;
}

.medium {

    background: #FF9800;

    padding: 22px;

    border-radius: 18px;

    text-align: center;

    font-size: 30px;

    font-weight: bold;
}

.high {

    background: #D50000;

    padding: 22px;

    border-radius: 18px;

    text-align: center;

    font-size: 30px;

    font-weight: bold;
}

/* BUTTON */

.stButton > button {

    width: 100%;

    border-radius: 16px;

    height: 3.5em;

    font-size: 18px;

    font-weight: 700;

    border: none;

    color: white;

    background:
    linear-gradient(
    90deg,
    #00C9A7,
    #005BFF
    );
}

/* FOOTER */

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
# PAGE 1 - LANDING PAGE
# ============================================================

if st.session_state.page == 0:

    st.markdown("""
    <div class="hero">

        <div class="hero-title">
        🩺 Difficult Thyroidectomy Risk Calculator PRO
        </div>

        <br>

        <div class="hero-sub">
        AI-Powered Surgical Difficulty Prediction Platform
        </div>

        <br>

        <div style="font-size:18px;">
        Advanced Clinical Decision Support for Endocrine Surgery
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================

    c1,c2,c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="card">

        ## 📊 Prediction Engine

        Advanced multivariable
        surgical risk prediction
        platform designed for
        difficult thyroidectomy assessment.

        <br>

        ✅ Dynamic risk calculation  
        ✅ Nomogram-based scoring  
        ✅ Operative complexity assessment  
        ✅ Real-time prediction

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="card">

        ## 🧠 Surgical Intelligence

        AI-assisted endocrine surgery
        planning and operative
        difficulty evaluation.

        <br>

        ✅ RLN risk awareness  
        ✅ Surgical planning support  
        ✅ Complexity alerts  
        ✅ Neck dissection impact

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="card">

        ## 🚀 Professional Dashboard

        Premium endocrine surgery
        clinical decision support
        interface.

        <br>

        ✅ Interactive dashboard  
        ✅ Clinical recommendations  
        ✅ Downloadable reports  
        ✅ Mobile responsive UI

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ========================================================

    st.markdown("""
    <div style='text-align:center;'>

    <h2 style='color:white;'>
    Begin Patient Risk Assessment
    </h2>

    <p style='font-size:18px;color:#D0D0D0;'>
    Predict operative difficulty using advanced clinical,
    imaging and surgical parameters.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    a,b,c = st.columns([1,2,1])

    with b:

        if st.button("🚀 Start AI Assessment"):
            st.session_state.page = 1
            st.rerun()

# ============================================================
# PAGE 2 - INPUT PAGE
# ============================================================

elif st.session_state.page == 1:

    st.markdown("""
    <div class="section-title">
    Patient Assessment Wizard
    </div>
    """, unsafe_allow_html=True)

    progress = st.progress(10)

    # ========================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 Patient Demographics")

    c1,c2,c3 = st.columns(3)

    with c1:
        age = st.number_input("Age",18,90,40)

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

    st.markdown('<div class="card">', unsafe_allow_html=True)

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

    progress.progress(55)

    # ========================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🔬 Cytology")

    fnac = st.selectbox(
        "FNAC Score",
        [1,2,3,4,5,6]
    )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(70)

    # ========================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("⚠ Symptoms")

    c1,c2 = st.columns(2)

    with c1:

        compressive = st.selectbox(
            "Compressive Symptoms",
            ["No","Yes"]
        )

    with c2:

        symptom_duration = st.number_input(
            "Duration of Symptoms (months)",
            0,
            240,
            12
        )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(85)

    # ========================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🩺 Procedure Planned")

    procedure = st.selectbox(
        "Procedure Type",
        [
            "Hemithyroidectomy",
            "Total Thyroidectomy",
            "Total Thyroidectomy + Lymph Node Dissection"
        ]
    )

    st.markdown('</div>', unsafe_allow_html=True)

    progress.progress(100)

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================

    c1,c2 = st.columns(2)

    with c1:

        if st.button("⬅ Back to Home"):
            st.session_state.page = 0
            st.rerun()

    with c2:

        if st.button("🧠 Calculate Surgical Risk"):

            with st.spinner("Running AI Surgical Analysis..."):
                time.sleep(1.5)

            st.session_state.age = age
            st.session_state.bmi = bmi
            st.session_state.neck = neck
            st.session_state.tirads = tirads
            st.session_state.rse = rse
            st.session_state.shear = shear
            st.session_state.thyroiditis = thyroiditis
            st.session_state.fnac = fnac
            st.session_state.compressive = compressive
            st.session_state.symptom_duration = symptom_duration
            st.session_state.procedure = procedure

            st.session_state.page = 2
            st.rerun()

# ============================================================
# PAGE 3 - RESULTS PAGE
# ============================================================

elif st.session_state.page == 2:

    age = st.session_state.age
    bmi = st.session_state.bmi
    neck = st.session_state.neck
    tirads = st.session_state.tirads
    rse = st.session_state.rse
    shear = st.session_state.shear
    thyroiditis = st.session_state.thyroiditis
    fnac = st.session_state.fnac
    compressive = st.session_state.compressive
    symptom_duration = st.session_state.symptom_duration
    procedure = st.session_state.procedure

    # ========================================================

    rse_bin = 1 if rse == "Yes" else 0
    thyroiditis_bin = 1 if thyroiditis == "Yes" else 0
    compressive_bin = 1 if compressive == "Yes" else 0

    proc_bin = 0

    if procedure == "Total Thyroidectomy":
        proc_bin = 1

    elif procedure == "Total Thyroidectomy + Lymph Node Dissection":
        proc_bin = 1.5

    # ========================================================
    # MODEL
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

    if risk_percent > 99:
        risk_percent = 99

    if risk_percent < 1:
        risk_percent = 1

    # ========================================================

    if risk_percent < 20:
        risk_class = "LOW RISK"
        risk_style = "low"

    elif risk_percent < 50:
        risk_class = "MODERATE RISK"
        risk_style = "medium"

    else:
        risk_class = "HIGH RISK"
        risk_style = "high"

    # ========================================================

    st.markdown("""
    <div class="section-title">
    AI Surgical Risk Dashboard
    </div>
    """, unsafe_allow_html=True)

    # ========================================================

    m1,m2,m3 = st.columns(3)

    m1.metric("Risk %",f"{risk_percent}%")
    m2.metric("Procedure",procedure)
    m3.metric("TIRADS",tirads)

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================

    left,right = st.columns([1,1])

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

    with right:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📊 Nomogram Point Allocation")

        points = {
            "Procedure Type": round(proc_bin * 100,1),
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
        """)

    elif risk_percent < 50:

        st.warning("""
        Intermediate surgical difficulty.

        Recommendations:
        • Experienced endocrine surgeon
        • Consider RLN monitoring
        """)

    else:

        st.error("""
        High-risk difficult thyroidectomy predicted.

        Recommendations:
        • Senior endocrine surgeon
        • RLN monitoring
        • ICU backup consideration
        • Extended OR scheduling
        """)

    # ========================================================

    if procedure == "Total Thyroidectomy + Lymph Node Dissection":

        st.error("""
        ⚠ HIGH COMPLEXITY ALERT

        Planned lymph node dissection significantly
        increases operative complexity.
        """)

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
            "Compressive Symptoms",
            "Symptom Duration",
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
            compressive,
            symptom_duration,
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

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================

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

    st.markdown("---")

    st.caption("""
    Advanced endocrine surgery clinical decision support platform.
    """)
