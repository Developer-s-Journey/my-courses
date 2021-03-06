# Day 7
"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""

import pandas as pd
df = pd.read_csv("Salaries.csv")

"""
solution 1
"""
df.groupby('sex').agg({'salary':['max','min']})
df.groupby('sex')[['salary']].min()

"""
solution 2
"""
df.loc[(df['salary'] == df['salary'].max()) & (df['rank'] == 'Prof') | (df['salary'] == df['salary'].min()) & (df['rank'] == 'Prof')]

df.groupby('rank').agg({'salary':['max','min']})
"""
solution 3
"""
df[['salary']].fillna(df.groupby('service')[['salary']].mean())

"""
solution 4
"""
df[['phd']].fillna(df.groupby('service').mean())

"""
solution 5
"""
df['sex'].value_counts()
df['sex'].value_counts().plot.pie()
df['sex'].value_counts(normalize=True).mul(100)

"""
solution 6
"""
df['rank'].value_counts()
df['rank'].value_counts().plot.pie()

"""
solution 7
"""
df.agg({'service':['max','min']})

"""
solution 8
"""
df['salary'].plot.hist(bins=9)