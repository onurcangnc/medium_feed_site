import feedparser
import os
import json
from jinja2 import Environment, FileSystemLoader

FEED_URL = "https://onurcangencbilkent.medium.com/feed"
STATE_FILE = "last_feed_ids.json"
OUTPUT_FILE = "output/index.html"

def get_last_ids():
    if not os.path.exists(STATE_FILE):
        return []
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_last_ids(ids):
    with open(STATE_FILE, "w") as f:
        json.dump(ids, f)

def fetch_new_entries():
    feed = feedparser.parse(FEED_URL)
    last_ids = get_last_ids()
    new_entries = []
    new_ids = []

    for entry in feed.entries:
        entry_id = entry.id if hasattr(entry, "id") else entry.link
        new_ids.append(entry_id)
        if entry_id not in last_ids:
            new_entries.append(entry)

    save_last_ids(new_ids[:10])
    return new_entries if new_entries else feed.entries

def render_html(entries):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html.j2")
    output = template.render(entries=entries)
    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    entries = fetch_new_entries()
    render_html(entries)
