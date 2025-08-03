import feedparser

def test_feed_is_accessible():
    feed = feedparser.parse("https://onurcangencbilkent.medium.com/feed")
    assert len(feed.entries) > 0, "Feed boş geldi"

def test_entry_has_fields():
    feed = feedparser.parse("https://onurcangencbilkent.medium.com/feed")
    entry = feed.entries[0]
    assert hasattr(entry, "title")
    assert hasattr(entry, "summary")
    assert hasattr(entry, "link")
