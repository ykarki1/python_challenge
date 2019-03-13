#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = "election.csv"


# In[3]:


election = pd.read_csv(file)


# In[4]:


election.head()


# In[5]:


#counts of all unique voter ID
total_voters=(int(election["Voter ID"].nunique()))
print(total_voters)


# In[6]:


# Array of all candidates
candidates = election["Candidate"].unique()
print(candidates)
print(len(election[election["Candidate"] == "Khan"]))


# In[7]:


#created a new blank list
candidate_votes = []

#looped through the candidates to add their total votes in the list "candidate_votes"
for i in range(len(candidates)):
    candidate_votes.append(len(election[election["Candidate"] == str(candidates[i])]))
    
print(candidate_votes)


# In[8]:


percentlist = []
for k in range(len(candidate_votes)):
    percentlist.append("{0:.3f}".format(candidate_votes[k]*100/total_voters))
    
print(percentlist)


# In[9]:


# Created dictionary with candidate's name and their votes percentage
candidate_dict = dict(zip(candidates, percentlist))
print(candidate_dict)


# In[17]:


#Hardest part of the homework #Googled this function
def get_max_val_key(candidate_dict):
    max_value = None
    for key in candidate_dict:
        if max_value is None or max_value < candidate_dict[key]:
            max_value = candidate_dict[key]
            max_key = key
    return max_key

winner = get_max_val_key(candidate_dict)
print(winner)


# In[18]:


print("Election Results")
print(("-")*25)
print("Total Votes:      "+ str(total_voters))
print(("-")*25)
i = 0
for key in candidate_dict:
    print(key, candidate_dict[key]+"% ("+str(candidate_votes[i])+")")
    i = i+1
print(("-")*25)
print("Winner :  "+ winner)


# In[19]:


# python untitled.ipynb >> results.txt


# In[ ]:




