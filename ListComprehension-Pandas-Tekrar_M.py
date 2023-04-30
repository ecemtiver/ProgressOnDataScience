#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3 List Comprehension ve 23 Pandas Görevi


# In[ ]:


#Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.


# In[ ]:


#Numeric olmayan değişkenlerin de isimleri büyümeli.
#Tek bir list comprehension yapısı kullanılmalı.


# In[2]:


import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) #pandas'ın tüm satır ve sütunları yazdırmasını istedim
pd.set_option('display.width', 250) #dframe'in maksimum genişlik ayarı

df = sns.load_dataset("car_crashes")
df.columns


# In[3]:


df.info() #eksik veri ve veri tipleri hakkında genel bilgi aldım


# In[13]:


#tek satır

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# In[14]:


["NUM_" + col.upper() if df[col].dtype != "0" else col.upper() for col in df.columns] #ilk hata


# In[12]:


["NUM_" + col.upper() if col != "abbrev" else col.upper() for col in df.columns] #alternatif hata düzeltme


# In[ ]:


#Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.


# In[ ]:


#Tüm değişkenlerin isimleri büyük harf olmalı.
#Tek bir list comprehension yapısı ile yapılmalı.


# In[11]:


[col.upper() + "FLAG" if "no" not in col else col.upper() for col in df.columns]


# In[ ]:


#Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.


# In[ ]:


#Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
#Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz


# In[22]:


og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head(10)


# In[29]:


#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import pandas as pd
import seaborn as sns
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = sns.load_dataset("titanic")
df.head()


# In[28]:


df.shape


# In[30]:


#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts()


# In[32]:


#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique()


# In[33]:


#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].unique()


# In[35]:


#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df[["pclass", "parch"]].nunique()


# In[37]:


#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

df["embarked"].dtype


# In[39]:


df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype


# In[40]:


df.info()


# In[42]:


#Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.

df[df["embarked"] == "C"].head()


# In[44]:


#Görev 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz.

df[df["embarked"] != "S"].head()


# In[46]:


df[df["embarked"] != "S"]["embarked"].unique() #S nan olarak tanımlandı


# In[49]:


df[~(df["embarked"] == "S")]["embarked"].unique() #alternatif


# In[50]:


#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df["age"] < 30) & (df["sex"] == "female")].head()


# In[51]:


#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df[(df["fare"] > 500) | (df["age"] > 70)]. head()


# In[52]:


#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz. (eksik değer analizi)

df.isnull().sum()


# In[58]:


#Görev 12: who değişkenini dataframe’den çıkarınız. (sütunsa,x=1;satır,x=0)

df.drop("who", axis=1, inplace=True)
df.info()


# In[66]:


#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"].mode()
#type(df["deck"].mode())


# In[64]:


type(df["deck"].mode()) #en sıkı tekrar eden değer için mode döndürdüm


# In[65]:


df["deck"].mode()[0] #en sık tekrar eden değerlerden ilkini döndürmek için


# In[67]:


df["deck"].fillna(df["deck"].mode()[0], inplace=True) #hatırlatma: pandas series oldduğu için köşeli parantex ve kalıcı değişiklik için inplace


# In[69]:


#check
df["deck"].isnull().sum()


# In[72]:


#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

type(df["age"].mean())


# In[73]:


df["age"].mean()


# In[77]:


df["age"].fillna(df["age"].mean(), inplace=True)
df.head()


# In[79]:


#check
df.isnull().sum()


# In[82]:


#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})


# In[87]:


#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

def age_thirty(age):
    if age<30:
        return küçük
    else:
        return büyük
    
df["age_flag"] = df["age"].apply(lambda x:age_thirty(x)) #her değere fonksiyonu uygulatmak için lambda


# In[91]:


#alternatif

df["age_flag"] = df["age"].apply(lambda x: 0 if  x<30 else 1)
df.head()


# In[93]:


#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset("tips")
df.head()


# In[95]:


df.shape


# In[97]:


#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["time"]).agg({"total_bill": ["min", "max", "mean"]})


# In[100]:


#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["day", "time"]).agg({"total_bill": ["min", "max", "mean", "sum"]})


# In[104]:


#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["min", "max", "mean", "sum"],
                                                                         "tip": ["min", "max", "mean", "sum"]})


# In[108]:


#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()


# In[116]:


#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head(21)


# In[121]:


#Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[0:30] #ascending=false; büyükten küçüğe sıralama
new_df

