# Kế hoạch thực hiện Lab 10 — From PoC to Pilot (Gate 1)

Kế hoạch này chia việc cho nhóm 3 thành viên, bám timeline 240 phút trong README.md và problem-set.md. Thay TV1–TV3 bằng tên thật của nhóm trong TEAM.md.

## 1. Mục tiêu và nguyên tắc làm việc

Nhóm xây hồ sơ Gate 1 cho trợ lý LogiX-VN xử lý yêu cầu hoàn tiền khi giao hàng trễ. Quyết định cần dựa trên bằng chứng về chất lượng, an toàn, chi phí, nhân lực và vận hành.

- Ký tiêu chí chấp nhận và commit/push trước lần đánh giá đầu tiên. Không sửa tiêu chí sau khi ký.
- base là kết quả không có cổng của nhóm; prepared là kết quả với cổng vòng 1 đã chốt; after là kết quả sau sửa ở vòng 2.
- Không sửa snapshot vòng 1 (lab10/guards_round1.py, config/operating_gates.round1.json) hoặc lock file.
- Chỉ làm thẻ sự cố nhóm đã bốc. Không viết xử lý riêng theo mã ticket hoặc câu chữ cụ thể; có bài kiểm tra ẩn.
- Không làm hỏng ticket vốn đúng; không chặn hết, thu phạm vi về 0 hoặc đẩy mọi ca sang người duyệt.
- lab10.grade là công cụ tự kiểm tra trong buổi học; chấm chính thức diễn ra sau buổi học.

## 2. Phân vai cho 3 thành viên

| Thành viên | Vai chính | Việc và file sở hữu |
|---|---|---|
| TV1 — Trưởng nhóm, kỹ sư cổng | Tích hợp, cổng code và lệnh | Tạo repo, cấu hình Git/remotes, chạy eval/checkpoint/grade; triển khai và sửa pre_guard/write_gate trong lab10/guards.py; cùng TV2 truy vết, thử hành vi và kiểm tra hồi quy. |
| TV2 — Sản phẩm và kinh doanh | Tiêu chí và quyết định | Điền config/acceptance_criteria.json trước khi ký; phân tích chi phí/ROI/phạm vi; cấu hình business trong config/operating_gates.json; đề xuất v1/v2 và ghi bằng chứng. |
| TV3 — Vận hành và pháp lý | Người trực, quy trình, dữ liệu và hồ sơ | Cấu hình operations/legal; lập HAZOP/checklist có PIC; viết runbook và giờ cao điểm; kiểm soát PII; ghi mã lần chạy/commit, quản lý phiếu và rà submission. |

TV1 chịu trách nhiệm chạy lệnh và sửa code; TV2 rà số liệu và kiểm tra tính hợp lý từ góc nhìn sản phẩm; TV3 ghi bằng chứng và kiểm tra yêu cầu vận hành/pháp lý. Mọi người cùng đọc trace, đánh giá hồi quy và chốt quyết định.

### Phối hợp theo phiếu

- Phiếu A: TV2 chủ trì tiêu chí; TV1 làm metric offline; TV3 làm telemetry production, ghi giờ ký và mã commit.
- Phiếu B: TV1 phụ trách lần chạy, trace và guard; TV2 phụ trách bản đồ dữ liệu, kinh doanh và quyết định v1; TV3 phụ trách HAZOP, checklist, runbook và nhật ký bằng chứng; cả nhóm làm pre-mortem.
- Phiếu C: TV1 phụ trách trace, sửa code và chạy report; TV2 phụ trách specification, số liệu kinh doanh và quyết định; TV3 phụ trách giả định vận hành/pháp lý, HAZOP, runbook và hồ sơ; cả nhóm cùng làm fault tree, monitor và chốt v2.

Mỗi thành viên tự hoàn thiện mục cá nhân, đóng góp và exit ticket trong TEAM.md.

## 3. Kế hoạch theo timeline 240 phút

### Phút 0–15 — Chuẩn bị repo và chia vai

1. TV1 tạo repo nhóm từ template bằng Use this template (không Fork), đặt đúng tên K5-<L3A hoặc L3B>-DAY10-<TenNhom>-PoCtoPilotGate1, để Public và mời thành viên.
2. Cả nhóm clone repo về máy và dùng chung repo của bàn.
3. TV1 thêm remote upstream trỏ tới repo mẫu; xác nhận origin trỏ repo nhóm và upstream trỏ repo mẫu. Cấu hình danh tính Git theo hướng dẫn lab.
4. Cả nhóm chọn một eval card và PRD v1.1 từ Lab 9 làm bản chung.
5. TV3 điền bảng thành viên/vai trong TEAM.md; mỗi người tạo mục cá nhân.
6. TV3 mở sẵn ba phiếu trong templates/ và chuẩn bị ghi mã commit, mã lần chạy, bằng chứng.
7. Chạy bài kiểm tra công khai theo README; mục tiêu là thấy Ran 13 tests và OK.

Hoàn thành khi repo đúng tên và Public, origin/upstream chính xác, nhóm có vai rõ ràng và bài kiểm tra công khai qua.

### Phút 15–60 — Xác định mục tiêu và tiêu chí (Phiếu A)

1. TV2 chủ trì viết mục tiêu cấp hệ thống và mục tiêu của kế toán Oanh/trưởng ca Hạnh.
2. TV1 chọn một bước của agent và đề xuất metric offline, gồm thước đo, dữ liệu, cách tính và nguồn nhãn.
3. TV3 đề xuất telemetry production để phát hiện tác hại tới bên ngoài LogiX; nêu thời gian đo và ngưỡng báo động. Production không có nhãn đúng/sai.
4. Cả nhóm đọc ví dụ khoảng tin cậy ở câu 1.5 và thống nhất cách diễn giải.
5. TV2 điền config/acceptance_criteria.json và Phiếu A. Phải có:
   - Ngưỡng bắt buộc: pass_rate_min, pass_k_min, wrongful_refund_vnd_max, wrongful_carrier_faults_max, pii_leaks_max.
   - Ngưỡng nên có: escalation_rate_max.
   - business_ops: cost_per_ticket_vnd_max, roi_min, queue_stuck_max.
   - stop_condition và quy tắc cho đủ bốn quyết định.
   - Hai ranh giới đầu ra trong phiếu; không thêm trường JSON ngoài schema.
6. Cả nhóm rà Phiếu A; TV3 kiểm tra cách tính, ngưỡng và các mục bắt buộc đã điền đủ.

Ngưỡng là quyết định của nhóm. Dùng dữ kiện trong data/world.json và bối cảnh pilot để giải thích; không chép ngưỡng từ file example.

### Phút 60–65 — Ký tiêu chí trước khi đo

1. TV2 xác nhận nhóm đã chốt ngưỡng, điều kiện dừng và decision_rule.
2. TV1 chạy python3 -m lab10.criteria sign, sau đó chạy đúng lệnh Git mà chương trình in ra để commit và push tiêu chí cùng lock file.
3. TV3 ghi giờ ký và mã commit vào Phiếu A.

Điểm kiểm soát: không chạy eval hoặc grade trước khi tiêu chí được ký; không sửa acceptance_criteria.json sau ký.

### Phút 65–85 — Đo baseline và tìm rủi ro (Phiếu B)

#### Phút 65–75: làm song song

- TV1 chạy eval suite base ở stage base, so với tiêu chí, ghi mã lần chạy; trace T-002 seed 55 và xác định bước sai đầu tiên.
- TV2 lập bản đồ dữ liệu then chốt, phân biệt nguồn sự thật với bản sao, viết một ví dụ drift và chỉ số bị ảnh hưởng.
- TV3 làm HAZOP vòng 1 (ít nhất 3 dòng trên một tool ghi, trong đó ít nhất 2 dòng ngoài kỹ thuật); điền checklist 9 nhóm việc, mỗi dòng có trạng thái, bằng chứng và PIC có tên.
- TV3 ghi mã lần chạy vào Phiếu B; TV2 tổng hợp bằng chứng và các chỉ số kinh doanh/vận hành theo kho, hãng.

#### Phút 75–85: pre-mortem cả nhóm

1. Xét đủ bốn lăng kính: kỹ thuật; kinh doanh; con người/vận hành; pháp lý.
2. Chọn 2–3 rủi ro cụ thể để chuyển thành cổng vòng 1.
3. Ghi lập luận ủng hộ/phản đối việc để cổng tự chặn so với chuyển người duyệt.

### Phút 85–105 — Dựng cổng phòng ngừa vòng 1

- TV1 triển khai 2–3 cổng trong lab10/guards.py, gắn với pre-mortem/HAZOP. pre_guard(ctx) chạy trước khi agent đọc ticket; write_gate(ctx, action) chạy trước mỗi thao tác ghi.
- TV1 cùng TV2 viết một behavioral property và thử bằng hai ticket adhoc; TV2 rà kết quả trace, TV3 ghi kết quả và nêu hai bước tránh rò rỉ dữ liệu khi phát triển/kiểm thử.
- TV2 điền business trong config/operating_gates.json: trần hoàn tự động mỗi ngày, ngân sách chi phí/ticket, phạm vi pilot và ROI tối thiểu; ghi lý do cho từng số.
- TV3 điền operations và legal: PIC, approver, số người trực, công suất, thời gian chờ tối đa, điều kiện dừng, kênh báo động, dữ liệu cá nhân không gửi bên thứ ba, yêu cầu có nguyên nhân tracking trước khi ghi lỗi hãng.
- TV3 viết runbook phần 1–3, thời hạn từ tín hiệu đỏ đến dừng xong và mục giờ cao điểm (người trực, gọi thêm người, thu hẹp/tắt).
- Cả nhóm chạy eval base/after và bài kiểm tra công khai theo hướng dẫn lab; đọc kết quả để phát hiện hồi quy trước khi chốt.

### Phút 105–115 — Chốt prepared và quyết định v1

1. TV1 chạy python3 -m lab10.checkpoint để chụp code/config vòng 1.
2. TV1 chạy eval suite base, stage prepared; TV2 đối chiếu với tiêu chí đã ký; TV3 ghi mã lần chạy và bằng chứng.
3. TV2 đề xuất một trong bốn quyết định v1 và nêu ba bằng chứng có mã lần chạy.
4. Cả nhóm xác nhận quyết định khớp decision_rule; điền Phiếu B mục B8, gồm ngày cần xem xét lại.
5. TV1 commit và push mốc vòng 1/quyết định theo hướng dẫn phiếu.

Điểm kiểm soát: từ đây chỉ sửa file gốc lab10/guards.py và config/operating_gates.json ở vòng 2. Không sửa snapshot vòng 1 hoặc lock.

### Phút 115–125 — Nghỉ

Kiểm tra lại kết nối upstream. Chưa xem hoặc xử lý thẻ của bàn khác.

### Phút 125–135 — Nhận thẻ và đo prepared trước sửa

1. TV1 pull cập nhật từ upstream bằng đúng lệnh trong README.
2. Một thành viên đại diện cặp bàn bốc số S1–S8; cả nhóm chỉ làm thẻ đã bốc.
3. TV3 ghi số thẻ vào đầu Phiếu C và submission/submission.json.
4. TV1 chạy python3 -m lab10.grade --incident Sx ngay, trước khi sửa code/config.
5. Cả nhóm ghi phần cổng vòng 1 đã đỡ được, số liệu vượt trần và thẻ có/không nằm trong pre-mortem.

### Phút 135–155 — Phân tích sự cố

- TV1 trace ít nhất hai ticket lỗi thuộc hai kiểu khác nhau; TV2/TV3 cùng rà nguồn lỗi và tác động. Phiếu C phải có ít nhất hai lỗi từ nguồn khác nhau, trong đó có một lỗi chìm.
- TV2 viết specification có thể kiểm bằng code hoặc report; nêu chỉ số liên quan và tác động tới tiêu chí đã ký.
- TV3 nêu giả định môi trường có khả năng sai; hoàn thành phần riêng của thẻ và HAZOP của thẻ (ít nhất 3 dòng, không ghi đè HAZOP vòng 1).
- Cả nhóm dựng fault tree trước sửa; sự kiện đỉnh là tác hại cụ thể, có ít nhất hai nhánh ở các tầng khác nhau; mỗi lá có bằng chứng ticket@seed, trường dữ liệu hoặc report.

### Phút 155–185 — Sửa đúng nguyên nhân, thêm monitor và kiểm tra

#### Phút 155–180: sửa và đo lại

- TV1 sửa guard cho nguyên nhân kỹ thuật, không viết logic theo mã ticket/câu chữ cụ thể.
- TV2 chỉnh business nếu nguyên nhân thuộc phạm vi, ngân sách hoặc ROI; ghi lý do và ảnh hưởng tới độ phủ.
- TV3 chỉnh nhân lực, lấy mẫu, quy trình hoặc cổng pháp lý; cập nhật runbook phần 4–5.
- TV1 thêm một hàm monitor mới vào lab10/monitors.py và đăng ký trong MONITORS; TV2 kiểm tra monitor có bắt được rủi ro liên quan; TV3 ghi cách đo vào Phiếu C. escalation_rate có sẵn không tính là monitor mới.
- Chạy eval suite Sx, stage after; chạy thêm suite base, stage after để kiểm tra hồi quy; chạy lại grade trên sự cố.

#### Phút 180–185: ghi phần sau sửa

- Cả nhóm cập nhật fault tree sau sửa; đánh dấu cổng chặn ở nhánh nào, nhánh nào còn hở và biện pháp chỉ giảm khả năng hay ngăn hẳn.
- TV3 cập nhật ít nhất một dòng risk register.
- TV3 cập nhật checklist và runbook phần 4–5.
- TV1 xác nhận report có monitor; TV2 rà regression và các ngưỡng còn vượt; TV3 ghi bằng chứng vào Phiếu C.

### Phút 185–200 — Quyết định v2 và kiểm đủ bài

1. TV2 tổng hợp số liệu base · prepared · after, đề xuất v2 và giải thích đổi/giữ so với v1.
2. Cả nhóm chốt quyết định và điền Phiếu C mục C12, kèm ba dòng bắt buộc:
   - Một giả định môi trường thiết kế đang dựa vào nhưng có thể sai.
   - Cổng chỉ giảm xác suất hay ngăn được tác hại, và vì sao.
   - Cần đo lại điều gì trong pilot thật trước Gate 2.
3. TV3 hoàn thiện submission/submission.json; đảm bảo team, members, incident, hai quyết định và ba dòng khớp với phiếu/TEAM.md.
4. TV1 chạy python3 -m lab10.check_submission --collect; nhóm xử lý từng dòng THIẾU tới khi lệnh báo ĐỦ THÀNH PHẦN.

Quy tắc quyết định: chỉ chọn Tiếp tục nếu các chỉ số bắt buộc đạt trên bộ nền và gói sự cố, đồng thời không còn vượt trần kinh doanh/vận hành. Thu hẹp, Cải tiến thêm hoặc Dừng đều có thể phù hợp nếu có số liệu và lý do cụ thể.

### Phút 200–230 — Demo và phản biện

- TV1 trình bày cổng vòng 1 và cách cổng/sửa đổi tác động tới ticket.
- TV2 trình bày ngưỡng, chi phí/ROI và bằng chứng cho quyết định v2.
- TV3 trình bày vận hành, nhân lực, runbook, pháp lý và rủi ro còn lại.
- TV3 chiếu report ba mốc, monitor mới và kết quả kiểm tra hồi quy; TV1 chạy ticket adhoc khi được yêu cầu.
- Sau thử nghiệm demo, hoàn nguyên mọi thay đổi tạm thời về đúng bản v2.

### Phút 230–240 — Kiểm cuối và nộp

1. TV1 chạy lại python3 -m lab10.grade --incident Sx và lệnh check_submission --collect sau khi hoàn nguyên thay đổi demo; TV2 đối chiếu quyết định với report, TV3 rà hồ sơ và manifest.
2. Cả nhóm kiểm tra file nộp và tình trạng Git; TV1 commit/push lần cuối lên repo nhóm.
3. Từng thành viên hoàn thiện mục cá nhân và exit ticket trong TEAM.md, tự nộp link repo trên LMS trước deadline.

## 4. Checklist hoàn thành

### Quy trình và tính toàn vẹn

- [ ] Repo đúng tên, Public; origin và upstream đúng.
- [ ] Tiêu chí được ký, commit và push trước lần eval đầu tiên.
- [ ] Tiêu chí không đổi sau khi ký.
- [ ] Snapshot và lock vòng 1 còn nguyên.
- [ ] Chỉ xử lý đúng thẻ đã bốc; không có logic theo mã ticket/câu chữ.

### Bằng chứng và phân tích

- [ ] Có report base, prepared và after.
- [ ] Phiếu B có trace, bản đồ dữ liệu/drift, HAZOP, checklist có PIC và pre-mortem đủ bốn lăng kính.
- [ ] Phiếu C có ít nhất hai trace lỗi khác kiểu, HAZOP riêng, specification, giả định môi trường và fault tree có bằng chứng ở lá.
- [ ] Có monitor mới, risk register, fault tree sau sửa và runbook cập nhật.
- [ ] Đã kiểm tra không làm hỏng bộ nền và không chọn phạm vi pilot bằng 0.

### Hồ sơ nộp

- [ ] Phiếu A, B, C đã điền trong templates/.
- [ ] submission/submission.json khớp tên repo, tiêu chí và TEAM.md; thành viên có MSSV.
- [ ] submission/ có code/config hai vòng, tiêu chí và lock, report ba mốc, journal, phiếu và manifest.
- [ ] Lệnh gom bài báo ĐỦ THÀNH PHẦN trên code/config cuối cùng.
- [ ] Bài đã push; từng thành viên đã tự nộp link repo trên LMS.

## 5. Lưu ý khi dùng AI và dữ liệu

Theo RULES.md, AI có thể hỗ trợ đọc code, gợi ý cách nghĩ về cổng và rà câu chữ. Không dùng AI để viết xử lý riêng theo mã ticket hoặc câu chữ cụ thể. Mỗi người ghi việc dùng AI vào mục cá nhân TEAM.md. Không commit API key, mật khẩu hoặc .env; dữ liệu trong lab là dữ liệu giả.
