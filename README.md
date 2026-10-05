# Repositório de Técnicas de Inspeção de Acessibilidade no Navegador

Este repositório contém a realização prática e os artefatos de evidência da atividade **"Técnicas de Inspeção de Acessibilidade no Navegador"**, embasada na norma **ISO/IEC 25010** e nas diretrizes **WCAG 2.1 (Nível AA)**.

---

## 📸 Evidências Exigidas e Geradas

As três evidências solicitadas foram inspecionadas via DevTools e salvas na pasta [`evidencias/`](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/evidencias/):

1. **Emulando Deficiências Visuais:**  
   - [evidencia_1_emulando_deficiencias_visuais.png](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/evidencias/evidencia_1_emulando_deficiencias_visuais.png)  
   - *Validação do selo de urgência `.status-badge` sob simulação de Protanopia e visão embaçada (DevTools > Rendering).*

2. **Inspeção e Cálculo da Taxa de Contraste com o Color Picker:**  
   - [evidencia_2_taxa_contraste.png](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/evidencias/evidencia_2_taxa_contraste.png)  
   - *Cálculo automático de taxa de contraste no Color Picker dos elementos `.descricao-campanha` (2.40:1) e `.meta-arrecadacao` (3.50:1).*

3. **Ordem e Fluxo de Tabulação (`tabindex` e Foco):**  
   - [evidencia_3_ordem_tabulacao_foco.png](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/evidencias/evidencia_3_ordem_tabulacao_foco.png)  
   - *Inspeção da inversão de fluxo causada por `tabindex` positivo (`"1"` e `"2"`), ausência do anel de foco (`*:focus { outline: none }`) e exclusão de elementos não-semânticos (`<div class="btn-acao">`).*

---

## 📁 Arquivos do Projeto

- [`painel-campanha.html`](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/painel-campanha.html) - Código fornecido com as não-conformidades intencionais para auditoria.
- [`painel-campanha-corrigido.html`](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/painel-campanha-corrigido.html) - Versão refatorada e totalmente conforme com as diretrizes WCAG 2.1 Nível AA.
- [`evidencias/`](file:///c:/Users/Roky/ATREPO-Tecnicas-de-Inspecao-de-Acessibilidade-no-Navegador/evidencias/) - Pasta contendo todas as imagens de alta resolução capturadas.
