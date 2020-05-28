"""
Run these tests after completing the setup steps to verify that the framework works.
"""

from pages.register import ToDoRegisterPage
import time




def test_register_user(browser):
    register_page = ToDoRegisterPage(browser)
    username = 'Ryan111'
    email = 'test@email111.com'
    password = '123'
    repeat_password = '123'

    # given register page loads
    register_page.load()

    # when the user complete register form

    register_page.username(username)
    register_page.email(email)
    register_page.password(password)
    register_page.repeat_password(repeat_password)
    time.sleep(1)
    register_page.register_button()
    time.sleep(1)
    message = register_page.congrats_message()


    # then te user is successfully registered

    assert message == 'Congratulations, you are now registered'
