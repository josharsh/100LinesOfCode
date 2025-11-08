# WCAG Contrast Checker

> A simple, lightweight WCAG contrast checker built as part of the [100LinesOfCode](https://github.com/josharsh/100LinesOfCode) project.

This tool provides an interactive way for developers and designers to check color contrast ratios and ensure their designs meet WCAG accessibility standards.

## Features

* **Dual Color Selection:** Choose text and background colors using interactive color pickers
* **Real-time Contrast Calculation:** Instantly see the contrast ratio between your selected colors
* **WCAG Compliance Check:** Automatic validation against WCAG AA (4.5:1) and AAA (7:1) standards
* **Multiple Format Support:** Get color values in both HEX and RGB formats
* **Live Preview:** See exactly how your text will look with the selected color combination
* **Copy to Clipboard:** One-click copy functionality for all color values
* **Accessible Design:** Built with accessibility in mind, following best practices

## Project Structure

```
wcag-checker/
├── index.html          # Main HTML structure
├── style.css           # Styling (organized with clear comments)
├── script.js           # JavaScript logic (under 100 lines)
└── README.md           # Project documentation
```

## How to Run

### Option 1: Direct File Opening
1. Clone or download this repository
2. Navigate to the `wcag-checker` folder
3. Open `index.html` in your web browser

### Option 2: Using a Local Server
```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (with http-server)
npx http-server

# Using PHP
php -S localhost:8000
```

Then open your browser and navigate to `http://localhost:8000`

## How It Works

1. **Select Colors:** Use the color pickers to choose your text and background colors
2. **View Results:** The tool automatically calculates the contrast ratio using the WCAG formula
3. **Check Compliance:** See if your color combination passes WCAG AA and AAA standards
4. **Preview:** View a live preview of how your text will look
5. **Copy Values:** Click the copy buttons to get HEX or RGB values for use in your projects

## WCAG Standards

- **WCAG AA (4.5:1):** Minimum contrast ratio for normal text, required for most web content
- **WCAG AAA (7:1):** Enhanced contrast ratio for the highest level of accessibility

## Tech Stack

* **HTML5:** Semantic structure with accessibility in mind
* **CSS3:** Modern styling with Flexbox layout and custom properties
* **Vanilla JavaScript:** All logic implemented in under 100 lines
* **Web APIs:** Clipboard API for copy functionality

## Browser Support

Works on all modern browsers that support:
- `<input type="color">`
- Clipboard API
- ES6+ JavaScript features

---

# WCAG Contrast Checker

> Uma ferramenta simples e leve para verificação de contraste WCAG, construída como parte do projeto [100LinesOfCode](https://github.com/josharsh/100LinesOfCode).

Esta ferramenta oferece uma forma interativa para desenvolvedores e designers verificarem a taxa de contraste de cores e garantir que seus designs atendem aos padrões de acessibilidade WCAG.

## Funcionalidades

* **Seleção Dupla de Cores:** Escolha cores de texto e fundo usando seletores de cores interativos
* **Cálculo de Contraste em Tempo Real:** Veja instantaneamente a taxa de contraste entre suas cores selecionadas
* **Verificação de Conformidade WCAG:** Validação automática contra os padrões WCAG AA (4.5:1) e AAA (7:1)
* **Suporte a Múltiplos Formatos:** Obtenha valores de cores nos formatos HEX e RGB
* **Visualização ao Vivo:** Veja exatamente como seu texto ficará com a combinação de cores selecionada
* **Copiar para Área de Transferência:** Funcionalidade de cópia com um clique para todos os valores de cores
* **Design Acessível:** Construído pensando em acessibilidade, seguindo as melhores práticas

## Estrutura do Projeto

```
wcag-checker/
├── index.html          # Estrutura HTML principal
├── style.css           # Estilos (organizados com comentários claros)
├── script.js           # Lógica JavaScript (menos de 100 linhas)
└── README.md           # Documentação do projeto
```

## Como Executar

### Opção 1: Abertura Direta do Arquivo
1. Clone ou baixe este repositório
2. Navegue até a pasta `wcag-checker`
3. Abra o arquivo `index.html` no seu navegador

### Opção 2: Usando um Servidor Local
```bash
# Usando Python 3
python -m http.server 8000

# Usando Node.js (com http-server)
npx http-server

# Usando PHP
php -S localhost:8000
```

Em seguida, abra seu navegador e navegue até `http://localhost:8000`

## Como Funciona

1. **Selecione as Cores:** Use os seletores de cores para escolher suas cores de texto e fundo
2. **Visualize os Resultados:** A ferramenta calcula automaticamente a taxa de contraste usando a fórmula WCAG
3. **Verifique a Conformidade:** Veja se sua combinação de cores passa nos padrões WCAG AA e AAA
4. **Pré-visualize:** Veja uma prévia ao vivo de como seu texto ficará
5. **Copie os Valores:** Clique nos botões de copiar para obter valores HEX ou RGB para usar em seus projetos

## Padrões WCAG

- **WCAG AA (4.5:1):** Taxa de contraste mínima para texto normal, necessária para a maioria dos conteúdos web
- **WCAG AAA (7:1):** Taxa de contraste aprimorada para o mais alto nível de acessibilidade

## Stack Tecnológica

* **HTML5:** Estrutura semântica pensando em acessibilidade
* **CSS3:** Estilização moderna com layout Flexbox e propriedades customizadas
* **JavaScript Vanilla:** Toda a lógica implementada em menos de 100 linhas
* **Web APIs:** API Clipboard para funcionalidade de cópia

## Suporte de Navegadores

Funciona em todos os navegadores modernos que suportam:
- `<input type="color">`
- API Clipboard
- Recursos JavaScript ES6+