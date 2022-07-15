#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn')


# In[2]:


df = pd.read_csv('ford.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.describe()


# In[7]:


df.columns


# In[8]:


sns.countplot(x='transmission', data=df)
plt.title('Transmission types')
plt.show()


# In[10]:


fig = plt.figure(figsize=(7,7))
colors = ("gold", "red", "yellowgreen")
wp = {'linewidth':2, 'edgecolor':"black"}
tags = df['transmission'].value_counts()
explode= (0.1, 0.1, 0.1)
tags.plot(kind='pie', autopct='%1.1f%%', shadow=True, colors = colors, startangle=90, 
          wedgeprops = wp, explode=explode, label='')
plt.title('Distribution of the different transmission types')
plt.show()


# In[12]:


sns.countplot(y='fuelType', data=df)
plt.title('Fuel type')
plt.show()


# In[13]:


print(df['fuelType'].value_counts())


# In[14]:


fueltype = df['fuelType']
transmission = df['transmission']
price = df['price']


# In[17]:


fig, axes = plt.subplots(1,2, figsize=(15,5), sharey=True)
fig.suptitle('Visualizing categorical data columns')
sns.barplot(x=fueltype, y=price, ax = axes[0])
sns.barplot(x=transmission, y=price, ax=axes[1])


# In[20]:


fig, axes = plt.subplots(1,2, figsize=(15,5), sharey=True)
fig.suptitle('Visualizing categorical data columns')
sns.boxenplot(x=fueltype, y=price, ax = axes[0])
sns.boxenplot(x=transmission, y=price, ax= axes[1])


# In[21]:


df['year'].hist()


# In[22]:


sns.displot(df.price)
plt.title('Car price distribution plot')
plt.show()


# In[23]:


df[['mileage', 'tax', 'mpg', 'engineSize']].hist(bins=30, figsize=(10,10), color='blue')
plt.show()


# In[25]:


plt.figure(figsize=(8,6))
plt.title('fuel economy vs price')
sns.scatterplot(x=df['mpg'], y=df['price'], hue=df['fuelType'])
plt.xlabel('Fuel Economy')
plt.ylabel('Price')
plt.show()


# In[26]:


df.replace({'transmission':{'Manual':0, 'Automatic':1, 'Semi-Auto':2}}, inplace=True)
df.replace({'fuelType':{'Petrol':0, 'Diesel':1, 'Hybrid':2, 'Electric':3, 'Other':4}}, inplace=True)


# In[27]:


df.head()


# In[28]:


plt.figure(figsize=(12,10))
sns.countplot(y='model', data=df)
plt.title('Model Types')
plt.show()


# In[29]:


print(df['model'].value_counts())


# In[30]:


modified_df = df.drop("model", axis=1)
modified_df.head()


# In[31]:


df.corr()


# In[32]:


plt.figure(figsize=(10,7))
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation between the columns')
plt.show()


# In[33]:


df.corr()['price'].sort_values()


# In[34]:


fig = plt.figure(figsize=(7,5))
plt.title('Correlation between year and price')
sns.regplot(x='price', y='year', data=df)

