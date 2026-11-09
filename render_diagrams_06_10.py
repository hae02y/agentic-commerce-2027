from pathlib import Path
from html import escape

ROOT = Path('/private/tmp/agentic-commerce-2027/assets/diagrams')
ROOT.mkdir(parents=True, exist_ok=True)

DIAGRAMS = {
    '06-approval-boundary.svg': ('구매 권한의 경계', ['목적·예산 설정', 'AI의 탐색·비교', '조건 확인·승인', '결제·주문 증거'], '사람의 허락은 구체적인 거래 조건에 붙습니다.'),
    '07-payment-roles.svg': ('대화 화면 뒤의 결제 흐름', ['구매자 승인', 'AI가 주문 연결', '판매자 주문 확정', '결제 기록 확인'], '판매자와 결제 기록에서 완료를 확인합니다.'),
    '08-after-purchase.svg': ('주문 후 사실 확인', ['주문번호', '배송 상태', '반품 접수', '환불 기록'], 'AI의 설명은 각 시스템의 최신 기록으로 검증합니다.'),
    '09-b2b-invoice.svg': ('기업 청구서 결제 경계', ['발주·검수 대조', '담당자 지급 승인', 'AI가 지급 실행', '장부·은행 대사'], 'AI는 승인된 결제를 실행하고 예외는 사람에게 돌립니다.'),
    '10-machine-payments.svg': ('에이전트의 서비스 구매', ['업무·총예산 승인', '유료 서비스 선택', '건별 한도 검증', '결과·지출 기록'], '작은 결제가 반복될수록 누적 비용을 확인합니다.'),
}

for filename, (title, steps, foot) in DIAGRAMS.items():
    boxes = []
    for i, label in enumerate(steps):
        x = 30 + i * 232
        boxes.append(f'<rect x="{x}" y="102" width="200" height="88" rx="14" fill="#ffffff" stroke="#386C75" stroke-width="2"/>')
        boxes.append(f'<text x="{x + 100}" y="153" text-anchor="middle" class="step">{escape(label)}</text>')
        if i < len(steps) - 1:
            boxes.append(f'<path d="M{x + 203} 146 L{x + 228} 146" stroke="#386C75" stroke-width="3" marker-end="url(#arrow)"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="280" viewBox="0 0 960 280" role="img" aria-label="{escape(title)}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#386C75"/></marker></defs>
<style>.title{{font:700 26px -apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Malgun Gothic',sans-serif;fill:#173B44}}.step{{font:600 18px -apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Malgun Gothic',sans-serif;fill:#173B44}}.foot{{font:16px -apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Malgun Gothic',sans-serif;fill:#44616A}}</style>
<rect width="960" height="280" rx="18" fill="#EDF6F3"/>
<text x="30" y="54" class="title">{escape(title)}</text>
{''.join(boxes)}
<text x="30" y="238" class="foot">{escape(foot)}</text>
</svg>'''
    (ROOT / filename).write_text(svg, encoding='utf-8')
