from pages.landing_page import LandingPage
from pages.redirect_page import RedirectPage
from conftest import driver
import allure

@allure.title('Проверка перехода на главную страницу Я.Самокат при клике на Лого сервиса в шапке')
def test_logo_redirect_main_success(driver):
    order_page = LandingPage(driver)
    order_page.open_url()
    order_page.click_on_order_button()
    logo_page = RedirectPage(driver)
    logo_page.click_on_LOGO_SCOOTER()
    assert logo_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'

@allure.title('Проверка перехода на страницу "Дзена" при клике на лого яндекса в хедере')
def test_logo_redirect_to_dzen_success(driver):
    order_page = LandingPage(driver)
    order_page.open_url()
    redirect_dzen_test = RedirectPage(driver)
    redirect_dzen_test.click_on_LOGO_YANDEX()
    redirect_dzen_test.switch_to_next_tab()
    assert redirect_dzen_test.get_page_title() == 'Дзен — платформа для просмотра и создания контента. Вы всегда найдёте здесь то, что подходит именно вам: сотни тысяч авторов ежедневно делятся постами, статьями, видео и короткими роликами'
