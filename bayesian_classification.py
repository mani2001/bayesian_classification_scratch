#!/usr/bin/env python
# coding: utf-8

# In[2]:


#manikantan
#500075394
#108
#cse-ai and ml-batch-4
import pandas as pd


# In[68]:


data = pd.read_csv("C:/Users/manikantan/Desktop/decision.csv")
data.head()


# In[56]:


features = ['Age','income','student','credit_range']
target = ['buy']
Age = {'youth':sum(data['Age']=='youth'),'middle':sum(data['Age']=='middle'),'senior':sum(data['Age']=='senior')}
income = {'high':sum(data['income']=='high'),'medium':sum(data['income']=='medium'),'low':sum(data['income']=='low')}
student = {'yes':sum(data['student']=='yes'),'no':sum(data['student']=='no')}
credit_range = {'fair':sum(data['credit_range']=='fair'),'excellent':sum(data['credit_range']=='excellent')}
buy = {'yes':sum(data['buy']=='yes'),'no':sum(data['buy']=='no')}


# In[67]:


age_user = input('enter age range ')
income_user = input('enter income range ')
student_user = input('enter student status ')
credit_range_user = input('enter credit range')
prob_yes = (sum((data['Age']==age_user) & (data['buy']=='yes'))/Age[age_user])*(sum((data['income']==income_user) & (data['buy']=='yes'))/income[income_user])*(sum((data['student']==student_user) & (data['buy']=='yes'))/student[student_user])*(sum((data['credit_range']==credit_range_user) & (data['buy']=='yes'))/credit_range[credit_range_user])
prob_no = (sum((data['Age']==age_user) & (data['buy']=='no'))/Age[age_user])*(sum((data['income']==income_user) & (data['buy']=='no'))/income[income_user])*(sum((data['student']==student_user) & (data['buy']=='no'))/student[student_user])*(sum((data['credit_range']==credit_range_user) & (data['buy']=='no'))/credit_range[credit_range_user])
if(prob_yes>=prob_no):
    print('Yes! Student buys laptop')
else:
    print('*************************')
    print('NO. Student does not buy laptop')


# In[ ]:





# In[ ]:




