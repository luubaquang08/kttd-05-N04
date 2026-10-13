# Ghi chú tuần 5 – Kiểm thử chức năng đăng nhập

## Thành viên: Bách

### Nội dung bài làm

File bài làm: `test_login_bach.py`, dùng Python, Selenium và pytest để kiểm thử trang https://the-internet.herokuapp.com/login.

- Đúng tài khoản `tomsmith` và mật khẩu `SuperSecretPassword!`: mong đợi vào trang `/secure` và có thông báo đăng nhập thành công.
- Sai tài khoản `wrong_user`: mong đợi ở trang `/login` và có thông báo `Your username is invalid!`.
- Sai mật khẩu `WrongPassword123`: mong đợi ở trang `/login` và có thông báo `Your password is invalid!`.

### Những điều rút ra từ bài

Một bài kiểm thử giao diện có ba bước chính: tìm phần tử, thao tác với phần tử và kiểm tra kết quả. Trong bài này, các thao tác nhập thông tin và bấm Login được đưa vào hàm `dang_nhap()` để ba test dùng chung, tránh viết lặp lại.

`@pytest.fixture` chuẩn bị trình duyệt trước mỗi test. Phần sau `yield` dùng để dọn dẹp; đặt `browser.quit()` trong `finally` giúp đóng trình duyệt kể cả khi test gặp lỗi. `WebDriverWait` chờ phần tử hiển thị tối đa 10 giây trước khi tiếp tục thao tác.

### Trả lời câu hỏi phần đọc (nhóm Web)

**Với ô tên đăng nhập ở trang `/login`, nên xác định bằng cách nào, vì sao?**

Trong bài dùng `By.ID` với giá trị `username` vì ô này có id riêng, cách viết ngắn và dễ hiểu. Với nút Login, bài dùng CSS selector `#login button` để tìm nút bên trong form có id `login`.

**Muốn nhập chữ vào một ô thì dùng lệnh gì?**

Dùng `send_keys()`, ví dụ `o_tai_khoan.send_keys(tai_khoan)`. Trước đó gọi `clear()` để xóa nội dung cũ trong ô.


### Ghi nhận sử dụng AI

Mình dùng ChatGPT (Codex) để hỗ trợ viết ba test đăng nhập đơn giản, có chú thích tiếng Việt và cách tổ chức khác file `test_login.py`; sau đó nhờ hỗ trợ soạn ghi chú phù hợp với bài và yêu cầu tuần 5. Nội dung hỗ trợ bám sát ba trường hợp đã có trong `testcases.md`. Qua phần giải thích kèm code, điểm cần nắm là cách dùng fixture, hàm chung `dang_nhap()`, chờ phần tử bằng `WebDriverWait` và kiểm tra kết quả bằng `assert`.

### Tình trạng kiểm tra

Chưa xác nhận ba test chạy thành công trong phiên hỗ trợ này vì lệnh Python của môi trường gặp lỗi truy cập. Cần chạy `python -m pytest test_login_bach.py -v` trên máy đã có Chrome, pytest và Selenium, rồi lưu ảnh kết quả vào thư mục `anh` khi cả ba test đều đạt.
