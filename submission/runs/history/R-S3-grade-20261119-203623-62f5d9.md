# Tự kiểm tra sự cố S3 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S3-grade-20261119-203623-62f5d9` · bàn: `K5-L3B-DAY10-Rua-PoCtoPilotGate1` · grader `lab10-1.0` · 0.255s
- Ba mốc: base `R-S3-before-20261119-203623-62f5d9` · prepared `R-S3-prepared-20261119-203623-62f5d9` · after `R-S3-after-20261119-203623-62f5d9` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `cb9f354e`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `62f5d92e00b7`
- Hash Bản tiêu chí chấp nhận: `abe188b49400` · đã ký: `abe188b49400` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S3` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S3 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ❌ | file khoá bị đổi: ['data/tickets.jsonl', 'data/world.json', 'incidents/S3/card.json', 'incidents/S3/card.md', 'incidents/S3/tickets.jsonl', 'incidents/S3/world_patch.json', 'lab10/__init__.py', 'lab10/_gradectx.py', 'lab10/_noop_guards.py', 'lab10/agent.py', 'lab10/check_submission.py', 'lab10/checkpoint.py', 'lab10/criteria.py', 'lab10/eval.py', 'lab10/gate.py', 'lab10/grade.py', 'lab10/helpers.py', 'lab10/mock_llm.py', 'lab10/ops.py', 'lab10/tools.py', 'lab10/trace.py', 'lab10/world.py', 'tests/test_public.py'] |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ❌ | base có vấn đề: True; after sạch: False; ticket còn hỏng: ['S3-43@11', 'S3-43@22', 'S3-43@33', 'S3-43@44', 'S3-43@55']; trần còn vượt: ['ROI 0.24 < ngưỡng bàn đặt 0.25'] |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['carrier_fault_write_rate']; sáng đèn: [('carrier_fault_write_rate', 'before', 0.509091, 0.833333), ('carrier_fault_write_rate', 'after', 0.461538, 0.666667)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.1667 | 0.3333 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 3147 · 10000 | 7298 · 10000 | 8048 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 667 · 1500 | 671 · 1500 | 771 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -97759 | 16213 | 11713 |
| ROI | -2.59 | 0.37 | 0.24 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 180000 · 2000000 | 80000 · 2000000 | 80000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 180000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5 | 0.5 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 35 | 5 | 5 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.0; hoàn sai 0; oan 20; PII 0; chi phí 662đ | — | — |
| kho DN | pass 0.0; hoàn sai 0; oan 5; PII 0; chi phí 664đ | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 664đ | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 764đ |
| kho HCM | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 661đ | — | — |
| kho HN | pass 0.5; hoàn sai 900000; oan 5; PII 0; chi phí 615đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3115đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4190đ |
| hãng DNB | pass 0.0; hoàn sai 0; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.5; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 0.2857; hoàn sai 0; oan 25; PII 0 | pass 0.5; hoàn sai 0; oan 5; PII 0 | pass 0.5; hoàn sai 0; oan 5; PII 0 |
| hãng VNX | pass 0.0; hoàn sai 900000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.3077 | 0.3077 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 5942 · 10000 | 6011 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 670 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 52755 | 51855 |
| ROI | 1.34 | 0.68 | 0.66 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5909 | 0.5909 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4646đ |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | — | — |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- VƯỢT TRẦN: ROI 0.24 < ngưỡng bàn đặt 0.25 (trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: pass_rate ≥ 0.98 (thực tế 0.8333, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: pass_k ≥ 0.95 (thực tế 0.8333, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: wrongful_carrier_faults ≤ 0 (thực tế 5, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: cost_per_ticket_vnd ≤ 8000 (thực tế 8048, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: roi ≥ 0.25 (thực tế 0.24, trên visible)
- KHÔNG đủ căn cứ để chọn 'Tiếp tục'. Thu hẹp, Cải tiến thêm hoặc Dừng, kèm lý do và con số, vẫn là quyết định đạt.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.3077 | 0.3077 | +0.0804 |
| visible | pass_rate | 0.25 | 0.8333 | 0.8333 | +0.5833 |
| visible | pass_k | 0.25 | 0.8333 | 0.8333 | +0.5833 |
| visible | wrongful_refund_vnd | 900000 | 0 | 0 | -900000 |
| visible | under_refund_vnd | 667000 | 0 | 0 | -667000 |
| visible | wrongful_carrier_faults | 35 | 5 | 5 | -30 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.1667 | 0.1667 | +0.1667 |
