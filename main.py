import os
import re
import math
import shutil
import feedparser
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Ayarlar
FEED_URL = "https://onurcangencbilkent.medium.com/feed"
OUTPUT_DIR = "output"
POSTS_PER_PAGE = 10
SITE_TITLE = "Onurcan Genç | Medium Articles"

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(['html', 'xml', 'j2']),
    extensions=["jinja2.ext.do"]
)

# Thumbnail çıkar
def extract_thumbnail(summary_html):
    match = re.search(r'<img[^>]+src="([^">]+)"', summary_html)
    return match.group(1) if match else None

# HTML tag temizle
def strip_tags(html):
    return re.sub(r'<[^>]+>', '', html)

# RSS verisini çek
def fetch_entries():
    feed = feedparser.parse(FEED_URL)
    for entry in feed.entries:
        entry.thumbnail = extract_thumbnail(entry.summary)
        entry.summary = strip_tags(entry.summary)
        entry.tags = [tag['term'].lower() for tag in entry.get("tags", []) if 'term' in tag]
    return feed.entries

# Sayfa oluştur
def generate_pages(entries):
    total_pages = math.ceil(len(entries) / POSTS_PER_PAGE)
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

        output_path = (
            os.path.join(OUTPUT_DIR, "index.html")
            if page_num == 1
            else os.path.join(page_dir, f"{page_num}.html")
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

# static klasörünü output içine kopyala
def copy_static_files():
    static_src = "static"
    static_dst = os.path.join(OUTPUT_DIR, "static")
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst, dirs_exist_ok=True)

if __name__ == "__main__":
    entries = fetch_entries()
    generate_pages(entries)
    copy_static_files()
