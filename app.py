import streamlit as st

st.title("الطبيب الافتراضي")

# قاعدة بيانات بسيطة للأعراض، التشخيص، والنصائح
medical_data = {
    "حمى": {
        "diagnosis": "التهاب أو عدوى محتملة",
        "advice": "اشرب سوائل كثيرة، واسترح، وإذا استمرت الحرارة أكثر من 3 أيام، راجع الطبيب."
    },
    "صداع": {
        "diagnosis": "صداع توتري أو نصفي",
        "advice": "جرب الراحة، تناول مسكنات مثل الباراسيتامول، وقلل من التوتر."
    },
    "سعال": {
        "diagnosis": "التهاب في الجهاز التنفسي",
        "advice": "اشرب مشروبات دافئة، وحاول تجنب التدخين والهواء الملوث."
    },
    "رشح": {
        "diagnosis": "نزلة برد",
        "advice": "الراحة وتناول فيتامين سي، واستخدام أدوية الزكام حسب الحاجة."
    },
    "آلام في المعدة": {
        "diagnosis": "مشاكل هضمية أو التهاب معدة",
        "advice": "تجنب الأطعمة الحارة والدهنية، وتناول وجبات صغيرة ومتكررة."
    }
}

# إدخال الأعراض
symptoms_input = st.text_input("ادخل أعراضك (مثلاً: صداع، حمى، سعال)")

if st.button("تشخيص"):
    symptoms_list = [s.strip() for s in symptoms_input.split(",")]

    results = []
    for symptom in symptoms_list:
        if symptom in medical_data:
            info = medical_data[symptom]
            results.append(f"**{symptom}**: التشخيص: {info['diagnosis']} \nنصيحة: {info['advice']}")
        else:
            results.append(f"**{symptom}**: لا يوجد معلومات كافية، يرجى استشارة الطبيب.")
    
    if results:
        st.markdown("\n\n".join(results))
    else:
        st.warning("يرجى إدخال أعراض صحيحة.")

