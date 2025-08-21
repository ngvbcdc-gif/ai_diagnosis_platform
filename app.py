import streamlit as st

# قاموس الأعراض مع التشخيصات + نصائح دوائية
diagnosis_dict = {
    "كحة": {
        "تشخيص": "قد تكون عرض لنزلة برد أو التهاب في الجهاز التنفسي.",
        "علاج": "يمكن استخدام شراب للكحة مثل ديكستروميثورفان، وشرب الكثير من السوائل الدافئة."
    },
    "صداع": {
        "تشخيص": "قد يكون بسبب إجهاد أو صداع نصفي.",
        "علاج": "تناول مسكنات مثل الباراسيتامول أو الإيبوبروفين مع الراحة."
    },
    "حمى": {
        "تشخيص": "ممكن تشير إلى وجود عدوى في الجسم.",
        "علاج": "استخدام خافض حرارة مثل الباراسيتامول وشرب الماء بكثرة."
    },
    "غثيان": {
        "تشخيص": "قد يكون عرض لمشاكل في الجهاز الهضمي.",
        "علاج": "يمكن تناول مضادات الغثيان بعد استشارة الطبيب."
    },
    "دوخة": {
        "تشخيص": "قد تكون نتيجة انخفاض ضغط الدم أو مشاكل في الأذن الداخلية.",
        "علاج": "الجلوس والاسترخاء وشرب الماء، وإذا استمرت استشر الطبيب."
    },
    "ألم في الصدر": {
        "تشخيص": "ينصح باستشارة طبيب فوراً لأنه قد يشير لمشاكل قلبية.",
        "علاج": "يجب مراجعة الطوارئ فوراً."
    },
    "تورم": {
        "تشخيص": "قد يدل على التهاب أو احتباس سوائل.",
        "علاج": "رفع الجزء المصاب واستشارة الطبيب."
    },
    "إرهاق": {
        "تشخيص": "يمكن أن يكون عرضاً لنقص الفيتامينات أو مشاكل في الغدة الدرقية.",
        "علاج": "تناول فيتامينات والحصول على قسط كاف من الراحة."
    },
    "سعال": {
        "تشخيص": "ممكن بسبب التهاب في الجهاز التنفسي أو حساسية.",
        "علاج": "شراب للسعال مع تجنب المهيجات."
    },
    "ضيق في التنفس": {
        "تشخيص": "يحتاج تقييم طبي عاجل، قد يكون ناتج عن الربو أو أمراض القلب.",
        "علاج": "مراجعة الطبيب فوراً."
    },
    "آلام في المفاصل": {
        "تشخيص": "قد تكون التهاب مفاصل أو روماتويد.",
        "علاج": "مسكنات الالتهاب مثل الإيبوبروفين بعد استشارة الطبيب."
    },
    "طفح جلدي": {
        "تشخيص": "قد يدل على حساسية أو عدوى جلدية.",
        "علاج": "استخدام مراهم مضادة للحساسية."
    },
    "إسهال": {
        "تشخيص": "غالباً نتيجة التهاب أو تسمم غذائي.",
        "علاج": "شرب محاليل تعويض السوائل والراحة."
    },
    "إمساك": {
        "تشخيص": "قد يكون بسبب قلة الألياف أو جفاف الجسم.",
        "علاج": "زيادة تناول الألياف والماء."
    },
    "فقدان الشهية": {
        "تشخيص": "يرتبط بأمراض متعددة، من بينها مشاكل في الجهاز الهضمي.",
        "علاج": "مراجعة الطبيب لمعرفة السبب."
    },
    "عطس": {
        "تشخيص": "غالباً بسبب الحساسية أو نزلة برد.",
        "علاج": "مضادات الهيستامين للحساسية."
    }
}

# تصميم الواجهة
st.set_page_config(page_title="🩺 منصة تشخيص الأمراض", page_icon="🩺", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background: #F0F2F6;
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        color: #0B5394;
        font-weight: bold;
        font-size: 2.5rem;
        margin-bottom: 0;
    }
    .subheader {
        color: #1155CC;
        font-size: 1.2rem;
        margin-top: 0;
    }
    .diagnosis {
        background-color: #D9EAD3;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #6AA84F;
        margin-top: 20px;
        font-size: 1.1rem;
    }
    .medication {
        background-color: #FFE599;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #D9B800;
        margin-top: 15px;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<h1 class="title">🩺 منصة تشخيص الأمراض بالعربي</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">أدخل الأعراض التي تشعر بها، وسنقدم تشخيصًا مبدئيًا مع نصيحة علاجية.</p>', unsafe_allow_html=True)

symptoms_input = st.text_area("✍️ اكتب الأعراض هنا (يمكنك ذكر أكثر من عرض مفصول بفاصلة أو نقط):")

if st.button("تشخيص"):
    symptoms = symptoms_input.lower().replace(".", "").split(",")
    symptoms = [s.strip() for s in symptoms if s.strip() != ""]

    if symptoms:
        found_diagnoses = []
        for symptom in symptoms:
            if symptom in diagnosis_dict:
                diag = diagnosis_dict[symptom]
                found_diagnoses.append((symptom, diag["تشخيص"], diag["علاج"]))
        if found_diagnoses:
            st.markdown('<div class="diagnosis">', unsafe_allow_html=True)
            st.success("✅ التشخيص المبدئي بناءً على الأعراض:")
            for symptom, diagnosis, medication in found_diagnoses:
                st.markdown(f"• **{symptom}**: {diagnosis}")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="medication">', unsafe_allow_html=True)
            st.info("💊 نصيحة علاجية:")
            for symptom, diagnosis, medication in found_diagnoses:
                st.markdown(f"• **{symptom}**: {medication}")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ لم نتمكن من تشخيص الأعراض المدخلة. يرجى استشارة طبيب متخصص.")
    else:
        st.warning("يرجى إدخال الأعراض أولاً.")

# إضافة توقيع أسفل الصفحة
st.markdown(
    """
    <hr>
    <p style="text-align: center; color: gray; font-size: 0.9rem; margin-top: 30px;">
    تم ابتكاره و تطويره من قبل مبارك الرشيدي
    </p>
    """, 
    unsafe_allow_html=True
)
