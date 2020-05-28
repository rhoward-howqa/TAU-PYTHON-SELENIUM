from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

class ToDoRegisterPage:

    # url
    URL = 'https://flask-todo-test.herokuapp.com/register'

    # locators
    USERNAME_INPUT = (By.ID, 'username')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    REPEAT_PASSWORD_INPUT = (By.ID, 'password2')

    REGISTER_BUTTON = (By.ID, 'submit')

    CONGTATS_MESSAGE = (By.XPATH, '//body/div/div/div/div/form/div[1]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def username(self, username):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def email(self, email):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

    def password(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def repeat_password(self, repeat_password):
        repeat_password__input = self.browser.find_element(*self.REPEAT_PASSWORD_INPUT)
        repeat_password__input.send_keys(repeat_password)

    def register_button(self):
        register_button = self.browser.find_element(*self.REGISTER_BUTTON)
        register_button.click()

    def congrats_message(self):
        congrats_message = self.browser.find_element(*self.CONGTATS_MESSAGE)
        message = congrats_message.text

        print(message)

        return message




