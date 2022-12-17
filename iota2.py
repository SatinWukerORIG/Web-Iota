import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from argparse import ArgumentParser

"""
Main Process:
Step 1. Parse command line arguments
Step 2. Find suburls or links of the web page
Step 3. Add raw links/urls to a list
Step 4. Remove duplicates of the list and output
"""
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

download_img = False

class LOG:
    def warn(msg):
        print("warning: " + msg)
    
    def error(msg):
        print("error: " + msg)
    
    def info(msg):
        print("info: " + msg)

    def decoration(output):
        print('\n', output, '\n', '--' * 20)

class HELPER:

    def if_url(url):
        return ('http' or 'www.') in url

    def remove_url_ends(url):
        try:
            if 'https' in url:
                return 'https://' + url.split('//')[1].split('/')[0]
            return 'http://' + url.split('//')[1].split('/')[0]
        except:
            print("please input the full url")

    def download_image(name, url):
        with open(name, 'wb') as f:
            f.write(requests.get(url).content)

    def get_html(parent_url):
        driver.get(parent_url)
        soup = BeautifulSoup(str(driver.page_source), 'html.parser')
        return soup


class Instructions(HELPER):
    def find_files(self, parent_url):
        LOG.decoration('Files:')
        url_list = []
        suffix = input('file suffix: ')
        for x in find_links(parent_url):
            if suffix in x:
                print(x)
                url_list.append(x)

        if len(url_list) == 0:
            print("Couldn't find anything...")

    # Find suburls or links of the web page
    def find_links(self, parent_url):
        url_list = []
        url_prefix = HELPER.remove_url_ends(parent_url)
        for link in HELPER.get_html(parent_url).find_all('a'):
            try:
                href = link.get('href')
                if if_url(href):
                    url_list.append(href)
                else:
                    url_list.append(url_prefix + href)
            except Exception as e:
                LOG.warn(e)

        return list(set(url_list))

    def find_img(self, parent_url):
        url_list = []
        url_prefix = HELPER.remove_url_ends(parent_url) # http||https
        html = HELPER.get_html(parent_url) # soup(html)

        for link in html.find_all('img'):
            url_list.append(link.get('src')
            if HELPER.if_url(link.get('src'))
            else url_prefix + link.get('src'))

        return list(set(url_list))

    def find_all_img(self, url):
        pass

    def find_all_links(self, url):
        print(find_links(url))


def main():
    # Parse command line arguments
    parser = ArgumentParser()
    parser.add_argument("url", nargs="?", default="", help='The URL of the target website/webpage')
    parser.add_argument('-img', help='Find all of the image on the webpage', action='store_true')
    parser.add_argument('-all_img', help='Find all of the image on the webpage and subwebpages', action='store_true')
    parser.add_argument('-link', help='Find the suburls/links on the webpage', action='store_true')
    parser.add_argument('-all_links', help='Find all of the suburls/links on the webpage', action='store_true')
    parser.add_argument('--download', help='Download images', action='store_true')
    args = parser.parse_args()

    global download_img
    download_img = args.download
    INSTRUC = Instructions()

    if args.img:
        url_list = INSTRUC.find_img(args.url)
        LOG.decoration('Images:')
        for i in range(len(url_list)):
            print(f'[{i + 1}]{url_list[i]}')
            if not download_img: continue
            try:
                HELPER.download_image(f'img[{i + 1}].png', url_list[i])
                LOG.info('download successfully...')
            except:
                LOG.error('invalid image...')


    if args.all_img:
        INSTRUC.find_all_img(args.url)

    if args.link:
        url_list = INSTRUC.find_links(args.url)
        LOG.decoration('Links:')
        for i in range(len(url_list)):
            print(f'[{i + 1}]{url_list[i]}')

    if args.all_links:
        INSTRUC.find_all_links(args.url)


if __name__ == '__main__':
    main()
