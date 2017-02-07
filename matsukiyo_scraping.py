#!/usr/bin/env/python
#coding: utf-8

from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from time import time
import requests, random, datetime, re, os, json

index_url = "http://www.matsukiyo.co.jp/store/corp/c/004?page="
articleurl = "http://www.matsukiyo.co.jp/store/online"
downloadDirectory = "Downloaded/daily"

def pageget(index_page_list):
    # ページ数をゲットする(334ページある)
    index_page_list = []
    for i in range(0,335):
        index_page_list.append(index_url + str(i))
        print(index_page_list)

def urlget(title_list,summary_url_list,img_list,index_page_list):
    title_list = []
    summary_url_list = []
    img_list = []
    for index_page in index_page_list:
        print(index_page)
        
        for j in range(0,30):
            # urlをsoupに
            result = requests.get(index_page)
        # print(index_page)
            c = result.content
            soup = BeautifulSoup(c,"html.parser")
        #　タイトルをゲット
            summary = soup.find_all('p',{'class':'itemContainer__img'})
        # print(summary[0])
            title_list.append(summary[j].find_all("a")[0].get("title"))
            print(summary[j].find_all("a")[0].get("title"))
            # URLをゲット
            # print(summary_s)
            summary = soup.find_all('h4',{'class':'itemContainer__title'})
        # print(summary_e
            summary_url_list = summary[j].find_all("a")[0].get("href")
            # print(summary_url_list)
        #print(articleurl + summary_url_list[-16:])
            
            summary = soup.find_all('p',{'class':'itemContainer__img'})
            img_list.append(summary[j].find_all("img")[0])
            img_url = "http://www.matsukiyo.co.jp" + summary[j].find_all("img")[0].get("src")
        #print("http://www.matsukiyo.co.jp/" + summary[j].find_all("img")[0].get("src"))
            
        def getDownloadPath(img_url, downloadDirectory):
            path = img_url.replace("www.", "")
            path = path.replace("http://", "")
            path = path.replace("https://", "")
            path = downloadDirectory+"/"+path
            directory = os.path.dirname(path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            return path

        urlretrieve(img_url, getDownloadPath(img_url, downloadDirectory))
