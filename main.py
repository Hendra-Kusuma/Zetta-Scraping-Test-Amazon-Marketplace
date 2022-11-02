import json
from bs4 import BeautifulSoup
import os
from playwright.sync_api import sync_playwright
import pandas as pd

params = {
    'k': 'computer monitor',
    'sprefix': 'compu,aps,451',
    'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.52'}
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon'
              '.com%2Fs%3Fk%3Dnokia%26crid%3D35KNQ4VMTGVTP%26sprefix%3Dnokia%252Caps%252C449%26ref%3Dnav_signin'
              '&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle'
              '=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
              '%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
    page.fill('input#ap_email', 'ap.ms.em.yuni19ta@gmail.com')
    page.click('input#continue')
    page.fill('input#ap_password', 'abc12345@hk')
    page.click('input#signInSubmit')
    page.goto('https://www.amazon.com/s?k=computer+monitor&sprefix=compu%2Caps%2C451&ref=nb_sb_ss_pltr-ranker'
              '-1hour_2_5')
    # page.goto('https://www.amazon.com/s?k=nokia&crid=2RQWKTJW974O1&sprefix=nokia%2Caps%2C354&ref=nb_sb_noss_2')
    page.is_visible('#search')
    html = page.inner_html('#search')

def Get_Total_Pages():
    params = {
        'k': 'computer monitor',
        'sprefix': 'compu,aps,451',
        'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24"}

    # Scraping Data
    soup = BeautifulSoup(html, 'html.parser')
    total_pages = soup.find('span', 's-pagination-item s-pagination-disabled').text
    return total_pages


def Get_All_Item():
    global price, star
    params = {
        'k': 'computer monitor',
        'sprefix': 'compu,aps,451',
        'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5'
    }
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all('div',"s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")
    prices = soup.find_all('span', attrs={'data-a-color':'base'})
    data_result = []
    for pricess in prices :
        price = pricess.find('span', attrs={'class':'a-offscreen'}).text
    stars = soup.find_all('span', 'a-icon-alt')
    for starss in stars:
        star = starss.text
    for item in result:
        title = item.find('span', "a-size-medium a-color-base a-text-normal").text
        images = item.find('div', 'a-section aok-relative s-image-fixed-height')
        image = images.find('img')['src']

        # Sorting Data
        data_dict = {
            'title': title,
            'price': price,
            'star': star,
            'image': image,
        }
        data_result.append(data_dict)

    # Write Json File
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open(f'json_result/data_result.json', 'w+') as json_data:
        json.dump(data_result, json_data)
    print(f'json page created')





    # titles = soup.find_all('span', "a-size-medium a-color-base a-text-normal")
    # for titlesss in titles:
    #     title = titlesss.text
    #
    # prices = soup.find_all('span', 'a-price-whole')
    # for pricess in prices:
    #     price = pricess.text
    #     print(price)
    #
    # cents = soup.find_all('span', 'a-price-fraction')
    # for centss in cents:
    #     cent = centss.text
    #
    # stars = soup.find_all('span', 'a-icon-alt')
    # for starss in stars:
    #     star = starss.text
    #
    # imagess = soup.find_all('div', 'a-section aok-relative s-image-fixed-height')
    # for images in imagess:
    #     image = images.find('img')['src']










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
    Get_All_Item()
