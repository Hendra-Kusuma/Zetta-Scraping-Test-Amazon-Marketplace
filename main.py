import json
from bs4 import BeautifulSoup
import os
from playwright.sync_api import sync_playwright
import pandas as pd
site = 'https://www.amazon.com'
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

def Get_Total_Pages():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(
        f'https://www.amazon.com/s?k=computer+monitor&sprefix=compu%2Caps%2C451&ref=nb_sb_ss_pltr-ranker-1hour_2_5')
        html1 = page.inner_html('#search')
    params = {
        'k': 'computer monitor',
        'sprefix': 'compu,aps,451',
        'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5',
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24"}

    # Scraping Data
    soup = BeautifulSoup(html1, 'html.parser')
    total_pages = soup.find('span', 's-pagination-item s-pagination-disabled').text
    return total_pages

def Get_All_Item(pages):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'https://www.amazon.com/s?k=computer+monitor&page={pages}&crid=2UY22WBLSPS3V&qid=1667476685&sprefix=computer+monitor%2Caps%2C604&ref=sr_pg_{pages}')
        # page.goto(f'https://www.amazon.com/s?k=computer+monitor&page=8&crid=2UY22WBLSPS3V&qid=1667476685&sprefix=computer+monitor%2Caps%2C604&ref=sr_pg_8')
        html2 = page.inner_html('#search')
    params = {
        'k': 'computer monitor',
        'sprefix': 'compu,aps,451',
        'ref': 'nb_sb_ss_pltr-ranker-1hour_2_5',
        'pages': pages
    }
    soup = BeautifulSoup(html2, 'html.parser')
    results = soup.find_all('div', 's-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border')
    data_info = []
    for item in results:
        title = item.find('span', "a-size-medium a-color-base a-text-normal").text
        images = item.find('div', 'a-section aok-relative s-image-fixed-height')
        image = images.find('img')['src']
        links = item.find('a', 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']
        link = site + links

        try:
            price = item.find('span', {'class': 'a-offscreen'}).text
            stars = item.find('span', 'a-icon-alt').text

        # Sorting Data
            data_dict = {
                'title': title,
                'price': price,
                'star': stars,
                'image': image,
                'link': link
            }
            data_info.append(data_dict)

        except AttributeError:
            pass
        except NameError:
            pass
        except None:
            price = 'not have a price'

    # Write Json File
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open(f'json_result/computer-monitor_page_{pages}.json', 'w+') as json_data:
        json.dump(data_info, json_data)
    print(f'json page {pages} created')

    return data_info

def Creating_Document(dataFrame, query):
    try:
        os.mkdir('data_result')
    except:
        pass

    df = pd.DataFrame(dataFrame)
    df.to_csv(f'data_result/{query}.csv', index=False)
    df.to_excel(f'data_result/{query}.xlsx', index=False)
    print(f'File {query}.csv and {query}.xlsx succesfully created')

def Run():
    # bisa dibuat input untuk scraping data lain.
    # query = input('Input your Query : ')
    query = 'computer monitor'

    total = int(Get_Total_Pages())

    final_result = []
    counter = 0
    for pages in range(total):
        pages += 1
        counter += 1
        final_result += Get_All_Item(pages)

    # Formating Data
    try:
        os.mkdir('reports')
    except FileExistsError:
        pass

    with open(f'reports/{query}.json', 'w+') as final_data:
        json.dump(final_result, final_data)

    print('Data Json Has Been Created')
    # create docement
    Creating_Document(final_result, query)

if __name__ == '__main__':
    Run()
