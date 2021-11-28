from selenium import webdriver 
from bs4 import BeautifulSoup 
import time 
import csv 
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/Owner/Desktop/PythonWH/Planet APLI/web scraping/chromedriver.exe")
browser.get(START_URL) 
time.sleep(10)

def scraper():
    headers = ["NAME","LIGHT YEARS FROM EARTH","PLANET MASS", "STELLAE MAGNITUDE","DISCOVERY DATE"]
    exoplanet = []
    for i in range(0,1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for x in soup.find_all("ul",attrs={"class", "exoplanet"}):
            fiveli = []
            for index,n in enumerate(x.find_all("li")):
                if index == 0:
                    f = n.find_all("a")
                    fiveli.append(f[0].contents[0])
                else:
                    fiveli.append(n.contents[0])
            exoplanet.append(fiveli)
        print(exoplanet)

    with open("scrapper_2.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(exoplanet)




scraper()


