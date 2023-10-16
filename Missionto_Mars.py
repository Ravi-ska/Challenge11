{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ea984d6",
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
   "id": "e1661a2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6c0c371",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5083e2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')\n",
    "\n",
    "slide_elem.find(\"div\", class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cf9fa0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ae36415",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_p = slide_elem.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22010f97",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.jpl.nasa.gov/spaceimages/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca0587b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_elem = browser.find_by_id('full_image')\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "747201bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.is_element_present_by_text('more info', wait_time=1)\n",
    "more_info_elem = browser.links.find_by_partial_text('more info')\n",
    "more_info_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "035a3b43",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd4131b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url_rel = img_soup.select_one('figure.lede a img').get(\"src\")\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4123894c",
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url = f'https://www.jpl.nasa.gov{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "545bd5c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "df.columns=['description', 'value']\n",
    "df.set_index('description', inplace=True)\n",
    "df\n",
    "df.to_html()\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87eabe7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "128b2655",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ed26b2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "022c1aca",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')\n",
    "slide_elem.find(\"div\", class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68bd2435",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ce5ba2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "news_p = slide_elem.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b659677",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9747835a",
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_elem = browser.find_by_id('full_image')\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e39c419",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.is_element_present_by_text('more info', wait_time=1)\n",
    "more_info_elem = browser.links.find_by_partial_text('more info')\n",
    "more_info_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd9d592d",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c87582dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url_rel = img_soup.select_one('figure.lede a img').get(\"src\")\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "254d819c",
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url = f'https://www.jpl.nasa.gov{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fed3e700",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "df.head()\n",
    "df.columns=['Description', 'Mars']\n",
    "df.set_index('Description', inplace=True)\n",
    "df\n",
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7731c15c",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/insight/weather/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1549dad5",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "weather_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a6e3b44",
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_table = weather_soup.find('table', class_='mb_table')\n",
    "print(weather_table.prettify())\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "521063ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e66e6d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a674789",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4e104c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "hemi_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae4efad9",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemi_links = hemi_soup.find_all('h3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "933a3ce7",
   "metadata": {},
   "outputs": [],
   "source": [
    "for hemi in hemi_links:\n",
    "    img_page = browser.find_by_text(hemi.text)\n",
    "    img_page.click()\n",
    "    html= browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "    \n",
    "    img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])\n",
    "    \n",
    "    title = img_soup.find('h2', class_='title').text\n",
    "    \n",
    "    hemi_dict = {'img_url': img_url,'title': title}\n",
    "    hemisphere_image_urls.append(hemi_dict)\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e31985c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14ee8207",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
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
