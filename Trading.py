#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Trading:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, sales, expenses, revenue):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.sales = sales
        self.expenses = expenses
        self.revenue = revenue
        
    def print_report(self):
        print(f"""
        The company name is {self.company_name} and was founded in {self.foundation_year}.
        The founder of the company is {self.founder_name}.
        Company slogan: {self.company_slogan}
        Total sales: {self.sales}
        Total expenses: {self.expenses}
        Total revenue: {self.revenue}""")
        
    def update_sales_and_expenses(self, new_sales, new_expenses):
        self.sales += new_sales
        self.expenses += new_expenses
        print("Sales and expenses are updated!")
        
    def calculate_revenue(self):
        self.revenue = self.sales - self.expenses
        print(f"The revenue of the company is: {self.revenue}")


# In[13]:


trading_company1 = Trading('Tracom', 2005, 'Chong Wu', 'We revolutionize trading.', 5000, 2000, 3000)

trading_company1.update_sales_and_expenses(100,50)


# In[12]:


trading_company1.calculate_revenue()


# In[14]:


trading_company1.print_report()

