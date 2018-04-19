
# coding: utf-8

# In[2]:


#program 2

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)


# In[28]:


#program 1

s=input("Enter string:")
count = 0
vowels = set("aeiouAEIOU")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)


# In[25]:


#program 3

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)-set(s2))
print("The letters are:")
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


# In[23]:


#program 9
file3=open('D:/test.txt',"a")
c=input("Enter string to append: \n");
file3.write("\n")
file3.write(c)
file3.close()
print("Contents of appended file:");
file4=open('D:/test.txt','r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()    
file4.close()


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


# In[22]:


#program 11
f=open('D:/test.txt', 'r')
f1=open('D:/test1.txt', 'w')
for line in f:
    f1.write(line)


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


# In[20]:


#program 13
f= open('D:/test.txt', 'r')
for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print(letter)


# In[21]:


#program 14

fin = open('D:/test.txt', "r")
data2 = fin.read()
fin.close()
fout = open('D:/test1.txt', "a")
fout.write(data2)
fout.close()


# In[27]:


#program 15
k = 0
 
f= open('D:/test.txt', 'r')
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

