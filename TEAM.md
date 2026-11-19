# Team

## Thông tin nhóm

- Tên nhóm: Rua
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Rua-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): 

## Thành viên

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Vũ Nam Khánh | 2A202604112 | Kỹ sư cổng | x |
|   2 | Nguyễn Tuấn Anh | 2A202604089 | Vận hành và pháp lý |   |
|   3 | Phạm Duy Thành | 2A202604075 | Sản phẩm và kinh doanh |   |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

## VuNamKhanh-2A202604112

### Phần việc phụ trách

Kỹ sư cổng · Phiếu B mục B1–B2 và B7.1–B7.3; Phiếu C phần phân tích nguyên nhân và C7–C9. Phụ trách các cổng kỹ thuật trong lab10/guards.py, chỉ số lab10/monitors.py, đọc trace và kiểm tra ảnh hưởng của thay đổi lên bộ nền.

### Đóng góp cụ thể

Đối chiếu baseline và trace T-002@55, sau đó phân tích sự cố S3 theo các nhánh policy hết hiệu lực, tracking thiếu cause và lệnh ghi lỗi hãng không đủ căn cứ. Đề xuất cổng dùng policy hiệu lực theo as_of, chặn ghi lỗi khi thiếu nguyên nhân đã ghi nhận, và theo dõi carrier_fault_write_rate. Ghi rõ giới hạn còn lại: monitor chỉ đo tần suất, và 5 ca S3-43 vẫn tạo lỗi hãng oan nên chưa thể chọn Tiếp tục.

### Bằng chứng

R-base-before-20261119-161343-bde05c; R-S3-grade-20261119-203623-62f5d9; trace S3-43@11/22/33/44/55; Phiếu B B1–B2, B7.1–B7.3; Phiếu C C2, C6–C9; lab10/guards.py và lab10/monitors.py. Commit liên quan: e9554aa, 4736a5a.

### Exit ticket

Dự thảo để thành viên xác nhận: Em học được rằng guard phải kiểm soát hành động ghi dựa trên nguồn sự thật và tác hại có thể xảy ra, không chỉ đánh giá câu trả lời. Em còn chưa chắc cần nguồn chứng cứ độc lập nào để kết luận cause CARRIER đủ căn cứ khiếu nại trong pilot thật.


## NguyenTuanAnh-2A202604089

### Phần việc phụ trách

Vận hành và pháp lý · Phiếu B mục B7.5–B7.6; Phiếu C mục C10–C11. Chịu trách nhiệm rà PIC, người duyệt, công suất và SLA hàng chờ, kiểm mẫu, kênh cảnh báo, điều kiện dừng và bảo vệ dữ liệu bên thứ ba trong config/operating_gates.json.

### Đóng góp cụ thể

Tổng hợp cách vận hành khi có ticket ngoài phạm vi, dữ liệu thiếu hoặc hàng chờ tăng; rà các cổng operations và legal cùng bằng chứng trong report. Trong vòng S3, ghi nhận hàng chờ không ùn và PII bằng 0, nhưng còn lỗi hãng oan và chưa có phản hồi production từ hãng/shop để xác nhận lỗi. Cần nhóm xác nhận PIC trong config khớp tên người và vai trò trong TEAM trước khi chốt vận hành.

### Bằng chứng

config/operating_gates.json; Phiếu B B7.5–B7.6; Phiếu C C10–C11; R-S3-grade-20261119-203623-62f5d9 (1 reviewer, công suất 6 ca/giờ, SLA 60 phút, pii_leaks=0, wrongful_carrier_faults=5). Commit liên quan: 8be47dc, f5f6460.

### Exit ticket

Dự thảo để thành viên xác nhận: Em học được rằng ngưỡng an toàn cần gắn với người nhận cảnh báo, quy trình chuyển người và điều kiện dừng cụ thể. Em còn chưa chắc cách đo phản hồi của hãng/shop và thời gian xử lý khi có tranh chấp trong pilot thật.


## PhamDuyThanh-2A202604075

### Phần việc phụ trách

Sản phẩm và kinh doanh · Phiếu A mục A1–A5; Phiếu B mục B8; Phiếu C mục C12. Chịu trách nhiệm nối mục tiêu hệ thống và nhu cầu Oanh/Hạnh với tiêu chí chấp nhận, phạm vi pilot, chi phí/ROI và quyết định Gate 1.

### Đóng góp cụ thể

Định hình mục tiêu theo giá trị cho khách hàng, LogiX và các bên bị ảnh hưởng; tham gia chốt tiêu chí đã ký trước khi xem kết quả sự cố. Ở v1, nhóm chọn Thu hẹp theo bằng chứng baseline và phạm vi HN/DN. Sau sự cố S3, v2 chọn Cải tiến thêm vì còn 5 lỗi hãng oan, pass_rate/pass_k=0,8333, chi phí 8.048đ/ticket và ROI=0,24; không thay đổi tiêu chí đã ký.

### Bằng chứng

Commit ký tiêu chí c413f9c, hash abe188b4; Phiếu A A1–A5; Phiếu B B8; Phiếu C C12; R-base-prepared-20261119-170938-6eb725 và R-S3-grade-20261119-203623-62f5d9.

### Exit ticket

Dự thảo để thành viên xác nhận: Em học được rằng quyết định kinh doanh phải xem cả ngưỡng đã ký, tác động tới bên thứ ba và năng lực vận hành, không chỉ ROI tổng thể. Em còn chưa chắc cần bao nhiêu dữ liệu pilot thật theo từng kho/hãng để ước lượng ổn định chi phí và rủi ro.
