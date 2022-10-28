from bs4 import BeautifulSoup
import requests
import os



params = {
    'k': 'computer monitor',
    'sprefix': 'compu,aps,451',
    'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.52'}

def Get_Total_Pages():
    url = 'https://www.amazon.com/s?k=computer+monitor&sprefix=compu%2Caps%2C451&ref=nb_sb_ss_pltr-ranker-1hour_2_5'
    # url = 'https://web.facebook.com/'

    params = {
        'k': 'computer monitor',
        'sprefix': 'compu,aps,451',
        'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
    }

    res = requests.get(url, params=params, headers=headers)
    print(res.status_code)

    # try:
    #     os.mkdir('temp')
    # except FileExistsError:
    #     pass
    #
    # with open('temp/res.html', 'w+') as outfile:
    #     outfile.write(res.text)
    #     outfile.close()

    # Scraping Step


    # soup = BeautifulSoup(res.text, 'html.parser')
    # pages = soup.find(



if __name__ == '__main__':
    Get_Total_Pages()