# Team

## Thông tin nhóm

- Tên nhóm: Rua
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Rua-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3

## Thành viên

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Vũ Nam Khánh | 2A202604112 | Kỹ sư cổng | x |
|   2 | Nguyễn Tuấn Anh | 2A202604089 | Vận hành và pháp lý |   |
|   3 | Phạm Duy Thành | 2A202604075 | Sản phẩm và kinh doanh |   |

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

Sản phẩm và kinh doanh: tiêu chí chấp nhận tại Phiếu A, phạm vi pilot, chi phí/ROI và quyết định Gate 1 tại Phiếu B B8, Phiếu C C12.

### Đóng góp cụ thể

Rà soát mục tiêu hệ thống, các ngưỡng đã ký và hiệu quả kinh doanh của phương án pilot. Đối chiếu kết quả S3 còn 5 lỗi hãng oan, pass_rate/pass_k = 0,8333, chi phí 8.048đ/ticket và ROI = 0,24 để xác nhận quyết định v2 **Cải tiến thêm**, chưa mở pilot ở phần chưa đạt; xem lại ngày **26/11/2026** theo tiêu chí đã ký. Không thay đổi ngưỡng đã ký để hợp thức hóa kết quả.

Trong quá trình hoàn thiện, yêu cầu trợ lý rà soát dự án và giải thích các điểm chưa đạt. Sau rà soát, yêu cầu hoàn nguyên thay đổi code/config/hồ sơ bổ sung về bản main trước 20:54, chỉ giữ cập nhật phần cá nhân này trong TEAM.md.

### Bằng chứng

- Tiêu chí đã ký: commit `19dc58a`, hash `abe188b4`; Phiếu A A1–A5.
- Phiếu B B8, Phiếu C C12 và submission/submission.json ghi quyết định v1/v2.
- Báo cáo nhóm đã có trước khi hoàn nguyên: `R-S3-grade-20261119-203623-62f5d9`, tại submission/runs/grade-report.json.

### Exit ticket

Điều rút ra: quyết định kinh doanh cần xem đồng thời ngưỡng đã ký, tác động tới hãng/khách hàng và chi phí vận hành. Bộ nền đạt không có nghĩa pilot đã sẵn sàng; khi S3 còn lỗi hãng oan và ROI chưa đạt, cần chọn Cải tiến thêm.

Điều còn chưa chắc: cách đồng bộ lịch sử lỗi hãng của ca tự động và ca xử lý tay, và cần bao nhiêu dữ liệu pilot theo kho/hãng để ước lượng ổn định chi phí và rủi ro trước Gate 2.

### Sử dụng AI

Dùng Codex hỗ trợ đọc đề/rubric, rà code và hồ sơ, giải thích kết quả chi phí/ROI và soạn lại phần cá nhân từ các xác nhận trong phiên trao đổi. Đã yêu cầu hoàn nguyên các thay đổi code/config/hồ sơ bổ sung của đợt rà soát; bản cuối chỉ giữ cập nhật TEAM.md so với main trước 20:54. Tiêu chí đã ký giữ nguyên; không nhận các thao tác code/kiểm thử do AI thực hiện là tự làm thủ công.
