import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
import os,time

fake = Faker()

class Simple_Test(unittest.TestCase):

    def setUp(self):
        app = os.path.abspath('/Users/user/Downloads/data_sim/data.app')
        desired_capabilities = {
            'app': app,
            'platformName': 'iOS',
            'platformVersion': '11.3',
            'deviceName': 'iPhone 5s'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)

    def test_login(self):
        def login():
            self.driver.switch_to.alert.accept()
            for i in range(1,5):
                self.driver.swipe(314,218,0,221,200)
            time.sleep(5)
            self.driver.find_element_by_accessibility_id('getting_started_now').click()
            Accnt = self.driver.find_element_by_accessibility_id('enter_account_name')
            Accnt.send_keys("Drifting")
            self.driver.find_element_by_accessibility_id('data_logo').click()
            self.driver.find_element_by_accessibility_id('Continue').click()
            WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,'//XCUIElementTypeTextField[@name="email"]')))

            Email = self.driver.find_element_by_accessibility_id('email')
            Email.send_keys("user")
            self.driver.find_element_by_accessibility_id('logo').click()
            Pswd = self.driver.find_element_by_accessibility_id('password')
            Pswd.send_keys("pswd")
            self.driver.find_element_by_accessibility_id('logo').click()
            self.driver.find_element_by_accessibility_id('login_with_email').click()
            time.sleep(5)
            Leads()

        ## Lead Creation
        def Leads():
            self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="data"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[2]').click()
            self.driver.find_element_by_accessibility_id('ic add lead').click()
            Fname = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="data"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField')
            Fname.send_keys(fake.name())
            self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()
            Email = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="data"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
            Email.send_keys(fake.email())
            self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()
            self.driver.swipe(265, 409, 272, 95, 2000)
            Mob = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="data"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
            Mob.send_keys(fake.phone_number())
            self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()
            self.driver.find_element_by_accessibility_id('Submit').click()
            time.sleep(2)

            try:
                msg = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="data"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextView').text
                print(msg)
            except NoSuchElementException:
                msg = ""
            self.assertEqual(Fname.lower(), msg.lower(), "Common Buddy Check Your Code --> Lead Not Created")



        login()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Simple_Test)
    unittest.TextTestRunner(verbosity=2).run(suite)

