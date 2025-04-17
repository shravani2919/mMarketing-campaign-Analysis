#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


pip install pandas


# In[3]:


import numpy as np
import pandas as pd


# In[31]:


df = pd.read_csv('marketing_campaign.csv');


# In[32]:


df


# In[33]:


import pandas as pd

df = pd.read_csv('marketing_campaign.csv', delimiter='\t')
df.head()


# In[34]:


df


# In[35]:


ID = df.ID.sort_values()
print(ID)


# In[36]:


df_sorted = df.sort_values(by='ID')
df_sorted.to_csv("sorted_marketing_campaign.csv", index=False)

print("Sorted CSV saved.")


# In[37]:


df.columns


# In[38]:


df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Check column names
print(df.columns)

# Sort by ID
df_sorted = df.sort_values(by='ID')

# Save the sorted CSV
df_sorted.to_csv("sorted_marketing_campaign.csv", index=False)

print("Sorted CSV saved successfully.")


# In[39]:


df


# In[40]:


import pandas as pd

# Read with correct separator
df = pd.read_csv("marketing_campaign.csv", sep='\t')

# Sort by ID
df_sorted = df.sort_values(by='ID')

# Show top 5 sorted rows
print(df_sorted.head(10))  # Or .tail(10) if you want to see end

# Save to a new CSV file
df_sorted.to_csv("transformed_marketing_campaign.csv", index=False)


# In[41]:


df_sorted.to_csv("transformed_marketing_campaign.csv", index=False)


# In[42]:


import os
print(os.getcwd())


# In[43]:


df_sorted.to_csv("/Users/shravani/Desktop/transformed_marketing_campaign.csv", index=False)


# In[17]:


#CHECKING NULL VALUES


# In[18]:


df.isnull().sum()


# DROP NULL VALUES

# In[19]:


df = df.dropna()


# In[20]:


df.isnull().sum()


# In[21]:


df['Age'] = 2025 - df['Year_Birth']


# # AGE OF A CUSTOMER

# In[22]:


df['Age']


# TOTAL SPEND
# 

# In[23]:


df['TotalSpend'] = (
    df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] +
    df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
)


# In[24]:


df['TotalSpend']


# Family size

# In[25]:


df['FamilySize'] = df['Kidhome'] + df['Teenhome'] + 1  # +1 for customer
df['FamilySize']


# Customer Tenure

# In[26]:


df['TenureDays'] = df['Year_Birth'] * 365

print(df[['Dt_Customer', 'TenureDays']].head())


# Segment Customer

# In[27]:


df['SpenderType'] = pd.qcut(df['TotalSpend'], 3, labels=['Low', 'Medium', 'High'])
df['SpenderType']


# Based on Age

# In[28]:


df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 30, 45, 60, 100], labels=['Young', 'Mid-Age', 'Adult', 'Senior'])
df['AgeGroup']


# In[29]:


df.drop(['Z_CostContact', 'Z_Revenue'], axis=1, inplace=True)


# In[30]:


df.to_csv("transformed_marketing_campaign.csv", index=False)

df.to_csv("/Users/shravani/Desktop/transformed_marketing_campaign.csv", index=False)
  


# In[ ]:





# In[ ]:




