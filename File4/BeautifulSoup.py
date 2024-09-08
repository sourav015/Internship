#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[123]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[23]:


page2=requests.get("https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/")
page2


# In[24]:


soup=BeautifulSoup(page2.content)
soup


# In[26]:


titles=[]
for i in soup.find_all('h2',class_="h5 article-title"):
    titles.append(i.text)
titles


# In[27]:


dates=[]
for i in soup.find_all('p',class_="article-date"):
    dates.append(i.text)


# In[28]:


dates


# In[29]:


author=[]
for i in soup.find_all('p',class_="article-authors"):
    author.append(i.text)


# In[30]:


author


# In[31]:


print(len(titles),len(dates),len(author))


# In[32]:


most_downloaded_article=pd.DataFrame({'Article_Title':titles,'Date':dates,'Author':author})
most_downloaded_article


# In[33]:


page3=requests.get("https://www.bewakoof.com/bestseller?sort=popular%20")
page3


# In[34]:


soup3=BeautifulSoup(page3.content)
soup3


# In[39]:


p_name=[]
for i in soup3.find_all('div',class_="productNaming bkf-ellipsis"):
    p_name.append(i.text)


# In[40]:


p_name


# In[66]:


price=[]
for i in soup3.find_all('div',class_="discountedPriceText clr-p-black false"):
    price.append(i.text.replace('₹',''))


# In[67]:


price


# In[60]:


image=[]
for i in soup3.find_all('img',class_="productImgTag"):
    image.append(i['src'])


# In[61]:


image


# In[68]:


print(len(p_name),len(price),len(image))


# In[69]:


Top_Ten_Product=pd.DataFrame({'Product Name':p_name,'Price':price,'Image':image})
Top_Ten_Product


# In[70]:


page4=requests.get("https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,Jayanagar,Rajajinagar")
page4


# In[73]:


soup4=BeautifulSoup(page4.content)
soup4


# In[113]:


h_title=[]
for i in soup4.find_all('h2',class_="flex items-center m-0 heading-6 font-semi-bold"):
    h_title.append(i.text)


# In[114]:


h_title


# In[78]:


location=[]
for i in soup4.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    location.append(i.text)


# In[79]:


location


# In[98]:


EMI=[]
for i in soup4.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0"):
    EMI.append(i.text.replace('₹',''))


# In[99]:


EMI


# In[100]:


print(len(h_title),len(location),len(EMI))


# In[121]:


Property=pd.DataFrame({"House Name & Location":h_title,"Area":location,"EMI":EMI})


# In[122]:


Property


# In[124]:


page5=requests.get("https://www.cnbc.com/world/?region=world")
page5


# In[125]:


soup5=BeautifulSoup(page5.content)
soup5


# In[126]:


headlines=[]
for i in soup5.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    headlines.append(i.text)
headlines


# In[146]:


date=[]
for i in soup5.find_all('span',class_="RiverByline-datePublished"):
    date.append(i.text)
date


# In[132]:


link=[]
for i in soup5.find_all('a',class_='LatestNews-headline'):
    link.append(i['href'])
    
link   


# In[129]:


print(len(headlines),len(date),len(link))


# In[133]:


page7=requests.get("https://www.patreon.com/coreyms")
page7


# In[134]:


soup7=BeautifulSoup(page7.content)
soup7


# In[148]:


headlines=[]
for i in soup7.find_all('div',class_="sc-1cvoi1y-0 hxhWXn"):
    headlines.append(i.text)
headlines


# In[ ]:




