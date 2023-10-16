{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f499807",
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fc639e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b03ad5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\n",
    "        \"news_title\": news_title,\n",
    "        \"news_paragraph\": news_paragraph,\n",
    "        \"featured_image\": featured_image(browser),\n",
    "        \"facts\": mars_facts(),\n",
    "        \"last_modified\": dt.datetime.now(),\n",
    "        \"hemisphere_data\": hemisphere_scrape(browser)\n",
    "\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "527ea17e",
   "metadata": {},
   "outputs": [],
   "source": [
    "  browser.quit()\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d433adeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_news(browser):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3858848c",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url)\n",
    "    \n",
    "    browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)\n",
    "    \n",
    "    html = browser.html\n",
    "    news_soup = soup(html, 'html.parser')\n",
    "    \n",
    "    slide_elem = news_soup.select_one(\"ul.item_list li.slide\")\n",
    "    \n",
    "    news_title = slide_elem.find(\"div\", class_=\"content_title\").get_text()\n",
    "    \n",
    "    news_p = slide_elem.find(\"div\", class_=\"article_teaser_body\").get_text()\n",
    "    except AttributeError:\n",
    "        return None, None\n",
    "    return news_title, news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e411442",
   "metadata": {},
   "outputs": [],
   "source": [
    "def featured_image(browser):\n",
    "    \n",
    "    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "    browser.visit(url)\n",
    "\n",
    "    full_image_elem = browser.find_by_id('full_image')[0]\n",
    "    full_image_elem.click()\n",
    " \n",
    "    browser.is_element_present_by_text('more info', wait_time=1)\n",
    "    more_info_elem = browser.links.find_by_partial_text('more info')\n",
    "    more_info_elem.click()\n",
    "\n",
    "    html = browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "   \n",
    "        img_url_rel = img_soup.select_one('figure.lede a img').get(\"src\")\n",
    "    except AttributeError:\n",
    "        return None\n",
    "  \n",
    "    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'\n",
    "    return img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e2cb5e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_facts():\n",
    "  \n",
    "    try:\n",
    "        \n",
    "        df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "    except BaseException:\n",
    "        return None\n",
    "\n",
    "    df.columns=['Description', 'Mars']\n",
    "    df.set_index('Description', inplace=True)\n",
    "   \n",
    "    return df.to_html(classes=\"table table-striped\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e07295c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hemisphere_scrape(browser) :\n",
    "  \n",
    "    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "    browser.visit(url)\n",
    "    browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)\n",
    "    \n",
    "    hemisphere_image_urls = []\n",
    "\n",
    "    html = browser.html\n",
    "    hemi_soup = soup(html, 'html.parser')\n",
    "\n",
    "    \n",
    "    hemi_links = hemi_soup.find_all('h3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a35a98b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "    for hemi in hemi_links:\n",
    "      \n",
    "        img_page = browser.find_by_text(hemi.text)\n",
    "        img_page.click()\n",
    "        html= browser.html\n",
    "        img_soup = soup(html, 'html.parser')\n",
    "   \n",
    "        img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])\n",
    "    \n",
    "        title = img_soup.find('h2', class_='title').text\n",
    "\n",
    "        hemisphere = {'img_url': img_url,'title': title}\n",
    "        hemisphere_image_urls.append(hemisphere)\n",
    "        browser.back()\n",
    "      \n",
    "    return hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2049f3c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    print(scrape_all())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
