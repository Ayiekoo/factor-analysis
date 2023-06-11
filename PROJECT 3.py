#!/usr/bin/env python
# coding: utf-8

# In[1]:


### age in weeks
age = input("Please enter your age: ")
age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)


# In[2]:


### PIE CHART
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


# the dataset
cause = ['Chronic illnesses', 'Unintentional injuries', 'Influenza and Pneumonia', 'Sepsis', 'Others']
# percentile
percentile = [62, 5, 4, 2, 26]

# setting the size of the figure
plt.figure(figsize=(10,10))
# explode the largest pie in the dataset
explode = (0.05, 0, 0, 0, 0)
# set the pie chart properties
plt.pie(percentile, labels=cause, explode=explode, autopct='%1.1f%%', startangle=70)
# set the axis to draw the circle
plt.axis('equal')
# set the title of the pie chart
plt.title('Ohio State - 2012 : Leading Causes of Death')
# show the pie chart
plt.show()


# In[10]:


### FEATURE SELECTION
import numpy as np
import pandas as pd


# In[11]:


# setting a seed for reproducibility
np.random.seed(0)

# Creating a data for 5 factors (traits), with 3 observed variables each
extraversion = np.random.normal(5, 2, 1000)
agreeableness = np.random.normal(5, 2, 1000)
conscientiousness = np.random.normal(5, 2, 1000)
neuroticism = np.random.normal(5, 2, 1000)
openness = np.random.normal(5, 2, 1000)

# For each trait, we have 3 observed variables (questions)
data = {
    "extraversion_1": extraversion + np.random.normal(0, 1, 1000),
    "extraversion_2": extraversion + np.random.normal(0, 1, 1000),
    "extraversion_3": extraversion + np.random.normal(0, 1, 1000),
    "agreeableness_1": agreeableness + np.random.normal(0, 1, 1000),
    "agreeableness_2": agreeableness + np.random.normal(0, 1, 1000),
    "agreeableness_3": agreeableness + np.random.normal(0, 1, 1000),
    "conscientiousness_1": conscientiousness + np.random.normal(0, 1, 1000),
    "conscientiousness_2": conscientiousness + np.random.normal(0, 1, 1000),
    "conscientiousness_3": conscientiousness + np.random.normal(0, 1, 1000),
    "neuroticism_1": neuroticism + np.random.normal(0, 1, 1000),
    "neuroticism_2": neuroticism + np.random.normal(0, 1, 1000),
    "neuroticism_3": neuroticism + np.random.normal(0, 1, 1000),
    "openness_1": openness + np.random.normal(0, 1, 1000),
    "openness_2": openness + np.random.normal(0, 1, 1000),
    "openness_3": openness + np.random.normal(0, 1, 1000)
}

# Creating a DataFrame from our data
df = pd.DataFrame(data)


# In[ ]:




