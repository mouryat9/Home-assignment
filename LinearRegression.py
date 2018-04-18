
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[3]:


df=pd.read_csv("D:/linearregression.csv")
df.head()


# In[4]:


df.corr()


# In[6]:


plt.figure(1)
plt.scatter(df['Certification'],df['Salary'])
plt.title("certification vs salary")
plt.xlabel("certification")
plt.ylabel("salary")
plt.show()


# In[7]:


plt.figure(1)
plt.scatter(df['Experience in years'],df['Salary'])
plt.title("Experience in years vs salary")
plt.xlabel("Experience in years")
plt.ylabel("salary")
plt.show()


# In[41]:


from sklearn.cross_validation import train_test_split
X= np.array(df["Experience in years"]).reshape(-1,1)
Y= np.array(df["Salary"]).reshape(-1,1)

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3)


# In[42]:


linear = LinearRegression()
linear.fit(x_train,y_train)



# In[45]:


plt.figure(1)
plt.scatter(x_test,y_test,color='blue')
plt.plot(x_train,linear.predict(x_train),color='red')
plt.title("certification vs salary")
plt.xlabel("certification")
plt.ylabel("salary")
plt.show()

