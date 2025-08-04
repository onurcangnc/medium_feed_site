from jinja2 import Environment, FileSystemLoader

def test_template_render():
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html.j2")
    html = template.render(posts=[], current_page=1, total_pages=1, site_title="Test")
    assert "<!DOCTYPE html>" in html
