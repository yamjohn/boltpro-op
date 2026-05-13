import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="BoltPro Engineering Suite",
    page_icon="🔩",
    layout="centered"
)

# =========================
# CUSTOM STYLE
# =========================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #202124;
    color: white;
}

.stApp {
    background-color: #202124;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

div[data-baseweb="select"] {
    color: white;
}

.stButton>button {
    width: 100%;
    background-color: #ff8800;
    color: white;
    border: none;
    padding: 14px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #ffaa33;
    color: white;
}

.result-box {
    background-color: #2b2b2b;
    padding: 20px;
    border-radius: 12px;
    color: white;
    font-family: Consolas;
    white-space: pre-wrap;
}

.footer {
    text-align: center;
    color: #888888;
    margin-top: 30px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<h1 style='text-align:center; color:#ff8800;'>
🔩 BoltPro
</h1>

<h4 style='text-align:center; color:#bbbbbb; margin-top:-10px;'>
Engineering Suite
</h4>
""", unsafe_allow_html=True)

st.write("")

# =========================
# BOLT SIZES
# =========================

bolt_sizes = {
    "M4": 0.004,
    "M5": 0.005,
    "M6": 0.006,
    "M8": 0.008,
    "M10": 0.010,
    "M12": 0.012,
    "M14": 0.014,
    "M16": 0.016,
    "M18": 0.018,
    "M20": 0.020
}

# =========================
# MATERIALS
# =========================

materials = {

    "Steel": {
        "4.6": 4000,
        "8.8": 8000,
        "10.9": 12000,
        "12.9": 15000
    },

    "Stainless": {
        "304": 5200,
        "316": 5800
    },

    "Aluminum": {
        "6061": 3100,
        "7075": 5500
    },

    "Titanium": {
        "Grade 2": 9000,
        "Grade 5": 14000
    },

    "Brass": {
        "Standard": 2500
    }
}

# =========================
# INPUT SECTION
# =========================

st.markdown("## Bolt Configuration")

# BOLT SIZE
size = st.selectbox(
    "Bolt Size",
    list(bolt_sizes.keys()),
    index=2
)

# MATERIAL
material = st.selectbox(
    "Material",
    list(materials.keys())
)

# GRADE
grade = st.selectbox(
    "Material Grade",
    list(materials[material].keys())
)

# K FACTOR
k_option = st.selectbox(
    "K Factor",
    [
        "0.10 - Heavy Grease",
        "0.15 - Light Oil",
        "0.20 - Dry Bolt",
        "0.25 - Rust/Friction"
    ],
    index=2
)

# THREAD LENGTH
length = st.number_input(
    "Thread Length (mm)",
    min_value=0.0,
    value=50.0,
    step=1.0
)

st.write("")

# =========================
# CALCULATE BUTTON
# =========================

if st.button("CALCULATE"):

    # VALUES
    d = bolt_sizes[size]

    F = materials[material][grade]

    K = float(
        k_option.split(" - ")[0]
    )

    # TORQUE
    T = K * F * d

    # LB-FT
    lbft = T * 0.73756

    # CLAMP FORCE
    clamp_force = T / (K * d)

    # RESULT
    result = f"""
SYSTEM READY

Material : {material}
Bolt Size : {size}
Grade     : {grade}
Length    : {length} mm

K Factor  : {K}

========================

Torque
{T:.2f} N·m

{lbft:.2f} lb-ft

========================

Clamp Force
{clamp_force:.2f} N
"""

    st.success("Calculation Complete")

    st.markdown(
        f"""
<div class="result-box">
{result}
</div>
""",
        unsafe_allow_html=True
    )

# =========================
# FOOTER
# =========================

st.markdown(
    """
<div class="footer">
BoltPro v3.0
</div>
""",
    unsafe_allow_html=True
)