%%writefile simple_app.py

import streamlit as st
import plotly.express as px
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

fig1 = px.bar(tips, x="day", y="tip")

fig2 = px.violin(tips, x="sex", y="tip")

st.title("Data Visualization with Plotly")

st.header("Plot 1: Bar Plot - Tips by Day")
st.plotly_chart(fig1)
st.markdown('''**Insight Observed**: (Add your insights here)''')

st.header("Plot 2: Violin Plot - Tips by Gender")
st.plotly_chart(fig2)
st.markdown('''**Insight Observed**: (Add your insights here)''')

