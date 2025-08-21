import streamlit as st
from transformers import pipeline
from deep_translator import GoogleTranslator

# تحميل النموذج من Hugging Face
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

model = load_model()

# إعدادات الصفحة
st.set_page_config(page_title="الطبيب الافتراضي", layout="wide", page_icon="🧠")

# تصميم CSS لتحسين المظهر
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 2rem 3rem;
    }
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #0a71c5;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #555555;
        margin-bottom: 2rem;
    }
    .textarea {
        font-size: 1.1rem;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #ddd;
        background-color: white;
        width: 100%;
    }
    .btn-primary {
        background-color: #0a71c5;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
    .btn-primary:hover {
        background-color: #065a9f;
    }
    .footer {
        font-size: 0.9rem;
        color: #999999;
        margin-top: 3rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<h1 class="title">🧠 الطبيب الافتراضي (مجاني)</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">📝 اكتب الأعراض التي تشعر بها باللغة العربية وسنقوم بتحليل مبدئي باستخدام الذكاء الاصطناعي.</p>', unsafe_allow_html=True)

    symptoms_ar = st.text_area("✍️ اكتب الأعراض هنا:", height=140, key="symptoms_input", help="مثلاً: صداع، سعال، حمى...")

    if st.button("تشخيص", key="diagnose_button"):
        if symptoms_ar.strip() != "":
            with st.spinner("🧠 جاري تحليل الأعراض..."):
                try:
                    symptoms_en = GoogleTranslator(source='auto', target='en').translate(symptoms_ar)
                    result = model(symptoms_en)
                    result_text_en = result[0]['label']
                    result_text_ar = GoogleTranslator(source='en', target='ar').translate(result_text_en)

                    advice_map = {
                        "1 star": "ننصح بمراجعة الطبيب فوراً.",
                        "2 stars": "يمكن استخدام مسكنات خفيفة مثل الباراسيتامول.",
                        "3 stars": "الأعراض خفيفة، راحة وشرب ماء كثير مفيد.",
                        "4 stars": "الأعراض معتدلة، يمكن استخدام أدوية مساعدة بعد استشارة الصيدلي.",
                        "5 stars": "الأعراض جيدة، حافظ على نمط حياة صحي."
                    }
                    advice = advice_map.get(result_text_en, "يرجى مراجعة طبيب مختص.")

                    st.success("✅ التشخيص المبدئي:")
                    st.markdown(f"**⚕️ التحليل:** {result_text_ar}")
                    st.markdown(f"📊 (التقييم من النموذج: `{result_text_en}`)")
                    st.info(f"💊 **نصيحة دوائية:** {advice}")

                except Exception as e:
                    st.error(f"حدث خطأ أثناء التحليل: {e}")
        else:
            st.warning("يرجى إدخال الأعراض أولاً.")

    st.markdown('<div class="footer">تم ابتكاره و تطويره من قبل مبارك الرشيدي</div>', unsafe_allow_html=True)
