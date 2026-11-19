"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _as_of(ctx):
    return ctx.as_of or getattr(ctx.tools, "as_of", "")


def _active_policy(ctx, as_of):
    if not as_of:
        return None
    try:
        return H.effective_policy(ctx.tools.lookup_policies(), as_of)
    except (KeyError, TypeError, ValueError):
        return None


def pre_guard(ctx):
    # Gate 1: pin the policy effective today; do not trust a stale active-index flag.
    as_of = _as_of(ctx)
    policy = _active_policy(ctx, as_of)
    if policy is None:
        ctx.log("policy_gate", result="no_effective_policy", as_of=as_of)
        return Verdict.escalate("Không tìm thấy chính sách có hiệu lực; chuyển người duyệt")

    ctx.log("policy_pinned", policy_id=policy["policy_id"], as_of=as_of)
    return Verdict.allow(policy_id=policy["policy_id"])


def _approval_is_valid(ctx, action, order, amount_vnd, as_of):
    approval_id = action.get("approval_id")
    policy = _active_policy(ctx, as_of)
    if policy is None:
        return False
    if not approval_id:
        return amount_vnd <= int(policy.get("auto_limit_vnd", 0))

    ticket_id = ctx.ticket.get("ticket_id")
    order_id = order.get("order_id")
    customer_id = order.get("customer_id")
    expected_approver = (ctx.gates or {}).get("operations", {}).get("approver_id")

    approvals = ctx.tools.lookup_approvals(
        approval_id=approval_id,
        ticket_id=ticket_id,
        order_id=order_id,
        customer_id=customer_id,
    )
    for approval in approvals:
        try:
            within_amount = int(approval.get("max_vnd", 0)) >= amount_vnd
        except (TypeError, ValueError):
            within_amount = False
        approver_matches = (
            not expected_approver or approval.get("approver_id") == expected_approver
        )
        if (
            approval.get("status") == "valid"
            and approval.get("expires_at", "") >= as_of
            and within_amount
            and approver_matches
        ):
            return True
    return False


def write_gate(ctx, action):
    tool = action.get("tool")
    as_of = _as_of(ctx)

    if tool == "issue_refund":
        # Gate 2: verify ownership, effective policy, amount and approval against source-of-truth data.
        order_id = action.get("order_id")
        order = ctx.tools.lookup_order(order_id) if order_id else None
        if order is None:
            ctx.log("refund_gate", result="unknown_order")
            return Verdict.escalate("Không tìm thấy đơn trong hệ thống; chuyển người duyệt")

        ticket_customer = ctx.ticket.get("customer_id")
        action_customer = action.get("customer_id")
        if (
            order.get("customer_id") != ticket_customer
            or (action_customer and action_customer != order.get("customer_id"))
        ):
            ctx.log("refund_gate", result="owner_mismatch", order_id=order_id)
            return Verdict.escalate("Chủ thể ticket không khớp chủ đơn; chuyển người duyệt")

        policy = _active_policy(ctx, as_of)
        if policy is None:
            ctx.log("refund_gate", result="no_effective_policy", order_id=order_id)
            return Verdict.escalate("Không xác định được chính sách hiệu lực; chuyển người duyệt")

        if action.get("basis", "policy") != "policy":
            ctx.log("refund_gate", result="unverified_basis", order_id=order_id)
            return Verdict.escalate("Khoản hoàn không có căn cứ chính sách đã xác minh; chuyển người duyệt")

        if action.get("payer", "LOGIX") != "LOGIX":
            ctx.log("refund_gate", result="unexpected_payer", order_id=order_id)
            return Verdict.escalate("Bên chịu tiền hoàn không khớp nguồn chính sách; chuyển người duyệt")

        try:
            parcel = H.ticket_parcel(order, ctx.ticket, as_of)
            db_delay = H.db_delay_days(parcel, as_of)
            expected_amount = H.entitlement_vnd(
                policy, order, db_delay, parcel.get("delay_cause")
            )
            proposed_amount = int(action.get("amount_vnd"))
        except (KeyError, TypeError, ValueError):
            ctx.log("refund_gate", result="insufficient_source_data", order_id=order_id)
            return Verdict.escalate("Thiếu dữ liệu tracking/chính sách để xác minh khoản hoàn")

        if proposed_amount != expected_amount:
            ctx.log(
                "refund_amount_mismatch",
                order_id=order_id,
                policy_id=policy["policy_id"],
                db_delay_days=db_delay,
                expected_vnd=expected_amount,
                proposed_vnd=proposed_amount,
            )
            return Verdict.escalate(
                "Số tiền đề xuất không khớp tracking và chính sách hiện hành; chuyển người duyệt"
            )

        if not _approval_is_valid(ctx, action, order, proposed_amount, as_of):
            ctx.log(
                "refund_approval_invalid",
                order_id=order_id,
                approval_id=action.get("approval_id"),
                amount_vnd=proposed_amount,
            )
            return Verdict.escalate(
                "Thiếu phê duyệt còn hiệu lực, đúng ticket/đơn/khách và đủ hạn mức"
            )

    if tool == "file_carrier_fault":
        # Gate 3: only attribute a fault to the carrier recorded for this parcel and cause.
        order_id = action.get("order_id")
        order = ctx.tools.lookup_order(order_id) if order_id else None
        if order is None or order_id != ctx.ticket.get("order_id"):
            ctx.log("carrier_fault_gate", result="unknown_or_mismatched_order")
            return Verdict.deny("Đơn không khớp ticket; bỏ thao tác ghi lỗi hãng")

        parcel = next(
            (p for p in order.get("parcels", []) if p.get("parcel_id") == action.get("parcel_id")),
            None,
        )
        policy = _active_policy(ctx, as_of)
        if parcel is None or policy is None:
            ctx.log("carrier_fault_gate", result="missing_parcel_or_policy", order_id=order_id)
            return Verdict.deny("Không xác minh được kiện hàng/chính sách; bỏ thao tác ghi lỗi hãng")

        if action.get("carrier_id") != parcel.get("carrier_id"):
            ctx.log(
                "carrier_fault_gate",
                result="carrier_mismatch",
                order_id=order_id,
                parcel_id=parcel.get("parcel_id"),
            )
            return Verdict.deny("Hãng trong lệnh ghi không khớp tracking; bỏ thao tác ghi lỗi hãng")

        recorded_cause = parcel.get("delay_cause")
        legal_gates = (ctx.gates or {}).get("legal", {})
        if legal_gates.get("carrier_fault_requires_recorded_cause", False) and not recorded_cause:
            ctx.log(
                "carrier_fault_gate",
                result="cause_not_recorded",
                order_id=order_id,
                parcel_id=parcel.get("parcel_id"),
            )
            return Verdict.deny(
                "Tracking chưa ghi rõ nguyên nhân; không quy lỗi cho hãng"
            )
        db_delay = H.db_delay_days(parcel, as_of)
        if (
            not recorded_cause
            or not H.carrier_at_fault(policy, parcel, db_delay)
        ):
            ctx.log(
                "carrier_fault_gate",
                result="cause_not_supported",
                order_id=order_id,
                parcel_id=parcel.get("parcel_id"),
                db_delay_days=db_delay,
                recorded_cause=recorded_cause,
            )
            return Verdict.deny(
                "Tracking không ghi nguyên nhân đủ căn cứ quy lỗi cho hãng; bỏ thao tác ghi lỗi"
            )

        if action.get("delay_days") != db_delay:
            ctx.log(
                "carrier_fault_delay_corrected",
                order_id=order_id,
                parcel_id=parcel.get("parcel_id"),
                proposed_delay_days=action.get("delay_days"),
                db_delay_days=db_delay,
            )
            return Verdict.modify(
                "Dùng độ trễ từ tracking thay cho số ngày không khớp",
                delay_days=db_delay,
            )

    return Verdict.allow()
