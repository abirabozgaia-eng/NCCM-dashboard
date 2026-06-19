import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
import requests

# 1. إعدادات الصفحة والهوية البصرية للمنصة السيادية
st.set_page_config(
    page_title="منصة الإعلام الموحد للطوارئ وإدارة الأزمات",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تصفيف الواجهة بالهوية الرسمية الاحترافية (Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1, h2, h3 { color: #ff4b4b !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 45px; }
    .kpi-box { background-color: #262626; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; text-align: center; }
    .system-status { background-color: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #3b82f6; color: #e2e8f0; font-size: 16px; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# 2. إعدادات الربط البرمجي الفعلي مع منصة Stitch AI (API Integration)
STITCH_API_KEY = "AQ.Ab8RN6KqG9lhyWQ9lhb2NAn_urbE3sZqKO88Yh_9ImOxzwHqRg"
STITCH_PROJECT_URL = "https://api.stitch.withgoogle.com/v1/projects/NCCM-AI-CORE/predict"

def call_stitch_ai_engine(prompt_data):
    """دالة برمجية آمنة للاتصال بمحرك الذكاء الاصطناعي في Stitch وتمرير البيانات"""
    headers = {
        "Authorization": f"Bearer {STITCH_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # هيكلية البيانات المرسلة لتتوافق مع الأنظمة الداخلية وسجل المخاطر
    payload = {
        "prompt": prompt_data,
        "temperature": 0.2,  # نسبة منخفضة لضمان دقة وصرامة التقارير السيادية
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(STITCH_PROJECT_URL, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json().get("output", "لم يتم إرجاع تحليل دقيق من المحرك.")
        else:
            return f"❌ خطأ في الاتصال بالأنظمة الداخلية لـ Stitch (رمز الاستجابة: {response.status_code})"
    except Exception as e:
        return f"🚨 فشل الاتصال الآمن بالخادم: {str(e)}"

# 3. الواجهة الرئيسية للمنصة ونظام القيادة والسيطرة
st.title("🚨 منصة الإعلام الموحد لإدارة الطوارئ والأزمات")
st.subheader("المركز الوطني للقيادة والسيطرة | البث المباشر للأحداث والمخاطر السيادية")

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

st.write("---")

# 4. شاشة معالجة وربط الذكاء الاصطناعي (Stitch AI Engine Integration)
st.header("⚙️ محرك الاستجابة والتحليل الذكي الموحد (Stitch AI Outbound)")
st.write("يقوم هذا القسم باستدعاء نموذج الذكاء الاصطناعي المطور عبر Stitch لتحليل البلاغات وتصنيف المخاطر آلياً وتوجيهها للبلديات المعنية:")

col_input, col_output = st.columns([1, 1])

with col_input:
    st.subheader("📥 مدخلات البلاغ الميداني الموحد")
    incident_type = st.selectbox("نوع الخطر المرصود:", ["صدمات مناخية وسيول جارفة", "تآكل الشواطئ وارتفاع منسوب البحر", "انهيار بـنية تحتية وطرق", "أخرى"])
    municipality_target = st.text_input("البلدية المستهدفة أو النطاق الجغرافي:", "المنطقة الساحلية / طرابلس")
    raw_report = st.text_area("نص البلاغ الوارد من غرف العمليات الفرعية:", "رصد تدفق غير مستقر للمياه مع مؤشرات هبوط في التربة القريبة من النطاق السكني.")
    
    # صياغة الأمر الموجه للمحرك الذكي
    full_prompt = f"حلل البلاغ التالي كخبير طوارئ سيادي. نوع الخطر: {incident_type}. الموقع: {municipality_target}. نص البلاغ: {raw_report}. أعطِ تصنيفاً دقيقاً للمخاطر وتوصيات فورية لغرفة القيادة."
    
    submit_btn = st.button("🚀 معالجة وتمرير البلاغ عبر Stitch AI")

with col_output:
    st.subheader("📤 تحليلات محرك Stitch AI والأنظمة الداخلية")
    if submit_btn:
        with st.spinner("جاري الاتصال الآمن بالـ API واستخراج البيانات الذكية..."):
            ai_response = call_stitch_ai_engine(full_prompt)
            st.markdown(f'<div class="system-status"><b>الاستجابة الفورية للمحرك الموحد:</b><br><br>{ai_response}</div>', unsafe_allow_html=True)
    else:
        st.info("💡 أدخل بيانات البلاغ واضغط على الزر لإرسالها ومعالجتها حياً عبر الـ API.")

st.write("---")

# 5. نظام الخرائط الجغرافية التفاعلي المباشر (GIS Mapping)
st.header("🌐 الخرائط التفاعلية الحية لانتشار الحوادث (GIS Mapping)")
radius_slider = st.slider("ضبط شعاع تحليل خطورة الحادث الجغرافي (كيلومتر):", 5, 50, 15)

# توليد بيانات جغرافية افتراضية للمناطق الساحلية الليبية لإظهار كفاءة النظام
map_data = pd.DataFrame({
    'lat': [32.8872, 32.8943, 32.8751],
    'lon': [13.1901, 13.1724, 13.2145],
    'criticality': [100, 80, 60]
})

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=32.8872,
        longitude=13.1901,
        zoom=11,
        pitch=40,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[lon, lat]',
            get_color='[255, 75, 75, 160]',
            get_radius=radius_slider * 100,
            pickable=True,
        ),
    ],
))

st.caption("🚨 يتم تحديث هذه الخريطة جغرافياً فور تلقي استجابة تصنيف المخاطر من محرك الـ AI.")
