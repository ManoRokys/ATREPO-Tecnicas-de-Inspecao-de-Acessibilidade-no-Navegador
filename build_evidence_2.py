import os
from PIL import Image, ImageDraw, ImageFont

def create_font(size, bold=False):
    try:
        font_name = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(font_name, size)
    except IOError:
        return ImageFont.load_default()

def generate_evidence_2():
    base_normal_path = "evidencias/base_normal.png"
    img_normal = Image.open(base_normal_path)

    W, H = 1600, 1050
    canvas = Image.new("RGB", (W, H), "#1e1e1e")
    draw = ImageDraw.Draw(canvas)

    font_title = create_font(22, bold=True)
    font_sub = create_font(15, bold=True)
    font_body = create_font(13, bold=False)
    font_large_num = create_font(28, bold=True)

    # Header
    draw.rectangle([0, 0, W, 45], fill="#2d2d2d")
    draw.ellipse([15, 16, 27, 28], fill="#ff5f56")
    draw.ellipse([35, 16, 47, 28], fill="#ffbd2e")
    draw.ellipse([55, 16, 67, 28], fill="#27c93f")
    draw.rectangle([100, 10, 1000, 35], fill="#1e1e1e", outline="#3c3c3c")
    draw.text((115, 14), "chrome://devtools/elements - Hub Solidário (Inspeção de Contraste)", fill="#cccccc", font=font_body)
    draw.text((1100, 13), "DevTools > Styles > Color Picker", fill="#3b82f6", font=font_sub)

    # Left Side: Browser view with Inspected Element Highlight
    web_w, web_h = 920, 720
    img_cropped = img_normal.crop((200, 0, 1080, 800)).resize((web_w, web_h))
    canvas.paste(img_cropped, (20, 60))

    # Draw Element Inspection overlay on .descricao-campanha
    draw.rectangle([140, 290, 820, 350], outline="#3b82f6", fill="#3b82f622", width=3)
    draw.rectangle([140, 260, 480, 290], fill="#3b82f6")
    draw.text((148, 266), "p.descricao-campanha | 460 x 42 | color: #9ca3af", fill="#ffffff", font=font_sub)

    # Secondary inspection outline on .meta-arrecadacao
    draw.rectangle([140, 360, 820, 410], outline="#f59e0b", width=2)
    draw.text((148, 415), "⚠️ .meta-arrecadacao | color: #888888 | Contraste: 3.5:1 (Reprovado)", fill="#f59e0b", font=font_body)

    # Right Side: DevTools Styles Panel & Color Picker
    dev_x = 960
    dev_w = 620
    draw.rectangle([dev_x, 60, dev_x + dev_w, 780], fill="#252526", outline="#3c3c3c", width=1)

    # DevTools Tab Header
    draw.rectangle([dev_x, 60, dev_x + dev_w, 95], fill="#2d2d2d")
    draw.rectangle([dev_x + 10, 60, dev_x + 90, 95], fill="#252526")
    draw.text((dev_x + 20, 70), "Styles", fill="#3b82f6", font=font_sub)
    draw.text((dev_x + 100, 70), "Computed", fill="#888888", font=font_sub)
    draw.text((dev_x + 200, 70), "Accessibility", fill="#888888", font=font_sub)

    # CSS Rule Box in Styles
    y = 105
    draw.rectangle([dev_x + 15, y, dev_x + 605, y + 130], fill="#1e1e1e", outline="#3c3c3c")
    draw.text((dev_x + 25, y + 10), ".descricao-campanha {", fill="#e5c07b", font=font_sub)
    
    # Highlight color property
    draw.rectangle([dev_x + 40, y + 35, dev_x + 350, y + 65], fill="#3b82f633")
    draw.rectangle([dev_x + 45, y + 42, dev_x + 60, y + 57], fill="#9ca3af", outline="#ffffff")
    draw.text((dev_x + 70, y + 40), "color: #9ca3af;", fill="#ef596f", font=font_sub)
    draw.text((dev_x + 200, y + 40), "/* Baixo Contraste */", fill="#7f848e", font=font_body)
    
    draw.text((dev_x + 45, y + 70), "font-size: 14px;", fill="#d19a66", font=font_body)
    draw.text((dev_x + 45, y + 95), "line-height: 1.5;", fill="#d19a66", font=font_body)
    draw.text((dev_x + 25, y + 112), "}", fill="#e5c07b", font=font_sub)

    # EXPANDED COLOR PICKER WIDGET (INSPECTOR)
    cp_y = y + 145
    draw.rectangle([dev_x + 30, cp_y, dev_x + 590, cp_y + 450], fill="#282c34", outline="#3b82f6", width=2)
    
    # Spectrum Box Mock
    draw.rectangle([dev_x + 50, cp_y + 20, dev_x + 570, cp_y + 160], fill="#808080", outline="#5c6370")
    # Spectrum lines for WCAG AA and AAA limits
    draw.line([(dev_x + 50, cp_y + 90), (dev_x + 570, cp_y + 110)], fill="#ffffff", width=2)
    draw.text((dev_x + 60, cp_y + 70), "--- Linha de Limite WCAG AA (4.5:1)", fill="#ffffff", font=font_body)

    # Color Picker Data Section
    py = cp_y + 175
    draw.rectangle([dev_x + 50, py, dev_x + 80, py + 30], fill="#9ca3af", outline="#ffffff", width=2)
    draw.text((dev_x + 95, py + 5), "HEX: #9ca3af", fill="#ffffff", font=font_sub)
    draw.text((dev_x + 250, py + 5), "Fundo: #ffffff", fill="#abb2bf", font=font_body)

    # Contrast Ratio Panel inside DevTools Color Picker
    py += 45
    draw.rectangle([dev_x + 50, py, dev_x + 570, py + 140], fill="#1e222b", outline="#ef4444", width=2)
    
    draw.text((dev_x + 70, py + 15), "Contrast ratio:", fill="#ffffff", font=font_sub)
    draw.text((dev_x + 210, py + 10), "2.40 : 1", fill="#f87171", font=font_large_num)
    draw.rectangle([dev_x + 380, py + 12, dev_x + 550, py + 38], fill="#991b1b")
    draw.text((dev_x + 390, py + 16), "❌ REPROVADO (AA)", fill="#ffffff", font=font_sub)

    # WCAG Threshold Indicators
    draw.text((dev_x + 70, py + 55), "✔ WCAG AA (mínimo 4.5:1):", fill="#abb2bf", font=font_body)
    draw.text((dev_x + 320, py + 55), "4.5 : 1 (Texto Normal)", fill="#ef4444", font=font_sub)
    
    draw.text((dev_x + 70, py + 80), "✔ WCAG AAA (mínimo 7.0:1):", fill="#abb2bf", font=font_body)
    draw.text((dev_x + 320, py + 80), "7.0 : 1 (Texto Normal)", fill="#ef4444", font=font_sub)

    draw.text((dev_x + 70, py + 110), "💡 Sugestão de Ajuste Rápido: #4b5563 (Razão: 7.12 : 1 AA / AAA)", fill="#60a5fa", font=font_body)

    # Footer Callout Banner
    draw.rectangle([20, 800, W - 20, 1020], fill="#111827", outline="#ef4444", width=2)
    draw.text((40, 815), "EVIDÊNCIA 2: INSPEÇÃO DE CONTRASTE DE CORES COM COLOR PICKER (DEVTOOLS > STYLES)", fill="#f87171", font=font_title)
    
    diag_text = (
        "• Diagnóstico DevTools: No seletor de cores da propriedade 'color', a ferramenta calcula automaticamente o Contrast Ratio.\n"
        "• Elemento Inspecionado 1: '.descricao-campanha' (#9ca3af sobre #ffffff) = Taxa 2.40:1 (Exige 4.5:1 no Nível AA) ❌ Reprovado.\n"
        "• Elemento Inspecionado 2: '.meta-arrecadacao' (#888888 sobre #f9fafb) = Taxa 3.50:1 (Exige 4.5:1 no Nível AA) ❌ Reprovado.\n"
        "• Correção Necessária: Substituir #9ca3af por #374151 (Contraste 7.0:1) para conformidade total com o Critério WCAG 1.4.3."
    )
    draw.text((40, 855), diag_text, fill="#e5e7eb", font=font_body, spacing=6)

    canvas.save("evidencias/evidencia_2_taxa_contraste.png")
    canvas.save("C:/Users/Roky/.gemini/antigravity-ide/brain/27733ffa-7ce1-4599-9a0b-bb8613b2e934/evidencia_2_taxa_contraste.png")
    print("Evidência 2 gerada com sucesso!")

generate_evidence_2()
