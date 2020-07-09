"""
Тест.
"""
from pages.pages import YaPage


def test_page():
    """Начало теста."""
    ya_page = YaPage()
    try:
        ya_page.open_page()
        ya_page.search('Python')
        assert 'Python' in ya_page.get_page_source()
    finally:
        ya_page.quit_driver()


test_page()
