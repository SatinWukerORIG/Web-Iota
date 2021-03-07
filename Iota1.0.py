import requests
from bs4 import BeautifulSoup
import sys

"""
Main Process:
Step 1. Parse command line arguments
Step 2. Find suburls or links of the web page
Step 3. Add raw links/urls to a list
Step 4. Remove duplicates of the list and output
"""


def decoration(output):
    print('\n', output), print('--' * 20)

def help_menu():
    print("""
    Iota 1.0
    -img: find image
    -files: kinds of file you want
    -link: find links insert in the web page
    -help: help""")

# Step 4
def remove_url_ends(url):
    final_url = url.split('//')[1].split('/')[0]
    return final_url

#Step 4
def remove_duplicates(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)

    for i in range(len(new_arr)):
        print(f'[{i + 1}]', new_arr[i], sep='')


def get_url(parent_url):
    head = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    re = requests.get(parent_url, headers=head)
    soup = BeautifulSoup(re.text, 'html.parser')
    return soup

# Step 2
def find_suburls(parent_url):
    url_list = []
    for link in get_url(parent_url).find_all('a'):
        try:
            if 'http' in link.get('href'):
                url_list.append(link.get('href'))
            else:
                # Step 3
                url_list.append(remove_url_ends(parent_url) + link.get('href'))
        except:
            continue

    return url_list


def find_img(parent_url):
    decoration('Images:')
    url_list = []
    for link in get_url(parent_url).find_all('img'):
        url_list.append(link.get('src'))
    return remove_duplicates(url_list)


def find_files(parent_url):
    decoration('Files:')
    url_list = []
    suffix = input('file suffix: ')
    for x in find_suburls(parent_url):
        if suffix in x:
            print(x)
            url_list.append(x)

    if len(url_list) == 0:
        print("Couldn't find anything...")


def input_url():
    # Step 1
    main_url = sys.argv[len(sys.argv) - 1]
    for i in range(1, len(sys.argv) - 1):
        if sys.argv[i] == '-img':
            find_img(main_url)

        elif sys.argv[i] == '-link':
            decoration('Links:')
            remove_duplicates(find_suburls(main_url))

        elif sys.argv[i] == '-files':
            find_files(main_url)

        elif sys.argv[i] == '-help':
            help_menu()

        else:
            print('\n   Syntax is wrong...')
            help_menu()


try:
    input_url()

except:
    print('Interupted...')