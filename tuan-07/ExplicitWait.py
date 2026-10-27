from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # 1. Chờ nút Remove sẵn sàng & nhấn để xóa checkbox
    remove_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form#checkbox-example button")))
    remove_btn.click()

    # 2. Chờ thông báo trạng thái "It's gone!" xuất hiện
    msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("Thông báo:", msg.text)

    # 3. Chờ cho checkbox biến mất hoàn toàn khỏi giao diện (Invisibility)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div#checkbox input[type='checkbox']")))
    print("Checkbox đã biến mất khỏi DOM.")

    # 4. Nhấn lại nút (lúc này đã đổi thành Add) để đưa checkbox trở lại
    add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form#checkbox-example button")))
    add_btn.click()

    # 5. Chờ thông báo "It's back!" xuất hiện
    msg_back = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("Thông báo:", msg_back.text)

    # 6. Chờ checkbox hiển thị trở lại trên màn hình
    checkbox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#checkbox input[type='checkbox']")))
    print("Checkbox đã xuất hiện trở lại, trạng thái displayed:", checkbox.is_displayed())

finally:
    driver.quit()