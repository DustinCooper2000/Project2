from bs4 import BeautifulSoup
import requests
import pandas
import matplotlib
import lxml

def scraper():
    url = "https://en.wikisource.org/wiki/Portal:State_of_the_Union_Speeches_by_United_States_Presidents"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "lxml")
    print(soup)

def main():
    scraper()


main()

