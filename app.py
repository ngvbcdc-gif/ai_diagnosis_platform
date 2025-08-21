import streamlit as st

st.set_page_config(
    page_title="الطبيب الافتراضي",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Header ---
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE; font-family: Arial, sans-serif;'>
        الطبيب الافتراضي 🩺
    </h1>
    <p style='text-align: center; font-size:18px; color: #555;'>
        تشخيص الأمراض بناءً على الأعراض وإعطاء النصائح العلاجية المناسبة.
    </p>
    <hr>
""", unsafe_allow_html=True)

# --- Sidebar for input ---
st.sidebar.header("أدخل الأعراض")
symptoms = st.sidebar.text_area("اكتب أعراضك هنا:", height=150)

# --- Main content ---
if st.sidebar.button("تشخيص"):
    if not symptoms.strip():
        st.warning("الرجاء إدخال الأعراض أولاً")
    else:
        # هنا تضيف دالة التشخيص الخاصة بك
        # مثلاً:
        diagnosis = "احتمال الإصابة بإنفلونزا"
        advice = "ينصح بالراحة، شرب السوائل، واستشارة الطبيب إذا استمر التعب."

        st.markdown(f"""
            <div style="background-color:#DFF2FF; padding:20px; border-radius:10px; margin-top:20px;">
                <h2 style="color:#0B3D91;">التشخيص:</h2>
                <p style="font-size:20px;">{diagnosis}</p>
                <h3 style="color:#0B3D91;">نصيحة العلاج:</h3>
                <p style="font-size:18px;">{advice}</p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("يرجى إدخال الأعراض في الشريط الجانبي ثم الضغط على زر التشخيص")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: #888; font-size:14px;'>
        © 2025 الطبيب الافتراضي. جميع الحقوق محفوظة.
    </p>
""", unsafe_allow_html=True)
