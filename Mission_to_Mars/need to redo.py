from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # previous example
    # listings["headline"] = soup.find("a", class_="title").get_text()
    # listings["price"] = soup.find("h4", class_="price").get_text()
    # listings["reviews"] = soup.find("p", class_="pull-right").get_text()

    #  INSTRUCTIONS: * Complete the code in `scrape_costa.py` to scrape typical
    #               min and max temperatures from the
    #               [Costa Rica Vacation Page](https://visitcostarica.herokuapp.com/).
    #               The `scrape_info` function should return the typical min and max 
    #               temperatures as a Python Dictionary.

    # Get the average temps
    # @TODO: YOUR CODE HERE!
    avg_temps = soup.find('div', id='weather')

    # Get the min avg temp
    # @TODO: YOUR CODE HERE!
    min_temp = avg_temps.find_all('strong')[0].text

    # Get the max avg temp
    # @TODO: YOUR CODE HERE!
    max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
    # @TODO: YOUR CODE HERE!
    relative_image_path = soup.find_all('img')[2]['src']
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Quite the browser after scraping
    browser.quit()

    # Return results
    return costa_data
