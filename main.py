from bs4 import BeautifulSoup
import requests

def main():
    url = 'https://www.uffs.edu.br/campi/chapeco/restaurante_universitario'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    vrau = []

    for table in soup.find_all('tbody'):
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                vrau.append(td.find('p').text)


    json = {}
    for day in range(5):
        temp = {}
        for i in range(day, len(vrau), 5):
            if i == day:
                json[vrau[i]] = {}
            else:
                if len(vrau[i]) >= 3:
                    print(1)
                    # temp[list(json.keys())[day]] = 33
                    # print()
                    # print(list(json.items()))
                    pass
        # json[list(json.keys())[day]] = temp


    print()
    print(json)


if __name__ == '__main__':
    main()

# token = "OTQwNDUyOTkyOTcxMzEzMTky.YgHnGg.YZGwp2Tuq9Ei654o5NKIfcdrbUY"
# app_id = "940452992971313192"
# invite_link = " https://discord.com/oauth2/authorize?&client_id=940452992971313192&scope=bot&permissions=8"