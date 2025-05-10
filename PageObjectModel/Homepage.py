
from seleniumpagefactory import PageFactory

class Login(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators = {"username": ("NAME", "username"),
                "password": ("NAME", "password"),
                "login_button": ("TAG", "button")
                }
    def send_username(self, data):
        self.username.send_keys(data)
    def send_password(self, data):
        self.password.send_keys(data)
    def click_login_button(self):
        self.login_button.click()

class Admin(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators ={
                "Admin":("XPATH","(//a[@class='oxd-main-menu-item'])[1]"),
                "Add":("XPATH","//button[text()=' Add ']")
              }
    def click_Admin(self):
        self.Admin.click()
    def click_Add(self):
        self.Add.click()

class UserAdmin(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
              "select":("XPATH","//div[@class='oxd-select-text-input']"),
              "status":("XPATH", "(//div[@class='oxd-select-text-input'])[2]"),
              "pwd":("XPATH", "//input[@type='password']"),
              "E_name":("XPATH", "//input[@placeholder='Type for hints...']"),
              "username":("XPATH", "(//input[@class='oxd-input oxd-input--active'])[2]"),
              "conf_pwd":("XPATH", "(//input[@class='oxd-input oxd-input--active'])[3]"),
              "submit":("XAPTH", "//button[@type='submit']")
             }
    def click_select(self):
        self.select.click()
    def click_status(self):
        self.status.click()
    def send_pass(self, data):
        self.pwd.send_keys(data)
    def send_Emp(self, data):
        self.E_name.send_keys(data)
    def send_User(self, data):
        self.Username.send_keys(data)
    def send_confpwd(self, data):
        self.conf_pwd.send_keys(data)
    def click_sub(self):
        self.submit.click()
