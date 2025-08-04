import requests
from bs4 import BeautifulSoup
from main import extract_thumbnail, strip_tags

def test_real_feed_item_parsing():
    response = requests.get("https://medium.com/feed/@onurcangencbilkent")
    soup = BeautifulSoup(response.content, 'xml')
    first_item = soup.find_all("item")[0]
    description = first_item.description.text

    thumbnail = extract_thumbnail(description)
    assert thumbnail.startswith("https://"), "Thumbnail not extracted properly"

    text = strip_tags(description)
    assert len(text) > 20, "Stripped text is too short"
