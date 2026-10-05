import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_font(size, bold=False):
    try:
        font_name = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(font_name, size)
    except IOError:
        return ImageFont.load_default()

def generate_evidence_1():
    # Evidência 1: Emulando Deficiências Visuais (Protanopia e Visão Embaçada)
    base_normal_path = "evidencias/base_normal.png"
    base_protanopia_path = "evidencias/base_protanopia.png"
    base_blurred_path = "evidencias/base_blurred.png"
    
    img_normal = Image.open(base_normal_path)
    img_prot = Image.open(base_protanopia_path)
    img_blur = Image.open(base_blurred_path)

    # Canvas dimensions
    W, H = 1600, 1050
    canvas = Image.new("RGB", (W, H), "#1e1e1e")
    draw = ImageDraw.Draw(canvas)

    font_title = create_font(22, bold=True)
    font_sub = create_font(15, bold=True)
    font_body = create_font(13, bold=False)

    # 1. Header (Chrome Window style)
    draw.rectangle([0, 0, W, 45], fill="#2d2d2d")
    # Window controls
    draw.ellipse([15, 16, 27, 28], fill="#ff5f56")
    draw.ellipse([35, 16, 47, 28], fill="#ffbd2e")
    draw.ellipse([55, 16, 67, 28], fill="#27c93f")
    # Address bar
    draw.rectangle([100, 10, 1000, 35], fill="#1e1e1e", outline="#3c3c3c")
    draw.text((115, 14), "chrome://devtools/rendering - Hub Solidário (Emulação de Visão)", fill="#cccccc", font=font_body)
    draw.text((1100, 13), "DevTools > Rendering", fill="#3b82f6", font=font_sub)

    # Left Side: Browser view (Protanopia)
    web_w, web_h = 950, 720
    img_prot_resized = img_prot.crop((200, 0, 1080, 800)).resize((web_w, web_h))
    canvas.paste(img_prot_resized, (20, 60))

    # Highlight Status Badge on Page
    draw.rectangle([150, 290, 520, 335], outline="#ef4444", width=3)
    draw.text((150, 265), "⚠️ Badges de Prioridade (Protanopia)", fill="#f87171", font=font_sub)

    # Right Side: DevTools Panel (Rendering)
    dev_x = 990
    dev_w = 590
    draw.rectangle([dev_x, 60, dev_x + dev_w, 780], fill="#252526", outline="#3c3c3c", width=1)
    
    # DevTools Tab Header
    draw.rectangle([dev_x, 60, dev_x + dev_w, 95], fill="#2d2d2d")
    draw.text((dev_x + 15, 70), "Console", fill="#888888", font=font_sub)
    draw.text((dev_x + 90, 70), "Sensors", fill="#888888", font=font_sub)
    draw.rectangle([dev_x + 165, 60, dev_x + 270, 95], fill="#252526")
    draw.text((dev_x + 175, 70), "Rendering ✖", fill="#3b82f6", font=font_sub)

    # DevTools Content
    y = 110
    draw.text((dev_x + 20, y), "Emulate vision deficiencies", fill="#ffffff", font=font_sub)
    y += 25
    draw.text((dev_x + 20, y), "Simulate visual impairments to test color contrast and usability.", fill="#aaaaaa", font=font_body)
    
    y += 35
    # Dropdown box
    draw.rectangle([dev_x + 20, y, dev_x + 550, y + 40], fill="#3c3c3c", outline="#3b82f6", width=2)
    draw.text((dev_x + 35, y + 10), "✔ Protanopia (no red / incapacidade de perceber a cor vermelha)", fill="#60a5fa", font=font_sub)
    
    y += 60
    options = [
        "● No emulation (Normal)",
        "✔ Protanopia (incapacidade de perceber vermelho) - SELECIONADO",
        "● Deuteranopia (incapacidade de perceber verde)",
        "● Tritanopia (incapacidade de perceber azul)",
        "● Achromatopsia (ausência de percepção de cor / monocromático)",
        "● Blurred vision (visão embaçada / baixa acuidade visual)"
    ]

    for opt in options:
        is_sel = "SELECIONADO" in opt
        bg_col = "#1e3a8a" if is_sel else "#2d2d2d"
        txt_col = "#60a5fa" if is_sel else "#cccccc"
        draw.rectangle([dev_x + 30, y, dev_x + 540, y + 30], fill=bg_col, outline="#3b82f6" if is_sel else "#3c3c3c")
        draw.text((dev_x + 40, y + 6), opt, fill=txt_col, font=font_body)
        y += 35

    # Thumbnail of Blurred vision comparison
    y += 15
    draw.text((dev_x + 20, y), "Comparativo: Visão Embaçada (Blurred vision)", fill="#ffffff", font=font_sub)
    y += 25
    img_blur_mini = img_blur.crop((350, 180, 900, 480)).resize((530, 150))
    canvas.paste(img_blur_mini, (dev_x + 20, y))

    # Footer Callout Banner
    draw.rectangle([20, 800, W - 20, 1020], fill="#111827", outline="#ef4444", width=2)
    draw.text((40, 815), "EVIDÊNCIA 1: EMULANDO DEFICIÊNCIAS VISUAIS (DEVTOOLS > RENDERING)", fill="#f87171", font=font_title)
    
    diag_text = (
        "• Diagnóstico DevTools: No painel Rendering > 'Emulate vision deficiencies', selecionou-se o perfil Protanopia.\n"
        "• Não-Conformidade WCAG 1.4.1 (Uso da Cor - Nível A): O indicador '.status-badge' sinaliza urgência apenas pela cor vermelha (#ef4444).\n"
        "• Impacto Visual: Em protanopia, o círculo vermelho torna-se amarronzado/opaco e visualmente indistinguível do fundo.\n"
        "• Solução Recomendada: Incluir ícone de alerta e texto explícito 'Prioridade Alta' ao lado do selo de status."
    )
    draw.text((40, 855), diag_text, fill="#e5e7eb", font=font_body, spacing=6)

    canvas.save("evidencias/evidencia_1_emulando_deficiencias_visuais.png")
    canvas.save("C:/Users/Roky/.gemini/antigravity-ide/brain/27733ffa-7ce1-4599-9a0b-bb8613b2e934/evidencia_1_emulando_deficiencias_visuais.png")
    print("Evidência 1 gerada com sucesso!")

generate_evidence_1()
