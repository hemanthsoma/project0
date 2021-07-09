#!/usr/bin/env python
# coding: utf-8

# In[3]:


import warnings
from pymongo import MongoClient
warnings.filterwarnings('ignore')


# In[4]:


#LocalHost 
client = MongoClient('localhost',27017)


# In[5]:


database = client["mealsinfo"]


# In[7]:


info_data = database["collection"]


# In[8]:


#find one
print(info_data.find_one())


# In[9]:


#find all
for i in info_data.find():
    print(i)


# In[10]:


#limit
for i in info_data.find().limit(5):
    print(i)


# In[11]:


record = {'meal_id': 2755, 'category': 'Somosa', 'state': 'Indian'}


# In[12]:


#Inserting one record
info_data.insert_one(record)


# In[13]:


manyRecords = [
    {"meal_id":2700,'category':'hjk'},
    {"meal_id":2701,'category':'jik'}
]


# In[14]:


#inserting many records
info_data.insert_many(manyRecords)


# In[15]:


myquery = {"address":"Ap"}
newValues = {"$set":{"address":"nlr"}}


# In[16]:


#updating one record
info_data.update_one(myquery,newValues)


# In[17]:


#deleting one record
info_data.delete_one(record)


# In[18]:


#updating many records
info_data.update_many({'meal_ids': 1}, {'$inc': {'meals_ids': 3}})


# In[19]:


#deleting many records
info_data.delete_many(myquery)


# In[20]:


#counting data
count = info_data.find().count()


# In[22]:


#sorting data
info_data.find().sort("_id",1)


# In[ ]:


#Drop data
info_data.drop()

