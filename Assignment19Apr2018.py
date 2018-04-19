
# coding: utf-8

# In[2]:


#program 2

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)


# In[3]:


#program 4

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)


# In[4]:


#program 5

s1=input("Enter first string:")
s2=input("Enter second string:")
s=s1+s2
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in s:
    if(i in a):
        continue
    else:
        print(i)


# In[6]:


#program 6
file=open("D:/test.txt",'r')
line=file.readline()
while(line!=""):
    print(line)
    line=file.readline()
file.close()


# In[10]:


#program 7

f=open('D:/test.txt', 'r')
num_words=0
for line in f:
    words = line.split()
    num_words += len(words)
print("Number of words:")
print(num_words)
f.close()


# In[11]:


#program 8
f=open('D:/test.txt', 'r')
num_lines=0
for line in f:
    
    num_lines += 1
print("Number of Lines:")
print(num_lines)
f.close()


# In[13]:


#program 10
word=input("Enter word to be searched:")
k = 0
 
f=open('D:/test.txt', 'r')
for line in f:
    words = line.split()
    for i in words:
        if(i==word):
            k=k+1
print("Occurrences of the word:")
print(k)


# In[16]:


#program 12

l=input("Enter letter to be searched:")
k = 0
 
f=open('D:/test.txt', 'r')
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
            if(letter==l):
                k=k+1
print("Occurrences of the letter:")
print(k)


# In[17]:


#program 15
k = 0
 
with open('D:/test.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isspace):
                    k=k+1
print("Occurrences of blank spaces:")
print(k)


# In[18]:


#program 16
f=open('D:/test.txt', 'r')
for line in f:
    l=line.title()
    print(l)


# In[19]:


#program 17
for line in reversed(list(open('D:/test.txt', 'r'))):
    print(line.rstrip())

