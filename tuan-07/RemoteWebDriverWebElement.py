from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com"

def thao_tac_enable_disable(driver):
    # Truy cập trang Dynamic Controls
    driver.get(f"{BASE_URL}/dynamic_controls")
    wait = WebDriverWait(driver, 10)

    # 1. Tìm ô input và nút Enable/Disable trong phần thứ 2
    input_field = driver.find_element(By.CSS_SELECTOR, "#input-example input")
    toggle_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")

    # 2. Kiểm tra trạng thái ban đầu (Ô input đang bị khóa / disabled)
    print("--- TRẠNG THÁI BAN ĐẦU ---")
    print("Nút hiện tại có tên:", toggle_button.text)
    print("Ô input có được phép thao tác (is_enabled):", input_field.is_enabled()) # Mong đợi: False[cite: 1]

    # 3. Nhấn nút "Enable" để mở khóa ô input
    toggle_button.click()

    # 4. Dùng Explicit Wait chờ thông báo "It's enabled!" xuất hiện
    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("\n--- SAU KHI BẤM ENABLE ---")
    print("Thông báo trạng thái:", message.text)

    # 5. Dùng Explicit Wait kết hợp điều kiện lambda để chờ ô input thực sự chuyển sang trạng thái enabled (True)
    wait.until(lambda d: input_field.is_enabled())
    print("Ô input đã được mở khóa (is_enabled):", input_field.is_enabled()) # Mong đợi: True[cite: 1]

    # 6. Thao tác nhập liệu với ô input đã được kích hoạt
    input_field.send_keys("Học tự động hóa Selenium")[cite: 1]
    print("Giá trị văn bản bên trong ô input:", input_field.get_attribute("value"))

    # 7. Nhấn lại nút (lúc này đổi thành "Disable") để khóa lại ô input
    toggle_button.click()

    # 8. Chờ thông báo "It's disabled!" và chờ ô input trở về trạng thái vô hiệu hóa (False)
    wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's disabled!"))
    wait.until(lambda d: not input_field.is_enabled())
    print("\n--- SAU KHI BẤM DISABLE ---")
    print("Ô input đã bị khóa trở lại (is_enabled):", input_field.is_enabled()) # Mong đợi: False[cite: 1]

def main():
    driver = webdriver.Chrome()
    try:
        thao_tac_enable_disable(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()