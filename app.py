import streamlit as st

st.set_page_config(page_title="الطبيب الافتراضي", layout="centered")

st.markdown(
    """
    <style>
    /* تحسين مظهر الصفحة للجوال */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        padding: 1rem;
        background: #f5f7fa;
    }
    .main {
        max-width: 600px;
        margin: auto;
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgb(0 0 0 / 0.1);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    label {
        font-weight: bold;
        margin-top: 1rem;
        display: block;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.9rem;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# قائمة الأمراض مع أعراضها ونصائح العلاج
diseases = {
    "الأنفلونزا": {
        "symptoms": ["حمى", "سعال", "احتقان الحلق", "صداع", "آلام عضلية"],
        "advice": "تناول مسكنات الألم، الراحة، شرب السوائل الدافئة."
    },
    "نزلات البرد": {
        "symptoms": ["سيلان الأنف", "عطس", "احتقان الأنف", "سعال خفيف"],
        "advice": "تناول فيتامين سي، الراحة، شرب السوائل."
    },
    "التهاب الحلق": {
        "symptoms": ["ألم في الحلق", "صعوبة في البلع", "احمرار"],
        "advice": "غرغرة بماء دافئ وملح، تناول مسكنات الألم."
    },
    "السكري": {
        "symptoms": ["عطش زائد", "كثرة التبول", "تعب شديد"],
        "advice": "مراجعة الطبيب، الالتزام بالدواء، متابعة النظام الغذائي."
    },
    "الضغط المرتفع": {
        "symptoms": ["صداع", "دوخة", "تعب عام"],
        "advice": "اتباع نظام غذائي صحي، ممارسة الرياضة، تناول الأدوية الموصوفة."
    }
}

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("الطبيب الافتراضي")

st.write("اختر الأعراض التي تعاني منها:")

# جمع كل الأعراض الفريدة
all_symptoms = []
for disease in diseases.values():
    all_symptoms.extend(disease["symptoms"])
all_symptoms = list(sorted(set(all_symptoms)))

# اختيار الأعراض من المستخدم
selected_symptoms = st.multiselect("الأعراض", all_symptoms)

# التشخيص بناء على الأعراض
if st.button("تشخيص المرض"):
    if not selected_symptoms:
        st.warning("يرجى اختيار عرض واحد على الأقل.")
    else:
        matched = []
        for disease, info in diseases.items():
            # إذا كان جميع أعراض المرض موجودة في الأعراض المختارة
            if all(symptom in selected_symptoms for symptom in info["symptoms"]):
                matched.append((disease, info["advice"]))

        if matched:
            st.success("التشخيص:")
            for disease, advice in matched:
                st.markdown(f"**{disease}**")
                st.markdown(f"النصيحة: {advice}")
        else:
            st.info("لم يتم التعرف على المرض بناءً على الأعراض المختارة، يرجى مراجعة طبيب مختص.")
st.markdown("</div>", unsafe_allow_html=True)

# النص في أسفل الصفحة
st.markdown("---")
st.markdown('<div class="footer">تم ابتكاره و تطويره من قبل <strong>مبارك الرشيدي</strong></div>', unsafe_allow_html=True)
