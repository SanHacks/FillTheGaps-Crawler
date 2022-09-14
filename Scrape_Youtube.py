import pipe as pipe
from bs4 import BeautifulSoup
import requests
import time
import mysql.connector
import os
pipe2 = mysql.connector.connect(host='localhost', user='root', database='fillthegap')
cursor2 = pipe2.cursor()
searchs = "SELECT subject FROM subjects ORDER BY RAND()"
pape = cursor2.execute(searchs)

for subject in cursor2:
# PREPARE ALL SUBJECTS TO REQUEST QUESTION PAPERS
    found = subject[0]
    print(found)
    def add_grade_12(s):
        return s + " Grade 12"
    
    #This is a function to scrape each video per subject, chapter, section
    
    

    leading = add_grade_12(found)

    # Give CRAWLER https://www.youtube.com/results?search_query=Mathematics+grade+12&sp=EgIYAw%253D%253D
    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30"
                             " ("
                             "KHTML, like Gecko) Version/4.0 Safari/534.30"}
    # 3. Send get() Request and fetch the webpage contents
    response = requests.get("https://www.youtube.com/results?search_query=" + leading + "&sp=EgIYAw%253D%253D",
                            headers=headers)
    pages = response.content
    Videos = BeautifulSoup(pages, 'lxml')
    sourc = Videos.find('a', class_='yt-simple-endpoint style-scope ytd-video-renderer').text
    description = Videos.find('div', class_='metadata-snippet-container-one-line style-scope ytd-video-renderer').text
    
    source = sourc.get('href')
    title = sourc.get('title').text
    name = videos.find_all('div', class_='title').text
    section = "12"
    timestamp = time()
    push = (
            "INSERT INTO youtube (subject, title, grade, section, source, description, timestamp)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    # noinspection PyUnboundLocalVari   able
    aas = (found, title, section,  source, section, description, timestamp)
    cursor2.execute(push, aas)
    cursor2.commit()
    print("YT Video Added For:")
    print(title)
    print(">>>>>>>>>>>>>>>>>>>>>>>>")
cursor2.close()