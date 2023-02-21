#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

#Read Data
df = pd.read_csv(r'C:\Users\KRIST\Downloads\archive\movies.csv')


# In[2]:


#Overview data
df.head(5)


# In[3]:


#Finding missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[4]:


# Data Types 
print(df.dtypes)


# In[5]:


df['released'].astype(str)


# In[6]:


pd.set_option('display.max_rows',None)


# In[7]:


#Drop duplicates
df['company'].drop_duplicates().sort_values(ascending=False)


# In[8]:


#Scatterplot for Budget vs Gross 
sns.regplot(x="gross", y="budget", data=df, scatter_kws={"color": "red"}, line_kws ={"color": "blue"})
plt.title('Gross Earnings vs Budget')
plt.show()


# In[9]:


sns.regplot(x="score", y="gross", data=df,scatter_kws={"color": "red"}, line_kws ={"color": "blue"})


# In[10]:


df.corr(method ='spearman')


# In[11]:


#High correlation between gross and budget, gross and votes


# In[12]:


correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[13]:


df.head()


# In[26]:


df_numerized = df
for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
        
df_numerized.head()


# In[15]:


df.head(5)


# In[16]:


correlation_matrix = df_numerized.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[17]:


#Votes and gross, gross and budget are highly correlated.


# In[18]:


df_numerized.corr(method='pearson')


# In[19]:


correlation_mat = df_numerized.corr()
correlation_pairs = correlation_mat.unstack()
correlation_pairs


# In[20]:


sorted_pairs = correlation_pairs.sort_values(ascending=True)
sorted_pairs


# In[21]:


#Sorted high correlation pairs
high_corr = sorted_pairs[(sorted_pairs)>0.5]
high_corr


# In[22]:


#Votes and budgets have highest correlation earnings 
#Company has low correlation


# In[23]:


print(df.dtypes)


# In[24]:


for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes
        
print(df.dtypes)


# In[25]:


sns.stripplot(x="votes", y="budget", data=df)


# In[ ]:




