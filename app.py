import streamlit as st
import pandas as pd

# إعدادات أساسية
st.set_page_config(page_title="Volleyball Matches", layout="wide")

st.title("🏐 تطبيق بطولات الكرة الطائرة")

# قائمة البطولات (اللي مربوطة بملفات Excel)
tournaments = {
    "تحت 15 سنة": "data/u15.xlsx",
    "تحت 17 سنة": "data/u17.xlsx",
    "الدرجة الأولى": "data/seniors.xlsx"
}

# اختيار البطولة
choice = st.sidebar.selectbox("اختر البطولة", list(tournaments.keys()))

# تحميل البيانات من الملف المرتبط
file_path = tournaments[choice]

try:
    matches_df = pd.read_excel(file_path, sheet_name="matches")
    results_df = pd.read_excel(file_path, sheet_name="results")
    ranking_df = pd.read_excel(file_path, sheet_name="ranking")
except Exception as e:
    st.error(f"خطأ في قراءة ملف {file_path}: {e}")
    st.stop()

# Tabs
tab1, tab2, tab3 = st.tabs(["📅 جدول المباريات", "📊 النتائج", "🏆 الترتيب"])

with tab1:
    st.subheader("📅 جدول المباريات")
    st.dataframe(matches_df, use_container_width=True)

with tab2:
    st.subheader("📊 النتائج")
    st.dataframe(results_df, use_container_width=True)

with tab3:
    st.subheader("🏆 الترتيب")
    st.dataframe(ranking_df, use_container_width=True)
