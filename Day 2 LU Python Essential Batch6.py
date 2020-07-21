#!/usr/bin/env python
# coding: utf-8

# # Basic syntax
#     Back slash \
#     Triple Quotes
#     String inside the quotes
#     Escape Sequence of String
#     Formatted Output
#   
#     

# Back slash is for continuation in python

# In[3]:


print("Hello python")


# Triple Quotes  are used when using multi-lines of strings
#     Suitaible for printing Text Art
#     Also when making a Document String
#     
#     

# In[8]:


print("""(”)….(”)
( ‘ o ‘ )
(”)–(”)
(””’)-(””’)""")


# In[9]:


print('hello world')


# # String inside Quotes
# 

# Escape Sequence of Strings

# In[10]:


print("python's world")


# In[13]:


print("Hello\tpthon")


# In[14]:


print("Hello\npython")


# In[11]:


print('python\'s world')


# # formatted output

# In[14]:


name = "Eve"
marks = 70.789
age = 30
print("The name of person is ", name, "marks is", marks,"age is",age)


# In[18]:


print(f"The name of person is {name} the marksis{70.789} age is{age}")


# In[19]:


print(f"The name of the person is {name} the marks is {marks} age is {age}")


# # python variables
# 
#     Variables means linking of a data to a name.
#     According to the data-type, the interpreter reserves the memory data space.
#     Variables refers tothe memory location that contains the data

# In[27]:


a=10
b=10
_=20


# In[23]:


if1 = 10


# In[29]:


_10 = 6 


# In[30]:


cisco_temp = 40


# # Python Assignment statement
# You can use multiple statement
# 
# <variable name>=<data>Example
#     x = y = z = 10 

# In[32]:


x = y = 10


# In[33]:


id(x)


# In[34]:


id(y)


# In[35]:


del x means not deleting value but the binding i.e =, ->


# # Arithmetics operators

# In[36]:


5**5


# In[37]:


15+35


# In[38]:


10-25


# In[39]:


10/5


# In[40]:


20/3


# In[43]:


10%3


# In[44]:


20//6


# # Comparison perators

# In[45]:


a = 10
b = 20
a == b


# In[46]:


c = 10
a == c


# In[47]:


c <a


# In[48]:


c <= a


# In[49]:


a >= b


# In[53]:


a = get_ipython().getoutput('b')


# # Assignment operator

# In[ ]:


a = a+b
a+=b


# In[56]:


a = 20
20*30


# # Bitwise Operators

# In[57]:


a = 240
b = 1
a|b 


# In[58]:


bin(a)


# In[59]:


bin(b)


# In[60]:


a & b


# # Logical operators

# In[ ]:


True or True = True
True or F = True
F or T = True
F or F = False

T and F = F
F and T = F
F and F = F
T and T = T


# In[62]:


a = 10 
b = 20
a > 20


# In[63]:


a > 20 or 10 > 9


# In[64]:


a > 20 and 10 > 9


# In[66]:


M


# In[67]:


10 < 9and 20 > M


# In[68]:


10 < 9


# In[69]:


not 10 >9


# In[70]:


not 10 <9


# In[71]:


not True


# # Membership operators

# In[74]:


str1 = "pythonprogramming"
"a" in str1


# In[75]:


"x" in str1


# In[76]:


"x" not in str1


# # Identity Operators

# In[77]:


a = 10
b = 10
a == b


# In[78]:


a is b


# In[79]:


id(a)


# In[80]:


id(b)


# In[81]:


x = 1.5
y = 1.5
x == y


# In[82]:


x is y


# In[83]:


id(x)


# In[84]:


id(y)


# In[85]:


a = -4
b = -4
a is b


# In[86]:


a = 257
b = 257
a is b


# In[87]:


a == b


# # Operator Precedence
#  Increases in descending order

# In[88]:


10/20*4


# In[89]:


20+20/40*2


# # Important points
# 
# Operators in the same box have the same precedence.
# 
# Operators in the same box group left to right
# 
# Exponentiation, in which groups are from right to left.
# 
# 

# In[90]:


2**-1


# In[91]:


5**-2


# Floor Division

# In[92]:


8/3


# In[93]:


8//3


# In[94]:


10 >8 >9


# In[ ]:




