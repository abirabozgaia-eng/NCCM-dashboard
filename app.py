import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk

# 1. إعدادات الصفحة والهوية البصرية للمنصة السيادية
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
    
    /* تنسيق صندوق محرك الأزمات الذكي */
    .stitch-container { background-color: #1f2937; padding: 25px; border-radius: 12px; border-right: 5px solid #3b82f6; margin-bottom: 25px; }
    .agent-response { background-color: #111827; border: 1px solid #374151; padding: 20px; border-radius: 8px; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# 2. الواجهة الرئيسية للمنصة ونظام القيادة والسيطرة السيادي
st.markdown('<h1 class="main-title">🚨 منصة الإعلام الموحد لإدارة الطوارئ والأزمات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #9ca3af; font-size: 16px; margin-top: -15px;">المركز الوطني للقيادة والسيطرة | منظومة المعالجة الفورية والتحليل الجغرافي الذكي للأحداث والمخاطر</p>', unsafe_allow_html=True)

# عرض المؤشرات الحيوية الرقمية (KPIs) لغرف الطوارئ
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="kpi-box"><h4>🔴 الأزمات النشطة</h4><h2>3 مناطق حرجـة</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="kpi-box"><h4>🌐 البلديات المتصلة</h4><h2>14 / 14 بلديات</h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="kpi-box"><h4>⚠️ تنبيهات الإخلاء</h4><h2>2 بـلاغ معلّـق</h2></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="kpi-box"><h4>🛡️ السيادة الرقمية</h4><h2>مؤمن بالكامل (محلي)</h2></div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.write("---")

# 3. محرك الاستجابة والتحليل الذكي الموحد (Stitch AI Local Outbound Engine)
st.header("⚙️ محرك الاستجابة والتحليل الذكي الموحد (Stitch AI Outbound Engine)")
st.write("بيئة تفاعلية مدمجة بالكامل لإدارة وتحليل البلاغات الواردة وصياغة الإعلام الموحد:")

# بناء واجهة الاستجابة الذكية محلياً داخل بيئة العمل
st.markdown('<div class="stitch-container">', unsafe_allow_html=True)
st.subheader("🤖 نظام معالجة الرسائل التفاعلي وإعلام الأزمات")

# خيارات نوع الخطر المرصود
hazard_type = st.selectbox(
    "اختر نوع الخطر المرصود في الميدان لتنشيط النموذج:",
    ["تآكل الشواطئ وارتفاع منسوب البحر", "صدمات مناخية وسيول جارفة", "انهيار بنية تحتية وطرق", "أخرى"]
)

# مدخلات إضافية لوصف الحالة وموقعها الجغرافي
location_input = st.text_input("البلدية المستهدفة أو النطاق الجغرافي:", value="المنطقة الساحلية / طرابلس")
additional_details = st.text_area("أدخل تفاصيل البلاغ الوارد من المركز الميداني (اختياري):", placeholder="رصد تدفق غير مستقر للمياه مع مؤشرات هبوط في التربة القريبة من النطاق السكني...")

# زر المعالجة والتشغيل الفوري للـ Agent
if st.button("🚀 تشغيل المحرك ومعالجة البلاغ فورياً"):
    st.markdown('<div class="agent-response">', unsafe_allow_html=True)
    st.markdown("### 📋 الاستجابة الفورية للمحرك الموحد:")
    
    # محاكاة ذكية مخصصة ومطابقة لأهداف مشروعكِ السيادي بناءً على المدخلات
    if hazard_type == "تآكل الشواطئ وارتفاع منسوب البحر":
        st.error("⚠️ **حالة التنبيه الحالية: خطورة مرتفعة (مستوى 4)**")
        st.write(f"**التحليل الجغرافي:** تم تأكيد رصد تآكل متسارع في شريط التربة ببلدية **{location_input}**.")
        st.write("**توصية النموذج الذكي للعمليات:**")
        st.write("1. تفعيل خطة الطوارئ 'ج' وتوجيه فرق الرصد الميداني لإيقاف خطوط السير القريبة.")
        st.write("2. صياغة بيان الإعلام الموحد الموجه للسكان لتوخي الحيطة والابتعاد عن حرَم الشاطئ بمسافة لا تقل عن 500 متر.")
    else:
        st.warning("⚠️ **حالة التنبيه الحالية: قيد التقييم والمتابعة**")
        st.write(f"تم تسجيل البلاغ بنجاح لنطاق **{location_input}** وجاري مطابقة البيانات الجغرافية الحية لمعالجة المخاطر.")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.write("---")

# 4. نظام الخرائط الجغرافية التفاعلي المباشر (GIS Mapping)
st.header("🌐 الخرائط التفاعلية لانتشار البلاغات الحية (GIS Mapping)")
radius_slider = st.slider("ضبط شعاع تحليل خطورة الحادث الميداني (كيلومتر):", 5, 50, 15)

# إحداثيات تقريبية للأزمات الميدانية الجارية لتفعيل الخريطة فورياً
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
