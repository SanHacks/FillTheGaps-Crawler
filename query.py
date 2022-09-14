from typing import BinaryIO

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
    print("Subject Found In The DB")
    print("Trying to Save To Fetch Via Gorrilla Pull")
    leading = found.replace(" ", "")

    # Give CRAWLER
    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30"
                             " ("
                             "KHTML, like Gecko) Version/4.0 Safari/534.30"}
    # 3. Send get() Request and fetch the webpage contents
    response = requests.get("https://www.saexampapers.co.za/grade-12-" + leading,
                            headers=headers)
    pages = response.content
    QuestionPapers = BeautifulSoup(pages, 'lxml')
    Subjecte = QuestionPapers.find_all('div', class_='elementor-button-wrapper')
    time.sleep(8)
    for Subjects in Subjecte:
        Line = Subjects.find('span', class_='elementor-button-text').text
        file = Subjects.find('a')
        
        file.get('href')
        # Get response object for link
        response = requests.get(file.get('href'))
        # Write content in pdf file
        pdf = open("papers/FillTheGaps.xyz " + Line + ".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        
        print("File ", Line, " downloaded")
        timestamps = time.time()
        subjectin = found
        names = Line
        ff = "files/papers/"
        loco = ff + "FillTheGap.xyz " + Line + ".pdf"
        curriculums = "NSC"
        grades = "12"
        provinces = "National"
        names = Line
        #province = Line
        papers = loco
        kinds = Line
        curriculums = Line
        terms = Line
        years = Line
       
        pipe = mysql.connector.connect(user='root', database='fillthegap')
        cursor = pipe.cursor()

        add_paper = ("INSERT INTO papers "
                        "(subject, name, grade, year, province, term, paper, curriculum, timestamp) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_paper = (subjectin, names, grades,  years, provinces, terms, papers,  curriculums, timestamps)
        cursor.execute(add_paper, data_paper)

        pipe.commit()
        
        cursor.close()
        pipe.close()
        print('PAPER Successfully added to database :) !')
        print(Line)
        print("Taking A Break(-_-) ")
        time.sleep(10)
        print("Gorrilla Pull Continues...")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
