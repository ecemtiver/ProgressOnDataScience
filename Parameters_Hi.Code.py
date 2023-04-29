#!/usr/bin/env python
# coding: utf-8

# # Exercise 1
# 
# x = 3 ----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# y = 4.5 -----> integere çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# z = "8" -----> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# a = "12" -----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# b = "46.8" ------> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.

# In[15]:


x=3
x=float(x)
print(x)
print(type(x))

y=4.5
y=int(y)
print(y)
print(type(y))

z="8"
z=int(z)
print(z)
print(type(z))

a="12"
a=float(a)
print(a)
print(type(a))

b="46.8"
b=float(b)
b=int(b)
print(b)
print(type(b))


# # Excersice 2
# 
# Üç değişken belirleyelim, bu değşkenler kişi adı olsun. Değişkenlere kişilerin yaşlarını atayalım. (ÖRN: ayse=22)
# 
# Belirlediğimiz üç değişkeni bir biriyle karşılaştırma operatörleri ile karşılatıralım. (ayse>mehmet)
# 
# Bu karşılaştırmalara mantıksal operatörleride ekleyelim.

# In[23]:


irem=22
ecem=33
mert=44

print(irem<ecem)
print(mert<ecem)

print(irem<ecem or mert<ecem)
print(irem<ecem and mert<ecem)
print(irem<ecem or irem<mert)

print(not irem<ecem and irem<mert)
print(not (irem>ecem and irem>mert))
print(not irem>ecem)


# # Excercise 3
# 
# Kullanıcıdan iki değer girmesini isteyin. Girilen değerlerin toplama,çıkarma,çarpma,bölme sonuçlarını yazdıralım.

# In[6]:


j=int(input("değer no1 giriniz:"))
i=int(input("değer no2 giriniz:"))

summation=j+i
print(summation)

subtraction=j-i
print(subtraction)

division=j/i
print(division)

multiplication=j*i
print(multiplication)


# # Excercise 4
# 
# Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini isteyelim ve cevaplarını yazdıralım.

# In[7]:


name=input("what's your name? ")
age=input("how old are you? ")
city=input("where are you live? ")
job=input("what is your occupation? ")

print("I am " + name + " and I am " + age + " years old. I live in " + city + ". I am a " + job + ".")


# # Excersice 5 
# 
# "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlayalım.
# - İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçelim.
# - İfadeyi hepsini büyük harf olacak hale çevirelim.  ("HI-KOD VERİ BİLİMİ ATÖLYESİ")
# - İfadeyi hepsini büyük harf olacak hale çevirelim.("hi-kod veri bilimi atölyesi")
# 
# "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçelim. ("02468", "13579")
# 

# 

# In[10]:


h = "Hi-Kod Veri Bilimi Atölyesi"
print(h.split())
print(h.upper())
print(h.lower())


# In[18]:


numbers = "0123456789" 
even = numbers[::2]
odd = numbers[1::2]
print(even)
print(odd)