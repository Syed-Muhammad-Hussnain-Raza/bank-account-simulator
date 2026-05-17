import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_url():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'index.html'))
    return f"file:///{path.replace(os.sep, '/')}"


SCREENSHOTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'screenshots'))


def save(driver, name):
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, f"{name}.png"))


class TestBankSimulator(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Uncomment to run without browser window
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(get_url())
        time.sleep(1)
        save(self.driver, "01_app_home")
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        self.driver.quit()

    # Helpers
    def enter_amount(self, value):
        field = self.driver.find_element(By.ID, "amount")
        field.clear()
        field.send_keys(str(value))
        time.sleep(0.5)

    def click(self, btn_id):
        self.driver.find_element(By.ID, btn_id).click()
        time.sleep(1)

    def get_balance(self):
        return self.driver.find_element(By.ID, "balance").text

    def get_message(self):
        return self.driver.find_element(By.ID, "message").text

    # Test Cases

    # TC-01: Valid deposit
    def test_01_valid_deposit(self):
        self.enter_amount(500)
        self.click("deposit-btn")
        save(self.driver, "02_deposit_success")
        self.assertIn("500.00", self.get_balance())
        self.assertIn("deposited successfully", self.get_message())

    # TC-02: Valid withdrawal
    def test_02_valid_withdraw(self):
        self.enter_amount(500)
        self.click("deposit-btn")
        self.enter_amount(200)
        self.click("withdraw-btn")
        save(self.driver, "03_withdraw_success")
        self.assertIn("300.00", self.get_balance())
        self.assertIn("withdrawn successfully", self.get_message())

    # TC-03: Overdraft protection
    def test_03_overdraft_protection(self):
        self.enter_amount(100)
        self.click("deposit-btn")
        self.enter_amount(500)
        self.click("withdraw-btn")
        save(self.driver, "04_overdraft_error")
        self.assertIn("Insufficient funds", self.get_message())
        self.assertIn("100.00", self.get_balance())

    # TC-04: Empty deposit input
    def test_04_empty_deposit_input(self):
        self.click("deposit-btn")
        save(self.driver, "05_empty_deposit_error")
        self.assertIn("Please enter a valid amount", self.get_message())

    # TC-05: Empty withdraw input
    def test_05_empty_withdraw_input(self):
        self.click("withdraw-btn")
        save(self.driver, "06_empty_withdraw_error")
        self.assertIn("Please enter a valid amount", self.get_message())

    # TC-06: Negative deposit
    def test_06_negative_deposit(self):
        self.enter_amount(-100)
        self.click("deposit-btn")
        save(self.driver, "07_negative_deposit_error")
        self.assertIn("Amount must be positive", self.get_message())

    # TC-07: Transaction history updates
    def test_07_transaction_history(self):
        self.enter_amount(300)
        self.click("deposit-btn")
        self.enter_amount(100)
        self.click("withdraw-btn")
        save(self.driver, "08_transaction_history")
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#history-body tr")
        self.assertGreaterEqual(len(rows), 2)

    # TC-08: Reset account
    def test_08_reset_account(self):
        self.enter_amount(500)
        self.click("deposit-btn")
        self.click("reset-btn")
        save(self.driver, "09_reset_account")
        self.assertEqual(self.get_balance(), "$0.00")
        self.assertIn("reset", self.get_message())


if __name__ == "__main__":
    unittest.main()