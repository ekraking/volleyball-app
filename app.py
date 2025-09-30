# import streamlit as st
# import pandas as pd

# # إعدادات أساسية
# st.set_page_config(page_title="Volleyball Matches", layout="wide")

# st.title("🏐 تطبيق بطولات الكرة الطائرة")

# # قائمة البطولات (اللي مربوطة بملفات Excel)
# tournaments = {
#     "تحت 15 سنة": "data/u15.xlsx",
#     "تحت 17 سنة": "data/u17.xlsx",
#     "الدرجة الأولى": "data/seniors.xlsx"
# }

# # اختيار البطولة
# choice = st.sidebar.selectbox("اختر البطولة", list(tournaments.keys()))

# # تحميل البيانات من الملف المرتبط
# file_path = tournaments[choice]

# try:
#     matches_df = pd.read_excel(file_path, sheet_name="matches")
#     results_df = pd.read_excel(file_path, sheet_name="results")
#     ranking_df = pd.read_excel(file_path, sheet_name="ranking")
# except Exception as e:
#     st.error(f"خطأ في قراءة ملف {file_path}: {e}")
#     st.stop()

# # Tabs
# tab1, tab2, tab3 = st.tabs(["📅 جدول المباريات", "📊 النتائج", "🏆 الترتيب"])

# with tab1:
#     st.subheader("📅 جدول المباريات")
#     st.dataframe(matches_df, use_container_width=True)

# with tab2:
#     st.subheader("📊 النتائج")
#     st.dataframe(results_df, use_container_width=True)

# with tab3:
#     st.subheader("🏆 الترتيب")
#     st.dataframe(ranking_df, use_container_width=True)


import streamlit as st
import pandas as pd

# تحميل ملف الاكسل


def load_data(file):
    return pd.read_excel(file)


# واجهة التطبيق
st.title("🏐 Volleyball Matches & Results")

# اختيار البطولة
tournament = st.selectbox("اختر البطولة:", ["U15", "U17", "Seniors"])

# ربط البطولة بالملف
files = {
    "U15": "u15.xlsx",
    "U17": "u17.xlsx",
    "Seniors": "seniors.xlsx"
}

# تحميل البيانات
df = load_data(files[tournament])

# لو النتيجة فاضية → Upcoming
df["Status"] = df["Result"].apply(
    lambda x: "Upcoming" if pd.isna(x) or x == "-" else "Finished")

# عرض الجدول
st.dataframe(df, use_container_width=True)
