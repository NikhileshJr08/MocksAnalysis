# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns

# Read CSV file
mocks_df = pd.read_csv("mocks.csv")

# Convert student_department, student_section interviewer_name, interviewer_company, to category datatype
mocks_df["student_department"] = mocks_df["student_department"].astype("category")
mocks_df["student_section"] = mocks_df["student_section"].astype("category")
mocks_df["interviewer_name"] = mocks_df["interviewer_name"].astype("category")
mocks_df["interviewer_company"] = mocks_df["interviewer_company"].astype("category")

# Convert interview_date to date datatype
mocks_df["interview_date"] = pd.to_datetime(mocks_df["interview_date"])

# Get Series for the average interview score in each department
average_interview_score_department = mocks_df.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True)
departments = average_interview_score_department.index
average_interview_score = average_interview_score_department.values

sns.set_style(style="darkgrid")
plots = sns.barplot(x=departments, y=average_interview_score)

# Annotate the bar graphs
for bar in plots.patches: 
    
    plots.annotate(
                   format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points'
                  ) 

plt.yticks(np.arange(5, 35, 5))
plt.xlabel("Department")
plt.ylabel("Interview Score Out Of 30")
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS)")
plt.show()
