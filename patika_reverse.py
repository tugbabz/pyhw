#!/usr/bin/env python
# coding: utf-8

# In[17]:


l = [[1, 2], [3, 4], [5, 6, 7]]
def revlist(l):
    for k in range(len(l)):
        l[k].reverse()
    l.reverse()
    print(l)
            


# In[18]:


revlist(l)

