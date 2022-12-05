from pages.base import WebPage
from pages.elements import WebElement
from conftest import *


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'
            # url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=6a7e77c3-f8e9-4760-8d48-525307d4a888&theme&auth_type'
            # url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%2216BC213D-D09C-4D53-93AF-A889D0AB4A06%22%7D'

        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    password = WebElement(id='password')
    btn_login = WebElement(id='kc-login')
    auth_title = WebElement(xpath='//*[@id="page-right"]/div/div/h1')
    registration_link = WebElement(id='kc-register')
    phone_tab = WebElement(id='t-btn-tab-phone')
    email_tab = WebElement(id='t-btn-tab-mail')
    logo_lk = WebElement(xpath='//*[@id="page-left"]/div/div[2]/h2')
    auth_form = WebElement(xpath='//*[@id="page-left"]/div/div')
    lk_form = WebElement(xpath='//*[@id="page-right"]/div/div[2]')
    message_invalid_username_or_password = WebElement(xpath='//*[@id="page-right"]/div/div/p')
    the_element_forgot_the_password = WebElement(xpath='//*[@id="forgot_password"]')
    form_error_message = WebElement(id='form-error-message')
    reset_btn_in_recovery = WebElement(id='reset')