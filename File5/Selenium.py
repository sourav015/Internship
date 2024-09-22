#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install selenium')


# In[421]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
import time


# In[65]:


driver=webdriver.Chrome()


# In[66]:


driver.get('https://www.naukri.com/')


# In[67]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[70]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/div[1]/div/input')
location.send_keys('Delhi/NCR')


# In[71]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[72]:


salary=driver.find_element(By.XPATH,'/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/label/i')
salary.click()


# In[73]:


job_tittle=[]
job_location=[]
company_name=[]
experience_required=[]


# In[74]:


title=driver.find_elements(By.XPATH,'//a[@class="title "]')
for i in title:
    title=i.text
    job_tittle.append(title)


# In[75]:


location=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location:
    location=i.text
    job_location.append(location)


# In[76]:


name=driver.find_elements(By.XPATH,'//span[@class=" comp-dtls-wrap"]')
for i in name:
    name=i.text
    company_name.append(name)


# In[77]:


experience=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience:
    experience=i.text
    experience_required.append(experience)


# In[90]:


df=pd.DataFrame({'Title':job_tittle[0:10],'Location':job_location[0:10],'Company':company_name[0:10],'Experience':experience_required[0:10]})
df


# In[95]:


df['Company']=df['Company'].str.replace('\n|[0-9]|Reviews|\.','',regex=True)
df


# In[281]:


driver=webdriver.Chrome()


# In[97]:


driver.get('https://www.shine.com/')


# In[98]:


designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Analyst')


# In[99]:


location=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location.send_keys('Bangalore')


# In[101]:


search=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button')
search.click()


# In[102]:


job_title=[]
job_location=[]
company=[]
experience=[]


# In[103]:


title=driver.find_elements(By.XPATH,'//strong[@class="jobCard_pReplaceH2__xWmHg"]')
for i in title:
    title=i.text
    job_title.append(title)


# In[104]:


location=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location:
    location=i.text
    job_location.append(location)


# In[105]:


name=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in name:
    name=i.text
    company.append(name)


# In[106]:


exp=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in exp:
    exp=i.text
    experience.append(exp)


# In[108]:


print(len(job_title),len(job_location),len(company),len(experience))


# In[109]:


Shine_Jobs=pd.DataFrame({'Job Title':job_title[0:10],'Job Location':job_location[0:10],'Company':company[0:10],'Experience':experience[0:10]})
Shine_Jobs


# In[110]:


Shine_Jobs['Job Location']=Shine_Jobs['Job Location'].str.replace('\n|[0-9]|\+','',regex=True)
Shine_Jobs


# In[355]:


driver=webdriver.Chrome()


# In[356]:


driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')
time.sleep(2)


# In[357]:


rating=[]
Review=[]
full_reviews=[]


# In[358]:


ratings=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings:
    ratings=i.text
    rating.append(ratings)
    rating[:100]


# In[359]:


reviews=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews:
    reviews=i.text
    full_reviews.append(reviews)
    full_reviews[:100]


# In[360]:


rev=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev:
    rev=i.text
    Review.append(rev)
    Review[:100]


# In[363]:


next2=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[2]')
next2.click()


# In[364]:


ratings2=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings2:
    ratings2=i.text
    rating.append(ratings2)


# In[365]:


reviews2=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews2:
    reviews2=i.text
    full_reviews.append(reviews2)


# In[366]:


rev2=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev2:
    rev2=i.text
    Review.append(rev2)


# In[367]:


next3=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[4]')
next3.click()


# In[368]:


ratings3=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings3:
    ratings3=i.text
    rating.append(ratings3)


# In[369]:


reviews3=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews3:
    reviews3=i.text
    full_reviews.append(reviews3)


# In[370]:


rev3=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev3:
    rev3=i.text
    Review.append(rev3)


# In[371]:


next4=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[5]')
next4.click()


# In[372]:


ratings4=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings4:
    ratings4=i.text
    rating.append(ratings4)


# In[373]:


reviews4=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews4:
    reviews4=i.text
    full_reviews.append(reviews4)


# In[374]:


rev4=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev4:
    rev4=i.text
    Review.append(rev4)


# In[375]:


next5=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[6]')
next5.click()


# In[376]:


ratings5=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings5:
    ratings5=i.text
    rating.append(ratings5)


# In[377]:


reviews5=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews5:
    reviews5=i.text
    full_reviews.append(reviews5)


# In[378]:


rev5=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev5:
    rev5=i.text
    Review.append(rev5)


# In[379]:


next6=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[7]')
next6.click()


# In[380]:


ratings6=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings6:
    ratings6=i.text
    rating.append(ratings6)


# In[381]:


reviews6=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews6:
    reviews6=i.text
    full_reviews.append(reviews6)


# In[382]:


rev6=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev6:
    rev6=i.text
    Review.append(rev6)


# In[383]:


next7=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[7]')
next7.click()


# In[384]:


ratings7=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings7:
    ratings7=i.text
    rating.append(ratings7)


# In[385]:


reviews7=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews7:
    reviews7=i.text
    full_reviews.append(reviews7)


# In[386]:


rev7=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev7:
    rev7=i.text
    Review.append(rev7)


# In[387]:


next8=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[7]')
next8.click()


# In[388]:


ratings8=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings8:
    ratings8=i.text
    rating.append(ratings8)


# In[389]:


reviews8=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews8:
    reviews8=i.text
    full_reviews.append(reviews8)


# In[390]:


rev8=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev8:
    rev8=i.text
    Review.append(rev8)


# In[392]:


next9=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[7]')
next9.click()


# In[393]:


ratings9=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings9:
    ratings9=i.text
    rating.append(ratings9)


# In[394]:


reviews9=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews9:
    reviews9=i.text
    full_reviews.append(reviews9)


# In[395]:


rev9=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev9:
    rev9=i.text
    Review.append(rev9)


# In[402]:


next10=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[7]")
next10.click()


# In[403]:


ratings10=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in ratings10:
    ratings10=i.text
    rating.append(ratings10)


# In[404]:


reviews10=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in reviews10:
    reviews10=i.text
    full_reviews.append(reviews10)


# In[405]:


rev10=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in rev10:
    rev10=i.text
    Review.append(rev10)


# In[409]:


print(len(rating),len(Review),len(full_reviews))


# In[407]:


flipkart_Product=pd.DataFrame({'Rating':rating[0:100],'Review':Review[0:100],'Full Review':full_reviews[0:100]})
flipkart_Product


# In[408]:


driver.close()


# In[562]:


driver=webdriver.Chrome()


# In[563]:


driver.get('https://www.flipkart.com/')


# In[564]:


product=driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys('sneakers')


# In[566]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
search.click()


# In[586]:


brand=[]
product_des=[]
price=[]


# In[587]:


name=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
for i in name:
    name=i.text
    brand.append(name)


# In[588]:


description=driver.find_elements(By.XPATH,'//a[1]')
for i in description:
    description=i.text
    product_des.append(description)


# In[589]:


cost=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj"]')
for i in cost:
    cost=i.text
    price.append(cost)


# In[ ]:





# In[ ]:





# In[590]:


print(len(brand),len(product_des),len(price))


# In[449]:


flipkart=pd.DataFrame({'Brand':brand,'Product Description':product_des,'Price':price})
flipkart


# In[593]:


driver=webdriver.Chrome()


# In[594]:


driver.get("https://www.amazon.in/")


# In[596]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/div/input")
search.send_keys('Laptop')


# In[597]:


search_button=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_button.click()


# In[599]:


check=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/span/div/div/div[5]/ul[2]/span/span[9]/li/span/a/div/label/i')
check.click()


# In[633]:


title=[]
rating=[]
price=[]


# In[638]:


name=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in name:
    name=i.text
    title.append(name)


# In[639]:


cost=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in cost:
    cost=i.text
    price.append(cost)


# In[636]:


ratings=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-3-5"]')
for i in ratings:
    ratings=i.text
    rating.append(ratings)


# In[640]:


title[:10]


# In[641]:


price[:10]


# In[642]:


rating[:10]


# In[605]:


print(len(title),len(price),len(rating))


# In[501]:


Amazon_Laptop_10=pd.DataFrame({'Title':title[:10],'Rating':rating[:10],'Price':price[:10]})
Amazon_Laptop_10


# In[531]:


driver=webdriver.Chrome()


# In[532]:


driver.get("https://www.azquotes.com/")


# In[505]:


Top_Quotes=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
Top_Quotes.click()


# In[506]:


quote=[]
author=[]
type_of_quote=[]


# In[507]:


authors=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors:
    authors=i.text
    author.append(authors)


# In[508]:


tag=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag:
    tag=i.text
    type_of_quote.append(tag)


# In[509]:


quotes=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes:
    quotes=i.text
    quote.append(quotes)


# In[511]:


next2=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
next2.click()


# In[512]:


authors2=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors2:
    authors2=i.text
    author.append(authors2)


# In[513]:


tag2=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag2:
    tag2=i.text
    type_of_quote.append(tag2)


# In[514]:


quotes2=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes2:
    quotes2=i.text
    quote.append(quotes2)


# In[516]:


next3=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next3.click()


# In[517]:


authors3=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors3:
    authors3=i.text
    author.append(authors3)


# In[518]:


tag3=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag3:
    tag3=i.text
    type_of_quote.append(tag3)


# In[521]:


quotes3=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes3:
    quotes3=i.text
    quote.append(quotes3)


# In[523]:


next4=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next4.click()


# In[524]:


authors4=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors4:
    authors4=i.text
    author.append(authors4)


# In[525]:


tag4=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag4:
    tag4=i.text
    type_of_quote.append(tag4)


# In[526]:


quotes4=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes4:
    quotes4=i.text
    quote.append(quotes4)


# In[533]:


next5=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next5.click()


# In[534]:


authors5=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors5:
    authors5=i.text
    author.append(authors5)


# In[535]:


tag5=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag5:
    tag5=i.text
    type_of_quote.append(tag5)


# In[536]:


quotes5=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes5:
    quotes5=i.text
    quote.append(quotes5)


# In[538]:


next6=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next6.click()


# In[539]:


authors6=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors6:
    authors6=i.text
    author.append(authors6)


# In[540]:


tag6=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag6:
    tag6=i.text
    type_of_quote.append(tag6)


# In[541]:


quotes6=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes6:
    quotes6=i.text
    quote.append(quotes6)


# In[543]:


next7=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next7.click()


# In[544]:


authors7=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors7:
    authors7=i.text
    author.append(authors7)


# In[545]:


tag7=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag7:
    tag7=i.text
    type_of_quote.append(tag7)


# In[546]:


quotes7=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes7:
    quotes7=i.text
    quote.append(quotes7)


# In[547]:


next8=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next8.click()


# In[548]:


authors8=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors8:
    authors8=i.text
    author.append(authors8)


# In[549]:


tag8=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag8:
    tag8=i.text
    type_of_quote.append(tag8)


# In[550]:


quotes8=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes8:
    quotes8=i.text
    quote.append(quotes8)


# In[551]:


next9=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next9.click()


# In[552]:


authors9=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors9:
    authors9=i.text
    author.append(authors9)


# In[553]:


tag9=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag9:
    tag9=i.text
    type_of_quote.append(tag9)


# In[554]:


quotes9=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes9:
    quotes9=i.text
    quote.append(quotes9)


# In[556]:


next10=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[13]/a')
next10.click()


# In[557]:


authors10=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in authors10:
    authors10=i.text
    author.append(authors10)


# In[558]:


tag10=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in tag10:
    tag10=i.text
    type_of_quote.append(tag10)


# In[559]:


quotes10=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes10:
    quotes10=i.text
    quote.append(quotes10)


# In[560]:


QUOTES=pd.DataFrame({'Quotes':quote[:1000],'Author':author[:1000],'Type of Quotes':type_of_quote[:1000]})
QUOTES


# In[561]:


driver.close()


# In[ ]:




