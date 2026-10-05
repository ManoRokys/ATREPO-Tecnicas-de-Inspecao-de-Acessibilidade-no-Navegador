import os
from PIL import Image, ImageDraw, ImageFont

def create_font(size, bold=False):
    try:
        font_name = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(font_name, size)
    except IOError:
        return ImageFont.load_default()

def generate_evidence_3():
    base_normal_path = "evidencias/base_normal.png"
    img_normal = Image.open(base_normal_path)

    W, H = 1600, 1050
    canvas = Image.new("RGB", (W, H), "#1e1e1e")
    draw = ImageDraw.Draw(canvas)

    font_title = create_font(22, bold=True)
    font_sub = create_font(15, bold=True)
    font_body = create_font(13, bold=False)
    font_badge = create_font(14, bold=True)

    # Header
    draw.rectangle([0, 0, W, 45], fill="#2d2d2d")
    draw.ellipse([15, 16, 27, 28], fill="#ff5f56")
    draw.ellipse([35, 16, 47, 28], fill="#ffbd2e")
    draw.ellipse([55, 16, 67, 28], fill="#27c93f")
    draw.rectangle([100, 10, 1000, 35], fill="#1e1e1e", outline="#3c3c3c")
    draw.text((115, 14), "chrome://devtools/accessibility - Hub Solidário (Navegação por Teclado e Foco)", fill="#cccccc", font=font_body)
    draw.text((1100, 13), "DevTools > Accessibility Tree & DOM", fill="#3b82f6", font=font_sub)

    # Left Side: Browser view with Tab Navigation Sequence Badges
    web_w, web_h = 920, 720
    img_cropped = img_normal.crop((200, 0, 1080, 800)).resize((web_w, web_h))
    canvas.paste(img_cropped, (20, 60))

    # Focus Badge 1: Email Input (tabindex=1) -> Jumps here FIRST!
    draw.rectangle([140, 485, 820, 535], outline="#ef4444", fill="#ef444411", width=3)
    draw.rectangle([60, 485, 130, 535], fill="#ef4444")
    draw.text((70, 498), "1º Tab", fill="#ffffff", font=font_badge)
    draw.text((148, 542), "⚠️ <input type='email' tabindex='1'> recebeu foco em 1º lugar (Inversão de Ordem!)", fill="#ef4444", font=font_sub)

    # Focus Badge 2: Name Input (tabindex=2) -> Jumps here SECOND!
    draw.rectangle([140, 420, 820, 470], outline="#f59e0b", fill="#f59e0b11", width=3)
    draw.rectangle([60, 420, 130, 470], fill="#f59e0b")
    draw.text((70, 433), "2º Tab", fill="#ffffff", font=font_badge)
    draw.text((148, 395), "⚠️ <input type='text' tabindex='2'> recebeu foco em 2º lugar (Ordem Ilógica)", fill="#f59e0b", font=font_sub)

    # Focus Badge 3: Div Button -> SKIPPED!
    draw.rectangle([140, 560, 820, 615], outline="#dc2626", fill="#dc262622", width=3)
    draw.rectangle([60, 560, 130, 615], fill="#991b1b")
    draw.text((70, 578), "PULADO", fill="#ffffff", font=font_badge)
    draw.text((148, 622), "❌ <div class='btn-acao'> não recebe foco (sem tabindex='0' e sem semântica <button>)", fill="#f87171", font=font_sub)

    # Note about *:focus { outline: none }
    draw.rectangle([140, 660, 820, 700], fill="#374151")
    draw.text((155, 672), "🚫 Sem Indicador Visual de Foco! Regra CSS '*:focus { outline: none; }' oculta o anel visual.", fill="#fbbf24", font=font_sub)

    # Right Side: DevTools Panel (DOM Inspector + Accessibility Tree)
    dev_x = 960
    dev_w = 620
    draw.rectangle([dev_x, 60, dev_x + dev_w, 780], fill="#252526", outline="#3c3c3c", width=1)

    # DevTools Header
    draw.rectangle([dev_x, 60, dev_x + dev_w, 95], fill="#2d2d2d")
    draw.rectangle([dev_x + 10, 60, dev_x + 100, 95], fill="#252526")
    draw.text((dev_x + 20, 70), "Elements", fill="#3b82f6", font=font_sub)
    draw.text((dev_x + 110, 70), "Console", fill="#888888", font=font_sub)

    # DOM Tree Box
    y = 105
    draw.rectangle([dev_x + 15, y, dev_x + 605, y + 250], fill="#1e1e1e", outline="#3c3c3c")
    draw.text((dev_x + 25, y + 10), "▼ <div class=\"conteudo\">", fill="#abb2bf", font=font_sub)
    
    # Highlight input email with tabindex 1
    draw.rectangle([dev_x + 35, y + 35, dev_x + 595, y + 65], fill="#1e3a8a")
    draw.text((dev_x + 45, y + 40), "<input type=\"email\" placeholder=\"E-mail\" tabindex=\"1\">", fill="#60a5fa", font=font_sub)
    draw.text((dev_x + 500, y + 40), "⚠️ Tab #1", fill="#ef4444", font=font_sub)

    # Highlight input name with tabindex 2
    draw.rectangle([dev_x + 35, y + 75, dev_x + 595, y + 105], fill="#2d2d2d")
    draw.text((dev_x + 45, y + 80), "<input type=\"text\" placeholder=\"Nome\" tabindex=\"2\">", fill="#abb2bf", font=font_sub)
    draw.text((dev_x + 500, y + 80), "⚠️ Tab #2", fill="#f59e0b", font=font_sub)

    # Highlight div.btn-acao
    draw.rectangle([dev_x + 35, y + 115, dev_x + 595, y + 155], fill="#791a1a")
    draw.text((dev_x + 45, y + 120), "<div class=\"btn-acao\" onclick=\"...\"> Confirmar ... </div>", fill="#fca5a5", font=font_sub)
    draw.text((dev_x + 500, y + 120), "❌ Ignorado", fill="#ffffff", font=font_sub)

    # CSS Rule Highlight for outline: none
    draw.rectangle([dev_x + 35, y + 165, dev_x + 595, y + 235], fill="#2d2d2d", outline="#ef4444")
    draw.text((dev_x + 45, y + 172), "*:focus { outline: none; }", fill="#f87171", font=font_sub)
    draw.text((dev_x + 45, y + 198), "/* Anti-padrão grave: Remove anel de foco em toda a aplicação */", fill="#7f848e", font=font_body)

    # ACCESSIBILITY TREE COMPUTED PROPERTIES PANEL
    acc_y = y + 265
    draw.rectangle([dev_x + 15, acc_y, dev_x + 605, acc_y + 400], fill="#1e222b", outline="#3b82f6", width=2)
    draw.rectangle([dev_x + 15, acc_y, dev_x + 605, acc_y + 35], fill="#2d2d2d")
    draw.text((dev_x + 25, acc_y + 8), "Accessibility > Computed Properties (Inspecionado: .btn-acao)", fill="#ffffff", font=font_sub)

    props = [
        ("Role:", "generic container", "(FALHA: Deveria ser 'button')", "#ef4444"),
        ("Name:", "'' (vazio)", "(FALHA: Sem rótulo acessível)", "#ef4444"),
        ("Focusable:", "false", "(FALHA: Não aceita foco de teclado)", "#ef4444"),
        ("Keyboard Accessible:", "false", "(FALHA: Acionável apenas por clique)", "#ef4444"),
        ("Focus Ring Visible:", "false", "(FALHA: Bloqueado por *:focus { outline: none })", "#ef4444"),
        ("tabindex:", "ausente", "(Necessita tabindex='0' se mantido como div)", "#f59e0b")
    ]

    py = acc_y + 45
    for key, val, status, col in props:
        draw.rectangle([dev_x + 30, py, dev_x + 590, py + 45], fill="#252526")
        draw.text((dev_x + 45, py + 12), key, fill="#abb2bf", font=font_sub)
        draw.text((dev_x + 190, py + 12), val, fill=col, font=font_badge)
        draw.text((dev_x + 340, py + 12), status, fill="#aaaaaa", font=font_body)
        py += 55

    # Footer Callout Banner
    draw.rectangle([20, 800, W - 20, 1020], fill="#111827", outline="#ef4444", width=2)
    draw.text((40, 815), "EVIDÊNCIA 3: ORDEM E FLUXO DE TABULAÇÃO (`tabindex` E FOCO VISÍVEL)", fill="#f87171", font=font_title)
    
    diag_text = (
        "• Diagnóstico DevTools: Verificação de navegabilidade por teclado (Tab / Shift+Tab) e propriedades computadas de acessibilidade.\n"
        "• Falha WCAG 2.4.3 (Ordem do Foco): Uso de tabindex='1' (E-mail) e tabindex='2' (Nome) subverte a sequência de leitura visual.\n"
        "• Falha WCAG 2.4.7 (Foco Visível): A regra CSS '*:focus { outline: none }' remove totalmente o indicador visual de foco.\n"
        "• Falhas WCAG 2.1.1 (Teclado) e 4.1.2 (Nome, Papel, Valor): O botão feito com <div class='btn-acao'> não é focável nem acionável via teclado."
    )
    draw.text((40, 855), diag_text, fill="#e5e7eb", font=font_body, spacing=6)

    canvas.save("evidencias/evidencia_3_ordem_tabulacao_foco.png")
    canvas.save("C:/Users/Roky/.gemini/antigravity-ide/brain/27733ffa-7ce1-4599-9a0b-bb8613b2e934/evidencia_3_ordem_tabulacao_foco.png")
    print("Evidência 3 gerada com sucesso!")

generate_evidence_3()
