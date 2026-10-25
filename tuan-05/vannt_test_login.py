import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_DANG_NHAP = "https://the-internet.herokuapp.com/login"


@pytest.fixture
def trinh_duyet():
    """Mở Chrome và trang đăng nhập trước mỗi bài kiểm thử."""
    browser = webdriver.Chrome()
    try:
        browser.get(URL_DANG_NHAP)
        yield browser
    finally:
        # Luôn đóng trình duyệt, kể cả khi bài kiểm thử bị lỗi.
        browser.quit()


def dang_nhap(browser, tai_khoan, mat_khau):
    """Nhập thông tin, bấm Login và trả về nội dung thông báo."""
    cho = WebDriverWait(browser, 10)

    # Tìm ô nhập bằng id; chờ ô tài khoản hiện ra trước khi nhập.
    o_tai_khoan = cho.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    o_mat_khau = browser.find_element(By.ID, "password")
    o_tai_khoan.clear()
    o_tai_khoan.send_keys(tai_khoan)
    o_mat_khau.clear()
    o_mat_khau.send_keys(mat_khau)

    # Tìm nút gửi trong form đăng nhập bằng CSS selector rồi bấm.
    browser.find_element(By.CSS_SELECTOR, "#login button").click()

    # Chờ thông báo xuất hiện để tránh kiểm tra khi trang chưa tải xong.
    return cho.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text


def test_dang_nhap_dung(trinh_duyet):
    """TC01: Đúng tài khoản và mật khẩu thì vào được trang bảo mật."""
    thong_bao = dang_nhap(trinh_duyet, "tomsmith", "SuperSecretPassword!")

    # assert đối chiếu kết quả thực tế với kết quả mong đợi.
    assert trinh_duyet.current_url == "https://the-internet.herokuapp.com/secure", (
        "Đăng nhập đúng nhưng chưa chuyển đến trang bảo mật"
    )
    assert "You logged into a secure area!" in thong_bao, (
        "Không hiển thị thông báo đăng nhập thành công"
    )


def test_sai_tai_khoan(trinh_duyet):
    """TC02: Sai tài khoản, đúng mật khẩu thì báo lỗi tài khoản."""
    thong_bao = dang_nhap(trinh_duyet, "wrong_user", "SuperSecretPassword!")

    # Đăng nhập thất bại phải ở lại trang đăng nhập và báo đúng lỗi.
    assert trinh_duyet.current_url == URL_DANG_NHAP, (
        "Sai tài khoản nhưng không ở lại trang đăng nhập"
    )
    assert "Your username is invalid!" in thong_bao, (
        "Thông báo lỗi tài khoản không đúng"
    )


def test_sai_mat_khau(trinh_duyet):
    """TC03: Đúng tài khoản, sai mật khẩu thì báo lỗi mật khẩu."""
    thong_bao = dang_nhap(trinh_duyet, "tomsmith", "WrongPassword123")

    # Kiểm tra cả địa chỉ trang và thông báo sau khi nhập sai mật khẩu.
    assert trinh_duyet.current_url == URL_DANG_NHAP, (
        "Sai mật khẩu nhưng không ở lại trang đăng nhập"
    )
    assert "Your password is invalid!" in thong_bao, (
        "Thông báo lỗi mật khẩu không đúng"
    )