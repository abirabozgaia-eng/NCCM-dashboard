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
    .stButton>button { background-color: #dc2626; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 50px; border: none; font-size: 16px; }
    .stButton>button:hover { background-color: #b91c1c; color: white; }
    .kpi-box { background-color: #1f2937; padding: 20px; border-radius: 12px; border-top: 4px solid #ef4444; text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); }
    .kpi-box h4 { color: #9ca3af; margin-bottom: 5px; font-size: 15px; }
    .kpi-box h2 { color: #f9fafb; margin: 0; font-size: 28px; }
    .system-status { background-color: #1e293b; padding: 25px; border-radius: 12px; border-left: 5px solid #10b981; color: #f1f5f9; font-size: 16px; line-height: 1.8; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2); }
    .recommendation-item { background-color: #0f172a; padding: 10px 15px; border-radius: 6px; margin-top: 10px; border-right: 4px solid #3b82f6; text-align: right; }
    </style>
""", unsafe_allow_html=True)

# 2. المحرك التحليلي المدمج الذكي (Stitch AI Built-in Logic)
def process_emergency_intelligence(incident, municipality, details):
    """محرك محاكاة ذكي مدمج لتصنيف البلاغات واستخراج التوصيات السيادية فوراً"""
    analysis = {}
    
    if incident == "صدمات مناخية وسيول جارفة":
        analysis["level"] = "🔴 حرج جداً (مستوى الخطر: مرتفع)"
        analysis["zone"] = f"النطاق البلدي المستهدف: {municipality}"
        analysis["summary"] = f"تأكيد رصد تدفقات مائية غير مستقرة ناجمة عن صدمة مناخية حادة. المؤشرات الميدانية تدل على احتمالية حدوث انجرافات في التربة بالقرب من المجمعات السكنية والمرافق الحيوية نظراً لطبيعة البلاغ الوارد: '{details}'."
        analysis["steps"] = [
            "🚨 تفعيل خطة الطوارئ (ب) وإعلان حالة الاستنفار القصوى في البلدية المعنية.",
            "📡 توجيه فرق الطوارئ الميدانية لتأمين مصارف المياه وحماية النقاط المنخفضة.",
            "📢 إرسال تناهي وإنذارات مبكرة للسكان عبر منصة الإعلام الموحد لإخلاء الطوابق الأرضية القريبة من مجاري التدفق.",
            "🚧 نشر حواجز مؤقتة لوقف هبوط التربة وحماية الطرق الاستراتيجية المؤدية للمستشفيات."
        ]
        # إحداثيات تقريبية للمحاكاة الجغرافية لتدفق السيول والسيادة الرقمية
        analysis["coords"] = {'lat': [32.8872, 32.8943, 32.8751], 'lon': [13.1901, 13.1724, 13.2145]}
        
    elif incident == "تآكل الشواطئ وارتفاع منسوب البحر":
        analysis["level"] = "🟠 مرتفع (مستوى الخطر: متوسط إلى حرج)"
        analysis["zone"] = f"الشريط الساحلي: {municipality}"
        analysis["summary"] = f"المؤشرات الجغرافية تؤكد تسارع معدلات تآكل التربة الشاطئية مع رصد تصدعات في الحواجز الخرسانية الحامية. استناداً إلى البيانات الحالية: '{details}'، فإن الخطر يهدد البنية التحتية القريبة مباشرة من خط الساحل الأول."
        analysis["steps"] = [
            "🏗️ النشر الفوري لكتل خرسانية إضافية لدعم الحواجز المتضررة بشكل مؤقت.",
            "🗺️ الاستعانة بنظم المعلومات الجغرافية الجارية لتحديد مسار زحف مياه البحر خلال الـ 48 ساعة القادمة.",
            "🛑 إغلاق الطرق الساحلية الفرعية المحاذية لمنطقة الهبوط حفاظاً على سلامة المركبات.",
            "💧 تفعيل غرف العمليات المشتركة لمراقبة جودة المياه الجوفية ومنع تملح الآبار القريبة."
        ]
        analysis["coords"] = {'lat': [32.9021, 32.9150, 32.8910], 'lon': [13.1510, 13.2100, 13.1250]}
        
    elif incident == "انهيار بـنية تحتية وطرق":
        analysis["level"] = "🔴 حرج (مستوى الخطر: مرتفع)"
        analysis["zone"] = f"المحور اللوجستي: {municipality}"
        analysis["summary"] = f"انهيار أو هبوط جزئي في شبكة الطرق الجذعية يعيق حركة الآليات والخدمات الحيوية. نص البلاغ المرصود: '{details}' يشير إلى ضرورة التدخل الهندسي السريع لمنع اتساع رقعة الانهيار."
        analysis["steps"] = [
            "🚒 تحويل مسارات السير بالتنسيق مع شرطة المرور لتأمين تدفق سيارات الإسعاف والطوارئ.",
            "🛠️ إرسال فريق هندسي استشاري ميداني لتقييم السلامة الهيكلية للجسور والطرق المحيطة.",
            "🔌 عزل خطوط الإمداد (كهرباء، مياه، غاز) المارة أسفل المنطقة المتضررة لتجنب الحوادث الثانوية.",
            "📊 تحديث السجل الوطني للمخاطر لتصنيف هذا المحور كمنطقة غير آمنة مؤقتاً."
        ]
        analysis["coords"] = {'lat': [32.8610, 32.8720, 32.8550], 'lon': [13.1810, 13.1950, 13.2210]}
        
    else:
        analysis["level"] = "⚪ تنبيه عام"
        analysis["zone"] = f"النطاق المحدد: {municipality}"
        analysis["summary"] = f"بلاغ عام بحاجة إلى تدقيق ميداني إضافي للتصنيف النهائي. تفاصيل: {details}"
        analysis["steps"] = ["🔍 إرسال دورية استطلاع ميدانية للتحقق.", "📈 مراقبة البلاغات المشابهة عبر النظام الموحد."]
        analysis["coords"] = {'lat': [32.8872], 'lon': [13.1901]}
        
    return analysis

# 3. الواجهة الرئيسية للمنصة ونظام القيادة والسيطرة السيادي
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

# 4. شاشة معالجة البلاغات الميدانية (Stitch Intelligence Outbound Module)
st.header("⚙️ محرك الاستجابة والتحليل الذكي الموحد (Stitch AI Outbound Engine)")
st.write("يقوم هذا القسم بمحاكاة وتصدير القوالب التفاعلية ومخرجات النموذج المطور عبر Stitch لتصنيف المخاطر آلياً وتوجيهها للبلديات المعنية:")

col_input, col_output = st.columns([1, 1])

# وضع الإحداثيات الافتراضية المبدئية للخريطة لتجنب الأخطاء البرمجية عند الإقلاع
current_lat = [32.8872, 32.8943, 32.8751]
current_lon = [13.1901, 13.1724, 13.2145]

with col_input:
    st.subheader("📥 مدخلات البلاغ الميداني الموحد")
    incident_type = st.selectbox("نوع الخطر المرصود:", ["صدمات مناخية وسيول جارفة", "تآكل الشواطئ وارتفاع منسوب البحر", "انهيار بـنية تحتية وطرق", "أخرى"])
    municipality_target = st.text_input("البلدية المستهدفة أو النطاق الجغرافي:", "المنطقة الساحلية / طرابلس")
    raw_report = st.text_area("نص البلاغ الوارد من غرف العمليات الفرعية:", "رصد تدفق غير مستقر للمياه مع مؤشرات هبوط في التربة القريبة من النطاق السكني الحرج.")
    
    submit_btn = st.button("🚀 معالجة وتمرير البلاغ عبر محرك الذكاء الاصطناعي")

with col_output:
    st.subheader("📤 تحليلات ومخرجات محرك الاستجابة الموحد")
    if submit_btn:
        with st.spinner("جاري استخراج السجلات وتحليل مصفوفة المخاطر السيادية..."):
            # استدعاء المحرك التحليلي
            res = process_emergency_intelligence(incident_type, municipality_target, raw_report)
            
            # تحديث إحداثيات الخريطة تفاعلياً بناءً على اختيار نوع الأزمة
            current_lat = res["coords"]["lat"]
            current_lon = res["coords"]["lon"]
            
            # بناء المظهر الخارجي الذكي المطابق لتصميم Stitch
            st.markdown(f"""
            <div class="system-status">
                <h3 style="color: #f3f4f6 !important; margin-top:0;">📊 مخرجات تصنيف الأزمة الفورية:</h3>
                <hr style="border-color: #4b5563;">
                <p><b>مستوى الخطورة السيادية:</b> <span style="color: #f87171; font-weight:bold;">{res["level"]}</span></p>
                <p><b>النطاق الجغرافي للحدث:</b> {res["zone"]}</p>
                <p><b>التحليل الهيكلي للبلاغ:</b> {res["summary"]}</p>
                <h4 style="color: #60a5fa !important; margin-bottom: 5px;">🛠️ التوصيات والإجراءات الفورية لغرفة العمليات:</h4>
            </div>
            """, unsafe_allow_html=True)
            
            for step in res["steps"]:
                st.markdown(f'<div class="recommendation-item">{step}</div>', unsafe_allow_html=True)
    else:
        st.info("💡 أدخل بيانات البلاغ في القائمة الجانبية واضغط على الزر الأزرق لعرض وتمرير التوصيات الذكية حياً.")

st.write("---")

# 5. نظام الخرائط الجغرافية التفاعلي المباشر (GIS Mapping) بناءً على مخرجات الـ AI
st.header("🌐 الخرائط التفاعلية لانتشار البلاغات الحية (GIS Mapping)")
radius_slider = st.slider("ضبط شعاع تحليل خطورة الحادث الميداني (كيلومتر):", 5, 50, 15)

# تجهيز البيانات الجغرافية الحية لعرض الدوائر الحمراء التفاعلية للأزمات
map_data = pd.DataFrame({
    'lat': current_lat,
    'lon': current_lon
})

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=np.mean(current_lat),
        longitude=np.mean(current_lon),
        zoom=11,
        pitch=45,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[lon, lat]',
            get_color='[239, 68, 68, 180]',  # اللون الأحمر المطابق لمنصة الطوارئ
            get_radius=radius_slider * 100,  # التحكم التفاعلي بالشعاع الجغرافي
            pickable=True,
        ),
    ],
))

st.caption("🚨 يتم تحديث الإحداثيات الجغرافية وبؤرة انتشار الدوائر الحمراء تفاعلياً على الخريطة فور النقر على زر معالجة الأزمة بالأعلى.")
