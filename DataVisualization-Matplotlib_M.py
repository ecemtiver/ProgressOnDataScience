#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Veri Görselleştirme
#Matplotlab


# In[ ]:


#kategorik değişken:sütun grafil, countplot, barplot
#sayısal değişken: histogram, boxplot (hangi aralıklarda, hangi frekanslar var, kendi içindeki dağılım ve aykırı değerler)


# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None) #pandas'ın kısıtlı veri gösterme işlemine ayar
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()


# In[5]:


df["sex"].value_counts() #kategorik değişkenler için ilk adım


# In[7]:


df["sex"].value_counts().plot(kind='bar') #matplot library güncel olmalı
plt.show()


# In[ ]:


#pip install matplotlib
#pip install --upgrade matplotlib


# In[10]:


plt.hist(df["age"])
plt.show()


# In[11]:


plt.boxplot(df["fare"]) #aykırı değerleri çeyreklik değerler üzerinden gösterebilir, genel dağılım dışındaki gözlemleri yakalar
plt.show()


# In[14]:


import numpy as np

#plot özelliği

x = np.array([1,3])
y = np.array([0,130])

plt.plot(x,y)
plt.show()


# In[15]:


x = np.array([1,8])
y = np.array([0,150])

plt.plot(x,y)
plt.show()


# In[24]:


x = np.array([1,8])
y = np.array([0,150])
plt.plot(x, y, 'o') #grafik açık kalır ve kodları girersem, noktalar grafiğin üzerine yerleşir
plt.show() #sıfırdan yazdım


# In[25]:


x = np.array([2,3,4,5])
y = np.array([7,8,9,10])

plt.plot(x, y)
plt.show()


# In[27]:


x = np.array([2,3,4,5])
y = np.array([7,8,9,10])

plt.plot(x, y, 'o')
plt.show()


# In[30]:


#marker ('o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h')

y = np.array([22,88,99,100])
plt.plot(y, marker='o')
plt.show()


# In[32]:


y = np.array([22,88,99,100])
plt.plot(y, marker='P')
plt.show()


# In[29]:


y = np.array([22,88,99,100])
plt.plot(y, marker='*')
plt.show()


# In[40]:


y = np.array([10, 50, 150, 250]) #sıra fark etmiyor
plt.plot(y)
plt.show()


# In[35]:


y = np.array([11,33,55,150])
plt.plot(y, linestyle="dashed")
plt.show()


# In[42]:


x = np.array([1,3])
y = np.array([110,330,550,1500])
plt.plot(y, linestyle="dotted")
plt.show()


# In[37]:


y = np.array([11,33,55,150])
plt.plot(y, linestyle="dashdot")
plt.show()


# In[38]:


y = np.array([11,33,55,150])
plt.plot(y, linestyle="dashed", color='red')
plt.show()


# In[44]:


x = np.array([23, 17, 30, 60])
y = np.array([11,33,22,150])
plt.plot(x)
plt.plot(y)
#plt.show()


# In[46]:


#labels *

p = np.array([20, 25, 30, 35, 40, 45, 50, 55])
q = np.array([200, 210 ,220 ,230, 240, 250, 260, 270])

plt.plot(p,q)
plt.title("Başlık")


# In[50]:


p = np.array([20, 25, 30, 35, 40, 45, 50, 55])
q = np.array([200, 210 ,220 ,230, 240, 250, 260, 270])

plt.plot(p,q)
plt.title("Başlık")
plt.xlabel("p ekseni")
plt.ylabel("q ekseni")

plt.grid()
plt.show()


# In[ ]:


#SUBPLOTS


# In[57]:


#plot1

x = np.array([20, 25, 30, 35, 40, 45, 50, 55])
y = np.array([200, 210 ,220 ,230, 240, 250, 260, 270])
plt.subplot(1, 2, 1) #1 satırlı 2 sütunlu grağigin birinci grafiği
plt.title("ilk")


# In[58]:


x = np.array([20, 25, 30, 35, 40, 45, 50, 55])
y = np.array([200, 210 ,220 ,230, 240, 250, 260, 270])
plt.subplot(1, 2, 1)
plt.title("I")
plt.plot(x,y)


# In[65]:


#plot2

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([20, 21 ,22 ,23, 24, 25, 26, 27])
plt.subplot(1, 2, 2) #1 satırlı 2 sütunlu grağigin birinci grafiği
plt.title("II")
plt.plot(x,y)

plt.show()


# In[70]:


x = np.array([20, 25, 30, 35, 40, 45, 50, 55])
y = np.array([200, 210 ,220 ,230, 240, 250, 260, 270])
plt.subplot(1, 3, 1)
plt.title("I")
plt.plot(x,y)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([20, 21 ,22 ,23, 24, 25, 26, 27])
plt.subplot(1, 3, 2) #1 satırlı 2 sütunlu grağigin birinci grafiği
plt.title("II")
plt.plot(x,y)

#plot3
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([20, 21 ,22 ,23, 24, 25, 26, 27])
plt.subplot(1, 3, 3) #1 satırlı 2 sütunlu grağigin birinci grafiği
plt.title("III")
plt.plot(x,y)
plt.show()

