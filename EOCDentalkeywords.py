# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:57:53 2018

@author: user
"""
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import wordnet

file=open("D:/test1.html","r")

page=file.read()




from bs4 import BeautifulSoup

def getTextWapo(page):
    soup=BeautifulSoup(page,'lxml')
    text= ' '.join(map(lambda p:p.text,soup.find_all('p')))
    return text.replace ("\n"," ")


def getstopwords(p):
    stemmedwords=[]
    words=[]
    sents=[]
    wordsnostopwords=[]
    finalwords=[]
    text = getTextWapo(p)

    sents=sent_tokenize(text)
    words=(word_tokenize(sent) for sent in sents)

    wordsnostopwords=[word.lower() for word in word_tokenize(text) if word.isalpha()]
    
    customstopwords=set(stopwords.words('english'))
    finalwords = [word for word in wordsnostopwords if word not in customstopwords]
    return finalwords

    """
    st=LancasterStemmer()
    stemmedwords=[st.stem(w) for w in finalwords]
    return (stemmedwords)
    """

dentalwords = getstopwords(page)


ques = input(" Please enter the Query ")

Queswords = getstopwords(ques)

synonyms=[]
for w in Queswords:
    
    for syn in wordnet.synsets(w):
        for l in syn.lemmas():
            synonyms.append(l.name())
       
        
Queswords.append(synonyms)


def GetSentence(Queswords):
    finalResponse=[]
    Diagnostic_Preventive_Services = open ("D:/Diagnostic and Preventive Services.txt","r")

    DPSwords = getstopwords(Diagnostic_Preventive_Services)

    DPScount =0
    for w in Queswords:
        if w in DPSwords:
            DPScount+=1       


    Basic_Restorative_Services = open ("D:/Basic Restorative Services.txt","r")

    BRSwords = getstopwords(Basic_Restorative_Services)

    BRScount = 0
    for w in Queswords:
        if w in BRSwords:
            BRScount+=1       



    Oral_Surgery_Services = open ("D:/Oral Surgery Services.txt","r")

    OSSwords = getstopwords(Oral_Surgery_Services)

    OSScount =0
    for w in Queswords:
        if w in OSSwords:
            OSScount+=1       


    Major_Restorative_Services = open ("D:/Major Restorative Services.txt","r")

    MRSwords = getstopwords(Major_Restorative_Services)

    MRScount =0
    for w in Queswords:
        if w in MRSwords:
            MRScount+=1       


    Orthodontic_Care = open ("D:/Orthodontic Care.txt","r")

    OCwords = getstopwords(Orthodontic_Care)

    OCcount =0
    for w in Queswords:
        if w in OCwords:
            OCcount+=1       

    Endodontic_Services = open ("D:/Endodontic Services.txt","r")

    ESwords = getstopwords(Endodontic_Services)

    EScount =0
    for w in Queswords:
        if w in ESwords:
            EScount+=1       

    Preparing_Mouth_Medical_Treatments = open ("D:/Preparing the Mouth for Medical Treatments.txt","r")

    PMMTwords = getstopwords(Preparing_Mouth_Medical_Treatments)

    PMMTcount =0
    for w in Queswords:
        if w in PMMTwords:
            PMMTcount+=1    

    Treatment_Accidental_Injury = open ("D:/Treatment of Accidental Injury.txt","r")

    TAIwords = getstopwords(Treatment_Accidental_Injury)

    TAIcount =0
    for w in Queswords:
        if w in TAIwords:
            TAIcount+=1  

    Cleft_Palate_Cleft_Lip_Conditions = open ("D:/Cleft Palate and Cleft Lip Conditions.txt","r")

    CPCLCwords = getstopwords(Cleft_Palate_Cleft_Lip_Conditions)

    CPCLCcount =0
    for w in Queswords:
        if w in CPCLCwords:
            CPCLCcount+=1  
        
    Dental_Anesthesia_Children = open ("D:/Dental Anesthesia for Children.txt","r")

    DACwords = getstopwords(Dental_Anesthesia_Children)

    DACcount =0
    for w in Queswords:
        if w in DACwords:
            DACcount+=1  


    m= max(DPScount ,BRScount , OSScount , MRScount ,OCcount , EScount , DACcount , CPCLCcount , TAIcount , PMMTcount)
    if(m!=0):
        if (m==DPScount):
            dps=open ("D:/Diagnostic and Preventive Services.txt","r")
            
            for sent in dps.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
          
        """
        print("Diagnostic and Preventive Services")
        """
        
        if (m==BRScount):
            brs=open ("D:/Basic Restorative Services.txt","r")
            
            for sent in brs.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
           
            """
            print("Basic Restorative Services")
            """
        if (m==OSScount):
            oss=open ("D:/Oral Surgery Services.txt","r")
            
            for sent in oss.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
           
            """
            print("Oral Surgery Services")
            """
        if (m==MRScount):
            mrs=open ("D:/Major Restorative Services.txt","r")
            
            for sent in mrs.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
            
            """
            print("Major Restorative Services")
            """
        if (m==OCcount):
            oc= open ("D:/Orthodontic Care.txt","r")
            
            for sent in oc.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
            
            """
            
            print("Orthodontic Care")
            """
        if (m==EScount):
            es=open ("D:/Endodontic Services.txt","r")
           
            for sent in es.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
           
            """
            print("Endodontic Services")
            """
        if (m==DACcount):
            dac=open ("D:/Diagnostic and Preventive Services.txt","r")
          
            for sent in dac.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
            
            """
            print("Dental Anesthesia for Children")
            """
        if (m==CPCLCcount):
            cpclp=open ("D:/Cleft Palate and Cleft Lip Conditions.txt","r")
            
            for sent in cpclp.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
           
            """
            print("Cleft Palate and Cleft Lip Conditions")
            """
        if (m==TAIcount):
            tai=open ("D:/Treatment of Accidental Injury.txt","r")
            
            for sent in tai.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
            
            """
            print("Treatment of Accidental Injury")
            """
        if (m==PMMTcount):
            
            pmmt= open ("D:/Preparing the Mouth for Medical Treatments.txt","r")
            
            for sent in pmmt.readlines():
                if ques.lower() in sent.lower():
                    finalResponse.append(sent)
                    
            
            """
            print("Preparing the Mouth for Medical Treatments")
            """
    else:
        return ("We didn't find any Information related to the query Please Contact Customer Care !")
    
    strres = ''.join(finalResponse)
    return(strres)
 
response = GetSentence(Queswords)
print(response)