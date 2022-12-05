import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegPage
from pages.base import WebPage
from conftest import *


# Корректное отображение "Стандартной страницы авторизации"
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"

#Автосмена вкладки
def test_autochange_tab_if_input_other_texttype(web_browser):
    page = AuthPage(web_browser)
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    print(phone_tab_class)
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    page.phone.send_keys("test@test.ru")
    page.password.send_keys("test")
    email_tab_class_after_input_email_in_username = page.email_tab.get_attribute("class")
    assert email_tab_class_after_input_email_in_username == "rt-tab rt-tab--small rt-tab--active"

# Редирект после кнопки "Войти"
def test_redirect_after_click_login( web_browser : WebPage):
    page = AuthPage(web_browser)
    page = AuthPage(web_browser)
    page.phone.send_keys("+79000000000")
    page.password.send_keys("test")
    page.btn_login.click()
    page.wait_page_loaded()
    assert page.form_error_message.get_text() == "Неверный логин или пароль" or "Неверно введен текст с картинки"

def test_password_input_in_password_recovery(web_browser:WebPage):
    page = AuthPage(web_browser)
    page = AuthPage(web_browser) 
    page.the_element_forgot_the_password.click()
    assert page.password.find()
    assert page.reset_btn_in_recovery.get_text() == ""



# Элементы в левом и правом блоке страницы
@pytest.mark.xfail(reason="Расположение элементов на странице не соответствует ожидаемым требованиям")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)

# Проверка названия таб выбора "Номер"
@pytest.mark.xfail(reason="Таб выбора 'Номер' не соответствует ожидаемым требованиям")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"



# Проверка название кнопки "Продолжить" в форме "Регистрация"
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
# перекрашивается в оранжевый цвет
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79996677390')
    page.password.send_keys("parol123")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')

# Регистрация пользователя с некорректным значением в поле "Имя"(< 2 символов), появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Ал')
    reg_page.last_name_field.send_keys("Петрова")
    reg_page.email_or_mobile_phone_field.send_keys("test5@mail.ru")
    reg_page.password_field.send_keys("Parol12345")
    reg_page.password_confirmation_field.send_keys("Parol12345")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей от 2 до 30 символов."


# Регистрация пользователя с некорректным значением в поле "Фамилия"(>30 символов), появление текста с
# подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Соня")
    reg_page.last_name_field.send_keys("ллрвялтвклпдлтвдлвдлоачьдлерльопрапаакорадонпро")
    reg_page.email_or_mobile_phone_field.send_keys("test1@mail.ru")
    reg_page.password_field.send_keys("Parol123987")
    reg_page.password_confirmation_field.send_keys("Parol123987")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей от 2 до 30 символов."



# Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Соня")
    reg_page.last_name_field.send_keys("Петрова")
    reg_page.email_or_mobile_phone_field.send_keys("+79996677390")
    reg_page.password_field.send_keys("Parol123789")
    reg_page.password_confirmation_field.send_keys("Parol123789")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible



# Некорректный пароль при регистрации пользователя(< 8 символов), появления текста с подсказкой об ошибке
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Соня")
    reg_page.last_name_field.send_keys("Липова")
    reg_page.email_or_mobile_phone_field.send_keys("test5@mail.ru")
    reg_page.password_field.send_keys("Parol1")
    reg_page.password_confirmation_field.send_keys("Parol1")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"
