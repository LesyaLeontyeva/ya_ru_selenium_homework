"""Функции для работы со страницей ya.ru."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import YaPageLocator
from webdriver_manager.chrome import ChromeDriverManager

YA_URL = 'https://ya.ru/'


class YaPage:
    """Класс для работы с главной страницей ya.ru."""

    driver = webdriver.Chrome(ChromeDriverManager().install())

    def open_page(self) -> None:
        """Фукнция для открытия страницы."""
        self.driver.get(YA_URL)

    def quit_driver(self) -> None:
        """Фукнция для закрытия браузера после окончания теста."""
        self.driver.quit()

    def get_page_source(self) -> driver:
        """Функция получения всей страницы целиком."""
        return self.driver.page_source

    def search(self, request: str) -> None:
        driver = self.driver
        element = driver.find_element(*YaPageLocator.INPUT_SEARCH_FIELD)
        element.send_keys(request)
        self.try_to_click(YaPageLocator.SEARCH_BUTTON, 5)

    def try_to_click(self, locator: tuple, time_for_wait: int = 5) -> None:
        """Функция для работы с ожиданием времени нахождения поисковой строки."""
        driver = self.driver
        try:
            element = WebDriverWait(driver, time_for_wait).until(
                EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise TimeoutException('Время ожидания нажатия истекло')
