# Danh sách Test Cases - Tuần 05 (Chức năng Đăng nhập)
Trang web kiểm thử: https://the-internet.herokuapp.com/login

---

### TC01: Đăng nhập thành công với thông tin hợp lệ
- **Mục tiêu:** Xác minh người dùng đăng nhập thành công khi nhập đúng tên đăng nhập và mật khẩu.
- **Tiền điều kiện:** Trình duyệt mở trang `/login`.
- **Các bước thực hiện:**
  1. Nhập vào ô Username: `tomsmith`
  2. Nhập vào ô Password: `SuperSecretPassword!`
  3. Nhấn nút "Login".
- **Kết quả mong đợi:**
  - Chuyển hướng tới trang `/secure`.
  - Hiển thị thông báo màu xanh chứa nội dung: "You logged into a secure area!".

---

### TC02: Đăng nhập thất bại do sai Tên đăng nhập
- **Mục tiêu:** Xác minh hệ thống báo lỗi khi nhập sai tài khoản.
- **Tiền điều kiện:** Trình duyệt mở trang `/login`.
- **Các bước thực hiện:**
  1. Nhập vào ô Username: `wrong_user`
  2. Nhập vào ô Password: `SuperSecretPassword!`
  3. Nhấn nút "Login".
- **Kết quả mong đợi:**
  - Vẫn ở lại trang `/login`.
  - Hiển thị thông báo lỗi màu đỏ chứa nội dung: "Your username is invalid!".

---

### TC03: Đăng nhập thất bại do sai Mật khẩu
- **Mục tiêu:** Xác minh hệ thống báo lỗi khi nhập sai mật khẩu.
- **Tiền điều kiện:** Trình duyệt mở trang `/login`.
- **Các bước thực hiện:**
  1. Nhập vào ô Username: `tomsmith`
  2. Nhập vào ô Password: `WrongPassword123`
  3. Nhấn nút "Login".
- **Kết quả mong đợi:**
  - Vẫn ở lại trang `/login`.
  - Hiển thị thông báo lỗi màu đỏ chứa nội dung: "Your password is invalid!".