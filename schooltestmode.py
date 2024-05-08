# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:01:42 2024

@author: python2
"""

#📊#
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

from datetime import date

s103 = pd.read_csv('taiwan_all_school.csv', encoding = 'big5')

del merged_df['Unnamed: 0']

###計算年度各校學生總額####

year_to_select = 2023
selected_rows = merged_df[merged_df['年度'] == year_to_select]
school_count = {}

for index, row in selected_rows.iterrows():
    school_name = row["學校名稱"]
    people_count = row["總計"]
    if school_name in school_count:
        school_count[school_name] += people_count
    else:
        school_count[school_name] = people_count

print(f"{year_to_select} 年各校人數：")
for school, count in school_count.items():
    print(f"{school}: {count}")
for school, count in school_count.items():
    print(f"{school}: {count}")

print(f"總人数：{total_school_count}")    
    
    

####  

# 创建一个字典来存储每个年度的学校人数
yearly_school_count = {}

# 获取所有年度
years = merged_df['年度'].unique()

# 遍历每个年度
for year in years:
    # 选择特定年度的行
    selected_rows = merged_df[merged_df['年度'] == year]
    
    # 创建一个字典来存储该年度每个学校的人数
    school_count = {}
    
    # 遍历选择的行
    for index, row in selected_rows.iterrows():
        school_name = row["學校名稱"]
        people_count = row["總計"]
        if school_name in school_count:
            school_count[school_name] += people_count
        else:
            school_count[school_name] = people_count
    
    # 计算该年度所有学校的总人数
    total_school_count = sum(school_count.values())
    
    # 存储该年度的学校人数和总人数
    yearly_school_count[year] = {'school_count': school_count, 'total_school_count': total_school_count}

# 打印结果
for year, counts in yearly_school_count.items():
    print(f"{year} 年各校人數：")
    for school, count in counts['school_count'].items():
        print(f"{school}: {count}")
    print(f"总人数：{counts['total_school_count']}")
    print()


import matplotlib.pyplot as plt

# 存储各年度的总人数
total_counts = []

# 提取年度和总人数
for year, counts in yearly_school_count.items():
    total_count = counts['total_school_count']
    total_counts.append(total_count)

# 绘制折线图
plt.plot(years, total_counts, marker='o', linestyle='-')
plt.title('Total School Counts Over Years')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.xticks(years)  # 设置 x 轴刻度为年份
plt.grid(True)     # 显示网格线
plt.show()


##計算單一學校
school_name = '文藻外語大學'  # 要計算的學校名稱
school_total_count = {}  # 用於存儲每年該學校的總人數

# 遍歷每一年的數據
for year in merged_df['年度'].unique():
    # 選擇特定年度的數據
    year_data = merged_df[merged_df['年度'] == year]
    # 選擇特定學校的數據
    school_year_data = year_data[year_data['學校名稱'] == school_name]
    # 計算該年該學校的總人數
    total_count = school_year_data['總計'].sum()
    # 存儲到字典中
    school_total_count[year] = total_count

# 打印計算結果
print(f"{school_name}的歷年總人數：")
for year, count in school_total_count.items():
    print(f"{year} 年: {count}")
    
    
plt.figure(figsize=(10, 6))

# 繪製折線圖
plt.plot(list(school_total_count.keys()), list(school_total_count.values()), marker='o', linestyle='-')

# 添加標籤和標題
plt.xlabel('年度')
plt.ylabel('總人數')
plt.title(f'{school_name}的歷年總人數')

# 顯示網格
plt.grid(True)

# 顯示圖表
plt.show()    
    
    
####計算年度個學籍別總人數####

year_to_select = 2023
selected_rows = merged_df[merged_df['年度'] == year_to_select]
grade_count = {}

for index, row in selected_rows.iterrows():
    grade_name = row["等級別"]
    people_count = row["總計"]
    if grade_name in grade_count:
        grade_count[grade_name] += people_count
    else:
        grade_count[grade_name] = people_count

print(f"{year_to_select} 年學籍人數：")
for grade, count in grade_count.items():
    print(f"{grade}: {count}")
    


#########
  創建一個空字典來儲存每個年度的學籍人數
 yearly_enrollment = {}

 # 創建一個空字典來儲存每個年度每個學籍的人數
 yearly_grade_enrollment = {}

 # 選擇每個年度的資料並計算學籍人數
 for year in merged_df['年度'].unique():
     selected_rows = merged_df[merged_df['年度'] == year]
     total_enrollment = selected_rows['總計'].sum()
     yearly_enrollment[year] = total_enrollment

     # 計算每個學籍的人數
     grade_enrollment = {}
     for index, row in selected_rows.iterrows():
         grade_name = row["等級別"]
         people_count = row["總計"]
         grade_enrollment[grade_name] = people_count
     yearly_grade_enrollment[year] = grade_enrollment

 # 打印每個年度的學籍人數
 print("各年度學籍人數：")
 for year, enrollment in yearly_enrollment.items():
     print(f"{year} 年: {enrollment} 人")
     print(f"  各學籍人數：")
     for grade, count in yearly_grade_enrollment[year].items():
         print(f"    {grade}: {count} 人")  
         
# 創建一個空字典來儲存每個年度的學籍人數
yearly_enrollment = {}

# 創建一個空字典來儲存每個年度每個學籍的人數
yearly_grade_enrollment = {}


import matplotlib.pyplot as plt

# 創建一個空字典來儲存每個年度每個學籍的人數
yearly_grade_count = {}

# 選擇每個年度的資料並計算各學籍人數
for year in merged_df['年度'].unique():
    selected_rows = merged_df[merged_df['年度'] == year]
    grade_count = {}

    for index, row in selected_rows.iterrows():
        grade_name = row["等級別"]
        people_count = row["總計"]
        if grade_name in grade_count:
            grade_count[grade_name] += people_count
        else:
            grade_count[grade_name] = people_count

    yearly_grade_count[year] = grade_count

# 繪製每個年度每個學籍的人數
for year, grade_count in yearly_grade_count.items():
    plt.figure(figsize=(10, 6))
    plt.bar(grade_count.keys(), grade_count.values(), color='skyblue')
    plt.title(f"{year} 年各學籍人數")
    plt.xlabel("學籍")
    plt.ylabel("人數")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()



    
    