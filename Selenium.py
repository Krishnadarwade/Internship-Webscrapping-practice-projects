#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
import selenium                                
from selenium import webdriver                 
import pandas as pd                            
from selenium.webdriver.common.by import By      
import warnings                                  
warnings.filterwarnings("ignore")
import time                                     
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")


# In[2]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input") 
designation.send_keys('Data analyst')


# In[3]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
location.send_keys('Banglore')


# In[4]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[5]:


job_tittle=[]
job_location=[]
company_name=[]
experience_required=[]


# In[11]:


tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in tags[0:10]:
 title=i.text
 job_tittle.append(title)   
    
location=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location[0:10]:
 Banglore=i.text
 job_location.append(Banglore)
    
Company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company[0:10]:
 name=i.text
 company_name.append(name)
    
experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience[0:10]:
 required=i.text
 experience_required.append(required)


# In[12]:


print(len(job_tittle),len(job_location),len(company_name),len(experience_required))


# In[16]:


Tittle=job_tittle[0:10]
Location=job_location[0:10]
Company=company_name[0:10]
Expirience=experience_required[0:10]


# In[18]:


print(len(Tittle),len(Location),len(Company),len(Expirience))


# In[19]:


Dataframe_for_DataAnalyst_post=pd.DataFrame({'tittle':Tittle,'location':Location,'company':Company,'expirience':Expirience})


# In[20]:


Dataframe_for_DataAnalyst_post


# In[ ]:





# # Solution of question-2

# In[26]:


driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")


# In[27]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input") 
designation.send_keys('Data Scientist')


# In[28]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
location.send_keys('Banglore')


# In[29]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[30]:


job_tittle=[]
job_location=[]
company_name=[]
experience_required=[]


# In[33]:


tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]') 
for i in tags[0:10]:
 title=i.text
 job_tittle.append(title)   
    
location=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location[0:10]:
 Banglore=i.text
 job_location.append(Banglore)
    
Company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company[0:10]:
 name=i.text
 company_name.append(name)
    
experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience[0:10]:
 required=i.text
 experience_required.append(required)


# In[34]:


print(len(job_tittle),len(job_location),len(company_name),len(experience_required))


# In[35]:


Tittle=job_tittle[0:10]
Location=job_location[0:10]
Company=company_name[0:10]
Expirience=experience_required[0:10]


# In[36]:


print(len(Tittle),len(Location),len(Company),len(Expirience))


# In[37]:


Dataframe_for_Datascientist_post=pd.DataFrame({'tittle':Tittle,'location':Location,'company':Company,'expirience':Expirience})


# In[38]:


Dataframe_for_Datascientist_post


# In[ ]:





# 
# # Solution of question-3

# In[56]:


driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")


# In[57]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input") 
designation.send_keys('Data Scientist')


# In[58]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[60]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i')
location.click()


# In[63]:


salary=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
salary.click()


# In[64]:


job_tittle=[]
job_location=[]
company_name=[]
experience_required=[]


# In[65]:


tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]') 
for i in tags[0:10]:
 title=i.text
 job_tittle.append(title)   
    
location=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location[0:10]:
 Banglore=i.text
 job_location.append(Banglore)
    
Company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company[0:10]:
 name=i.text
 company_name.append(name)
    
experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience[0:10]:
 required=i.text
 experience_required.append(required)


# In[66]:


print(len(job_tittle),len(job_location),len(company_name),len(experience_required))


# In[68]:


Dataframe_for_Datascientist_post_in_Delhi=pd.DataFrame({'tittle':job_tittle,'location':job_location,'Comany_name':company_name,'Expirience':experience_required})


# In[69]:


Dataframe_for_Datascientist_post_in_Delhi


# In[ ]:





# # Solution of que-4

# In[99]:


driver = webdriver.Chrome()
driver.get("http://www.flipkart.com/")


# In[100]:


search=driver.find_element(By.CLASS_NAME,"_3704LK")
search.send_keys("Sunglasses")


# In[101]:


Find=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
Find.click()


# In[105]:


Brand=[]
description=[]
price=[]


# In[106]:


tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]') 
for i in tags:
 title=i.text
 Brand.append(title)
    
des=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in des:
 desc=i.text
 description.append(desc)
    
PRC=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in PRC:
 cost=i.text
 price.append(cost)


# In[108]:


Next=driver.find_element(By.CLASS_NAME,"_1LKTO3")
Next.click()


# In[109]:


Brands=[]
descriptions=[]
prices=[]


# In[110]:


tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]') 
for i in tags:
 title=i.text
 Brands.append(title)
    
des=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in des:
 desc=i.text
 descriptions.append(desc)
    
PRC=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in PRC:
 cost=i.text
 prices.append(cost)


# In[112]:


Next=driver.find_element(By.CLASS_NAME,"_1LKTO3")
Next.click()


# In[114]:


brands=[]
Descriptions=[]
Prices=[]


# In[115]:


tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]') 
for i in tags:
 title=i.text
 brands.append(title)
    
des=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in des:
 desc=i.text
 Descriptions.append(desc)
    
PRC=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in PRC:
 cost=i.text
 Prices.append(cost)


# In[132]:


Brand_name[0:100]=Brand+Brands+brands
Uploaded_price[0:100]=Prices+price+prices
Descrption_mentioned[0:100]=Descriptions+descriptions+description


# In[133]:


final_brand=Brand_name[0:100]
final_Uploaded_price=Uploaded_price[0:100]
final_Descrption_mentioned=Descrption_mentioned[0:100]


# In[135]:


print(len(final_brand),len(final_Uploaded_price),len(final_Descrption_mentioned))


# In[139]:


import pandas as pd


# In[141]:


Dataframe_for_sunglasses_of_flipkart=pd.DataFrame({"Brand_name":final_brand,"Assigned_price":final_Uploaded_price,"Description_for_glasses":final_Descrption_mentioned})


# In[142]:


Dataframe_for_sunglasses_of_flipkart


# In[ ]:





# # Solution for que-5

# In[172]:


driver=webdriver.Chrome()
driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')


# In[168]:


Rating=[]
Review_s=[]
f_review=[]


# In[169]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Rating.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Review_s.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_review.append(full)


# In[170]:


print(len(Rating),len(Review_s),len(f_review))


# In[188]:


Next=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]'))
Next.click()


# In[174]:


Ratin=[]
Revie_s=[]
f_revie=[]


# In[175]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Ratin.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Revie_s.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_revie.append(full)


# In[189]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[190]:


Rati=[]
Revi_s=[]
f_revi=[]


# In[191]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Rati.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Revi_s.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_revi.append(full)


# In[192]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[193]:


Rat=[]
Rev_s=[]
f_rev=[]


# In[194]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Rat.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Rev_s.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_rev.append(full)


# In[195]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[196]:


Ra=[]
Re_s=[]
f_re=[]


# In[197]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Ra.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Re_s.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_re.append(full)


# In[198]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[199]:


R=[]
R_s=[]
f_r=[]


# In[200]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 R.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 R_s.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_r.append(full)


# In[201]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[202]:


R7=[]
R_s7=[]
f_r7=[]


# In[203]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 R7.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 R_s7.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 f_r7.append(full)


# In[204]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[205]:


Rating8=[]
Rating_s8=[]
full_review8=[]


# In[207]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Rating8.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Rating_s8.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 full_review8.append(full)


# In[211]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[212]:


Rating9=[]
Rating_s9=[]
full_review9=[]


# In[213]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Rating9.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Rating_s9.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 full_review9.append(full)


# In[214]:


Next1=driver.find_element(By.XPATH,('/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]'))
Next1.click()


# In[215]:


Rating10=[]
Rating_s10=[]
full_review10=[]


# In[216]:


tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
for i in tags:
 title=i.text
 Rating9.append(title)
    
Rev=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rev:
 Re=i.text
 Rating_s9.append(Re)
    
Full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full:
 full=i.text
 full_review9.append(full)


# In[217]:


Ratings= Rating10+Rating9+Rating8+R7+R+Ra+Rat+Rati+Ratin+Rating
Review_summary=Rating_s10+Rating_s9+Rating_s8+R_s7+R_s+Re_s+Rev_s+Revi_s+Revie_s+Review_s
full_review=full_review10+full_review9+full_review8+f_r7+f_r+f_re+f_revi+f_revie+f_review


# In[218]:


print(len(Ratings),len(Review_summary),len(full_review))


# In[219]:


Mob_ratings=Ratings[0:100]
Mob_review_summary=Review_summary[0:100]


# In[220]:


Dataframe_for_rating_of_iphone_11=pd.DataFrame({"iphone_11_ratings":Mob_ratings,"Iphone_11_review_summary":Mob_review_summary,"full_reviews":full_review})


# In[221]:


Dataframe_for_rating_of_iphone_11


# In[ ]:





# # Solution of Question 6

# In[222]:


driver=webdriver.Chrome()
driver.get('https://www.flipkart.com/')


# In[228]:


search=driver.find_element(By.CLASS_NAME,"_3704LK")
search.send_keys('sneakers')


# In[229]:


Click=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
Click.click()


# In[232]:


Brand1=[]
Product_description1=[]
Price=[]


# In[237]:


Bd=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Bd:
 Br=i.text
 Brand1.append(Br) 
    
Pd=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Pd:
 Pr=i.text
 Product_description1.append(Pr)
    
Pe=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in Pe:
   Pr=i.text
   Price.append(Pr)


# In[245]:


Next=driver.find_element(By.CLASS_NAME,"_1LKTO3")
Next.click()


# In[242]:


Brand2=[]
Product_description2=[]
Price2=[]


# In[243]:


Bd=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Bd:
 Br=i.text
 Brand2.append(Br) 
    
Pd=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Pd:
 Pr=i.text
 Product_description2.append(Pr)
    
Pe=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in Pe:
   Pr=i.text
   Price2.append(Pr)


# In[246]:


Next=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]")
Next.click()


# In[247]:


Brand3=[]
Product_description3=[]
Price3=[]


# In[248]:


Bd=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Bd:
 Br=i.text
 Brand3.append(Br) 
    
Pd=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Pd:
 Pr=i.text
 Product_description3.append(Pr)
    
Pe=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in Pe:
   Pr=i.text
   Price3.append(Pr)


# In[249]:


BRAND=Brand1+Brand2+Brand3
PRODUCT_DESCRIPTION=Product_description1+Product_description2+Product_description3
PRICE=Price+Price2+Price3


# In[250]:


Brand=BRAND[0:100]
Product_description=PRODUCT_DESCRIPTION[0:100]
Prices=PRICE[0:100]


# In[252]:


print(len(Brand),len(Product_description),len(Prices))


# In[253]:


Dataframe_for_sneaker_on_fipkart=pd.DataFrame({"Brand_name":Brand,"Product_descr.":Product_description,"Price_of_shoe":Prices})


# In[254]:


Dataframe_for_sneaker_on_fipkart


# In[ ]:





# # Solution of question 7

# In[262]:


driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")


# In[268]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys('Laptop')


# In[269]:


click=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
click.click()


# In[271]:


i7=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/span[10]/li/span/a/div/label/i")
i7.click()


# In[278]:


tittle=[]
rating=[]
price=[]


# In[279]:


te=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in te:
 ti=i.text
 tittle.append(ti)


# In[301]:


rg=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star a-star-2-5"]')
for i in rg:
 ra=i.text
 rating.append(ra)


# In[282]:


pe=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in pe:
 pr=i.text
 price.append(pr)


# In[302]:


tittles=tittle[0:24]
ratings=rating[0:24]
prices=price[0:24]


# In[303]:


print(len(tittles),len(ratings), len(prices))


# In[304]:


Dataframe_for_laptops_from_Amazon=pd.DataFrame({"Tittle":tittles,'Ratings':ratings,"Price":prices})


# In[305]:


Dataframe_for_laptops_from_Amazon


# In[ ]:





# # Solution of question- 8

# In[346]:


driver=webdriver.Chrome()
driver.get('https://www.azquotes.com/')


# In[347]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
search.click()


# In[348]:


top_quotes1=[]
author1=[]
type_of_quote1=[]


# In[349]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes1.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author1.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote1.append(ty)


# In[350]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[351]:


top_quotes2=[]
author2=[]
type_of_quote2=[]


# In[352]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes2.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author2.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote2.append(ty)


# In[353]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[354]:


top_quotes3=[]
author3=[]
type_of_quote3=[]


# In[355]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes3.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author3.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote3.append(ty)


# In[356]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[357]:


top_quotes4=[]
author4=[]
type_of_quote4=[]


# In[358]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes4.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author4.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote4.append(ty)


# In[359]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[360]:


top_quotes5=[]
author5=[]
type_of_quote5=[]


# In[361]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes5.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author5.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote5.append(ty)


# In[362]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[363]:


top_quotes6=[]
author6=[]
type_of_quote6=[]


# In[364]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes6.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author6.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote6.append(ty)


# In[365]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[366]:


top_quotes7=[]
author7=[]
type_of_quote7=[]


# In[367]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes7.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author7.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote7.append(ty)


# In[368]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[369]:


top_quotes8=[]
author8=[]
type_of_quote8=[]


# In[370]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes8.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author8.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote8.append(ty)


# In[371]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[372]:


top_quotes9=[]
author9=[]
type_of_quote9=[]


# In[373]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes9.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author9.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote9.append(ty)


# In[374]:


Next=driver.find_element(By.CLASS_NAME,"next")
Next.click()


# In[375]:


top_quotes10=[]
author10=[]
type_of_quote10=[]


# In[376]:


tq=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in tq:
 to=i.text
 top_quotes10.append(to)
    
ar=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in ar:
 au=i.text
 author10.append(au)
    
te=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in te:
  ty=i.text
  type_of_quote10.append(ty)


# In[377]:


top_quotes=top_quotes1+top_quotes2+top_quotes3+top_quotes4+top_quotes5+top_quotes6+top_quotes7+top_quotes8+top_quotes9+top_quotes10
author=author1+author2+author3+author4+author5+author6+author7+author8+author9+author10
type_of_quote=type_of_quote1+type_of_quote2+type_of_quote3+type_of_quote4+type_of_quote5+type_of_quote6+type_of_quote7+type_of_quote8+type_of_quote9+type_of_quote10


# In[378]:


print(len(top_quotes),len(author),len(type_of_quote))


# In[379]:


Dataframe_for_quotes_page=pd.DataFrame({'Top_quotes':top_quotes,'Author':author,'Type_of_quotes':type_of_quote}) 


# In[380]:


Dataframe_for_quotes_page


# In[ ]:





# # Solution of question -9

# In[53]:


driver=webdriver.Chrome()
driver.get('https://www.jagranjosh.com/')


# In[54]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[3]/a')
search.click()


# In[55]:


search2=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a')
search2.click()


# In[56]:


Prime_minister=[]


# In[57]:


Name= driver.find_elements(By.XPATH,'//div[@class="table-box"]')
for i in Name:
 N=i.text
 Prime_minister.append(N)


# In[58]:


Prime_minister


# In[17]:


string="".join(Prime_minister)


# In[18]:


print(string)


# In[21]:


New=string.split("\n")


# In[22]:


New


# In[68]:


name=[]


# In[70]:


for a in range[0,113,5]:
 n=(New)
 name.append(n)


# In[ ]:





# # Solution of question 10

# In[77]:


driver=webdriver.Chrome()
driver.get('https://www.motor1.com/')


# In[79]:


search=driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input")
search.send_keys("50 MOST EXPENSIVE CARS")


# In[ ]:


click=driver.find_element(By.CLASS_NAME,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]/svg")
click.click()


# In[81]:


expensive_cars=driver.find_element(By.XPATH,"/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a")
expensive_cars.click()


# In[ ]:





# In[82]:


car=[]
costs=[]


# In[83]:


c=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in c:
 name=i.text
 car.append(name)


# In[88]:


P=driver.find_elements(By.XPATH,'//span[@class="arrow-holder"]')
for i in P:
  pr=i.text
  costs.append(pr)


# In[84]:


car


# In[89]:


costs


# In[90]:


cars=car[0:50]
prices=costs[0:50]


# In[91]:


print(len(cars),len(prices))


# In[92]:


Dataframe_most_expensive_cars=pd.DataFrame({'car_name':cars,'price':prices})


# In[93]:


Dataframe_most_expensive_cars


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




