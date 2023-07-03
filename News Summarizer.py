"""
    Copyright (C) 2023 ViridianTelamon (Viridian)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from bs4 import BeautifulSoup
from textblob import TextBlob
from newspaper import Article
import requests

print("News Summarizer")

print("\nBy:  ViridianTelamon.")

print("\n\n----------------------------------------------")

url = requests.get("https://www.ctvnews.ca/rss/ctvnews-ca-world-public-rss-1.822289")

website = BeautifulSoup(url.content, "xml")

items = website.findAll("item")

for item in items:
    article = Article(item.link.text)

    article.download()

    article.parse()

    article.nlp()

    article_rate = TextBlob(article.text)

    article_rate = article_rate.polarity

    print("\n\nArticle Title:  ")

    print(f"\n{article.title}")

    #print("\n\nArticle Authors:  ")

    #print(f"\n{article.authors}")

    print("\n\nArticle Publish Date:  ")

    print(f"\n{article.publish_date}")

    print("\n\nArticle Summary:  ")

    print(f"\n{article.summary}")

    print("\n\nArticle Content:  ")

    if article_rate > 0:
        print(f"\nPositive")
    elif article_rate < 0:
        print("\nNegative")
    else:
        print("\nNeutral")

    print("\n\nArticle Link:  ")

    print(f"\n{item.link.text}")

    print("\n\n----------------------------------------------")
