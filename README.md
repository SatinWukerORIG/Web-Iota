# Web Iota
Iota is a web scraper that can find all of the images and links/suburls on a webpage. In order to implement these features, the code uses certain python libraries, [Selenium](https://github.com/SeleniumHQ/selenium), [Request](https://github.com/request/request), webdriver_manager, and [Beautifulsoup](https://pypi.org/project/bs4/)

*warning: this project is educational, the author is not responsible for any damage on public websites that is caused by the users*

# Iota 1
- Supports scraping images and links on the raw html of webpages
- Using request lib and Beautifulsoup
- Unable to parse Javascript

# Iota 2
- Requires WebDriver
- Using request, selenium ChromeDriver, webdriver_manager, and Beautifulsoup
- Able to parse JavaScript
- Able to scrape most of the anti-scraping websites

# Installation
`pip install -r requirements.txt`

# Usage
Try to type `python iota1.py -h`
```
usage: iota.py [-h] [-img] [-all_img] [-link] [url]

positional arguments:
  url         The URL of the target website/webpage

optional arguments:
  -h, --help  show this help message and exit
  -img        Find all of the image on the webpage
  -all_img    Find all of the image on the webpage and subwebpages
  -link       Find all of the suburls/links on the webpage
```
Example:
`python iota2.py -img https://www.w3schools.com/html/html_classes.asp`
