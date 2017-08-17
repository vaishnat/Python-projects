# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:26:48 2017

A light weight twitter analysis on a popular television show.
Biggboss tamil.
This script analyses on the most recent tweets, and 
displays a chart on
the most famous contestants 
who are frequently being discusses on twitter.

The lookup also considers patterns in the language on which the show is based on.
@author: Vaishnavi
"""

import tweepy    #this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
import pandas as pd
from matplotlib import pyplot as plt
 
#provide your access details below 
access_token = "XXXXX"
access_token_secret = "XXXXX"
consumer_key = "XXXXX"
consumer_secret = "XXXX"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
search_text = "#BiggBossTamil"
search_result = api.search(search_text, rpp=100)

candidates = []
candcounts = []
#Contestants on the show
LABELS = ['OVIYA','GAYATHRI','SHAKTHI','AARAV','RIZA','BINDU']
for i in search_result:
   try:
       breakfromouterloop = False
       text1 = i.text.lower()
       print (text1)
       for k in LABELS:
                 started = False
                 #open the file that contains other matching patterns for lookup
                 with open('C:\\Users\\...\\yourfile.txt',encoding='UTF-8') as input_data:
                    for line in input_data:
                        if line.rstrip() == k:
                            started = True
                            continue
                        if started and line.strip()=='END':
                            started = False
                            break
                        elif (started):
                            if ( line.strip() in text1):
                                candidates.append(k.upper())                               
   except BaseException as e:
            print("Error on_data: %s" % str(e))
print (candidates)
s=pd.Series(candidates).value_counts()
fre1 =s.sort_index()
print(s)
fig = plt.figure()
ax =fig.add_axes([0,0,1,1])
s1=pd.Series(candidates).unique()
s1.sort()
plt.bar(range(len(fre1)),fre1,align = 'center',color='Green')
plt.xticks(range(len(fre1)), s1, size='small')

                    