#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file = "resources/budget_data.csv"


# In[3]:


original = pd.read_csv(file)
original.head(10)


# In[4]:


#count all months in the dataset
months = original['Date'].count()
print('Total months: ' + str(months))


# In[ ]:





# In[5]:


#sum the profit/losses column
net_pl = original['Profit/Losses'].sum()
print('Total profit/losses: ' + str(net_pl))


# In[6]:


#make a list of all the profits/losses for each month
pl_list = list(original['Profit/Losses'])

#use numpy to calculate differences between each month's profits/losses in the list
differences = np.diff(pl_list)

#use numpy to take the mean of those differences between months in the list
avg = np.average(differences)
avg = avg.round(2)

print('Average change: ' + str(avg))


# In[7]:


#find the greatest increase in differences in the list
maximum = np.max(differences)
maximum
print('Greatest gain: ' + str(maximum))


# In[8]:


#find the greatest decrease in differences in the list
minimum = np.min(differences)
minimum
print('Greatest loss: ' + str(minimum))


# In[9]:


#create list from numpy array of monthly changes
new_diff = list(differences)
#find length of changes list
len(new_diff)


# In[10]:


#add new row at index 0 with value 0 to indicate no change from the month before the first month, 
#since don't have the previous month's data to compare to, give zero
#now our list of monthly change is equal in length to our original dataframe and can be added to that as a new column
new_diff.insert(0, 0)
len(new_diff)


# In[12]:


#add change column to original dataframe
original['Change'] = new_diff


# In[13]:


original.head(10)


# In[17]:


# find the months associated with minimum and maximum

#create new data frame with just the columns for date and change
monthchange = original[['Date', 'Change']]
monthchange


# In[18]:


#from monthchange, sort by change, highest to lowest
highest_change = monthchange.sort_values('Change', ascending=False)
highest_change.head(10)


# In[25]:


highest_change = highest_change.reset_index(drop=True)
max_month = highest_change.loc[0, ]
print(str(max_month['Date']) + ' ' + str(max_month['Change']))


# In[26]:


lowest_change = monthchange.sort_values('Change')
lowest_change.head(10)


# In[27]:


lowest_change = lowest_change.reset_index(drop=True)
min_month = lowest_change.loc[0, :]


# In[28]:


print(str(min_month['Date']) + ' ' + str(min_month['Change']))


# In[29]:


print('Financial Analysis')
print('-----------------------')
print('Total months: ' + str(months))
print('Total profit/losses: ' + str(net_pl))
print('Average change: ' + str(avg))
print('Greatest gain: ' + str(max_month['Date']) + ' ' + str(max_month['Change']))
print('Greatest loss: ' + str(min_month['Date']) + ' ' + str(min_month['Change']))


# In[ ]:




