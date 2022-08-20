from webbrowser import BackgroundBrowser
import streamlit as st
from multipage import MultiApp
from app import data, visualisasi, model, explanation

app = MultiApp()

st.markdown("""
# PORTOFOLIO PROYEK RIZKI WAHYUDI

Dengan Portofolio ini Bapak/Ibu bisa mempertimbangkan skill saya
""")

app.add_app("Data", data.app)
app.add_app("Visualisasi", visualisasi.app)
app.add_app("Model", model.app)
app.add_app("Explanation", explanation.app)
app.run()
