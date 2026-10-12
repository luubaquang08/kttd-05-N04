from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def test_smoke_the_internet():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        time.sleep(2)

        expected_title = "The Internet"
        actual_title = driver.title
        assert expected_title in actual_title, f"Loi: Tieu de thuc te la '{actual_title}'"
        print("\nSmoke test thanh cong: Trang web dung tieu de!")
    finally:
        driver.quit()