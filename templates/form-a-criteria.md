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

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

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
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

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
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
