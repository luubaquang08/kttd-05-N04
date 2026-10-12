Hướng Dẫn Cài Đặt & Chạy Test

1. Cài đặt môi trường
Đảm bảo máy đã cài sẵn Python và trình duyệt Google Chrome.

Mở Terminal / Command Prompt tại thư mục dự án và cài các thư viện cần thiết:
  pip install pytest selenium

2. Câu lệnh thực thi test
Chạy test và xem kết quả chi tiết kèm log print:
  pytest -v -s test_smoke.py

Chỉ chạy để xem tổng kết Pass/Fail nhanh:
  pytest test_smoke.py

Chạy toàn bộ các file test có trong thư mục:
  pytest -v
  
3. Đọc kết quả
PASSED (màu xanh lá): Test case chạy đúng yêu cầu, trang web phản hồi chuẩn.

FAILED (màu đỏ): Có lỗi xảy ra hoặc tiêu đề trang web không khớp với kỳ vọng. Terminal sẽ chỉ rõ dòng bị sai.