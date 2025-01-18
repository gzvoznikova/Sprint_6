from selenium.webdriver.common.by import By
from data import Person

class Oder_page_locators:

    # "Для кого самокат"
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    Metro_one = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    TITLE_PAGE_PERSONAL_INFO= (
            By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    SELECT_DROPDOWN_METRO = (By.XPATH, ".//li[@class='select-search__row']")

    # Экран "Про аренду"
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SELECTED_DATE = (By.XPATH,
                     f"//div[@class='react-datepicker__day react-datepicker__day--00{Person.random_date} react-datepicker__day--selected']")
    RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    Dropdown_RENTAL_PERIOD = (By.XPATH, f'//div[text()="{Person.random_period}"]')
    CHECKBOX_COLOUR = (By.XPATH, f'//input[@id="{Person.random_color}"]')
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    CREATE_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    BUTTON_CONFIRM_ORDER_YES = [By.XPATH, '//button[text()="Да"]']
    title_of_page = (By.TAG_NAME, 'title')
    BUTTON_CHECK_STATUS_OF_ORDER = (By.XPATH, ".//*[text()='Посмотреть статус']")
    BUTTON_YES_CONFIRM_ORDER  = (By.XPATH, "//button[text()='Да']")
