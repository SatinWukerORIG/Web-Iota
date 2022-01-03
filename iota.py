import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from argparse import ArgumentParser

"""
Main Process:
Step 1. Parse command line arguments
Step 2. Find suburls or links of the web page
Step 3. Add raw links/urls to a list
Step 4. Remove duplicates of the list and output
"""

driver = webdriver.PhantomJS()


def decoration(output):
    print('\n', output), print('--' * 20)


def remove_url_ends(url):
    return url.split('//')[1].split('/')[0]


def get_html(parent_url):
    # head = {
    #     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    # }
    driver.get(parent_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

# Find suburls or links of the web page
def find_links(parent_url):
    url_list = []
    url_prefix = remove_url_ends(parent_url)
    for link in get_html(parent_url).find_all('a'):
        try:
            url_list.append(link.get('href') if 'http' in link.get('href') else url_prefix + link.get('href'))
        except:
            continue

    decoration('Links:')
    url_list = list(set(url_list))
    for i in range(len(url_list)):
        print(f'[{i + 1}]{url_list[i]}')


def find_img(parent_url):
    url_list = []
    url_prefix = remove_url_ends(parent_url)
    for link in get_html(parent_url).find_all('img'):
        url_list.append(link.get('src') if 'http' in link.get('src') else url_prefix + link.get('src'))

    url_list = list(set(url_list))

    decoration('Images:')
    for i in range(len(url_list)):
        print(f'[{i + 1}]{url_list[i]}')

def find_all_img(url):
    pass

def find_files(parent_url):
    decoration('Files:')
    url_list = []
    suffix = input('file suffix: ')
    for x in find_links(parent_url):
        if suffix in x:
            print(x)
            url_list.append(x)

    if len(url_list) == 0:
        print("Couldn't find anything...")


def main():
    # Parse command line arguments
    parser = ArgumentParser()
    parser.add_argument("url", nargs="?", default="", help='The URL of the target website/webpage')
    parser.add_argument('-img', help='Find all of the image on the webpage', action='store_true')
    parser.add_argument('-all_img', help='Find all of the image on the webpage and subwebpages', action='store_true')
    parser.add_argument('-link', help='Find all of the suburls/links on the webpage', action='store_true')
    args = parser.parse_args()

    if args.img:
        find_img(args.url)

    if args.all_img:
        find_all_img(args.url)

    if args.link:
        find_links(args.url)


if __name__ == '__main__':
    main()