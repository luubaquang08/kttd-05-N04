from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # 1. Chờ ô username hiển thị & nhập giá trị
    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")

    # 2. Nhập password & chờ nút submit sẵn sàng (clickable)
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_btn.click()

    # 3. Chờ thông báo flash xuất hiện sau khi đăng nhập thành công
    msg = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    print("Thông báo:", msg.text)

finally:
    driver.quit()