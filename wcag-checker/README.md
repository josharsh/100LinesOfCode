# WCAG Contrast Checker - Chrome Extension

> A lightweight Chrome extension for checking WCAG color contrast compliance, built as part of the [100LinesOfCode](https://github.com/josharsh/100LinesOfCode) project.

This browser extension provides an interactive way for developers and designers to check color contrast ratios and ensure their designs meet WCAG accessibility standards - right from their browser toolbar.

## Features

* **Triple Color Selection Methods:**
  * 🎨 Interactive color pickers
  * 💧 EyeDropper tool to pick colors directly from any webpage
  * ⌨️ Manual input (HEX or RGB format)
* **Real-time Contrast Calculation:** Instantly see the contrast ratio between your selected colors
* **WCAG Compliance Check:** Automatic validation against WCAG AA (4.5:1) and AAA (7:1) standards
* **Multiple Format Support:** Get and input color values in both HEX and RGB formats
* **Live Preview:** See exactly how your text will look with the selected color combination
* **Copy to Clipboard:** One-click copy functionality for all color values
* **Compact Design:** Optimized popup interface (400px width) perfect for quick checks
* **Accessible Design:** Built with accessibility in mind, following best practices

## Project Structure

```txt
wcag-checker/
├── index.html          # Main popup HTML structure
├── style.css           # Optimized styling with clean organization
├── script.js           # JavaScript logic (under 100 lines!)
├── manifest.json       # Chrome extension manifest v3
└── README.md           # Project documentation
```

## Installation

### Option 1: Install from Source (Developer Mode)

1. Clone or download this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top-right corner)
4. Click "Load unpacked"
5. Select the `wcag-checker` folder
6. The extension icon will appear in your toolbar!

### Option 2: Test Locally (Without Installing)

```bash
# Navigate to the project folder
cd wcag-checker

# Start a local server
python -m http.server 8000
# or
npx http-server
```

Then open your browser and navigate to `http://localhost:8000`

## How to Use

1. **Click the extension icon** in your Chrome toolbar
2. **Choose your colors** using one of three methods:
   * Click the color picker boxes
   * Click "Pick from Page" to use the EyeDropper on any visible color
   * Type directly in the HEX (`#FF5733`) or RGB (`rgb(255, 87, 51)`) fields
3. **View instant results:**
   * Contrast ratio displayed prominently
   * PASS/FAIL status for WCAG AA and AAA standards
   * Live preview of text appearance
4. **Copy values** with one click for use in your projects

## WCAG Standards

* **WCAG AA (4.5:1):** Minimum contrast ratio for normal text, required for most web content
* **WCAG AAA (7:1):** Enhanced contrast ratio for the highest level of accessibility

## Tech Stack

* **HTML5:** Semantic structure
* **CSS3:** Modern styling with Flexbox layout
* **Vanilla JavaScript:** All logic in under 100 lines (96 lines)
* **Chrome Extension APIs:** Manifest V3, EyeDropper API
* **Web APIs:** Clipboard API for copy functionality

## Browser Support

Requires:

* Chrome 95+ (for EyeDropper API)
* Clipboard API support
* ES6+ JavaScript features

## Permissions

* `activeTab`: Required for EyeDropper functionality to pick colors from the current page
* `scripting`: Required for extension popup interaction

---

## WCAG Contrast Checker - Extensão Chrome

> Uma extensão leve para Chrome que verifica a conformidade de contraste de cores WCAG, construída como parte do projeto [100LinesOfCode](https://github.com/josharsh/100LinesOfCode).

Esta extensão oferece uma forma interativa para desenvolvedores e designers verificarem taxas de contraste de cores e garantir que seus designs atendem aos padrões de acessibilidade WCAG - direto da barra de ferramentas do navegador.

## Funcionalidades

* **Três Métodos de Seleção de Cores:**
  * 🎨 Seletores de cores interativos
  * 💧 Ferramenta conta-gotas para pegar cores diretamente de qualquer página
  * ⌨️ Entrada manual (formato HEX ou RGB)
* **Cálculo de Contraste em Tempo Real:** Veja instantaneamente a taxa de contraste entre suas cores
* **Verificação de Conformidade WCAG:** Validação automática contra padrões WCAG AA (4.5:1) e AAA (7:1)
* **Suporte a Múltiplos Formatos:** Obtenha e insira valores de cores em formatos HEX e RGB
* **Visualização ao Vivo:** Veja exatamente como seu texto ficará com a combinação de cores
* **Copiar para Área de Transferência:** Funcionalidade de cópia com um clique
* **Design Compacto:** Interface otimizada (400px de largura) perfeita para verificações rápidas
* **Design Acessível:** Construído pensando em acessibilidade

## Estrutura do Projeto

```txt
wcag-checker/
├── index.html          # Estrutura HTML do popup principal
├── style.css           # Estilos otimizados com organização limpa
├── script.js           # Lógica JavaScript (menos de 100 linhas!)
├── manifest.json       # Manifest da extensão Chrome v3
└── README.md           # Documentação do projeto
```

## Instalação

### Opção 1: Instalar do Código Fonte (Modo Desenvolvedor)

1. Clone ou baixe este repositório
2. Abra o Chrome e navegue até `chrome://extensions/`
3. Ative o "Modo do desenvolvedor" (toggle no canto superior direito)
4. Clique em "Carregar sem compactação"
5. Selecione a pasta `wcag-checker`
6. O ícone da extensão aparecerá na sua barra de ferramentas!

### Opção 2: Testar Localmente (Sem Instalar)

```bash
# Navegue até a pasta do projeto
cd wcag-checker

# Inicie um servidor local
python -m http.server 8000
# ou
npx http-server
```

Em seguida, abra seu navegador e navegue até `http://localhost:8000`

## Como Usar

1. **Clique no ícone da extensão** na barra de ferramentas do Chrome
2. **Escolha suas cores** usando um dos três métodos:
   * Clique nas caixas de seleção de cor
   * Clique em "Pick from Page" para usar o conta-gotas em qualquer cor visível
   * Digite diretamente nos campos HEX (`#FF5733`) ou RGB (`rgb(255, 87, 51)`)
3. **Veja os resultados instantâneos:**
   * Taxa de contraste exibida de forma proeminente
   * Status PASS/FAIL para padrões WCAG AA e AAA
   * Pré-visualização ao vivo da aparência do texto
4. **Copie valores** com um clique para usar em seus projetos

## Padrões WCAG

* **WCAG AA (4.5:1):** Taxa de contraste mínima para texto normal, necessária para a maioria dos conteúdos web
* **WCAG AAA (7:1):** Taxa de contraste aprimorada para o mais alto nível de acessibilidade

## Stack Tecnológica

* **HTML5:** Estrutura semântica
* **CSS3:** Estilização moderna com layout Flexbox
* **JavaScript Vanilla:** Toda a lógica em menos de 100 linhas (96 linhas)
* **APIs de Extensão Chrome:** Manifest V3, EyeDropper API
* **Web APIs:** API Clipboard para funcionalidade de cópia

## Suporte de Navegadores

Requer:

* Chrome 95+ (para EyeDropper API)
* Suporte à API Clipboard
* Recursos JavaScript ES6+

## Permissões

* `activeTab`: Necessária para a funcionalidade do conta-gotas pegar cores da página atual
* `scripting`: Necessária para interação do popup da extensão
