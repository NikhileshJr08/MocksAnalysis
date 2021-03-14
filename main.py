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

print(average_interview_score_department)

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

#Deriving the DataFrame for the interview score for each department on 20-02-2021
options = ['20-02-2021']
student_deets_20 = mocks_df[mocks_df['interview_date'].isin(options)] #Selecting only the rows which had interview_date 20-02-2021
average_interview_score_department_20 = student_deets_20.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True) #Getting the mean of the interview_total group by department
average_interview_score_department_20_NaN = average_interview_score_department_20.fillna(0) #Replacing the NaN values with 0
departments_20 = average_interview_score_department_20.index
average_interview_score_20 = average_interview_score_department_20_NaN.values

print(average_interview_score_department_20_NaN)

#Plotting the graph
sns.set_style(style="darkgrid")
plots = sns.barplot(x=departments_20, y=average_interview_score_20)

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
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS - 20/02/2021)")
plt.show()


#Deriving the DataFrame for the interview score for each department on 21-02-2021
options = ['21-02-2021']
student_deets_21 = mocks_df[mocks_df['interview_date'].isin(options)] #Selecting only the rows which had interview_date 21-02-2021
average_interview_score_department_21 = student_deets_21.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True) #Getting the mean of the interview_total group by department
average_interview_score_department_21_NaN = average_interview_score_department_21.fillna(0) #Replacing the NaN values with 0
departments_21 = average_interview_score_department_21.index
average_interview_score_21 = average_interview_score_department_21_NaN.values

print(average_interview_score_department_21_NaN)

#Plotting the graph
sns.set_style(style="darkgrid")
plots = sns.barplot(x=departments_21, y=average_interview_score_21)

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
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS - 21/02/2021)")
plt.show()
