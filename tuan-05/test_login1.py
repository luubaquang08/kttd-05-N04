import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium:
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Thiết lập trước mỗi Test Case (Tương đương @BeforeEach trong Java)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        yield  # Chạy test case
        
        # Dọn dẹp sau mỗi Test Case (Tương đương @AfterEach trong Java)
        if self.driver:
            self.driver.quit()

    # ==========================
    # TEST CASE 1
    # Đăng nhập thành công
    # ==========================
    def test_login_success(self):
        # Nhập username
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")

        # Nhập password
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # Click Login
        self.driver.find_element(By.ID, "login-button").click()

        # Kiểm tra đã chuyển sang trang sản phẩm
        current_url = self.driver.current_url
        assert "inventory" in current_url

        print("\nTEST 1 PASSED - Đăng nhập thành công")

    # ==========================
    # TEST CASE 2
    # Đăng nhập sai mật khẩu
    # ==========================
    def test_login_wrong_password(self):
        # Nhập username
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")

        # Nhập password sai
        self.driver.find_element(By.ID, "password").send_keys("123456")

        # Click Login
        self.driver.find_element(By.ID, "login-button").click()

        # Lấy thông báo lỗi
        error_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")

        # Kiểm tra thông báo lỗi có xuất hiện
        assert error_message.is_displayed()

        print(f"\nThông báo: {error_message.text}")
        print("TEST 2 PASSED - Hệ thống báo lỗi khi sai mật khẩu")

    # ==========================
    # TEST CASE 3
    # Thêm sản phẩm vào giỏ hàng
    # ==========================
    def test_add_product_to_cart(self):
        # Đăng nhập
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Thêm sản phẩm Sauce Labs Backpack
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Mở giỏ hàng
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Lấy tên sản phẩm trong giỏ
        product_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

        # Kiểm tra sản phẩm
        assert product_name == "Sauce Labs Backpack"

        print("\nTEST 3 PASSED - Thêm sản phẩm vào giỏ thành công")