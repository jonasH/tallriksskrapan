import requests
from lxml import html

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
    
def main():
    parse_teknikparken()

if __name__ == '__main__':
    main()
