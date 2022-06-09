#!/usr/bin/env python
# coding: utf-8

# In[10]:


inputlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat = []
def flatten(inputlist):
    for i in inputlist:
        if isinstance(i, list):
            flatten(i)
        else:
            flat.append(i)
    
flatten(inputlist)
print(flat)
        

