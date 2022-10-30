from bs4 import BeautifulSoup, soup
import requests
import os
from playwright.sync_api import sync_playwright



params = {
    'k': 'computer monitor',
    'sprefix': 'compu,aps,451',
    'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.52'}

def Get_Total_Pages():

    params = {
        'k': 'computer monitor',
        'sprefix': 'compu,aps,451',
        'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24" }

    # Scraping Data
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5)
        page = browser.new_page()
        # page.goto('https://www.amazon.com/s?k=computer+monitor&sprefix=compu%2Caps%2C451&ref=nb_sb_ss_pltr-ranker'
        #           '-1hour_2_5')
        page.goto('https://www.amazon.com/s?k=nokia&crid=35KNQ4VMTGVTP&sprefix=nokia%2Caps%2C449&ref=nb_sb_noss_1')
        html = page.inner_html('#search')

        soup = BeautifulSoup(html, 'html.parser')
        total_pages = soup.find('span', 's-pagination-item s-pagination-disabled').text
        return total_pages

def Get_All_Item():

        check_titles = soup.find_all('div', 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16')
        titles = soup.find_all('span', 'a-size-medium a-color-base a-text-normal')
        for title in titles:
            title = print(title.text)



    # try:
    #     os.mkdir('temp')
    # except FileExistsError:
    #     pass
    #
    # with open('temp/res.html', 'w+') as outfile:
    #     outfile.write(res.text)
    #     outfile.close()

    # Scraping Step







if __name__ == '__main__':
    Get_Total_Pages()