import streamlit as st
import math

# ---------- Page Config ----------
st.set_page_config(
    page_title="Virtual Lab Assistant",
    page_icon="🧪",
    layout="wide"
)

# ---------- Header ----------
st.markdown(
    """
    <div style='background-color:#0E1117;padding:20px;border-radius:10px'>
        <h1 style='color:#FFD700;text-align:center;'>🧪 Virtual Lab Assistant</h1>
        <p style='color:white;text-align:center;font-size:18px;'>Interactive virtual chemistry lab with step-by-step guidance and automatic calculations</p>
    </div>
    """, unsafe_allow_html=True
)

st.write("\n")  # spacing

# ---------- Tabs for Practicals ----------
tabs = st.tabs([
    "⚗️ Solution Prep",
    "🧪 Titration",
    "🧾 pH Calc",
    "💧 Dilution",
    "🧂 Buffer Prep",
    "🔬 Complexometric",
    "🎨 Colorimetry",
    "📏 Volumetric"
])

# ---------- 1. Solution Preparation ----------
with tabs[0]:
    st.header("⚗️ Solution Preparation")
    st.write("**Principle:** Prepare solutions of known concentration from solute mass and solvent volume.")
    mass = st.number_input("Enter solute mass (g):", min_value=0.0, step=0.01, key="mass_sol_prep")
    volume = st.number_input("Enter solution volume (L):", min_value=0.0, step=0.01, key="vol_sol_prep")
    if st.button("Calculate Molarity", key="calc_sol_prep"):
        if volume > 0:
            molarity = mass / volume  # Simplified assumption
            st.success(f"Molarity = {molarity:.3f} M")
        else:
            st.error("Volume must be greater than 0")

# ---------- 2. Titration ----------
with tabs[1]:
    st.header("🧪 Titration")
    st.write("**Principle:** Determine unknown concentration using titrant volume.")
    M1 = st.number_input("Enter known concentration (M1, mol/L):", min_value=0.0, step=0.01, key="M1_titr")
    V1 = st.number_input("Enter volume of titrant (V1, L):", min_value=0.0, step=0.01, key="V1_titr")
    V2 = st.number_input("Enter volume of unknown solution (V2, L):", min_value=0.0, step=0.01, key="V2_titr")
    if st.button("Calculate Unknown Concentration (M2)", key="calc_titr"):
        if V2 > 0:
            M2 = (M1 * V1) / V2
            st.success(f"Unknown Concentration M2 = {M2:.3f} M")
        else:
            st.error("V2 must be greater than 0")

# ---------- 3. pH Calculation ----------
with tabs[2]:
    st.header("🧾 pH Calculation")
    st.write("**Principle:** Calculate pH from H+ concentration.")
    H_conc = st.number_input("Enter [H+] concentration (M):", min_value=0.0, step=0.0001, key="H_ph")
    if st.button("Calculate pH", key="calc_ph"):
        if H_conc > 0:
            pH = -math.log10(H_conc)
            st.success(f"pH = {pH:.2f}")
        else:
            st.error("H+ concentration must be greater than 0")

# ---------- 4. Dilution ----------
with tabs[3]:
    st.header("💧 Dilution")
    st.write("**Principle:** Calculate concentration after dilution.")
    C1 = st.number_input("Enter initial concentration (C1, M):", min_value=0.0, step=0.01, key="C1_dil")
    V1_dil = st.number_input("Enter initial volume (V1, L):", min_value=0.0, step=0.01, key="V1_dil")
    V2_dil = st.number_input("Enter final volume (V2, L):", min_value=0.0, step=0.01, key="V2_dil")
    if st.button("Calculate Final Concentration (C2)", key="calc_dil"):
        if V2_dil > 0:
            C2 = (C1 * V1_dil) / V2_dil
            st.success(f"Final Concentration C2 = {C2:.3f} M")
        else:
            st.error("Final volume must be greater than 0")

# ---------- 5. Buffer Preparation ----------
with tabs[4]:
    st.header("🧂 Buffer Preparation")
    st.write("**Principle:** Calculate pH using Henderson-Hasselbalch equation.")
    acid = st.number_input("Enter weak acid concentration (HA, M):", min_value=0.0, step=0.01, key="acid_buf")
    conjugate_base = st.number_input("Enter conjugate base concentration (A-, M):", min_value=0.0, step=0.01, key="base_buf")
    pKa = st.number_input("Enter pKa of the acid:", min_value=0.0, step=0.01, key="pKa_buf")
    if st.button("Calculate Buffer pH", key="calc_buf"):
        if acid > 0:
            pH = pKa + math.log10(conjugate_base / acid)
            st.success(f"Buffer pH = {pH:.2f}")
        else:
            st.error("Acid concentration must be greater than 0")

# ---------- 6. Complexometric Titration ----------
with tabs[5]:
    st.header("🔬 Complexometric Titration")
    st.write("**Principle:** Determine metal ion concentration using complexing agent.")
    known = st.number_input("Enter known concentration (M):", min_value=0.0, step=0.01, key="known_com")
    vol_known = st.number_input("Enter volume of titrant (L):", min_value=0.0, step=0.01, key="vol_known_com")
    vol_unknown = st.number_input("Enter volume of unknown solution (L):", min_value=0.0, step=0.01, key="vol_unknown_com")
    if st.button("Calculate Unknown Concentration", key="calc_com"):
        if vol_unknown > 0:
            unknown = (known * vol_known) / vol_unknown
            st.success(f"Unknown Concentration = {unknown:.3f} M")
        else:
            st.error("Volume of unknown solution must be > 0")

# ---------- 7. Colorimetry ----------
with tabs[6]:
    st.header("🎨 Colorimetry")
    st.write("**Principle:** Determine concentration from absorbance.")
    absorbance = st.number_input("Enter absorbance (A):", min_value=0.0, step=0.01, key="abs_col")
    path_length = st.number_input("Enter path length (l, cm):", min_value=0.1, step=0.01, key="path_col")
    epsilon = st.number_input("Enter molar absorptivity (ε, L/mol*cm):", min_value=0.0, step=0.01, key="eps_col")
    if st.button("Calculate Concentration (C)", key="calc_col"):
        if path_length > 0 and epsilon > 0:
            C = absorbance / (epsilon * path_length)
            st.success(f"Concentration = {C:.5f} M")
        else:
            st.error("Path length and molar absorptivity must be > 0")

# ---------- 8. Volumetric Analysis ----------
with tabs[7]:
    st.header("📏 Volumetric Analysis")
    st.write("**Principle:** Determine unknown quantity using standard solution.")
    vol_standard = st.number_input("Enter volume of standard solution (L):", min_value=0.0, step=0.01, key="vol_std")
    conc_standard = st.number_input("Enter concentration of standard solution (M):", min_value=0.0, step=0.01, key="conc_std")
    vol_unknown_va = st.number_input("Enter volume of unknown solution (L):", min_value=0.0, step=0.01, key="vol_unk_va")
    if st.button("Calculate Unknown Concentration (M2)", key="calc_va"):
        if vol_unknown_va > 0:
            conc_unknown = (conc_standard * vol_standard) / vol_unknown_va
            st.success(f"Unknown Concentration = {conc_unknown:.3f} M")
        else:
            st.error("Volume of unknown solution must be > 0")

# ---------- Footer ----------
st.markdown(
    """
    <div style='background-color:#0E1117;padding:10px;border-radius:5px;margin-top:20px'>
        <p style='color:white;text-align:center;font-size:14px;'>Virtual Lab Assistant | Hackathon 2025 | Developed with Streamlit</p>
    </div>
    """, unsafe_allow_html=True
)
