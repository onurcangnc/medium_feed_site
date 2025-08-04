# tests/test_rss.py

from main import extract_thumbnail, strip_tags

def test_thumbnail_extraction():
    html = '<p><img src="https://example.com/image.jpg"/></p>'
    assert extract_thumbnail(html) == "https://example.com/image.jpg"

def test_strip_tags_removes_html():
    html = "<p>Hello <strong>world</strong></p>"
    assert strip_tags(html) == "Hello world"
