import os
import math
import feedparser
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Ayarlar
FEED_URL = "https://onurcangencbilkent.medium.com/feed"
OUTPUT_DIR = "output"
POSTS_PER_PAGE = 6
SITE_TITLE = "Onurcan Genç | Medium Articles"

# RSS verisini çek
def fetch_entries():
    feed = feedparser.parse(FEED_URL)
    return feed.entries

# Sayfa oluştur
def generate_pages(entries):
    total_pages = math.ceil(len(entries) / POSTS_PER_PAGE)
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(['html', 'xml', 'j2'])
    )
    template = env.get_template("index.html.j2")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    page_dir = os.path.join(OUTPUT_DIR, "page")
    os.makedirs(page_dir, exist_ok=True)

    for page_num in range(1, total_pages + 1):
        start = (page_num - 1) * POSTS_PER_PAGE
        end = start + POSTS_PER_PAGE
        chunk = entries[start:end]

        html = template.render(
            posts=chunk,
            current_page=page_num,
            total_pages=total_pages,
            site_title=SITE_TITLE
        )

        if page_num == 1:
            output_path = os.path.join(OUTPUT_DIR, "index.html")
        else:
            output_path = os.path.join(page_dir, f"{page_num}.html")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    entries = fetch_entries()
    generate_pages(entries)
