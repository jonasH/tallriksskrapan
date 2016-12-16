# -*- coding: utf-8 -*-
import requests
import urllib.request
from lxml import html

week_number = 0

def parse_vecka():
    answer = requests.get('http://www.vecka.nu')
    root = html.fromstring(answer.text)
    for child in root.xpath('//time'):
        global week_number
        week_number = child.text
    print('Det är nu vecka %s' % week_number)

def parse_kompassen():
    print("### KOMPASSEN ###")
    answer = requests.get('http://www.restaurangkompassen.se/index.php?option=com_content&view=article&id=64&Itemid=66')
    root = html.fromstring(answer.text)
    friday_found = False
    for child in root.xpath('//div[@class="screen"]/div/div/div'):
        if friday_found and child.text:
            print(child.text)
        elif child.text and "fredag" in child.text.lower():
            friday_found = True


def parse_teknikparken():
    print("### TEKNIKPARKEN ###")
    answer = requests.get('http://www.restaurangteknikparken.se/index.php?option=com_content&view=article&id=46')
    root = html.fromstring(answer.text)
    friday_found = False
    for child in root.xpath('//div[@class="screen"]/div/div/div'):
        if friday_found and child.text:
            print(child.text)
        elif child.text and "fredag" in child.text.lower():
            friday_found = True

def parse_gs():
    print("### Gourmetservice ###")
    answer = requests.get('http://www.geflegourmetservice.se/lunch.php')
    root = html.fromstring(answer.text)

    for child in root.xpath('//div[@class="left_holder"]/p')[1:3]:
        print(child.text_content())


def parse_hemlingby():
    print("### HEMLINGBY ###")
    answer = requests.get('http://www.gavle.se/Uppleva--gora/Idrott-motion-och-friluftsliv/Friluftsliv-och-motion/Hemlingby-friluftsomrade/Hemlingbystugan/Fika-och-ata/')
    root = html.fromstring(answer.text)
    for child in root.xpath('//a'):
        if child.text and "meny vecka" in child.text.lower() and week_number in child.text.lower():
            print(child.text)
            hemlingby_link='http://www.gavle.se' + child.get('href')
            print(hemlingby_link)
            break
    urllib.request.urlretrieve(hemlingby_link, "hemlingby.pdf")

def parse_gustafsbro():
    print("### Gustafsbro ###")
    answer = requests.get('http://www.gavlelunch.se/gustafsbro.asp')
    root = html.fromstring(answer.text)
    friday_found = False

    #Get friday from table
    for weekdayTable in root.xpath('//body/font/table/tr[1]/td[1]/div/table'):
        for day in weekdayTable.xpath('tr[1]/td[1]/font/strong'):
            if day.text and "fredag" in day.text.lower():
                friday_found = True
                break

    #If friday is found print food
    if friday_found:
           for food in weekdayTable.xpath('tr[2]/td[1]/font/ul/li'):
               print(food.text)
    else:
           print("Oops something went wrong")

def main():
    parse_vecka()
    parse_teknikparken()
    parse_kompassen()
    parse_hemlingby()
    parse_gs()
    parse_gustafsbro()
    
if __name__ == '__main__':
    main()
