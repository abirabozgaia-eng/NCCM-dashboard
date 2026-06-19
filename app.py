import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk

# 1. إعدادات الصفحة والهوية البصرية للمنصة السيادية للقيادة والسيطرة
st.set_page_config(
    page_title="منصة الإعلام الموحد للطوارئ وإدارة الأزمات",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تصفيف الواجهة بالكامل بالهوية الرسمية الاحترافية (Dark Cyber Theme)
st.markdown("""
    <style>
    .main { background-color: #111827; color: #ffffff; }
    h1, h2, h3, h4 { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: bold; }
    .main-title { color: #ef4444; text-align: center; padding: 10px; border-bottom: 2px solid #ef4444; margin-bottom: 20px; }
    .kpi-box { background-color: #1f2937; padding: 20px; border-radius: 12px; border-top: 4px solid #ef4444; text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); }
    .kpi-box h4 { color: #9ca3af; margin-bottom: 5px; font-size: 15px; }
    .kpi-box h2 { color: #f9fafb; margin: 0; font-size: 28px; }
    .iframe-container { border: 2px solid #ef4444; border-radius: 12px; overflow: hidden; background-color: #ffffff; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.5); }
    </style>
""", unsafe_allow_html=True)

# 2. الواجهة الرئيسية للمنصة ونظام القيادة والسيطرة السيادي
st.markdown('<h1 class="main-title">🚨 منصة الإعلام الموحد لإدارة الطوارئ والأزمات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #9ca3af; font-size: 16px; margin-top: -15px;">المركز الوطني للقيادة والسيطرة | البث المباشر للأحداث والمخاطر السيادية والربط مع الأداة الذكية لـ Stitch</p>', unsafe_allow_html=True)

# عرض المؤشرات الحيوية الرقمية (KPIs) لغرف الطوارئ
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="kpi-box"><h4>🔴 الأزمات النشطة</h4><h2>3 مناطق حرجـة</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="kpi-box"><h4>🌐 البلديات المتصلة</h4><h2>14 / 14 بلديات</h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="kpi-box"><h4>⚠️ تنبيهات الإخلاء</h4><h2>2 بـلاغ معلّـق</h2></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="kpi-box"><h4>🛡️ السيادة الرقمية</h4><h2>مؤمن بالكامل</h2></div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.write("---")

# 3. جلب وعرض مشروع Stitch الفعلي بالكامل أونلاين كما هو مصمم
st.header("⚙️ محرك الاستجابة والتحليل الذكي الموحد (Stitch AI Outbound Engine)")
st.write("يتم الآن استدعاء وتحميل مشروعكِ الفعلي بالكامل من خادم النشر أونلاين لتجربة تفاعلية مباشرة ومطابقة لتصميمكِ:")

# رابط النشر والمشاركة المباشر الخاص بمشروعك
STITCH_PROJECT_EMBED_URL = "https://stitch.withgoogle.com/projects/12533418267134678038"

# تضمين الواجهة بالكامل داخل المنصة السيادية بصورة احترافية ومتحركة
st.markdown(f"""
<div class="iframe-container">
    <iframe src="{STITCH_PROJECT_EMBED_URL}" width="100%" height="700px" style="border:none; background: #ffffff;" allow="microphone; camera; clipboard-write"></iframe>
</div>
""", unsafe_allow_html=True)

st.write("---")

# 4. نظام الخرائط الجغرافية التفاعلي المباشر (GIS Mapping)
st.header("🌐 الخرائط التفاعلية لانتشار البلاغات الحية (GIS Mapping)")
radius_slider = st.slider("ضبط شعاع تحليل خطورة الحادث الميداني (كيلومتر):", 5, 50, 15)

# إحداثيات تقريبية للأزمات الميدانية الجارية
map_data = pd.DataFrame({
    'lat': [32.8872, 32.8943, 32.8751],
    'lon': [13.1901, 13.1724, 13.2145]
})

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=32.8872,
        longitude=13.1901,
        zoom=11,
        pitch=45,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[lon, lat]',
            get_color='[239, 68, 68, 180]',
            get_radius=radius_slider * 100,
            pickable=True,
        ),
    ],
))
