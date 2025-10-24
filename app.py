import streamlit as st
import math

# =================== PAGE CONFIG ===================
st.set_page_config(page_title="Virtual Lab Assistant", layout="wide")

# =================== STATE INIT ===================
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
if 'selected_practical' not in st.session_state:
    st.session_state['selected_practical'] = None

# =================== HELPER FUNCTIONS ===================
def go_home():
    st.session_state['page'] = 'home'
    st.session_state['selected_practical'] = None

def go_practical(practical):
    st.session_state['selected_practical'] = practical
    st.session_state['page'] = 'practical'

def convert_mass(value, unit):
    if unit == "mg": return value / 1000
    elif unit == "g": return value
    elif unit == "kg": return value * 1000

def convert_volume(value, unit):
    if unit == "mL": return value / 1000
    elif unit == "L": return value
    elif unit == "μL": return value / 1e6

# =================== FRONT PAGE ===================
if st.session_state['page'] == 'home':
    st.markdown("""
    <style>
    .stApp {background-color: #0f111a; color: white;}
    .title {color:#00bfff; font-size:48px; font-weight:bold; text-align:center; margin-bottom:10px;}
    .subtitle {color:#ffffff; font-size:22px; text-align:center; margin-bottom:30px;}
    .features {font-size:18px; color:#ffffff; line-height:1.8; margin-bottom:30px;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Virtual Lab Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Perform Chemistry Practicals Virtually with Step-by-Step Guidance</div>', unsafe_allow_html=True)

    st.subheader("Why Use This App?")
    st.markdown("""
    <div class="features">
    - Step-by-step guided practicals<br>
    - Automatic calculations with formulas<br>
    - Interactive reagent selection and unit conversion<br>
    - Mimics real lab notebook workflow<br>
    - Perfect for students learning chemistry virtually
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Start Your Practical")
    practical = st.selectbox(
        "Choose a Practical to Begin:",
        [
            "Solution Preparation",
            "Acid-Base Titration",
            "pH Calculation",
            "Molarity from Weight",
            "Dilution of Solutions",
            "Buffer Preparation",
            "Complexometric Titration",
            "Colorimetry / Absorbance",
            "Volumetric Analysis"
        ]
    )

    if st.button("🚀 Start Practical"):
        go_practical(practical)

# =================== PRACTICAL PAGES ===================
elif st.session_state['page'] == 'practical':
    practical = st.session_state['selected_practical']

    if st.button("🏠 Back to Home"):
        go_home()

    # ---------------- SOLUTION PREPARATION ----------------
    if practical == "Solution Preparation":
        st.header("Solution Preparation")
        st.subheader("Principle")
        st.write("Preparation of solutions involves dissolving a known amount of solute in a solvent to obtain desired concentration.")

        st.subheader("Steps")
        st.write("""
        1. Weigh the solute accurately.
        2. Dissolve in part of the solvent.
        3. Transfer to volumetric flask.
        4. Make up the solution to the mark.
        """)

        st.subheader("Calculations")
        st.write("**Formula:** Molarity (M) = moles of solute / liters of solution")

        solute = st.selectbox("Select solute:", ["NaCl", "KCl", "CuSO4"])
        molar_masses = {"NaCl":58.44, "KCl":74.55, "CuSO4":159.6}
        molar_mass = molar_masses[solute]
        st.info(f"Typical molar mass of {solute} = {molar_mass} g/mol")

        mass_unit = st.selectbox("Mass unit:", ["g", "mg", "kg"])
        mass_input = st.number_input("Enter mass of solute:", min_value=0.0)
        mass_in_g = convert_mass(mass_input, mass_unit)

        vol_unit = st.selectbox("Volume unit:", ["L", "mL"])
        vol_input = st.number_input("Enter final volume:", min_value=0.0)
        vol_in_L = convert_volume(vol_input, vol_unit)

        if mass_in_g > 0 and vol_in_L > 0:
            moles = mass_in_g / molar_mass
            molarity = moles / vol_in_L
            st.success(f"Moles: {moles:.4f} mol")
            st.success(f"Molarity: {molarity:.4f} M")

    # ---------------- ACID-BASE TITRATION ----------------
    elif practical == "Acid-Base Titration":
        st.header("Acid-Base Titration")
        st.subheader("Principle")
        st.write("Determines concentration of unknown acid or base using a standard solution.")
        st.subheader("Formula: M1V1 = M2V2")

        acid = st.selectbox("Select Acid:", ["HCl","H2SO4","CH3COOH"])
        base = st.selectbox("Select Base:", ["NaOH","KOH"])

        M_acid = st.number_input(f"Concentration of {acid} (M):", min_value=0.0)
        V_acid = st.number_input(f"Volume of {acid} used (mL):", min_value=0.0)
        V_base = st.number_input(f"Volume of {base} used (mL):", min_value=0.0)

        V_acid_L = V_acid / 1000
        V_base_L = V_base / 1000

        if M_acid > 0 and V_acid_L > 0 and V_base_L > 0:
            M_base = (M_acid * V_acid_L) / V_base_L
            st.success(f"Concentration of {base}: {M_base:.4f} M")

    # ---------------- pH CALCULATION ----------------
    elif practical == "pH Calculation":
        st.header("pH Calculation")
        st.subheader("Formula: pH = -log10[H+]")
        H_conc = st.number_input("Enter H+ ion concentration [H+] (M):", min_value=0.0, format="%.10f")
        if H_conc > 0:
            pH = -math.log10(H_conc)
            st.success(f"Calculated pH = {pH:.4f}")

    # ---------------- MOLARITY FROM WEIGHT ----------------
    elif practical == "Molarity from Weight":
        st.header("Molarity from Weight")
        st.subheader("Formula: M = (weight / molar mass) / volume")

        weight_unit = st.selectbox("Weight unit:", ["g","mg","kg"])
        weight_input = st.number_input("Enter solute weight:", min_value=0.0)
        weight_in_g = convert_mass(weight_input, weight_unit)
        molar_mass = st.number_input("Enter molar mass (g/mol):", min_value=0.0)
        vol_unit = st.selectbox("Volume unit:", ["L","mL"], key="molweight")
        vol_input = st.number_input("Enter solution volume:", min_value=0.0)
        vol_in_L = convert_volume(vol_input, vol_unit)

        if weight_in_g>0 and molar_mass>0 and vol_in_L>0:
            moles = weight_in_g / molar_mass
            M = moles / vol_in_L
            st.success(f"Moles: {moles:.4f} mol")
            st.success(f"Molarity: {M:.4f} M")

    # ---------------- DILUTION ----------------
    elif practical == "Dilution of Solutions":
        st.header("Dilution of Solutions")
        st.subheader("Formula: C1V1 = C2V2")

        C1 = st.number_input("Stock concentration (M):", min_value=0.0)
        V1 = st.number_input("Stock volume (mL):", min_value=0.0)
        V2 = st.number_input("Final volume (mL):", min_value=0.0)

        V1_L = V1/1000
        V2_L = V2/1000

        if C1>0 and V1_L>0 and V2_L>0:
            C2 = (C1*V1_L)/V2_L
            st.success(f"Concentration after dilution: {C2:.4f} M")

    # ---------------- BUFFER PREPARATION ----------------
    elif practical == "Buffer Preparation":
        st.header("Buffer Preparation")
        st.subheader("Formula: pH = pKa + log([A-]/[HA])")
        acid_base = st.selectbox("Select weak acid:", ["Acetic acid","Citric acid","Phosphoric acid"])
        pKa_vals = {"Acetic acid":4.76,"Citric acid":3.13,"Phosphoric acid":2.12}
        pKa = pKa_vals[acid_base]
        st.info(f"Typical pKa = {pKa}")
        conc_A = st.number_input("Concentration of conjugate base [A-] (M):", min_value=0.0)
        conc_HA = st.number_input("Concentration of weak acid [HA] (M):", min_value=0.0)

        if conc_A>0 and conc_HA>0:
            pH = pKa + math.log10(conc_A/conc_HA)
            st.success(f"Calculated buffer pH = {pH:.4f}")

    # ---------------- COMPLEXOMETRIC TITRATION ----------------
    elif practical == "Complexometric Titration":
        st.header("Complexometric Titration")
        st.subheader("Formula: M1V1 = M2V2")
        M1 = st.number_input("EDTA concentration (M):", min_value=0.0)
        V1 = st.number_input("EDTA volume (mL):", min_value=0.0)
        V2 = st.number_input("Metal solution volume (mL):", min_value=0.0)

        V1_L = V1/1000
        V2_L = V2/1000

        if M1>0 and V1_L>0 and V2_L>0:
            M2 = (M1*V1_L)/V2_L
            st.success(f"Metal ion concentration = {M2:.4f} M")

    # ---------------- COLORIMETRY / ABSORBANCE ----------------
    elif practical == "Colorimetry / Absorbance":
        st.header("Colorimetry / Absorbance")
        st.subheader("Formula: A = ε × l × c → c = A/(ε×l)")
        A = st.number_input("Measured absorbance (A):", min_value=0.0)
        epsilon = st.number_input("Molar absorptivity ε (L/mol·cm):", min_value=0.0)
        path_unit = st.selectbox("Path length unit:", ["cm","mm"])
        path_length = st.number_input("Path length:", min_value=0.0)
        if path_unit=="mm": path_length/=10

        if A>0 and epsilon>0 and path_length>0:
            conc = A/(epsilon*path_length)
            st.success(f"Solution concentration = {conc:.4e} M")

    # ---------------- VOLUMETRIC ANALYSIS ----------------
    elif practical == "Volumetric Analysis":
        st.header("Volumetric Analysis")
        st.subheader("Formula: M1V1/n1 = M2V2/n2")
        M1 = st.number_input("Standard concentration (M):", min_value=0.0)
        V1 = st.number_input("Standard volume (mL):", min_value=0.0)
        n1 = st.number_input("Stoichiometric coeff of standard (n1):", min_value=1)
        V2 = st.number_input("Unknown solution volume (mL):", min_value=0.0)
        n2 = st.number_input("Stoichiometric coeff of unknown (n2):", min_value=1)

        V1_L = V1/1000
        V2_L = V2/1000

        if M1>0 and V1_L>0 and V2_L>0:
            M2 = (M1*V1_L*n2)/(V2_L*n1)
            st.success(f"Concentration of unknown solution = {M2:.4f} M")
