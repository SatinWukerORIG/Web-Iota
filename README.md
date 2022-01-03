# Web Iota
Iota is a web scraper which can find all of the images and links/suburls on a webpage. To reach this goal, I used some python libraries such as [Selenium](https://github.com/SeleniumHQ/selenium), [Request](https://github.com/request/request), and [Beautifulsoup](https://pypi.org/project/bs4/)

# Iota 1
- Support scraping images and links
- Using request lib and Beautifulsoup
- Unable to parse Javascript

# Iota 2


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
`python iota.py -img https://www.w3schools.com/html/html_classes.asp`
