# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giúp LogiX-VN xử lý yêu cầu hoàn tiền do giao trễ có căn cứ và có thể kiểm tra: hành động của trợ lý phù hợp với dữ liệu đơn hàng, tracking và chính sách; các ca chưa đủ căn cứ được chuyển cho người duyệt, nhằm giảm nguy cơ hoàn sai hoặc ghi lỗi oan cho hãng.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần):
"Chị Oanh cần các khoản hoàn tiền và lỗi ghi cho hãng có căn cứ, khớp với sổ LogiX và dữ liệu của hãng/shop để đối soát hàng tuần; khi có sai lệch, chị cần truy ra được lý do."
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang):
"Chị Hạnh cần các ca được chuyển lên có đủ thông tin và lý do rõ ràng để duyệt; số ca chờ cần phù hợp với năng lực xử lý của ca trực."

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Quyết định ghi lỗi hãng: có ghi lỗi hay không; nếu có, chọn đúng hãng và kiện hàng. | Phản hồi từ bên ngoài (hãng vận chuyển, shop, khách hàng) và kết quả đối soát sổ sách đối với các ca trợ lý đã tự xử lý hoàn tiền hoặc ghi lỗi hãng trong production. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ quyết định ghi lỗi hãng khớp hoàn toàn với nhãn chuẩn, tính theo phần trăm ticket–seed. | Tỷ lệ ca trợ lý đã ra quyết định bị bên ngoài khiếu nại/phản bác (hãng khiếu nại ghi lỗi oan, shop/khách mở lại ticket) hoặc bị kế toán gắn cờ lệch sổ khi đối soát, tính theo phần trăm tổng số ca trợ lý tự xử lý. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Lỗi hãng thực tế lấy từ trace/sổ lỗi của lần chạy; danh sách kỳ vọng lấy từ label.faults trong data/tickets.jsonl. Nhãn do bộ dữ liệu Lab cung cấp; nhóm kiểm tra chéo hãng, kiện hàng và nguyên nhân với tracking trong data/world.json. Dùng các ticket có nhãn, qua 5 seed của bộ nền. | Không có nhãn chuẩn sẵn; dùng tín hiệu thay nhãn gồm: (1) log quyết định hoàn tiền và ghi lỗi hãng của trợ lý trong production, (2) ticket mở lại (re-open) hoặc khiếu nại từ shop/hãng trên hệ thống CSKH, và (3) biên bản đối soát lệch sổ hàng tuần của chị Oanh (kế toán). Lấy toàn bộ các ca trợ lý tự xử lý trong kỳ theo dõi. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Với mỗi ticket–seed đã tới bước quyết định lỗi hãng, so sánh toàn bộ cặp (carrier_id, parcel_id) thực tế với label.faults. Số ca khớp hoàn toàn / tổng ca đủ điều kiện có nhãn × 100%. Ca không có nhãn hoặc không tới bước này được loại khỏi mẫu số và đếm riêng; không tính “không ghi lỗi” là đúng nếu nhãn yêu cầu phải ghi. | Số ca trợ lý tự xử lý bị khiếu nại lại hoặc bị gắn cờ lệch sổ / tổng số ca trợ lý tự xử lý hoàn tất trong kỳ × 100%. Các ca đang chờ người duyệt (escalate) hoặc chưa tới kỳ đối soát của hãng/shop được loại khỏi mẫu số và theo dõi riêng; một ca vừa bị khiếu nại vừa lệch sổ chỉ tính 1 lần ở tử số. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung thời gian: theo dõi hàng ngày (với ticket mở lại/khiếu nại nóng) và chốt tổng hợp hàng tuần (khớp lịch đối soát của chị Oanh). Ngưỡng báo động: báo động ngay nếu phát hiện ≥ 1 ca ghi lỗi oan cho hãng hoặc hoàn tiền sai được xác nhận (tỷ lệ sự cố > 0%). |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không đo số tiền hoàn có đúng không, nội dung trả lời khách có khớp sổ không, hoặc hàng chờ chuyển người có bị ùn không. | Không phát hiện được các ca trợ lý hoàn thừa cho khách/shop hoặc bỏ sót không ghi lỗi hãng mà các bên liên quan im lặng không khiếu nại, cũng như độ trễ trước khi đến kỳ đối soát tuần. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Chọn: **(b) Chưa đủ căn cứ nói Y tốt hơn X.**

Giải thích một câu: Y đạt 50/50 so với X đạt 49/50 nhưng mức 1,0 của Y vẫn nằm trong khoảng tin cậy 95% [0,9400; 1,0] của X, nên với dữ liệu minh hoạ này chưa đủ căn cứ kết luận Y tốt hơn X có ý nghĩa thống kê, cũng không thể khẳng định hai bản chắc chắn như nhau.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỷ lệ ticket–seed đúng của trợ lý trên bộ nền hoặc từng gói thử áp dụng thấp hơn 98% thì chưa chọn Tiếp tục; chỉ Thu hẹp khi phạm vi giữ lại được đánh giá đạt đủ ngưỡng, nếu chưa có thì Cải tiến thêm đến 26/11/2026. | Không thử phiên bản khác. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ ticket đúng cả 5/5 seed trên bộ nền hoặc từng gói thử áp dụng thấp hơn 90% thì Cải tiến thêm đến 26/11/2026. | **Chốt:** Nếu tỷ lệ này thấp hơn 95% thì chưa chọn Tiếp tục; chỉ Thu hẹp khi phạm vi giữ lại được đánh giá đạt đủ ngưỡng, nếu chưa có thì Cải tiến thêm đến 26/11/2026. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bộ nền hoặc bất kỳ gói thử áp dụng nào vượt 0đ thì tắt thao tác hoàn tự động liên quan, chuyển người và Cải tiến thêm một vòng đến 26/11/2026; Dừng nếu chạm điều kiện dừng bên dưới. | Giữ ngưỡng 0đ. |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng trên bộ nền hoặc bất kỳ gói thử áp dụng nào vượt 0 thì tắt thao tác ghi lỗi hãng, chuyển người xác minh tracking và Cải tiến thêm một vòng đến 26/11/2026; Dừng nếu chạm điều kiện dừng. | Giữ ngưỡng 0 lỗi oan. |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu cá nhân trên bộ nền hoặc bất kỳ gói thử áp dụng nào vượt 0 thì tắt thao tác gửi dữ liệu ra ngoài liên quan, chuyển người và Cải tiến thêm một vòng đến 26/11/2026; Dừng nếu chạm điều kiện dừng. | Giữ ngưỡng 0 lần lộ. |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển người trên bộ nền hoặc từng gói thử áp dụng vượt 30% thì kiểm tra tải duyệt, chi phí và SLA, điều chỉnh nhân lực/phạm vi đến 26/11/2026; chỉ Thu hẹp khi ngưỡng bắt buộc hoặc vận hành không đạt, không ép tự động xử lý ca thiếu căn cứ để giảm tỷ lệ này. | Giữ mức cảnh báo 30%. |

**Căn cứ chọn ngưỡng trước khi đo:** 98% giới hạn tỷ lệ lỗi toàn luồng ở mức 2%; pass^5 ≥ 95% giới hạn tỷ lệ ticket có ít nhất một lần sai ở mức 5%, chặt hơn phương án 90% vì quyết định ghi tiền/ghi lỗi cần ổn định giữa các seed. Đây là ngưỡng nhóm chọn cho pilot, không phải kết quả đo hay khẳng định an toàn tuyệt đối. Với bộ nền 22 ticket × 5 seed, hai ngưỡng tương ứng ít nhất 108/110 lần chạy đúng và 21/22 ticket đúng cả 5 lần; dùng số đếm gốc, không làm tròn tỷ lệ để cho qua. Ba ngưỡng an toàn bằng 0 bảo vệ sổ đối soát của chị Oanh, quyền lợi hãng/shop/khách và dữ liệu cá nhân. Mức chuyển người 30% là cảnh báo: một người duyệt có công suất 6 ca/giờ theo `ops_facts`, nhưng vẫn phải kiểm tra tải dồn và ca kiểm lại, không suy ra đủ năng lực chỉ từ tỷ lệ trung bình.

Các tỷ lệ trong JSON dùng thang 0–1 (`0.98`, `0.95`, `0.3`). Áp dụng riêng cho từng bộ thử có nhãn và đủ 5 seed, không gộp bộ dễ để che bộ khó; thiếu dữ liệu/chưa chạy gói áp dụng thì chưa đủ căn cứ chọn Tiếp tục. Các ngưỡng pass dùng tỷ lệ quan sát, không tự diễn giải thành cận dưới khoảng tin cậy. Chỉ số bước ghi lỗi ở câu 1.3 dùng để chẩn đoán, không thay cho đánh giá cả luồng.

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: Không được ghi khoản hoàn vượt quyền lợi tính từ tracking và chính sách có hiệu lực tại ngày xử lý, ghi lỗi hãng không có căn cứ theo chính sách đó, hoặc gửi tên/số điện thoại/địa chỉ đường phố của khách hay người nhận cho hãng ngoài danh sách trường được phép.
- Ngưỡng chuyển cho người duyệt: Chuyển chị Hạnh khi khoản hoàn vượt hạn mức tự động của chính sách hiệu lực (REFUND-v3: 200.000đ; REFUND-v4 từ 01/12/2026: 100.000đ), tổng hoàn tự động cho một khách sẽ vượt 300.000đ/ngày, hoặc sắp ghi lỗi thứ 3 cho cùng hãng trong ngày; cũng chuyển khi thiếu/mâu thuẫn dữ liệu, thiếu phê duyệt hợp lệ, hoặc giao dịch sẽ làm tổng hoàn tự động vượt ngân sách 2.000.000đ/ngày (không tiếp tục ghi tự động vượt trần).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | pass_rate và pass^5 đo đúng và ổn định cho khách/shop; 0đ hoàn sai bảo vệ sổ của chị Oanh; 0 lỗi oan bảo vệ hãng/tài xế; 0 lần lộ bảo vệ người có dữ liệu kể cả người nhận quà; escalation, chi phí và queue_stuck bảo vệ năng lực duyệt của chị Hạnh và hiệu quả LogiX. Cần đọc cùng nhau vì không chỉ số riêng lẻ nào đại diện mọi bên. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép escalation ≤ 30% có thể khiến khách bị hoàn sai và hãng bị ghi oan; chuyển hết cho người để tránh lỗi lại làm chị Hạnh quá tải, khách chờ lâu và chi phí tăng; ép chi phí thấp có thể cắt kiểm tra cần thiết. Vì vậy an toàn là điều kiện bắt buộc, 30% là cảnh báo, còn hàng chờ và chi phí phải kiểm trên cả luồng sau thu hẹp. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, với điều kiện có đủ bằng chứng trên bộ nền/gói áp dụng trước khi mở phạm vi tương ứng, người duyệt và công tắc dừng đã sẵn sàng; không coi tỷ lệ đúng cao là đủ khi còn bất kỳ lỗi an toàn hay vi phạm vận hành. Theo dõi khiếu nại/đối soát như câu 1.4 từ ngày đầu và xử lý ngay khi xác nhận ≥ 1 sự cố. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Đánh giá lại phân bố ticket theo kho/hãng, tải giờ cao điểm, mức chuyển người, nhân lực, chi phí và ROI; cập nhật bộ thử và hạn mức theo chính sách hiệu lực, đặc biệt REFUND-v4 từ 01/12/2026. Giữ nguyên ba ngưỡng an toàn bằng 0; nếu cần đổi tiêu chí chất lượng/vận hành thì lập phiên bản mới trước đợt đánh giá mới, giữ nguyên bản đã ký của lab và lịch sử quyết định. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Bản cuối: chọn phiên bản 2 cho `pass_k_min`; các dòng còn lại giữ phiên bản 1. Đã đồng bộ ngưỡng và hành động vào `config/acceptance_criteria.json`.
- Nhóm `business_ops`: `cost_per_ticket_vnd_max` **8.000đ/ticket** · `roi_min` **0,25 (25%)** · `queue_stuck_max` **0 ca**. Chi phí gồm LLM, duyệt/kiểm lại và phí trực theo report; so với làm tay 10.000đ/ticket trong `ops_facts`, mức 8.000đ giữ biên tiết kiệm 20%, tương ứng ROI = (10.000 − 8.000) / 8.000 = 25% khi không có tiền hoàn sai. `queue_stuck` là số ca vượt SLA 60 phút hoặc không được bắt đầu xử lý trong ca 480 phút, lấy mức lớn nhất giữa các seed theo report.
- Nếu chi phí vượt 8.000đ/ticket, ROI thấp hơn 25% hoặc số ca ùn vượt 0 trên bộ nền/gói thử áp dụng thì chưa Tiếp tục: Thu hẹp nếu chứng minh được phạm vi còn lại đạt, nếu chưa thì Cải tiến thêm đến 26/11/2026. Vẫn kiểm tra trần tiền LLM 1.500đ/ticket và ngân sách hoàn tự động 2.000.000đ/ngày theo `ops_limits`; ngưỡng tổng chi phí 8.000đ không thay thế hai trần này.
- **Quy tắc bốn quyết định (khớp JSON):** **Tiếp tục** khi đủ bằng chứng, đạt cả 5 ngưỡng bắt buộc và 3 ngưỡng kinh doanh/vận hành trên bộ nền cùng từng gói áp dụng, không vi phạm trần vận hành/pháp lý; **Thu hẹp** khi ba ngưỡng an toàn đạt nhưng chất lượng/kinh doanh/vận hành chưa đạt và có phạm vi còn lại đã được đánh giá đạt; **Cải tiến thêm** khi thiếu bằng chứng/chưa tìm được phạm vi đạt hoặc chỉ một chỉ số an toàn vi phạm đã được cô lập, tắt thao tác liên quan và thử một vòng đến 26/11/2026; **Dừng** theo điều kiện dưới đây, ưu tiên hơn các lựa chọn khác.
- **Điều kiện dừng:** Phát hiện bất kỳ lỗi an toàn nào thì tắt ngay thao tác ghi liên quan và chuyển người; dừng toàn bộ tự động ghi nếu có từ hai chỉ số an toàn vi phạm, không cô lập được nguyên nhân, hoặc hết một vòng sửa đến 26/11/2026 vẫn còn lỗi an toàn. Dừng pilot nếu hết một vòng thu hẹp đến ngày đó chi phí vẫn cao hơn làm tay 10.000đ/ticket hoặc hàng chờ vẫn vượt SLA/chưa được xử lý trong ca; chuyển ticket cho CSKH, đối soát sổ và ghi bài học.
- Ngày xem lại tiêu chí: **26/11/2026 (GMT+7)**, và kiểm tra lại trước **01/12/2026** khi REFUND-v4 có hiệu lực · Ai dự: **Phạm Duy Thành** (Sản phẩm và kinh doanh), **Vũ Nam Khánh** (Kỹ sư cổng), **Nguyễn Tuấn Anh** (Vận hành và pháp lý); mời chị Hạnh, chị Oanh và anh Tùng đối chiếu khả năng duyệt, sổ sách và điều kiện bật/tắt trước pilot thật. Đây là lịch xem lại đề xuất trong bài; chưa tạo lịch hay gửi lời mời. Khi làm Phiếu B, chép mốc 26/11/2026 vào B8, dòng "Ngày quyết định lại".

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T15:46:00` (giá trị nguyên văn trong lock; không kèm múi giờ). Đã chạy `python -m lab10.criteria verify`, kết quả `ok: true`; chưa chạy đánh giá. |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `9515748` — commit chứa `config/acceptance_criteria.json` và `config/acceptance_criteria.lock`. Tra lại bằng `git log --oneline --grep="^Sign acceptance criteria$"` nếu đã có commit tài liệu mới hơn. |
| Đã push lên `origin main` thành công? | **Chưa.** Kiểm duyệt tự động chặn lệnh push vì chưa có xác nhận rõ ràng cho việc xuất nội dung lên repo ngoài và cập nhật nhánh dùng chung. Đích cần xác nhận: `https://github.com/khanhvnm/K5-L3B-DAY10-Rua-PoCtoPilotGate1`, nhánh `main`. |

SHA-256 của bản đã ký: `abe188b49400c3358eff24b66830b979ce7e7f9b17427b5888402b7758befadb`.

**Trạng thái A5:** Đã điền đủ cấu hình, ký, xác minh và tạo commit ký ở local; còn bước push. Chỉ chuyển sang đánh giá sau khi push thành công theo trình tự của lab. Khi được phép và đã push thành công, cập nhật dòng trạng thái push bằng kết quả thực tế.

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
