"""Константы."""
from selenium.webdriver.common.by import By


class YaPageLocator:
    """Класс для констант на ya.ru"""

    INPUT_SEARCH_FIELD = (By.ID, 'text')
    SEARCH_BUTTON = (By.XPATH, "//div[@class='search2__button']/button")

