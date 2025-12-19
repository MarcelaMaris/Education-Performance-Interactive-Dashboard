
<p align="center">
  <img src="cover_education.png" width="100%" alt="E-Commerce Analytics Dashboard cover">
</p>


## <img src="icons/education.png" width="50">  &nbsp;&nbsp;Education Performance Dashboard — ENEM 2019
<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-0A3756?style=flat&logo=python&logoColor=F5F7FA&labelColor=E8AA3A)
![Pandas](https://img.shields.io/badge/Pandas-lib-0A3756?style=flat&logo=pandas&logoColor=F5F7FA&labelColor=E8AA3A)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-0A3756?style=flat&logo=plotly&logoColor=F5F7FA&labelColor=E8AA3A)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-0A3756?style=flat&logo=streamlit&logoColor=F5F7FA&labelColor=E8AA3A)
![Deployment](https://img.shields.io/badge/Deployment-Render-0A3756?style=flat&logo=render&logoColor=F5F7FA&labelColor=E8AA3A)

> This project analyses **student participation and performance patterns** in Brazil’s  
> **national high school exam (ENEM 2019)** using an **interactive, exploratory dashboard**.
>
> The objective is to understand **who takes the exam**, **how performance varies by age and gender**,  
> and **how these patterns differ across subject areas**.
>
> The project combines **Python-based data preparation** with a **Streamlit web dashboard**,  
> translating large-scale educational microdata into **clear, accessible insights** for  
> educators, analysts, and policy-oriented stakeholders.
>
> It is designed to mirror how a **data analyst or business analyst** would explore  
> large assessment datasets and communicate findings through **self-service analytics tools**.

🔗 **Live dashboard:** https://dashboard-enem-tvu8.onrender.com  
💻 **Repository:** https://github.com/MarcelaMaris/dashboard-enem  

---
## <img src="icons/objectives.png" width="30">  &nbsp;&nbsp;Objectives

- Analyse **age and gender distribution** among ENEM participants.
- Compare **performance distributions by subject** across genders.
- Explore **age × performance relationships** across different knowledge areas.
- Identify **performance concentration and dispersion patterns**.
- Deliver an **interactive dashboard** enabling self-service exploration by non-technical users.
- Demonstrate **end-to-end delivery**: data → analysis → dashboard → deployment.

---

## <img src="icons/features.png" width="30">  &nbsp;&nbsp;Key Analyses & Features

- **Participant Demographics Analysis:**  
  Distribution of candidates by age and gender, highlighting participation concentration and drop-off.

- **Subject-Level Performance Distribution:**  
  Boxplot-based comparison of score distributions across:
  - Mathematics  
  - Languages  
  - Human Sciences  
  - Natural Sciences  

- **Age × Performance Exploration:**  
  Scatter plots showing how scores evolve across age groups for each subject area and overall score.

- **Interactive Filtering:**  
  Global gender filter applied consistently across all visualisations.

- **Exploratory Dashboard Design:**  
  Designed to support **open-ended analysis**, enabling users to freely investigate patterns rather than consume predefined conclusions.

---
## <img src="icons/dataset.png" width="30">  &nbsp;&nbsp;Dataset

**Source:**  
ENEM 2019 — Brazilian National High School Exam (INEP)

**Data Scope**
- Candidate demographic attributes (age, gender)
- Subject-level exam scores
- Overall performance metrics

⚠️ **Data note**  
The dataset was preprocessed to support exploratory analysis and dashboard performance.  
Sensitive personal identifiers were removed prior to analysis.

---

## <img src="icons/dashboard.png" width="30">  &nbsp;&nbsp;Interactive Dashboard

The analytical results are summarised in a **Streamlit web dashboard**, designed for  
**exploratory analysis and insight discovery**.

### Dashboard Structure

1. **Who takes the exam?**  
   - Age distribution histogram segmented by gender.

2. **How do students perform?**  
   - Subject-level score distributions via interactive boxplots.

3. **How does age relate to performance?**  
   - Scatter plots showing age vs. score for:
     - Overall score  
     - Mathematics  
     - Languages  
     - Human Sciences  
     - Natural Sciences  

All charts update dynamically based on selected filters, enabling intuitive comparison across demographics and subjects.

---

## <img src="icons/conclusions.png" width="30">  &nbsp;&nbsp;Key Insights

- **Participation is highly age-concentrated:**  
  Most candidates are between **15 and 20 years old**, with participation declining sharply after age 25.

- **Performance declines with age:**  
  Average scores decrease and become more dispersed for older candidates across all subjects.

- **Gender differences are subject-specific:**  
  - Slight male advantage in **Mathematics**.  
  - Slight female advantage in **Languages**.  
  - Similar performance patterns in **Human** and **Natural Sciences**.

- **Score variability increases over time:**  
  Younger candidates show more consistent performance, while older groups exhibit wider dispersion.

---

## <img src="icons/impact.png" width="30">  &nbsp;&nbsp;Educational & Business Impact

- Supports **evidence-based educational policy discussions**.
- Highlights **demographic performance gaps** relevant to curriculum design and student support programmes.
- Demonstrates how **interactive dashboards democratise access to educational data**.
- Provides a scalable template for analysing **large-scale standardised assessments**.

---

## <img src="icons/objectives.png" width="30">  &nbsp;&nbsp;Key Performance Indicators (KPIs)

- **Average score by subject & gender**  
  Reveals small but consistent gender gaps (e.g. +10 points for men in Mathematics, +12 for women in Languages).

- **Top 10% performance age range**  
  Highest concentration between **15–20 years** across all subject areas.

- **Score drop after age 25**  
  Average decrease of approximately **15–20%** compared to younger candidates.

---

## <img src="icons/recommendations.png" width="30">  &nbsp;&nbsp;Recommendations

- Targeted academic support programmes for **candidates aged 25+**, focusing on exam strategy and content revision.
- Early **mathematics mentoring initiatives** for female students to address small but persistent performance gaps.
- Extension of the analysis to include **socioeconomic and regional variables**.
- Multi-year ENEM comparison to validate **long-term performance trends**.

---

## <img src="icons/techstack.png" width="30">  &nbsp;&nbsp;Tech Stack

- **Languages & Libraries:** Python (3.10), Pandas  
- **Visualisation:** Plotly  
- **Web Framework:** Streamlit  
- **Deployment:** Render  
- **Version Control:** Git & GitHub  

---

This project reflects a strong interest in **education analytics** and demonstrates how  
**interactive, exploratory dashboards** can support transparency, understanding, and  
data-driven decision-making in large-scale assessment systems.

---

<p align="center">
  <sub>📊 Designed & developed by <b>Marcela Maris</b> — Data Analytics Portfolio</sub><br>
  <sub><i>Education Analytics • Interactive Dashboards • Data-Driven Insights</i></sub>
</p>

