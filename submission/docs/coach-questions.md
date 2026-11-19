# Dự thảo trao đổi Coach — chưa gửi

Nhóm Rua, repo K5-L3B-DAY10-Rua-PoCtoPilotGate1, thẻ S3.

1. **Đã giải quyết, không cần hỏi Coach về snapshot:** file gốc trộn CRLF ở 35 dòng đầu và dòng cuối, LF ở giữa. Đã khôi phục đúng SHA-256 `8405217188d98fdca0c054a62c4cbd3fb5126cba27596cf0ee16559827eb7f4b`, khớp lock giữ nguyên; nội dung code không đổi. checkpoint verify hiện ok=true. .gitattributes giữ nguyên byte khi commit/checkout. Các câu hỏi còn lại chỉ phục vụ giải thích hồ sơ hoặc mô phỏng.

2. Đã khôi phục journal nhóm commit trên origin/main: baseline 16:13, prepared 17:09 và grade 17:17; thời gian ký 15:57, commit ký 15:59. Chưa tìm được report/trace đầy đủ của các run cũ đó. Phiếu B đã chốt còn thiếu dòng trong B0 và ô B7.1; nhóm ghi bổ sung trung thực ở Phiếu C, không viết lại v1 hoặc giả tạo lần chạy quá khứ. Xin hướng dẫn nếu cần bổ sung hồ sơ vòng 1.

3. S3 thu hẹp HN/DN chỉ replay hai trong bốn ca cùng hãng của S3-LOAT; trần dữ liệu là 2 lỗi/hãng/ngày nhưng nhãn S3-43 vẫn yêu cầu không ghi lỗi. Cổng dùng trần dữ liệu và không đọc nhãn, không sửa bộ mô phỏng; report cuối vẫn còn 5 lỗi oan, không tuyên bố đạt. Xin làm rõ kỳ vọng đối với lịch sử ca ngoài scope trước khi nhóm xét mở pilot.

Báo cáo hiện tại: `R-S3-grade-20261119-213142-e7cf28` (FAIL); người phụ trách Sản phẩm và kinh doanh đã xác nhận chốt v2 Cải tiến thêm, chưa mở pilot ở phần chưa đạt, xem lại 26/11/2026 theo tiêu chí đã ký.
