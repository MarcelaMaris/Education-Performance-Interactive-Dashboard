<p align="center">
  <img src="cover_education.png" width="100%" alt="E-Commerce Analytics Dashboard cover">
</p>


# 📊 Education Performance - ENEM 2019 — Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview
This project was developed as part of the **Data Analytics Bootcamp at [TripleTen](https://tripleten.com)**.  
It explores data from **ENEM 2019**, Brazil’s national high school exam, to uncover **performance patterns by gender and age group**.  
An **interactive Streamlit dashboard** was built to make data exploration intuitive and visually engaging.


🔗 **Live dashboard:** https://dashboard-enem-tvu8.onrender.com  
💻 **Repository:** [https://github.com/MarcelaMaris/dashboard-enem](https://github.com/MarcelaMaris/Project-5-Tripleten-ENEM-Dashboard)

---

## 🎯 Objectives
- Analyze the **age distribution** of participants by gender.  
- Explore performance across **different subject areas** by gender and age.  
- Investigate **age–performance patterns** (overall and per subject).  
- Deliver an **interactive web application** for data exploration.

---

## 🧭 Dashboard Features

- **🎚️ Gender Filter (Multiselect)**  
  Allows selection of one or both genders (female and male) to customize all visualizations.

- **📊 Age Distribution Histogram**  
  Visualizes participant age distribution by gender, highlighting demographic concentration.

- **📈 Math Score Boxplot**  
  Compares mathematics performance between genders, making differences in distribution visible.

- **🌐 Scatter Plot (Age vs Score)**  
  Lets the user select the **type of score** (overall, math, language, humanities, science) and analyze its relationship with age.

---


## 📌 Conclusions

**Age Distribution**
- Most participants are **15–20 years old**.  
- Participation **drops significantly** after **age 25**.

**Performance by Subject**
- **Overall Score:** concentrated between **400–600**, mostly among ages **15–20**.  
- **Math Score:** males show a **slightly higher median** and **greater dispersion**.  
- **Language Score:** similar distributions by gender, with a **slight female advantage**.  
- **Human Sciences Score:** similar results across genders, concentrated in **mid ranges**.  
- **Natural Sciences Score:** pattern similar to Human Sciences, with **no major gender gaps**.

**Age × Performance**
- **Highest scores** concentrate between **15–20** across all subjects.  
- After **25**, scores become **more dispersed** and generally **lower**.  
- Female scores tend to be **more tightly clustered**; male scores show **greater variability**, especially in Math.

---

### 🧩 Educational Impact & Key Metrics

This analysis highlights key patterns in Brazil’s national exam (ENEM 2019), offering actionable insights for educational policy and teaching strategies.

**Educational Impact:**

* Identifies **age and gender disparities** in student performance, supporting targeted interventions.
* Informs **curriculum design and mentoring programs** for students over 25 and for females in STEM areas.
* Demonstrates how **interactive dashboards** can democratize access to educational analytics.

**Key Performance Indicators (KPIs):**

| KPI                                  | Description                                        | Insight                                                       |
| ------------------------------------ | -------------------------------------------------- | ------------------------------------------------------------- |
| 🧮 **Average Score by Subject**      | Mean ENEM score per subject and gender             | Reveals small but consistent gender gaps in Math and Language |
| 🎓 **Top 10% Performance Age Range** | Age group with highest concentration of top scores | Ages **15–20** perform best across all subjects               |
| 📉 **Score Drop-off After Age 25**   | % decrease in average scores for older candidates  | ~15–20% lower average compared to younger participants        |
| ⚖️ **Gender Performance Gap**        | Difference in median scores (Math vs Language)     | Males +10 in Math, Females +12 in Language                    |

---
## 📝 Recommendations
- **Targeted support for older candidates (25+)** focusing on content review and test strategies.  
- **Math mentorship for female students** to address small performance gaps.  
- **Deeper analysis of socioeconomic and regional factors** to explain variance.  
- **Multi-year comparison** (other ENEM editions) to validate long-term trends.

---

## 🛠️ Technologies Used
- **Python**, **Pandas**, **Plotly**, **Streamlit**  
- Deployment with **Render**





