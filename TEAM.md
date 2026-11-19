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

**Xác nhận quyết định v2:** Người thao tác trong phiên trao đổi xác nhận vai Sản phẩm và kinh doanh và chốt **Cải tiến thêm**, chưa mở pilot ở phần chưa đạt, xem lại **26/11/2026**. Xác nhận này không thay việc từng thành viên tự xác nhận đóng góp/exit ticket.

Hai mục Vũ Nam Khánh và Nguyễn Tuấn Anh được giữ nguyên từ bản nháp nhóm đã commit tại `ddb3ca3` (`origin/main`), chưa thay bằng xác nhận cá nhân. Các số liệu 20:36 trong hai mục đó là bằng chứng lịch sử. Phần Phạm Duy Thành được cập nhật theo công việc và xác nhận trong phiên hoàn thiện bài, có khai báo việc dùng AI. Kết quả kiểm tra hiện tại xem Phiếu C và báo cáo cuối trong submission/runs/grade-report.json.

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

Sản phẩm và kinh doanh: tiêu chí chấp nhận ở Phiếu A, phạm vi pilot và chi phí/ROI, quyết định v1 tại Phiếu B mục B8 và quyết định v2 tại Phiếu C mục C12.

### Đóng góp cụ thể

Trong đợt hoàn thiện bài, tôi yêu cầu rà soát toàn bộ dự án theo đề và rubric, sau đó xác nhận cấu hình nhóm đã nêu trong B7.5: PIC NV-TUNG, người duyệt NV-HANH, 1 người trực, công suất 6 ca/giờ, SLA 60 phút, kiểm mẫu 10%, ghi chú quyết định và bảo vệ PII. Giữ phạm vi HN/DN, trần hoàn 1.500.000đ/ngày, trần LLM 1.500đ/ticket và ROI tối thiểu 0,25. Tôi giao trợ lý lựa chọn cách triển khai giới hạn lỗi hãng; bản cuối dùng trần 2 lỗi tự động/hãng/ngày theo ops_limits.

Tôi xác nhận chốt v2 **Cải tiến thêm**, chưa mở pilot ở phần chưa đạt và xem lại ngày **26/11/2026** theo tiêu chí đã ký. Căn cứ là S3 còn 5 lỗi hãng oan, pass_rate/pass_k = 0,8333, chi phí 8.048đ/ticket và ROI = 0,24. Không đổi ngưỡng đã ký để hợp thức hóa kết quả. Yêu cầu khôi phục snapshot đúng bằng chứng; kết quả cuối khớp hash gốc, không thay lock hoặc nội dung code vòng 1.

### Bằng chứng

- Tiêu chí đã ký: commit `19dc58a`, hash `abe188b4`; Phiếu A A1–A5.
- Quyết định v1: Phiếu B B8; quyết định v2 và cấu hình đã xác nhận: Phiếu C C11–C12, config/operating_gates.json và submission/submission.json.
- Báo cáo cuối: `R-S3-grade-20261119-213142-e7cf28`, được gom tại submission/runs/grade-report.json; các chỉ số S3 và bộ nền được đối chiếu trong cùng báo cáo.
- Snapshot đã khôi phục: checkpoint ok=true, hash chốt `cb9f354e`; submission/manifest.json ghi hash các file đã gom.

### Exit ticket

Điều rút ra: quyết định Gate 1 phải dựa đồng thời vào tiêu chí đã ký, tác động tới bên thứ ba và chi phí vận hành. Bộ nền đạt hoặc hồ sơ đủ thành phần không có nghĩa pilot đã sẵn sàng; khi S3 còn lỗi hãng oan và ROI chưa đạt, quyết định phù hợp là Cải tiến thêm.

Điều còn chưa chắc: cách đồng bộ sổ lỗi của các ca ngoài phạm vi pilot với ca tự động, và cần bao nhiêu dữ liệu thật theo kho/hãng để ước lượng ổn định chi phí, tải duyệt và rủi ro trước Gate 2.

### Sử dụng AI

Dùng Codex hỗ trợ đọc đề và rubric, rà code/tài liệu, sửa cổng và monitor, chạy kiểm tra, khôi phục cách xuống dòng của snapshot đúng hash gốc, cập nhật Phiếu C và gom hồ sơ. Tôi xác nhận cấu hình vận hành và quyết định v2 trong phiên trao đổi; các thao tác code/kiểm tra do trợ lý thực hiện được ghi rõ, không nhận là tự thực hiện thủ công. Các ngưỡng tiêu chí đã ký giữ nguyên; không dùng AI viết xử lý riêng theo mã ticket hoặc câu chữ cụ thể.
