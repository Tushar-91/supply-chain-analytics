#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[1]:


# Load the supply chain data from a CSV file


# In[2]:


data = pd.read_csv('supply_chain_data.csv')


# In[4]:


data.head()


# In[5]:


data.info()


# In[2]:


# Generate descriptive statistics of the numerical columns in the dataset


# In[7]:


data.describe()


# In[8]:


data.isna().sum()


# In[3]:


# Visualize the relationships between numerical variables, with each data point colored by "Product type"


# In[9]:


sns.pairplot(data,hue='Product type')


# In[4]:


# Separate the columns of the DataFrame into categorical and numerical lists


# In[10]:


categorical = [i for i in data.columns if data[i].dtypes=='object']
numerical = [i for i in data.columns if data[i].dtypes!='object']


# ## Exploratory Data Analysis

# In[5]:


# Count plot for each categorical column


# In[11]:


for i in data.select_dtypes(include='object'):
    sns.countplot(data=data,x=data[i])
    plt.xticks(rotation=90)
    plt.show()


# In[6]:


# Boxplot for each numerical column


# In[12]:


plt.figure(figsize=(12,6))
data.boxplot(grid=False,rot=45,fontsize=15)


# In[7]:


# Group the data by "Product type" and plot the sum of "Revenue generated" for each product type


# In[13]:


data.groupby(['Product type'])[['Revenue generated']].sum().plot(kind='bar',figsize=(8,5),title='Each Product generated revenue',fontsize=20)


# # OBSERVATIONS
# 
# ##### 1. THE MAIN CONCEPT OF ABOVE DATA IS TO FIND THE REVENUE OF PRODUCTS
# ##### 2. SKINCARE ITEMS GET MORE REVENUE GENERATED FOLLOWED BY HAIRCARE AND COSMETICS

# In[8]:


# Group the data by "Product type" and "Location" and plot the sum of "Revenue generated" for each combination


# In[14]:


data.groupby(['Product type','Location'])[['Revenue generated']].sum().sort_index().sort_values(by='Product type',ascending=False).unstack()


# # OBSERVATIONS 
# ##### 1. AS FROM THE DATA SKINCARE PRODUCTS GET MORE REVENUE IN KOLKATA FOLLOWED BY CHENNAI, MUMBAI, BANGALORE AND DELHI.
# 
# ##### 2. HAIRCARE PRODUCTS HAD HIGHEST REVENUE IN BANGALORE THEN MUMBAI AND KOLKATA.
# 
# ##### 3. COMING TO THE COSMETICS MUMBAI HAS PROFITTED THE MOST WITH DELHI ON THE SECOND PLACE AND KOLKATA ON THE THIRD.

# In[9]:


# Group the data by "Product type" and calculate the sum of each numerical column


# In[22]:


data.groupby(['Product type']).sum().sort_index()


# In[10]:


# Bar plot showing product availability with inspection result


# In[23]:


sns.set_theme(context='notebook',style='darkgrid')
sns.barplot(data=data,x='Product type',y='Availability',hue='Inspection results')
plt.title('Product Availability with inspection result')
plt.tight_layout()
plt.show()


# In[11]:


# Scatter plot showing the relationship between "Price" and "Costs" for different product types


# In[24]:


sns.set_theme(style='darkgrid')
sns.scatterplot(data=data,x='Price',hue='Product type',y='Costs')
plt.title('Price vs Cost')
plt.show()


# In[12]:


# Pie chart showing the proportion of manufacturing costs for each product type


# In[27]:


data.groupby(['Product type'])['Manufacturing costs'].sum().sort_values(ascending=False).plot(kind='pie',labels=['skincare','haircare','cosmetics'],autopct='%1.1f%%',title='Manufacturing costs for each product items')


# # OBSERVATIONS
# #### SKINCARE HAS MORE REQUIREMENT FOR MANUFACTURING COSTS

# In[13]:


# Pie chart showing the proportion of defect rates for each product type


# In[28]:


data.groupby(['Product type'])['Defect rates'].sum().sort_values(ascending=False).plot(kind='pie',labels=['skincare','haircare','cosmetics'],autopct='%1.2f%%',title='Defect Rates')


# In[14]:


# Pivot table showing the number of products sold for each product type and location


# In[32]:


pd.pivot_table(data,index='Product type',columns=['Location'],values='Number of products sold')


# In[15]:


# Histograms showing the distribution of "Revenue generated" for each product type


# In[33]:


plt.subplots(1,3,figsize=(25,6))
plt.subplot(141)
ax = sns.histplot(data=data[data['Product type']=='cosmetics'],x='Revenue generated',kde=True)
plt.subplot(142)
ax = sns.histplot(data=data[data['Product type']=='haircare'],x='Revenue generated',kde=True)
plt.subplot(143)
ax = sns.histplot(data=data[data['Product type']=='skincare'],x='Revenue generated',kde=True)
plt.show()


# In[16]:


# Bar plot showing the count of customer demographics for each product type


# In[34]:


data.groupby(['Product type'])['Customer demographics'].value_counts().sort_index().sort_values(ascending=False).plot(kind='bar',title='Customer Demographics product type wise',figsize=(17,6))
plt.xlabel('Product types')
plt.ylabel('Count of values')
plt.show()


# In[17]:


# Bar plot showing the count of customer demographics overall


# In[35]:


data.groupby(['Customer demographics']).sum().sort_index().plot(kind='bar',figsize=(16,8))
plt.title('Customer Demographics')
plt.xlabel('Customer demographics',fontweight=20)
plt.ylabel('Count of values')
plt.show()


# In[18]:


# Histogram showing the distribution of "Stock levels" for each product type


# In[36]:


sns.set_theme(style='darkgrid')
plt.rcParams['figure.facecolor'] = 'yellow'
sns.histplot(data=data,x='Stock levels',hue='Product type',bins=20,palette='viridis')
plt.xlabel('Stock Levels')
plt.ylabel('Count of values')
plt.show()


# ### Highest stock level is between 5 to 60

# In[19]:


# Count plot showing the distribution of "Order quantities"


# In[38]:


plt.figure(figsize=(17,8))
sns.countplot(data=data,x='Order quantities',palette='Wistia')
plt.xlabel('Order Quantities')
plt.ylabel('Count of Values')
plt.show()


# In[20]:


# Count plot showing the distribution of "Availability"


# In[39]:


plt.figure(figsize=(17,8))
sns.countplot(data=data,x='Availability',palette='RdGy')
plt.xlabel('Availability')
plt.ylabel('Count of values')
plt.show()


# In[21]:


# Bar plot showing the count of each "Shipping times" category


# In[40]:


plt.figure(figsize=(15,6))
plt.rcParams['figure.facecolor']='orange'
data['Shipping times'].value_counts().sort_values(ascending=False).plot(kind='bar',title='Shipping times')
plt.xlabel('Time')
plt.ylabel('Count of Values')
plt.show()


# In[22]:


# Bar plot showing the shipping costs of each supplier


# In[41]:


data.groupby(['Supplier name'])['Shipping costs'].sum().sort_values(ascending=False).plot(kind='bar',title='Shipping cost of each supplier',figsize=(15,6))
plt.xlabel('Supplier name')
plt.ylabel('Price of supplier')
plt.show()


# # OBSERVATIONS
# 
# ### 1. MOST OF THE SUPPLIERS SEND THEIR PRODUCTS WITH 7'O CLOCK OR 8'O CLOCK
# ### 2. SUPPLIER 1 SPENT THE MOST PRICE BETWEEN 140 TO 150

# In[23]:


# Group the data by "Supplier name" and "Location" and plot the sum of "Shipping costs" for each combination


# In[42]:


data.groupby(['Supplier name','Location'])[['Shipping costs']].sum().sort_index().unstack()


# In[24]:


# Bar plot showing the shipping costs of each supplier for different locations


# In[43]:


supplier = data.groupby(['Supplier name','Location'])[['Shipping costs']].sum()
supplier.plot(kind='bar',title='Supplier costs route wise',figsize=(15,6))
plt.xlabel('Supplier name')
plt.ylabel('Costs')
plt.show()


# # OBSERVATIONS
# ### 1.SUPPLIER 1 SPEND MORE SHIPPING COST IN KOLKATA AND MUMBAI
# ### 2.SUPPLIER 2 SPEND MORE SHIPPING COST IN DELHI AND BENGALURU
# ### 3.SUPPLIER 3 SPEND MORE SHIPPING COST IN MUMBAI AND BENGALURU
# ### 4.SUPPLIER 4 SPEND MORE SHIPPING COST IN MUMBAI AND KOLKATA
# ### 5.SUPPLIER 5 SPEND MORE SHIPPING COST IN CHENNAI AND MUMBAI

# In[25]:


# Group the data by "Shipping carriers" and "Location" and plot the sum of "Costs" for each combination


# In[44]:


data.groupby(['Shipping carriers','Location'])['Costs'].sum().unstack()


# # OBSERVATIONS
# 
# ### 1. CARRIER A RECIEVED MORE COST IN BENGALURU.
# ### 2. CARRIER B RECIEVED MORE COST IN KOLKATA.
# ### 3. CARRIER C RECIEVED MORE COST IN CHENNAI.

# In[27]:


# Pivot table showing the "Costs" for each supplier and route combination


# In[45]:


pd.pivot_table(data,index='Supplier name',columns=['Routes'],values='Costs')


# In[29]:


# Pivot table showing the plot for "Costs" for each supplier and route combination


# In[46]:


supp = pd.pivot_table(data,index='Supplier name',columns=['Routes'],values='Costs')
supp.plot(kind='bar',title='Supplier costs route wise',figsize=(15,6))
plt.xlabel('Routes')
plt.ylabel('Costs')
plt.show()


# In[30]:


# pivot table showing the plot for supplier cost for different transportation modes


# In[47]:


trans = pd.pivot_table(data,index='Supplier name',columns=['Transportation modes'],values='Costs')
trans.plot(kind='bar',title='Supplier cost vs transportation modes',figsize=(15,6))
plt.xlabel('Supplier name')
plt.ylabel('Costs')
plt.show()


# # OBSERVATIONS
# 
# ### 1. SUPPLIER 1 SPENDS MORE COST IN AIR AND ROAD.
# ### 2. SUPPLIER 2 SPENDS MORE COST IN AIR AND ROAD.
# ### 3. SUPPLIER 3 SPENDS MORE COST IN RAIL AND SEA.
# ### 4. SUPPLIER 4 SPENDS MORE COST IN AIR, RAILS AND ROAD.
# ### 5. SUPPLIER 5 SPENDS MORE COST IN AIR AND ROAD.
