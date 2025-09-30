import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="تطبيق الكرة الطائرة", layout="wide")

st.title("🏐 نتائج منطقة الإسكندرية للكرة الطائرة 🏐")
st.markdown(
    "مرحبًا بك! هنا تقدر تتابع النتائج، الترتيب، والمباريات القادمة لكل مرحلة سنية.")

# تحميل البيانات من ملف Excel


@st.cache_data
def load_data():
    matches = pd.read_excel("matches.xlsx", sheet_name="matches")
    standings = pd.read_excel("matches.xlsx", sheet_name="standings")
    return matches, standings


matches, standings = load_data()

# اختيار المرحلة السنية
age_group = st.selectbox("اختر المرحلة السنية:", matches["age_group"].unique())

# فلترة البيانات
matches_filtered = matches[matches["age_group"] == age_group]
standings_filtered = standings[standings["age_group"] == age_group]

# إنشاء التابات
tab1, tab2, tab3 = st.tabs(
    ["📊 جدول الترتيب", "✅ النتائج السابقة", "📅 المباريات القادمة"])

with tab1:
    st.subheader(f"جدول الترتيب - {age_group}")
    st.dataframe(standings_filtered)

with tab2:
    st.subheader(f"النتائج السابقة - {age_group}")
    past_matches = matches_filtered[matches_filtered["status"] == "played"]
    st.dataframe(past_matches)

with tab3:
    st.subheader(f"المباريات القادمة - {age_group}")
    upcoming_matches = matches_filtered[matches_filtered["status"] == "upcoming"]
    st.dataframe(upcoming_matches)
