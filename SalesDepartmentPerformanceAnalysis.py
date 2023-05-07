#!/usr/bin/env python
# coding: utf-8

# In[1]:


filepath="employee_revenue.txt"


# In[2]:


#open the file in read mode
with open(filepath, "r") as file:
    data=file.read()


# In[3]:


print(data)


# In[4]:


#seperate the data into lines
lines=data.splitlines()
print(lines)


# In[5]:


#take the first line
string=lines[0]
print(string)


# In[6]:


#remove the whitespaces from the edges
string=string.strip(" ")
print(string)


# In[7]:


#convert the string to lowercase
string=string.lower()
string


# In[8]:


#capitalize the first character
string=string.capitalize()
string


# In[9]:


#split the sentence into words
split_string=string.split(" ")
split_string


# In[10]:


#use the index 0 to access to the name element
name=split_string[0]
name


# In[11]:


#use the index 2 to access the number of calls elements
call_number=split_string[2]
call_number


# In[12]:


#find the element with the '$' sign
for i in split_string:
    #divide the number from it
    if '$' in i:
        average_deal_size=i.split("$")[0]
#print the average deal size
average_deal_size


# In[13]:


#find the index of element "dollars"
dollars_index = split_string.index("dollars")
dollars_index


# In[14]:


#subtract one from the index to identity the index of the revenue element
revenue_index = dollars_index - 1
revenue_index


# In[15]:


#extract the revenue
revenue = split_string[revenue_index]
revenue


# In[16]:


#print out the extracted information
print("Name:", name)
print("Number of calls:", call_number)
print("Average deal size:", average_deal_size)
print("Revenue:", revenue)


# In[17]:


#check the types
print("Name type:", type(name))
print("Number of calls type:", type(call_number))
print("Average deal size type:", type(average_deal_size))
print("Revenue type:", type(revenue))


# In[18]:


#convert the datatypes of average deal size, number of calls, and revenue
average_deal_size = int(average_deal_size)
call_number = int(call_number)
revenue = int(revenue)


# In[19]:


#print out the information again
print("Name type:", type(name))
print("Number of calls type:", type(call_number))
print("Average deal size type:", type(average_deal_size))
print("Revenue type:", type(revenue))


# In[20]:


#create empty lists for the names, number of calls, average deal sizes, revenues
names = []
call_numbers = []
average_deal_sizes = []
revenues = []


# In[55]:


#loop over the whole data
for employee in lines:
    
    #clean the string
    employee = employee.strip(" ")
    employee =  employee.lower()
    employee = employee.capitalize()

    #split the clean string
    split_employee = employee.split(" ")

    #extract the name
    name = split_employee[0]
    call_number = split_employee[2]

    #extract the average deal size
    for i in split_employee:
        if "$" in i:
            average_deal_size = i
    average_deal_size = average_deal_size.split("$")[0]

    #extract the revenue
    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index - 1
    revenue = split_employee[revenue_index]

    #convert to the correct data types
    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int(revenue)
    
    #append the information to the lists
    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)
    
#print out the information
print("Names:", names)
print("Number of calls", call_numbers)
print("Average deal size:", average_deal_sizes)
print("Revenues:", revenues)


# In[69]:


#create empyt lists again
names = []
call_numbers = []
average_deal_sizes = []
revenues = []


# In[70]:


#define a function to clean and extract the data
def clean_extract(lines):
    for employee in lines:
        
        employee=employee.strip(" ")
        employee=employee.lower()
        employee=employee.capitalize()
        
        split_employee=employee.split(" ")
        
        name=split_employee[0]
        call_number=split_employee[2]
        
        for i in split_employee:
            if "$" in i:
                average_deal_size=i
                average_deal_size=average_deal_size.split("$")[0]
                
        dollars_index=split_employee.index("dollars")
        revenue_index=dollars_index-1
        revenue=split_employee[revenue_index]
        
        average_deal_size=int(average_deal_size)
        call_number=int(call_number)
        revenue=int(revenue)
        
        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)
    
    return names, call_numbers, average_deal_sizes, revenues


# In[71]:


#assign returned values to variables
names, call_numbers, average_deal_sizes, revenues = clean_extract(lines)


# In[72]:


#print out the information
print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal sizes:", average_deal_sizes)
print("Revenues:", revenues)


# In[ ]:


#check the number of employees
print(len(names))


# In[73]:


#generate IDs
IDs=list(range(0,11))
print(IDs)


# In[76]:


#check the number of IDs
len(IDs)


# In[77]:


#pair the names with the IDs in a dictionary
dictionary1=dict(zip(IDs,names))
dictionary1


# In[78]:


#pair the names with the revenues
dictionary2=dict(zip(revenues,names))
dictionary2


# In[81]:


#find the lowest performing employees(ascending order)
sorted_dictionary=sorted(dictionary2)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])


# In[82]:


##find the best performing employees(descending order)
sorted_dictionary=sorted(dictionary2, reverse=True)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])

