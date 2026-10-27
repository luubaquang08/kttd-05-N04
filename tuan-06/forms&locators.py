from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




BASE_URL = "https://the-internet.herokuapp.com"


def thao_tac_dropdown(driver):
    """Chọn và đọc các giá trị của dropdown."""
    driver.get(f"{BASE_URL}/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    dropdown.select_by_value("1")
    print("Option đã chọn:", dropdown.first_selected_option.text)
    print("Giá trị:", dropdown.first_selected_option.get_attribute("value"))
    print("Tất cả option:", [option.text for option in dropdown.options])

    dropdown.select_by_visible_text("Option 2")
    print("Sau khi đổi:", dropdown.first_selected_option.text)


def thao_tac_checkbox(driver):
    """Chọn các checkbox đang chưa được chọn."""
    driver.get(f"{BASE_URL}/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    for i, checkbox in enumerate(checkboxes, start=1):
        print(f"Checkbox {i} trước khi thao tác:", checkbox.is_selected())
        if not checkbox.is_selected():
            checkbox.click()
        print(f"Checkbox {i} sau khi thao tác:", checkbox.is_selected())


def dang_nhap(driver):
    """Điền và gửi biểu mẫu đăng nhập mẫu."""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    print("URL sau khi đăng nhập:", driver.current_url)
    print("Thông báo:", driver.find_element(By.ID, "flash").text)


def tim_kiem_theo_id(driver):
    driver.get(f"{BASE_URL}/dropdown")
    element = driver.find_element(By.ID, "dropdown")
    print("ID:", element.get_attribute("id"))
    print("Thẻ HTML:", element.tag_name)


def tim_kiem_theo_name(driver):
    driver.get(f"{BASE_URL}/login")
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    print("Tên đăng nhập:", username.get_attribute("value"))
    print("Loại trường mật khẩu:", password.get_attribute("type"))


def tim_kiem_bang_css(driver):
    driver.get(f"{BASE_URL}/checkboxes")
    first_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    print("Tên thẻ:", first_checkbox.tag_name)
    print("Loại phần tử:", first_checkbox.get_attribute("type"))
    print("Trạng thái:", first_checkbox.is_selected())

    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, "form#checkboxes input[type='checkbox']"
    )
    print("Số checkbox:", len(checkboxes))


def main():
    driver = webdriver.Chrome()
    try:
        thao_tac_dropdown(driver)
        thao_tac_checkbox(driver)
        dang_nhap(driver)
        tim_kiem_theo_id(driver)
        tim_kiem_theo_name(driver)
        tim_kiem_bang_css(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
