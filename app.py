import streamlit as st
import pandas as pd
import plotly.express as px

# Título do dashboard
st.title("ENEM Dashboard - 2019 Analysis")

# Carregar os dados
df = pd.read_csv("enem.csv")

# Filtrar apenas o ano de 2019
df = df[df["year"] == 2019]

# Traduzir gênero
df["gender"] = df["gender"].map({"F": "Female", "M": "Male"})

# 👉 Multiselect para filtrar por gênero
selected_genders = st.multiselect(
    "Select gender(s):", 
    options=["Female", "Male"],
    default=["Female", "Male"]
)

# Aplicar filtro no dataframe com base nos gêneros escolhidos
df_gender = df[df["gender"].isin(selected_genders)]

# 📊 Checkbox 1 - Histograma por idade e gênero
if st.checkbox("Show age distribution by gender"):
    st.subheader("Age Distribution by Gender")
    fig = px.histogram(
        df_gender,
        x="age",
        color="gender",
        nbins=20,
        barmode="overlay",
        title="Age Distribution by Gender"
    )
    st.plotly_chart(fig)

# 📊 Checkbox 2 - Boxplot de notas de matemática
if st.checkbox("Show math score boxplot by gender"):
    st.subheader("Math Scores by Gender")
    fig = px.box(
        df_gender,
        x="gender",
        y="score_mathematics",
        color="gender",
        title="Math Scores by Gender"
    )
    st.plotly_chart(fig)

# 📊 Checkbox 3 - Dispersão entre idade e uma nota escolhida
if st.checkbox("Show scatter plot: Age vs Score"):
    st.subheader("Age vs Selected Score")

    score_options = {
        "Overall Score": "score_overall",
        "Math Score": "score_mathematics",
        "Language Score": "score_language_and_codes",
        "Human Sciences Score": "score_human_science",
        "Natural Sciences Score": "score_natural_science"
    }

    selected_score_label = st.selectbox("Select score type:", options=list(score_options.keys()))
    selected_score = score_options[selected_score_label]

    fig = px.scatter(
        df_gender.sample(n=1000, random_state=42),
        x="age",
        y=selected_score,
        color="gender",
        title=f"Age vs {selected_score_label}"
    )
    st.plotly_chart(fig)
