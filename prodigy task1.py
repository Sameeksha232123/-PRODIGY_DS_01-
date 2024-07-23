#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[9]:


df = pd.read_csv('C:/Users/Hp/Downloads/titanic/train.csv')
print(df.head())


# In[10]:


# Visualizing the distribution of ages using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'].dropna(), kde=False, bins=30)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[11]:


# Visualize the distribution of genders using a bar chart
plt.figure(figsize=(10, 6))
sns.countplot(x='Sex', data=df)
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[ ]:




