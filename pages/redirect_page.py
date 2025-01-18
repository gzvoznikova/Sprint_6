from selenium.webdriver.support import expected_conditions
import allure
from pages.base_page import BasePage
from locators.locators_landing_page import Testlocators
from locators.locators_order_page import Oder_page_locators

class RedirectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по Лого Самокат в шапке Сервиса')
    def click_on_LOGO_SCOOTER(self):
        self.click_on_element(Testlocators.LOGO_SCOOTER)

    @allure.step('Клик по Лого Яндекс в шапке Сервиса')
    def click_on_LOGO_YANDEX(self):
        self.click_on_element(Testlocators.YA_LOGO)

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        self.wait.until(expected_conditions.presence_of_element_located(Oder_page_locators.title_of_page))
        return self.driver.title


