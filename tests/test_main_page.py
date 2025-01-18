from pages.landing_page import LandingPage
from data import LandingAnswers
from conftest import driver
import allure
import pytest


@allure.title('Проверка раздела "Вопросы о важном"')
@allure.description('Проверка появления нужного текста при нажатии на каждую иконку развертывания в разделе')
@pytest.mark.parametrize("question_num, expected_answer", LandingAnswers.ANSWERS.items())
def test_landing_page(driver, question_num, expected_answer):
    landing_page = LandingPage(driver)
    landing_page.open_url()
    landing_page.scroll_to_questions()
    landing_page.click_on_question(question_num)
    answer_text = landing_page.get_answer_text(question_num)
    assert answer_text == expected_answer, f"Ответ для вопроса {question_num} не совпадает с ожидаемым"

