#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Logistic:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, inventory_space):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.inventory_space = inventory_space
        
    def print_report(self):
        print(f"""The company {self.company_name} was founded in {self.foundation_year}.
             The founder of the company is {self.founder_name}.
             Company slogan: {self.company_slogan}
             Inventory space of the company: {self.inventory_space}""")
        
    def update_inventory_space(self, new_storage_space):
        self.inventory_space=new_storage_space
        print(f"Inventory space has been changed to {self.inventory_space}:")


# In[2]:


#create the object "logistic_company1" with it's attributes
logistic_company1 = Logistic("LogCom", 1990, "Laura McCartey", "There is no place we cannot reach.", 2500)

#update the inventory space
logistic_company1.update_inventory_space(3000)
#call the print_report method for logistic_company1
logistic_company1.print_report()

