from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

def scrape_info():
    # Set up Requests
    url = 'https://redplanetscience.com/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    news_title = soup.title.text.strip()
    news_paragraph = soup.body.p.text.strip()

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit website and scrape page to soup
    url_image = 'https://spaceimages-mars.com'
    browser.visit(url_image)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')
    # Find the featured image
    featured_image_url = soup.find_all('img')[1]['src']
    featured_image_url = url_image + "/" + featured_image_url  

    #MARS FACTS:
    #Use Pandas to scrape the table
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)[0]
    tables = tables[:1]


    # Obtain high resolution images for each of Mar's hemispheres. 
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    #Find mars hemisphere URLs
    url_list = []
    for x in range(4,12,1):
     link = soup.find_all('a')[x]['href']
     url = 'https://marshemispheres.com/'
     link_url = url + link
     response = requests.get(link_url)
     soup = bs(response.text, 'lxml')
     #find all images
     imgs = soup.find_all('img', class_= "wide-image")
     for img in imgs:  
        url_list.append(url + img['src'])
    print(url_list)
    #Find mars hemisphere titles
    title_list = []
    for x in range(4,12,1):
      link = soup.find_all('a')[x]['href']
      url = 'https://marshemispheres.com/'
      link_url = url + link
      response = requests.get(link_url)
      soup = bs(response.text, 'lxml')
      titles = soup.find_all('h2', class_= "title")
      for title in titles:
        title_list.append(title.text.strip())
    #Dictionary mars hemispheres:
    hemisphere_image_urls = [
    {"title": title_list[0], "img_url": url_list[0]},
    {"title": title_list[1], "img_url": url_list[1]},
    {"title": title_list[2], "img_url": url_list[2]},
    {"title": title_list[3], "img_url": url_list[3]},
    ]

    # Quite the browser after scraping
    browser.quit()

  #Return one Python dictionary containing all of the scraped data.
    mars_data = {
    "news_title":news_title,
    "news_paragraph":news_paragraph,
    "featured_image_url":featured_image_url,
    "tables":tables,
    "hemisphere_image_urls":hemisphere_image_urls
    }
    # Return results
    return mars_data
    
