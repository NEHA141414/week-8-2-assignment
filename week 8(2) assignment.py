#!/usr/bin/env python
# coding: utf-8

# Q-1 List any five functions of the pandas library with execution.

# Ans-1 
#     1.  Value_counts() : pandas value_count() function is used to show the counts of all unique elements in columns of a dataframe.
#     
#     2. Read Data : we can read data in pandas data frame as read_csv() . two most used data read formates are csv and excel . if we are reading data in excel format , we can also give sheet names as follows . there are other less used options of other file types too.
#     
#     3. Head and Tail : To see the data frame we can use df.head(). Head returns the first rows, if no input is given it will always show above 5 row . In contrast to see below rows , we can use df.tail().
#     
#     4. Shape ,Size and  Info : Two most basic functions after reading data is to know the number of rows and columns , and to know the datatype of variables. we can use df.shape, it gives  a total number of rows and then columns . df.size() returns the number of rows times number of columns in the data frame .We can also use df.info() , from that we get different information such as rows from RangeIndex, data columns and then data type of each columns .It also includes the information of non-null counts.
#     
#     
#     5. Describe : Then to understand basic statistics of variables we can use df.describe() . It will give you count, mean , standard deviation, and also 5 number summary.
#     

# Q-2 Given a pandas dataframe df with columns 'A','B' AND 'C' , write a python function to re-index the dataframe with a new index that starts from 1 and increments by 2 for each row.

# In[2]:


import pandas as pd 
 
data={"a":[1,2,3],
      "b":[4,5,6],
      "c":["neha","krish","hitesh"]}
df=pd.DataFrame(data,index=['A','B','C'])


# In[3]:


df


# In[4]:


df.reindex([1,3,5])


# In[5]:


df


# Q-3 You have a pandas dataframe df with a column named values . Write a python function that iterates over the dataframe and calculates the sum of the first three  values in the values columns . The function should print the sum of the concole.
# 
# For example ,if the values columns of df contains the values [10,20,30,40,50] , your function should calculate and print the sum of the first three values, which is 60.

# In[10]:


data={'values':[10,20,30,40,50]}


# In[11]:


df=pd.DataFrame(data)


# In[12]:


df


# In[34]:


df.sum()


# In[41]:


def calculate_sum_of_first_three(df):
    first_three_values=df['values'].head(3)
    sum_of_first_three=first_three_values.sum()
    print(f"the sum of the first three values is :{ sum_of_first_three}")
df=pd.DataFrame({'values':[10,20,30,40,50]})
calculate_sum_of_first_three(df)


# Q-4 Given a pandas dataframe df with a columns text ,write a python function to create a new columns word_count that contains the number of words in each row of the text column.

# In[44]:


def word_count_columns(df):
    df['word_count']=df['text'].apply(lambda x:len(str(x).split()))
    return df
df=pd.DataFrame({'text':['hello, how are you ?, how do you do ?,this is a simple text,python is great']})
df_with_word_count=word_count_columns(df)
print(df_with_word_count)


# Q-5 How are dataframe .size() and dataframe.shape() different?

# Dataframe.size() : it returns the total number of element in the dataframe , which is calculate by multiplying the number of row by the number of columns.It returns a single values representing the size of the dataframe .
# 
# Dataframe.shape() :it returns a tuple representing the dimensions of the dataframe . It provides the number of row and columns .It returns a tuple with two elements.
# 
# 
# 

# Q-6 Which function of pandas do we use to read an excel file?

# Ans-6 Pandas read_excel() functon is used for reading the excel files. Files can be imported using a URL link or can be directly imported from the disk . 

# Q-7 You have a pandas dataframe df that contains a columns named Email that contains email address in the format username@domain.com. Write a python function that creates a new columns username in df that contains only the username part of each email address.
# 
# The username is the part of the email address that appears before the @ symbol. For example , if the email address is john.deo@example.com the username columns should contains john.deo .Your function should extract the username from each email address and store it in the new username column.

# In[4]:


import pandas as pd

def extract_username(df):
    df['username']=df['email'].str.split('@').str[0]
    return df
df=pd.DataFrame({'email':['john@example.com','jane@test.com','bob@domain.com']})
df=extract_username(df)
print(extract_username(df))


# Q-8 You have a pandas dataframe df with columns  'A','B' and 'C' .Write a python function all rows where the value in column 'A' is greater than value in column 'B' is less than 'C'  function should return a new dataframe that contains only the selected rows.
# 
# 
# 

# In[6]:


data={'A':[3,8,6,2,9],
      'B':[5,2,9,3,1],
       'c':[1,7,4,5,2]}
df=pd.DataFrame(data)
df


# In[7]:


df[0:3]


# In[ ]:




