from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




BASE_URL = "https://the-internet.herokuapp.com"


def thao_tac_webelement(driver):
    driver.get(f"{BASE_URL}/login")
    username = driver.find_element(By.ID, "username")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    print("Tag:", username.tag_name)
    print("ID:", username.get_attribute("id"))
    print("Hiển thị:", username.is_displayed())
    print("Cho phép thao tác:", username.is_enabled())

    username.send_keys("tomsmith")
    print("Giá trị:", username.get_attribute("value"))
    username.clear()
    print("Sau khi xóa:", username.get_attribute("value"))
    print("Nút hiển thị:", button.is_displayed())
    print("Nút được bật:", button.is_enabled())


def thao_tac_shadow_dom(driver):
    driver.get(f"{BASE_URL}/shadowdom")
    host = driver.find_element(By.CSS_SELECTOR, "my-paragraph")
    shadow_root = host.shadow_root
    print("Đã truy cập Shadow DOM:", shadow_root)
    print("Nội dung bên trong:", shadow_root.find_element(By.CSS_SELECTOR, "slot").text)


def kiem_tra_accessibility(driver):
    driver.get(f"{BASE_URL}/login")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Accessible name:", button.accessible_name)
    print("ARIA role:", button.aria_role)


def main():
    driver = webdriver.Chrome()
    try:
        thao_tac_webelement(driver)
        thao_tac_shadow_dom(driver)
        kiem_tra_accessibility(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
