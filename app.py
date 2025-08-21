import streamlit as st

st.set_page_config(page_title="الطبيب الافتراضي", layout="centered")

# أسلوب CSS بسيط لجعل العناصر أكبر ومريحة للعرض على الجوال
st.markdown("""
<style>
/* تكبير الخطوط والأزرار */
h1, h2, h3 {
    font-family: 'Arial', sans-serif;
    text-align: center;
}
div[data-baseweb="select"] > div > div > input {
    font-size: 18px;
    padding: 12px;
}
.stButton>button {
    font-size: 18px;
    padding: 12px 20px;
    width: 100%;
    border-radius: 10px;
}
.stMultiselect > div > div {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.title("👨‍⚕️ الطبيب الافتراضي")

# قاعدة بيانات الأمراض والأعراض والنصائح
diseases_db = {
    "نزلة برد": {
        "الأعراض": ["سعال", "احتقان أنف", "حكة في الحلق", "عطس"],
        "نصيحة العلاج": "الراحة، شرب سوائل دافئة، ومسكنات الألم مثل الباراسيتامول."
    },
    "الأنفلونزا": {
        "الأعراض": ["حمى", "سعال جاف", "آلام في العضلات", "إرهاق"],
        "نصيحة العلاج": "الراحة، شرب السوائل، يمكن استخدام مضادات الفيروسات بعد استشارة الطبيب."
    },
    "التهاب الحلق": {
        "الأعراض": ["ألم في الحلق", "صعوبة في البلع", "احمرار"],
        "نصيحة العلاج": "غرغرة بالماء المالح، مسكنات الألم، وزيارة الطبيب إذا استمر الألم."
    },
    "التهاب المعدة": {
        "الأعراض": ["ألم في البطن", "غثيان", "تقيؤ", "فقدان الشهية"],
        "نصيحة العلاج": "تناول أدوية مضادة للحموضة، تجنب الأطعمة الحارة والدهنية."
    }
}

st.header("أدخل الأعراض التي تشعر بها:")

symptoms_input = st.multiselect(
    "اختر أعراضك:",
    options=[
        "سعال", "احتقان أنف", "حكة في الحلق", "عطس",
        "حمى", "سعال جاف", "آلام في العضلات", "إرهاق",
        "ألم في الحلق", "صعوبة في البلع", "احمرار",
        "ألم في البطن", "غثيان", "تقيؤ", "فقدان الشهية"
    ]
)

if st.button("تشخيص المرض"):
    if not symptoms_input:
        st.warning("الرجاء اختيار عرض واحد على الأقل!")
    else:
        matched_diseases = []
        for disease, info in diseases_db.items():
            matched_symptoms = set(symptoms_input).intersection(set(info["الأعراض"]))
            if matched_symptoms:
                matched_diseases.append((disease, len(matched_symptoms), info["نصيحة العلاج"]))

        if matched_diseases:
            matched_diseases.sort(key=lambda x: x[1], reverse=True)
            st.success("التشخيص المحتمل:")
            for disease, count, advice in matched_diseases:
                st.markdown(f"### {disease}")
                st.write(f"عدد الأعراض المطابقة: {count}")
                st.info(f"نصيحة العلاج: {advice}")
        else:
            st.error("لم يتم العثور على مرض يتطابق مع الأعراض المدخلة.")
