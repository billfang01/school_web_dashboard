# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:01:42 2024

@author: python2
"""

import streamlit as st
import pandas as pd
import plotly.express as px
#from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
from streamlit_extras.metric_cards import style_metric_cards
st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.graph_objs as go
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False




st.set_page_config(page_title="Dashboard",page_icon="📊",layout="wide")
st.header("SCHOOL WEB DASHBOARD |  大專院校校別學生數 ")

df = pd.read_csv('taiwan_all_school.csv', encoding = 'big5')  

del df['Unnamed: 0']

def compute_grade_count(selected_year, filtered_df):
    selected_rows = filtered_df[filtered_df['年度'] == selected_year]
    grade_count = {}
    for index, row in selected_rows.iterrows():
        grade_name = row["等級別"]
        people_count = row["總計"]
        if grade_name in grade_count:
            grade_count[grade_name] += people_count
        else:
            grade_count[grade_name] = people_count
    return grade_count


# df = pd.read_csv('your_data.csv')  


selected_year = st.sidebar.selectbox('選擇年度', df['年度'].unique())


filtered_df = df[df['年度'] == selected_year]


school_name_input = st.sidebar.text_input('輸入學校名稱', '')


if school_name_input:
    filtered_df = filtered_df[filtered_df['學校名稱'] == school_name_input]


county_options = [''] + list(df['縣市'].unique())
selected_county = st.sidebar.selectbox('選擇縣市', county_options)


if selected_county:
    if selected_county == '':
        
        filtered_df = filtered_df.groupby('年度').sum().reset_index()
    else:
        filtered_df = filtered_df[filtered_df['縣市'] == selected_county]


with st.expander("VIEW EXCEL DATASET"):
    st.write(filtered_df)


grade_count = compute_grade_count(selected_year, filtered_df)


total1, total2, total3, total4, total5 = st.columns(5, gap='small')

with total1:
    st.info('博士', icon="🧑‍🎓")
    st.metric(label="總人數", value=f"{grade_count.get('博士', 0):,.0f}")

with total2:
    st.info('碩士', icon="🧑‍🎓")
    st.metric(label="Mode TZS", value=f"{grade_count.get('碩士', 0):,.0f}")

with total3:
    st.info('學士', icon="🧑‍🎓")
    st.metric(label="總人數", value=f"{grade_count.get('學士', 0):,.0f}")

with total4:
    st.info('四技', icon="🧑‍🎓")
    st.metric(label="總人數", value=f"{grade_count.get('四技', 0):,.0f}")

with total5:
    st.info('五專', icon="🧑‍🎓")
    st.metric(label="總人數", value=f"{grade_count.get('五專', 0):,.0f}")

style_metric_cards(background_color="#FFFFFF",border_left_color="#686664",border_color="#000000",box_shadow="#F71938")


def graphs():
    # Bar graph: investment by grade (男女總合)
    grade_count_df = pd.DataFrame(grade_count.items(), columns=['Grade', 'Total People'])
    fig_grade = px.bar(
        grade_count_df,
        x='Total People',
        y='Grade',
        orientation='h',
        title='<b>TOTAL PEOPLE BY GRADE</b>',
        color_discrete_sequence=["#0083B8"] * len(grade_count_df),
        template='plotly_white'
    )
    fig_grade.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="black"),
        yaxis=dict(showgrid=True, gridcolor='#cecdcd'),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        xaxis=dict(showgrid=True, gridcolor='#cecdcd'),
    )

    # Line graph: total people by school (學校總人數)
    school_total_df = filtered_df.groupby('學校名稱')['總計'].sum().reset_index()
    top_20_schools = school_total_df.nlargest(20, '總計')  # Select top 20 schools by total count
    fig_school_total = px.bar(
        top_20_schools,
        x='學校名稱',
        y='總計',
        title='<b>TOTAL PEOPLE BY SCHOOL (Top 20)</b>',
        color_discrete_sequence=["#0083b8"],
        template='plotly_white'
    )
    fig_school_total.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="black"),
        yaxis=dict(showgrid=True, gridcolor='#cecdcd'),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        xaxis=dict(showgrid=True, gridcolor='#cecdcd'),
    )

    # Pie chart: total people by region (% of total)
    total_people_percentage = {grade: count / sum(grade_count.values()) * 100 for grade, count in grade_count.items()}
    fig_pie = px.pie(
        names=list(total_people_percentage.keys()),
        values=list(total_people_percentage.values()),
        title='GRADE DISTRIBUTION',
        template='plotly_white'
    )
    fig_pie.update_layout(
        legend_title="Grades",
        legend_y=0.9,
        plot_bgcolor="rgba(0,0,0,0)",
    )
    fig_pie.update_traces(textinfo='percent+label', textposition='inside')

    left, right, center = st.columns(3)
    left.plotly_chart(fig_grade, use_container_width=True)
    right.plotly_chart(fig_school_total, use_container_width=True)
    center.plotly_chart(fig_pie, use_container_width=True)

graphs()




st.sidebar.markdown(
    """
    
    
    ### 全臺灣大專校院校別學生數使用說明
    1. 可依照各年度查詢該年度相關數據
    2. 可輸入各學校登記名稱查詢
    3. 可透過各縣市查詢，選擇空白則為全台總數
    4. 相關數據均來自政府資料開放平台
    5. 網路儀表測試範例  不定期更新 
    
    
    """
)



    
    
