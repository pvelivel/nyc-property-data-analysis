# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:08:45 2023

@author: Lenovo
"""

import os
os.getcwd()
os.chdir('D:/MS/GMU/AIT-580/Assignments/Project')
import pandas as pd
import seaborn as sns
#importing dataset
df=pd.read_csv('Dataset.csv',sep=',', header=None,index_col=False)
df = df.reset_index(drop=True)
#give column names
df.columns=['BBL','REQUIRED_DEP','BOROCODE','BLOCK','LOT',                           
'NUMBER_OF_BUILDINGS',      
'TAX_CLASS','BUILDING_CLASS','STREET_2','STREET_NAME','POSTCODE','BOROUGH','DOF_SQ_FOOTAGE','LATITUDE','LONGITUDE','COMMUNITY_BOARD','COUNCIL_DISTRICT','CENSUS_TRACT','BIN','NTA']
df.columns
#remove unwanted rows
df=df.drop(0)
import matplotlib.pyplot as plt
# Numerical data analysis
numerical_columns = ['NUMBER_OF_BUILDINGS', 'DOF_SQ_FOOTAGE', 'LATITUDE', 'LONGITUDE']
numerical_data = df[numerical_columns]
# Summary statistics
numerical_summary = numerical_data.describe()
numerical_summary

ordinal_column = 'TAX_CLASS'

# Value counts for ordinal data
ordinal_counts = df[ordinal_column].value_counts()

# Bar plot for ordinal data
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x=ordinal_column)
plt.title(f'Count of Properties by {ordinal_column}')
plt.show()

# Interval and Ratio data analysis
interval_ratio_columns = ['BLOCK', 'LOT', 'POSTCODE', 'COUNCIL_DISTRICT','CENSUS_TRACT','BIN']

#Research Question 1
# Select relevant columns
selected_columns = ['TAX_CLASS', 'NUMBER_OF_BUILDINGS']

# Drop rows with missing values in selected columns
df[selected_columns] = df[selected_columns].apply(pd.to_numeric, errors='coerce')
selected_data = df[selected_columns].dropna()
# Plotting the correlation
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TAX_CLASS', y='NUMBER_OF_BUILDINGS', data=selected_data, alpha=0.5)
plt.title('Correlation between Tax Class and Number of Buildings')
plt.xlabel('Tax Class')
plt.ylabel('Number of Buildings')
plt.show()

# Calculate correlation coefficient
correlation_coefficient = selected_data['TAX_CLASS'].corr(selected_data['NUMBER_OF_BUILDINGS'])
print(f"Correlation Coefficient: {correlation_coefficient}")

#Research Question2
# Select relevant columns
selected_columns2 = ['BOROUGH', 'TAX_CLASS']

# Drop rows with missing values in selected columns
selected_data2 = df[selected_columns2].dropna()

# Plotting the distribution of Tax Classes in each Borough
plt.figure(figsize=(12, 8))
sns.countplot(data=selected_data2, x='BOROUGH', hue='TAX_CLASS')
plt.title('Distribution of Tax Classes in Each Borough')
plt.xlabel('Borough')
plt.ylabel('Count')
plt.legend(title='Tax Class')
plt.show()

# Displaying predominant tax class for each borough
predominant_tax_class = selected_data2.groupby('BOROUGH')['TAX_CLASS'].agg(pd.Series.mode).reset_index()
print("Predominant Tax Class for Each Borough:")
print(predominant_tax_class)
