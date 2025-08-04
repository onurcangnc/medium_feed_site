import feedparser

def test_feed_is_accessible():
    feed = feedparser.parse("https://onurcangencbilkent.medium.com/feed")
    assert len(feed.entries) > 0, "Feed is empty or could not be accessed"

def test_entry_has_fields():
    feed = feedparser.parse("https://onurcangencbilkent.medium.com/feed")
    entry = feed.entries[0]
    assert hasattr(entry, "title"), "entry.title is missing"
    assert hasattr(entry, "summary"), "entry.summary is missing"
    assert hasattr(entry, "link"), "entry.link is missing"
