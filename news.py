import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

for i in range(5):
    df = pd.DataFrame(columns=['筆數','類別','新聞標題','新聞連結'])
    count = 1

    #焦點新聞
    res = requests.get("https://news.google.com/news/?hl=zh-TW&ned=tw")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"焦點",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1

    #財經新聞
    res = requests.get("https://news.google.com/news/headlines/section/topic/BUSINESS.zh-TW_tw/%E8%B2%A1%E7%B6%93?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"財經",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1

    #國際新聞
    res = requests.get("https://news.google.com/news/headlines/section/topic/WORLD.zh-TW_tw/%E5%9C%8B%E9%9A%9B?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"國際",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1

    #台灣
    res = requests.get("https://news.google.com/news/headlines/section/topic/NATION.zh-TW_tw/%E5%8F%B0%E7%81%A3?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"台灣",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1

    #科技
    res = requests.get("https://news.google.com/news/headlines/section/topic/SCITECH.zh-TW_tw/%E7%A7%91%E6%8A%80?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"科技",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1

    #體育
    res = requests.get("https://news.google.com/news/headlines/section/topic/SPORTS.zh-TW_tw/%E9%AB%94%E8%82%B2?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"體育",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1

    #娛樂
    res = requests.get("https://news.google.com/news/headlines/section/topic/ENTERTAINMENT.zh-TW_tw/%E5%A8%9B%E6%A8%82?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"娛樂",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1    

    #健康
    res = requests.get("https://news.google.com/news/headlines/section/topic/HEALTH.zh-TW_tw/%E5%81%A5%E5%BA%B7?ned=tw&hl=zh-TW")
    soup = BeautifulSoup(res.text,"html.parser")

    for item in soup.select(".nuEeue"):
        news_title = (item.text)
        news_url = item.get('href')
        df2 = pd.DataFrame([[count,"健康",news_title, news_url]],columns=['筆數','類別','新聞標題','新聞連結'])
        df=df.append(df2, ignore_index=True)
        count += 1
    
    print(df)
    time.sleep(60)