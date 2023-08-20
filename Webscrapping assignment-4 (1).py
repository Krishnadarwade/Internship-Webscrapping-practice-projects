#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[11]:


import selenium                                
from selenium import webdriver                 
import pandas as pd                            
from selenium.webdriver.common.by import By      
import warnings                                  
warnings.filterwarnings("ignore")
import time                                     
driver = webdriver.Chrome()


# In[2]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[3]:


rank=[]
name=[]
artist=[]
upload_date=[]
views=[]


# In[5]:


number=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"][1]')
for i in number:
 n=i.text
 name.append(n)


# In[6]:


name


# In[10]:


ra=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]')
for i in ra:
  r=i.text
  rank.append(r)


# In[11]:


rank


# # Solution of question-2 

# In[13]:


driver.get('https://www.bcci.tv/')


# In[15]:


click=driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div[1]/div[2]/a")
click.click()


# In[16]:


match=[] 
series=[]
place=[]
date=[]
time=[]


# In[18]:


click2=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
click2.click()


# In[19]:


click3=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
click3.click()


# In[20]:


click4=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
click4.click()


# In[21]:


click5=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
click5.click()


# In[22]:


name=driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]')
for i in name:
  n1=i.text
  match.append(n1)



# In[23]:


name1=driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for i in name1:
    n2=i.text
    series.append(n2)


# In[24]:


name2=driver.find_elements(By.XPATH,'//div[@class="match-place ng-scope"]')
for i in name2:
  n3=i.text
  place.append(n3)


# In[26]:


placee=[]


# In[27]:


name2=driver.find_elements(By.XPATH,'//div[@class="match-place ng-scope"]')
for i in name2:
  n3=i.text
  placee.append(n3)


# In[28]:


placee


# In[29]:


name3=driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in name3:
 n4=i.text
 date.append(n4)   


# In[30]:


name4=driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in name4:
  n5=i.text
  time.append(n5)


# In[31]:


print(len(match),len(series),len(place),len(date),len(time))


# In[35]:


Dataframe_for_upcoming_international_matches_of_INDIA= pd.DataFrame({'Match_title':match,'Series':series,'Place':place,'Date':date,'Time':time})


# In[36]:


Dataframe_for_upcoming_international_matches_of_INDIA


# # Solution of question 3

# In[31]:


driver.get('https://www.statisticstimes.com/')


# In[32]:


find=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
find.click()


# In[33]:


find2=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
find2.click()


# In[34]:


find3=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
find3.click()


# In[35]:


rank=[]
state=[]
gSDP1=[]
gSDP2=[]
share=[]
gDPbillion=[]


# In[36]:


top=driver.find_elements(By.XPATH,'//td[@class="data1"]')
for i in top:
  t2=i.text
  rank.append(t2)


# In[37]:


top2=driver.find_elements(By.XPATH,'//td[@class="name"]')
for i in top2:
  t3=i.text
  state.append(t3)


# In[38]:


top3=driver.find_elements(By.XPATH,'//td[@class="data sorting_1"]')
for i in top3:
  t4=i.text
  gSDP1.append(t4)


# In[45]:


gsdp2=[]


# In[46]:


top4=driver.find_elements(By.XPATH,'//td[@class="data"][1]')
for i in top4:
 t5=i.text
 gsdp2.append(t5)


# In[41]:


top5= driver.find_elements(By.XPATH,'//td[@class="data"][2]')
for i in top5:
 t6=i.text
 share.append(t6)


# In[49]:


top6= driver.find_elements(By.XPATH,'//td[@class="data"][3]')
for i in top6:
 t7=i.text
 gDPbillion.append(t7)


# In[52]:


ranks=rank[0:33]
states=state[0:33]
gsdp1=gSDP1[0:33]
gsdp2=gSDP2[0:33]
shares=share[0:33]
gsdpbillion=gDPbillion[0:33]


# In[53]:


Dataset_for_GDP= pd.DataFrame({'Rank':ranks,'State':states,'GSDP(18-19)- at current prices':gsdp1,'GSDP(19-20)- at current prices':gsdp2,'Share(18-19)':shares,'GDP($ billion)':gsdpbillion})


# In[54]:


Dataset_for_GDP


# # Solution of question-4

# In[ ]:


driver.get('')


# In[ ]:





# # Solution of question-5

# In[2]:


driver.get('https://www.billboard.com/')


# In[4]:


find=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div/div/div/ul/li[1]/h3/a')
find.click()


# In[10]:


find1=driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]/a')
find1.click()


# In[ ]:


song=[]


# In[7]:


last_week=[]
peak=[]
weeks=[]


# In[13]:


s1=driver.find_elements(By.XPATH,'//h3[@class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"]')
for i in s1:
  g=i.text
  song.append(g)


# In[17]:


artists=[]


# In[18]:


a1=driver.find_elements(By.XPATH,'//span[@class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"]')
for i in a1:
 t=i.text
 artists.append(t)


# In[20]:


artist


# In[10]:


lw1=driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')
for i in lw1:
 la=i.text
 last_week.append(la)


# In[37]:


last_week


# In[ ]:





# # solution of question-6

# In[12]:


driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-')


# In[ ]:





# # Solution of question-7

# In[13]:


driver.get('https://www.imdb.com/list/ls095964455/')


# In[14]:


name=[]
year_span=[]
genre=[]
run_time=[]
ratings=[]
votes=[]


# In[16]:


n1=driver.find_elements(By.XPATH,'//a[@href="/title/tt0944947/?ref_=ttls_li_tt"]')
for i in n1:
  na=i.text
  name.append(na)


# In[17]:


name


# In[19]:


ys=driver.find_elements(By.XPATH,'//span[@class="lister-item-year text-muted unbold"]')
for i in ys:
 ys=i.text
 year_span.append(ys)


# In[21]:


ge=driver.find_elements(By.XPATH,'//span[@class="genre"]')
for i in ge:
 gn=i.text
 genre.append(gn)


# In[23]:


rt=driver.find_elements(By.XPATH,'//span[@class="runtime"]')
for i in rt:
 ru=i.text
 run_time.append(ru)


# In[26]:


ra=driver.find_elements(By.XPATH,'//span[@class="ipl-rating-star__rating"]')
for i in ra:
  rg=i.text
  ratings.append(rg)


# In[32]:


vo=driver.find_elements(By.XPATH,'//span[@class="text-muted text-small"]')
for i in vo:
 vg=i.text
 votes.append(vg)


# In[33]:


votes


# In[ ]:





# # Solution of question-8

# In[7]:


driver.get('https://archive.ics.uci.edu/')


# In[16]:


dataset=[]
data_type=[]
task=[]
attribute_type=[]
instances=[]
attribute=[] 
year=[]


# In[13]:


view=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
view.click()


# In[14]:


expand=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/div/label[2]/div[2]/span[2]')
expand.click()


# In[17]:


ds=driver.find_elements(By.XPATH,'//h2[@class="truncate text-primary"]')
for i in ds:
 da=i.text
 dataset.append(da)
    


# In[19]:


tk=driver.find_elements(By.XPATH,'//span[@class="truncate"]')
for i in tk:
 ta=i.text
 task.append(ta)
    


# In[29]:


dty=driver.find_elements(By.XPATH,'//span[@class="truncate"][1]/tbody/tr/td[2]')
for i in dty:
 data=i.text
 data_type.append(data)


# In[30]:


data_type


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




