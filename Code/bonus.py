#!/usr/bin/env python
# coding: utf-8

# ## Loading libraries and dataset
import pandas as pd
pets = pd.read_csv(r'C:\Users\nick2\Desktop\MS\Denver Broncos\pets.csv')

# To supress the warnings
import warnings
warnings.filterwarnings("ignore")

# ## BONUS
# - Please upload a script with a user-defined function that accepts OwnerID as an input and returns a vector of pet names for the given OwnerID.

# In[63]:


def bonus_script(x):
    pet_names=pets[pets['OwnerID']==x].Name.to_list()
    print('Pets for OwnerID {}: {}'.format(x,pet_names))
print('Please enter Owner ID:')
bonus_script(int(input()))





