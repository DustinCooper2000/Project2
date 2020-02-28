from bs4 import BeautifulSoup
import requests
import pandas
import matplotlib
import lxml

first_decade = ["https://en.wikisource.org/wiki/Richard_Nixon%27s_First_State_of_the_Union_Address", 
"https://en.wikisource.org/wiki/Richard_Nixon%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Richard_Nixon%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Richard_Nixon%27s_Fourth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Richard_Nixon%27s_Fifth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Gerald_Ford%27s_First_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Gerald_Ford%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Gerald_Ford%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Jimmy_Carter%27s_First_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Jimmy_Carter%27s_Second_State_of_the_Union_Address"]

second_decade = ["https://en.wikisource.org/wiki/Jimmy_Carter%27s_Third_State_of_the_Union_Address",
 "https://en.wikisource.org/wiki/Jimmy_Carter%27s_Fourth_State_of_the_Union_Address",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_First_State_of_the_Union_Speech",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_Second_State_of_the_Union_Speech",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_Third_State_of_the_Union_Speech",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_Fourth_State_of_the_Union_Speech",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_Fifth_State_of_the_Union_Speech",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_Sixth_State_of_the_Union_Address",
 "https://en.wikisource.org/wiki/Ronald_Reagan%27s_Seventh_State_of_the_Union_Speech",
 "https://en.wikisource.org/wiki/George_Herbert_Walker_Bush%27s_First_State_of_the_Union_Address"]

third_decade = ["https://en.wikisource.org/wiki/George_Herbert_Walker_Bush%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_Herbert_Walker_Bush%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_Herbert_Walker_Bush%27s_Fourth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_First_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_Fourth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_Fifth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_Sixth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Bill_Clinton%27s_Seventh_State_of_the_Union_Address"]


fourth_decade = ["https://en.wikisource.org/wiki/Bill_Clinton%27s_Eighth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_First_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Fourth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Fifth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Sixth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Seventh_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/George_W._Bush%27s_Eighth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_First_State_of_the_Union_Address"]

fifth_decade = ["https://en.wikisource.org/wiki/Barack_Obama%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_Fourth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_Fifth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_Sixth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_Seventh_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Barack_Obama%27s_Eighth_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Donald_Trump%27s_First_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Donald_Trump%27s_Second_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Donald_Trump%27s_Third_State_of_the_Union_Address",
"https://en.wikisource.org/wiki/Donald_Trump%27s_Fourth_State_of_the_Union_Address"]




def scraper():
    for i in first_decade:
        url = i
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, "lxml")
        address = soup.find("div", class_= "mw-parser-output")
        print(address)

def main():
    url = "https://en.wikisource.org/wiki/Richard_Nixon%27s_First_State_of_the_Union_Address"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "lxml")
    body = soup.find("div", class_="mw-parser-output")
    print(body.text)


main()

