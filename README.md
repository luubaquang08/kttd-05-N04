# kttd-05-W4
- Môn học: Kiểm thử phần mềm – Thực hành kiểm thử tự động
- Nhóm: W4
- Thành viên:
  1. A46958 Lưu Bá Quang (Trưởng nhóm)
  2. A48566 Nguyễn Tường Vân
  3. A48138 Hồ Tùng Bách
  4. A48561 Vũ Thế Duyệt
  5. A48117 Phùng Minh Đức

## Hướng dẫn cài đặt và câu lệnh chạy kiểm thử

### 1. Chuẩn bị môi trường ảo
python3 -m venv .venv
source .venv/bin/activate

### 2. Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt

### 3. Câu lệnh chạy kiểm thử tuần 04
# Chạy bằng pytest
pytest -v tuan-04/test_smoke.py

# Hoặc chạy trực tiếp bằng python
python tuan-04/test_smoke.py

### 4. Kết quả mong đợi
- Trình duyệt Chrome tự động mở trang web kiểm thử, phóng to và tự đóng lại.
- Terminal hiển thị kết quả kiểm thử: 1 passed màu xanh lá.