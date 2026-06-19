import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

# --------------------------------------------------------
# 1. IDENTITY & ACCESS MANAGEMENT (IAM) CONFIGURATION
# --------------------------------------------------------
# HARDCODED SUPER ADMIN (Replace with your actual Gmail if needed)
SUPER_ADMIN_EMAIL = "your-email@gmail.com"

# Define Roles and Permissions Matrix
ROLE_PERMISSIONS = {
    "Super Admin": {"can_view": True, "can_broadcast": True, "can_edit_settings": True, "can_clear_logs": True},
    "Operations Manager": {"can_view": True, "can_broadcast": True, "can_edit_settings": False, "can_clear_logs": False},
    "Field Dispatcher": {"can_view": True, "can_broadcast": False, "can_edit_settings": False, "can_clear_logs": False},
    "Public Observer": {"can_view": True, "can_broadcast": False, "can_edit_settings": False, "can_clear_logs": False}
}

# --------------------------------------------------------
# 2. PAGE INITIALIZATION & SECURITY GATEWAY
# --------------------------------------------------------
st.set_page_config(
    page_title="Unified Crisis Command Center",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark/Professional Command Center Styling via CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 8px; border-left: 5px solid #ef4444; }
    .critical-alert { padding: 15px; background-color: #7f1d1d; border-radius: 5px; margin-bottom: 10px; }
    .verified-fact { padding: 10px; background-color: #064e3b; border-radius: 5px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Session State for Simulated Login
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_role" not in st.session_state:
    st.session_state.user_role = "Public Observer"

# --- SIDEBAR: SECURE AUTHENTICATION SIMULATOR ---
st.sidebar.title("🔐 Secure Identity Access")
email_input = st.sidebar.text_input("Enter Registered Email Address:", value=st.session_state.user_email)

# Gateway Authentication Logic
if email_input:
    st.session_state.user_email = email_input.strip().lower()
    if st.session_state.user_email == SUPER_ADMIN_EMAIL.lower():
        st.session_state.user_role = "Super Admin"
        st.sidebar.success(f"👑 Authenticated as Root Super Admin")
    else:
        # Fallback matrix simulation for testing other roles
        st.session_state.user_role = st.sidebar.selectbox(
            "Select Simulated Staff Role (Testing Mode):",
            ["Operations Manager", "Field Dispatcher", "Public Observer"]
        )
else:
    st.session_state.user_role = "Public Observer"

# Fetch permissions for active identity
current_perms = ROLE_PERMISSIONS[st.session_state.user_role]

st.sidebar.markdown("---")
st.sidebar.subheader("Identity Privileges")
st.sidebar.json(current_perms)

# --------------------------------------------------------
# 3. DASHBOARD MAIN HEADER & SOVEREIGN STATUS BAR
# --------------------------------------------------------
st.title("🚨 Unified Emergency Management & Crisis Platform")
st.subheader("National Command & Control Center | Incident Live Stream")
st.markdown("---")

# Metrics Grid (Stacked clean execution blocks)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="🔴 Active Crises", value="3 Major Zones")
with m2:
    st.metric(label="🏢 Connected Municipalities", value="14/14 Online")
with m3:
    st.metric(label="⚠️ Pending Evacuation Alerts", value="2 Reg. Pushed")
with m4:
    st.metric(label="🛡️ System Sovereignty Status", value="Secured & Encrypted")

st.markdown("---")

# --------------------------------------------------------
# 4. INTERACTIVE CRISIS MAPPING (GIS SIMULATION)
# --------------------------------------------------------
st.header("🌐 Live Regional Incident GIS Mapping")
risk_radius = st.slider("Adjust Hazard Analysis Radius (Kilometers)", 1, 50, 15)

# Generate simulated coordinates relative to capital/center area
map_data = pd.DataFrame({
    'lat': [32.8872, 32.8750, 32.8990],
    'lon': [13.1912, 13.1600, 13.2100],
    'incident': ['Flash Flood - Sector Alpha', 'Critical Grid Failure - Substation 4', 'Logistics Blockade - Highway South'],
    'severity': [150, 90, 200] # Controls visual radius sizes
})

# Render Pydeck High-Visibility Map Layer
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=32.8872,
        longitude=13.1912,
        zoom=11,
        pitch=40,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[lon, lat]',
            get_color='[239, 68, 68, 160]', # High visibility red-orange alert glow
            get_radius=risk_radius * 100,
            pickable=True
        ),
    ],
    tooltip={"text": "{incident}"}
))

st.markdown("---")

# --------------------------------------------------------
# 5. UNIFIED CRISIS COMMUNICATION HUB & ANTI-RUMOR LEDGER
# --------------------------------------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.header("📢 Official Multi-Channel Broadcast Center")
    
    # Access Enforcement Check for broadcasting
    if current_perms["can_broadcast"]:
        st.info("🔓 Access Granted: You have credentials to dispatch emergency broadcasts to TV, SMS, and Radio systems.")
        broadcast_text = st.text_area("Compose Instant Unified Public Alert:")
        if st.button("🚨 Deploy Omnichannel Emergency Alert"):
            st.success(f"Broadcast successfully queued and digitally signed by {st.session_state.user_email}.")
    else:
        st.error("🔒 Access Denied: Your current role does not have authorization to issue public emergency broadcasts.")

with col_right:
    st.header("🛡️ Public Fact-Checking & Anti-Rumor Ledger")
    st.markdown("Live verification matrix to prevent panic and secure public digital spaces:")
    
    # Simulated Anti-Rumor Relational Array
    rumor_data = {
        "Circulating Rumor / Misinformation": [
            "Main water treatment plant completely offline for two weeks.",
            "Evacuation order expanded to the entire Northern sector.",
            "Local fuel supplies completely depleted near central grid."
        ],
        "Verified Field Truth (Official Reality)": [
            "Plant offline for scheduled 4-hour technical mitigation. Online by 22:00.",
            "Evacuation is strictly limited to low-lying properties on Sector Alpha Basin.",
            "Strategic fuel reserves remain at 84% capacity. Distribution ongoing."
        ],
        "Verification Status": ["🟢 Resolved Fact", "🟢 Clarified", "🟡 Monitoring"]
    }
    df_rumors = pd.DataFrame(rumor_data)
    st.table(df_rumors)

st.markdown("---")

# --------------------------------------------------------
# 6. EMERGENCY RESOURCE ALLOCATOR (DYNAMIC ENGINE)
# --------------------------------------------------------
st.header("🧮 Dynamic Resource Allocation & Containment Forecasting")
st.markdown("Adjust operational field assets to dynamically project regional resilience recovery targets.")

res_teams = st.slider("Mobilized Rescue & Extraction Teams", 5, 100, 30)
med_units = st.slider("Mobile Medical Response Units Deployment", 2, 50, 12)

# Dynamic backend algorithmic forecasting formulas
projected_containment = max(1.5, round(48 - (res_teams * 0.3) - (med_units * 0.5), 1))
resilience_index = min(100, round(30 + (res_teams * 0.5) + (med_units * 1.2)))

c1, c2 = st.columns(2)
with c1:
    st.metric(label="⏱️ Projected Crisis Containment Window", value=f"{projected_containment} Hours", delta="-Estimated Time")
with c2:
    st.metric(label="📊 Computed Regional Resilience Index", value=f"{resilience_index}%", delta="+Stability Scale")

# --------------------------------------------------------
# 7. ROOT CONFIGURATION & AUDIT SYSTEM (SUPER ADMIN ONLY)
# --------------------------------------------------------
st.markdown("---")
st.header("⚙️ Critical Platform Administration & Core Infrastructure Settings")

if current_perms["can_edit_settings"] and st.session_state.user_email == SUPER_ADMIN_EMAIL.lower():
    st.success(f"👑 Root Verification Success: Welcome, Master Admin ({SUPER_ADMIN_EMAIL}).")
    
    col_adm1, col_adm2 = st.columns(2)
    with col_adm1:
        st.checkbox("Force Encryption Token Rotation (Hourly)", value=True)
        st.checkbox("Restrict Cross-Border Telemetry Feed Access", value=False)
    with col_adm2:
        if st.button("🗑️ Purge Operational System Logs"):
            st.warning("All temporary operational logs have been securely cleared from memory.")
else:
    st.error(f"🛑 Security Intercept: Infrastructure controls are reserved strictly for Root Admin ({SUPER_ADMIN_EMAIL}). Access Blocked.")
