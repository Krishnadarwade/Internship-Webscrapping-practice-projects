#!/usr/bin/env python
# coding: utf-8

# # Solution of assinment 1 of Regular expression

# In[ ]:





# Solution of que-1

# In[3]:


import regex as re


# In[12]:


String= "abcdefgAHEDF12045"
pattern=re.compile("[A-Za-z0-9]+")
X=pattern.fullmatch(String)
print(X)


# In[ ]:





# Solution of que-2

# In[35]:


def regex_func(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'we found such string'
        else:
                return('Not found')
print(text_match("a"))
print(text_match("ab"))
print(text_match("abc"))
print(text_match("abb"))


# In[ ]:





# Solution-3

# In[38]:


def regec_func1(text):
    Y = '^ab+$'
    if re.search(Y, text):
         return ' found such string'
    else:  
         return ("i have not found")
print(text_match("a"))        
        


# In[ ]:





# Solution-4

# In[40]:


def reg_fuc2(unit):
    pattern2='^a(b?)$'
    if re.search(pattern2, unit):
        return 'found such string'
    else:
        return ('Not found')
print(text_match("a"))      


# Solution-5

# In[10]:


def text_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("abbb"))
print(text_match("aabbbbbc"))


# Solution-6

# In[42]:


string= 'IndiaIsTheBestCountry'
X= re.findall('[A-Z][^A-Z]*',string)
print(X)


# In[ ]:





# Solution of que-7

# In[5]:


String= "abbb"
pattern='ab{2,3}'
X=re.findall(pattern, String)
print(X)


# In[ ]:





# Solution of que-8

# In[7]:


Word='jhjh_kjh'
pattern='^[a-z]+_[a-z]+$'
X=re.findall(pattern,Word)
print(X)


# In[ ]:





# Solution of que-9

# In[11]:


Sample_alphabet="aknkjabbb"
pattern='a.*?b$'
x=re.findall(pattern, Sample_alphabet)
print(x)


# In[ ]:





# Solution of que-10     # here if there would be any sign then we would get a blank list as result 

# In[15]:


Test= "we love pyhton programming"
pattern='^\w+'
x=re.findall(pattern,Test)
print(x)


# In[ ]:





# Solution of question -11

# In[21]:


Practice='Virat_Is_Number_1_Cricketer'
pattern='^[a-zA-Z0-9_]*$'
x=re.findall(pattern,Practice)
print(x)


# In[ ]:





# Solution of que- 12

# In[13]:


def match_num(string):
    text = re.compile(r"^20")
    if text.match(string):
        return "matched"
    else:
        return 'not matched'
print(match_num('20-2345861'))
print(match_num('6-2345861'))


# In[ ]:





# Solution of que-13

# In[23]:


ip_address = "543.05.352.05"
X= re.sub('\.[0]*', '.', ip_address)
print(X)


# Solution of que 14

# In[28]:


String='August 15th 1947'
pattern=re.match("August" "(/d{2})th" "(/d{4})",String)
X=print(pattern)


# In[ ]:





# Solution of que-15   

# In[29]:


pattern = 'successful'
text = 'I want to become a successful Datascientist'
match = re.search(pattern, text)
print(match.group())


# In[ ]:





# Solution of que-16

# In[30]:


pattern = 'successful'
text = 'I want to become a successful Datascientist'
match = re.search(pattern, text)
print(match)


# In[ ]:





# Solution for que-17

# In[31]:


text = 'Java script, Ptython script, c++ script'
pattern = 'script'
Match= re.findall(pattern, text)
print(Match)


# In[ ]:





# Solution of que-18

# In[36]:


text = 'Java script, Ptython script, c++ script'
pattern = 'script'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[ ]:





# Solution of que-19

# In[43]:


def new_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt = "2026-01-02"
print (change_date_format(dt1))


# In[ ]:





# Solution of que-20

# In[46]:


String= 'it is a rainy day it is not easy to go somewhere now a days as there is no easy source of transport available'
X = re.findall("[ae]\w+", String)
print(X)


# In[ ]:





# Solution of que-21

# In[4]:


Scoreboard= 'Virat has scored 50 runs, Rohit has scored 30 runs and Shikhar has scored 32 runs' 
result = re.split("\D+", Scoreboard)
for scores in result:
    print(scores)


# Solution of que-22 

# In[49]:


string='jytd654ulyfl852yj20kuyg630j784'
number = re.findall('\d+', string)
number = map(int, number)
print("Max_value:",max(number))


# In[ ]:





# Solution of que-23

# In[53]:


def test(word):
    result = ""
    for i in word:
        if i.isupper():
            result=result+" "+i.upper()
        else:
            result=result+i
    return result[1:]
word = "PythonExercises"
print("Original Word:", word)
print("Insert space before capital letters in the said word:")
print(test(word))


# In[ ]:





# Solution of que -24

# In[57]:


Text='Pythonprogramming'
pattern= '[A-Z]+[a-z]+$'
x=re.search(pattern,Text)
print(x)


# In[ ]:





# Solution of que-25

# In[14]:


def unique_list(text_str):
    l = text_str.split()
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return ' '.join(temp)

text_str = "Python Exercises Practice Solution Exercises"
print(text_str)


# In[ ]:





# Solution of que-26

# In[65]:


regex = '[a-zA-z0-9]$'
def check(string):
    if(re.search(regex, string)):
        print("Accept")
         
    else:
        print("Discard")
if __name__ == '__main__' :
    
    string = "krishna@"

    check(string)

    string = 'krishna326'
    check(string)
 


# In[ ]:





# Solution of que-27

# In[68]:


Text= 'i want to become a #datascientist and my #dream job is to work at #TSC india limited as a #Senior Datascientist'
pattern=(r'(?<=#)\w+')
x=re.findall(pattern,Text)
print(x)


# In[ ]:





# Solution of que-28

# In[23]:


string="Hello Python<Ujj>"
pattern=re.sub("<U..>","",string)
X=print(pattern)


# In[ ]:





# Solution of que-29

# In[70]:


text='Virat kohli completed his last santuary on 21-05-2023 and most probably he will complete his 100th sanctuary before 31-12-2024'
pattern="\d{2}[/-]\d{2}[/-]\d{4}"
dates = re.findall(pattern, text)
print(dates)


# In[ ]:





# Solution of que-30

# In[9]:


String='India, Pakistan,Srilanka, Afghanistan,Bangladesh.'
Pattern=re.sub("[ ,.]", ":", String)
x= print(Pattern)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




