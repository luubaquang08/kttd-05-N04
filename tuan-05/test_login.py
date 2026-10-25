import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def driver():
    """Khởi tạo trình duyệt Chrome trước mỗi bài test và tự động đóng sau khi xong."""
    options = webdriver.ChromeOptions()
    # Tắt cảnh báo và tối ưu hóa khi chạy kiểm thử tự động
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(driver):
    """
    Test Case 1: Đăng nhập thành công với tài khoản và mật khẩu hợp lệ.
    Kết quả mong đợi: Chuyển hướng tới trang /secure và hiển thị thông báo thành công.
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    
    username_field.clear()
    username_field.send_keys("tomsmith")
    password_field.clear()
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    assert "/secure" in driver.current_url, "Lỗi: Không chuyển hướng đến trang /secure"
    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in flash_message, "Lỗi: Không tìm thấy thông báo đăng nhập thành công"
    print("\n[TC01 - PASS] Đăng nhập thành công!")

def test_login_invalid_username(driver):
    """
    Test Case 2: Đăng nhập thất bại do nhập sai tên đăng nhập.
    Kết quả mong đợi: Vẫn ở trang /login và hiển thị thông báo lỗi 'Your username is invalid!'.
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    
    username_field.clear()
    username_field.send_keys("wrong_user")
    password_field.clear()
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "Your username is invalid!" in flash_message, "Lỗi: Thông báo sai tên đăng nhập không chính xác"
    print("\n[TC02 - PASS] Phát hiện đúng lỗi sai tên đăng nhập!")

def test_login_invalid_password(driver):
    """
    Test Case 3: Đăng nhập thất bại do nhập sai mật khẩu.
    Kết quả mong đợi: Vẫn ở trang /login và hiển thị thông báo lỗi 'Your password is invalid!'.
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    
    username_field.clear()
    username_field.send_keys("tomsmith")
    password_field.clear()
    password_field.send_keys("WrongPassword123")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "Your password is invalid!" in flash_message, "Lỗi: Thông báo sai mật khẩu không chính xác"
    print("\n[TC03 - PASS] Phát hiện đúng lỗi sai mật khẩu!")

def test_login_empty_fields(driver):
    """
    Test Case 4: Đăng nhập thất bại do bỏ trống Username và Password.
    Kết quả mong đợi: Vẫn ở trang /login và hiển thị thông báo lỗi (hệ thống báo lỗi username không hợp lệ).
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    # Không nhập gì vào username và password, chỉ click nút Login
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()

    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "Your username is invalid!" in flash_message, "Lỗi: Không hiển thị thông báo lỗi khi bỏ trống thông tin"
    print("\n[TC04 - PASS] Phát hiện đúng lỗi bỏ trống thông tin đăng nhập!")

def test_login_exceed_max_length(driver):
    """
    Test Case 5: Đăng nhập với chuỗi ký tự cực dài (vượt quá giới hạn thông thường hoặc kiểm tra khả năng chịu tải của input).
    Kết quả mong đợi: Hệ thống xử lý được chuỗi dài hoặc giới hạn ký tự (không bị crash trang), 
    đồng thời hiển thị thông báo lỗi đăng nhập thất bại.
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    
    # Tạo chuỗi cực dài (ví dụ: 500 ký tự)
    long_string = "a" * 500

    username_field.clear()
    username_field.send_keys(long_string)
    password_field.clear()
    password_field.send_keys(long_string)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Kiểm tra hệ thống vẫn hoạt động ổn định và báo lỗi đăng nhập
    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "Your username is invalid!" in flash_message, "Lỗi: Hệ thống không xử lý đúng khi nhập chuỗi quá dài"
    print("\n[TC05 - PASS] Xử lý tốt trường hợp nhập quá nhiều ký tự!")