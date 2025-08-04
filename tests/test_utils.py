from main import extract_thumbnail, strip_tags

def test_extract_thumbnail():
    html = '<p><img src="https://i.ibb.co/fxzGdMH/1.jpg"/></p>'
    assert extract_thumbnail(html) == "https://i.ibb.co/fxzGdMH/1.jpg"

def test_strip_tags():
    html = "<p>Hello <strong>world</strong></p>"
    assert strip_tags(html) == "Hello world"
