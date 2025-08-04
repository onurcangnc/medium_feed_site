# tests/test_template.py

import requests
from bs4 import BeautifulSoup
from main import extract_thumbnail, strip_tags
from jinja2 import Environment, FileSystemLoader, select_autoescape

def test_real_feed_rendering():
    response = requests.get("https://onurcangencbilkent.medium.com/feed")
    soup = BeautifulSoup(response.content, "xml")
    item = soup.find("item")
    assert item, "RSS item not found"

    summary = item.find("description").text
    title = item.find("title").text
    link = item.find("link").text

    post = {
        "title": title,
        "summary": strip_tags(summary),
        "thumbnail": extract_thumbnail(summary),
        "link": link
    }

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(['html', 'xml', 'j2'])
    )
    template = env.get_template("index.html.j2")
    html = template.render(posts=[post], current_page=1, total_pages=1, site_title="Test Site")

    assert "<html" in html and post["title"] in html, "Rendered HTML missing expected content"
