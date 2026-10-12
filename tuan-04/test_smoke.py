import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Hàm kiểm tra nhanh (smoke test) xem trang web có truy cập bình thường và đúng tiêu đề không
def test_smoke_the_internet():
    # 1. Khởi tạo và bật trình duyệt Google Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Điều hướng trình duyệt truy cập vào đường link web cần kiểm thử
        driver.get("https://the-internet.herokuapp.com/")

        # 3. Phóng to hết cỡ cửa sổ trình duyệt cho dễ nhìn
        driver.maximize_window()

        # 4. Tạm dừng 2 giây để chờ trang tải xong giao diện
        time.sleep(2)

        # 5. Khai báo tiêu đề kỳ vọng và lấy tiêu đề thực tế từ trang web
        expected_title = "The Internet"
        actual_title = driver.title

        # 6. So sánh: nếu tiêu đề chứa đúng chữ "The Internet" thì pass, ngược lại báo lỗi
        assert (
            expected_title in actual_title
        ), f"Loi: Tieu de thuc te la '{actual_title}'"

        # In thông báo ra màn hình nếu pass bước kiểm tra trên
        print("\nSmoke test thanh cong: Trang web dung tieu de!")

    finally:
        # 7. Luôn luôn đóng trình duyệt khi test xong để không bị tốn RAM máy tính
        driver.quit()