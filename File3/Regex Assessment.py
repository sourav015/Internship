#!/usr/bin/env python
# coding: utf-8

# In[1]:


import regex as re


# In[102]:


#Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

Text= 'Python Exercises, PHP exercises.'
search=re.sub('\s|,|\.',':',Text)
print(search)


# In[16]:


#Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.

import re
import pandas as pd


# In[17]:


df=pd.DataFrame({'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']})
df


# In[46]:


df1=df['SUMMARY'].str.replace('[^a-zA-Z\s]|XXXXX','',regex=True) 
df1


# In[72]:


#Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

def text_match(text):
    pattern=re.compile(r'\b\w{4}+\b')
    matches=pattern.findall(text)
    return matches


# In[73]:


text= 'Virat Kohli is the best batsman in the world'
result=text_match(text)
print(result)


# In[74]:


#Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
import re
def text_string(text):
    pattern1=re.compile(r'\b\w{3,5}+\b')
    search=pattern1.findall(text)
    return search


# In[75]:


text= 'Virat Kohli is the best batsman in the world'
result1=text_string(text)
print(result1)


# In[103]:


#Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.

import re

def remove_parentheses(strings):
    pattern = re.compile(r'[(+*)]')
    modified_strings = []
    for string in strings:
        modified_string = re.sub(pattern,"",string)
        modified_strings.append(modified_string)
    return modified_strings


# In[104]:


sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
result = remove_parentheses(sample_text)
print(result)


# In[172]:


#Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression

f = open("demofile100.txt", "w")
f.write("example (.com)")
f = open("demofile100.txt", "a")
f.write("hr@fliprobo (.com)")
f = open("demofile100.txt", "a")
f.write("github (.com)")
f = open("demofile100.txt", "a")
f.write("Hello (Data Science World)")
f = open("demofile100.txt", "a")
f.write("Data (Scientist)")
f.close()
with open('demofile100.txt', 'r') as file:
    text = file.read()
    modified_text = re.sub(r'\([^()]*\)', '', text)
    with open('demofile100.txt', 'w') as file:
        file.write(modified_text)


# In[173]:


f = open("demofile100.txt", "r")
print(f.read())


# In[11]:


#Write a regular expression in Python to split a string into uppercase letters.

import re
Sample_text= 'ImportanceOfRegularExpressionsInPython'
result=re.findall('[A-Z][^A-Z]*',Sample_text)
result


# In[12]:


#Create a function in python to insert spaces between words starting with numbers

import re

def insert_spaces(text):
  # Use regular expression to find words starting with numbers
    pattern = r'(\d+)([A-Za-z]+)'
    result = re.sub(pattern, r' \1\2', text)
    return result
text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(text)
print(output)


# In[13]:


#Create a function in python to insert spaces between words starting with capital letters or with numbers

import re

def insert_spaces(text):
  # Use regular expression to find words starting with numbers
    pattern = r'(\d+)([A-Za-z]+)'
    result = re.sub(pattern, r' \1 \2', text)
    return result
text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(text)
print(output)


# In[24]:


#Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters

import re
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv")
df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])
df['first_five_letters']


# In[49]:


#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores

def matching(string):
    pattern = r'^[\w]*$'
    if re.search(pattern, string):
        print("String matches the pattern")
    else:
        print("String does not match the pattern")


matching("Sourov_Majumder015")
matching("Sourov Majumder")
matching("SOUROV MAJUMDER")


# In[50]:


#Write a Python program where a string will start with a specific number

def match_num(string):
    text = re.compile(r"^\d")
    if text.match(string):
        return True
    else:
        return False
print(match_num('123sourov'))
print(match_num('sourov123'))


# In[51]:


#Write a Python program to remove leading zeros from an IP address

import re
ip = "192.168.001.001"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[61]:


#Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country"

pattern = r"(\b([A-Z][a-z]+) \d{1,2}(?:st|nd|rd|th)? \d{4}\b)"

matches = re.search(pattern, text)
print(matches)


# In[67]:


#Write a Python program to search some literals strings in a string

patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s"\n' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[68]:


#Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % (match.re.pattern, match.string, s, e))


# In[71]:


#Write a Python program to find the substrings within a string

text = 'Kohli Indian, Shami Indian, Binny Indian'
pattern = 'Indian'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# In[74]:


#Write a Python program to find the occurrence and position of the substrings within a string

text = 'Kohli Indian, Shami Indian, Binny Indian'
pattern = 'Indian'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" from %d to %d' % (text[s:e], s, e))


# In[79]:


#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

def change(date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date1 = "1992-01-29"
print("Original date: ",date1)
print("New date: ",change(date1))


# In[84]:


#Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory

def numbers(string):
  pattern = re.compile(r'\d+\.\d{1,2}\b')
  decimal_numbers = re.findall(pattern, string)
  return decimal_numbers
sample_text = "01.11 011.111 2.11111 111.2 123.05 23.89 5.99"
output = numbers(sample_text)
print(output)


# In[89]:


#Write a Python program to separate and print the numbers and their position of a given string

text = "The were 30 apples and 20 bananas"

for num in re.finditer("\d+", text):
    print(num.group(0))
    print("Position:", num.start())


# In[101]:


#Write a regular expression in python program to extract maximum/largest numeric value from a string

Sample_Text= 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
numbers = re.findall('\d+',Sample_Text)
max_num=map(int,numbers)
print('The largest Number:\n',max(max_num))


# In[118]:


#Create a function in python to insert spaces between words starting with capital letters

def insert_spaces(text):
  # Use regular expression to find words starting with numbers
    pattern = r'([A-Z][a-z0-9]+)'
    result = re.sub(pattern, r' \1', text)
    return result
text = "RegularExpressionIsAnImportantTopicInPython"
output = insert_spaces(text)
print(output)


# In[119]:


#Python regex to find sequences of one upper case letter followed by lower case letters

pattern = r'[A-Z][a-z]+'
text = "Regular Expression is an Important Topic in Python"

matches = re.findall(pattern, text)
print(matches)


# In[134]:


#Write a Python program to remove continuous duplicate words from Sentence using Regular Expression

sentence = "Hello hello world world"
pattern = r'\b(\w+)(?:\W+\1\b)+'
result = re.sub(pattern, r'\1', sentence)
print(result)


# In[143]:


#Write a python program using RegEx to accept string ending with alphanumeric character.

def check_string(string):
    pattern = r"[A-za-z0-9]$"
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False


# In[145]:


sample_text='sourov1'
print(check_string(sample_text))
sample_text1='12sourov'
print(check_string(sample_text1))
sample_text2='12sourov@'
print(check_string(sample_text2))


# In[150]:


#Write a python program using RegEx to extract the hashtags

import re
def text_string(text):
    pattern1=re.compile(r'#\w+')
    search=pattern1.findall(text)
    return search


# In[151]:


text= """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
result1=text_string(text)
print(result1)


# In[158]:


#Write a python program using RegEx to remove <U+..> like symbols 
input_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

pattern = r"<U\+\w{4}>"
output_text = re.sub(pattern, "", input_text)

print(output_text)


# In[171]:


#Write a python program to extract dates from the text stored in the text file

f = open("demofile3.txt", "w")
f.write("Ron was born on 12-09-1992 and he was admitted to school 15-12-1999")
f.close()
with open('demofile3.txt', 'r') as file:
    text = file.read()
    pattern = r'\d{2}-\d{2}-\d{4}'
    dates = re.findall(pattern, text)
    for date in dates:
        print(date)


# In[168]:


#Create a function in python to remove all words from a string of length between 2 and 4

import re

def remove(string):
    pattern = re.compile(r'\b\w{2,4}\b')
    update = re.sub(pattern, '', string)
    return update


# In[170]:


Sample_Text= "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
result = remove(Sample_Text)
print(result)


# In[ ]:




