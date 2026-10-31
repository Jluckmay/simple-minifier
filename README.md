# ⚡ Simple Minifier / Minificador Simples

🌍 Choose your language / Escolha seu idioma:
* [🇺🇸 English](#-english)
* [🇧🇷 Português (Brasil)](#-português-brasil)

---

## 🇺🇸 English

A modern, minimalist, and accessible web tool for minifying code directly in the browser. Simple Minifier processes files locally using Web Workers, ensuring high speed and privacy (your files are never uploaded to a server).

### ✨ Features

* **Smart Multi-Language Support:**
  * **JavaScript:** Uses the native *Terser* engine or a state-machine "Turbo Mode" for extreme obfuscation and compression.
  * **CSS:** Regex-based engine to strip comments and redundant spaces.
  * **JSON:** Native validation and compression (safe against corrupted files).
  * **Python & YAML:** Safe mode (`safeMinify`) that preserves structural indentation and only removes trailing whitespaces and empty lines, preventing logical code breakage.
  * **Generic Fallback:** Basic whitespace stripping for HTML, TXT, and other formats.
* **Accessibility (a11y):** Fully compatible with screen readers (`aria-live`, `aria-label` support), keyboard navigation, and high-contrast visual indicators.
* **Internationalization (i18n):** Instant toggling between **English (EN-US)** and **Portuguese (PT-BR)**.
* **View Modes:** Support for **Dark Mode** and **Light Mode** with a minimalist palette (auto-saves preference in `localStorage`).
* **Drag & Drop:** Unified area to drag files or paste code directly.

### 🗂️ Project Structure

Based on the repository structure, the project contains the following main files:

* `index.html`: The main web application containing the UI, Web Worker logic, theme CSS, and i18n dictionary.
* `minifier.py`: Auxiliary Python script for command-line/backend minification (depending on your local setup).
* `exemplo.js`: Example file used for testing obfuscation and compression.

### 🚀 How to Use

#### Local Web Interface
1. Double-click the `index.html` file to open it in any modern browser (Chrome, Edge, Firefox, Safari).
2. Drag and drop a file (e.g., `exemplo.js`) onto the dashed area, or simply paste your code into the text box.
3. Click **Minify Code**.
4. Download the optimized file (e.g., `exemplo.min.js`).

#### Public Web Page
Access the webpage: https://jluckmay.github.io/smart-minifier/ 

### 🛠️ Technologies Used

* **HTML5 / CSS3:** Semantic structure and CSS variables (`:root`) for dynamic theming.
* **Vanilla JavaScript:** No heavy framework dependencies.
* **Web Workers:** For asynchronous processing on large files (prevents UI freezing).
* **Terser (via CDN):** For AST building and deep JavaScript obfuscation.

---

## 🇧🇷 Português (Brasil)

Uma ferramenta web moderna, minimalista e acessível para minificação de código direto no navegador. O Simple Minifier processa arquivos localmente utilizando Web Workers, garantindo alta velocidade e segurança (seus arquivos nunca são enviados para um servidor).

### ✨ Funcionalidades

* **Suporte Multi-Linguagem Inteligente:**
  * **JavaScript:** Utiliza o motor *Terser* nativo ou um "Modo Turbo" de máquina de estados para ofuscação e compressão extrema.
  * **CSS:** Motor baseado em Regex para limpar comentários e espaços redundantes.
  * **JSON:** Validação e compressão nativa (segura contra arquivos corrompidos).
  * **Python & YAML:** Modo de segurança (`safeMinify`) que preserva a indentação estrutural e remove apenas quebras de linha/espaços inúteis, impedindo a quebra lógica do código.
  * **Fallback Genérico:** Suporte básico para HTML, TXT e outros formatos.
* **Acessibilidade (a11y):** Totalmente compatível com leitores de tela (suporte a `aria-live`, `aria-label`), navegação por teclado e indicadores visuais de alto contraste.
* **Internacionalização (i18n):** Alternância instantânea entre **Português (PT-BR)** e **Inglês (EN-US)**.
* **Modos de Visualização:** Suporte a **Dark Mode** e **Light Mode** com paleta minimalista (salvamento automático de preferência no `localStorage`).
* **Drag & Drop:** Área unificada para arrastar arquivos ou colar texto diretamente.

### 🗂️ Estrutura do Projeto

Conforme estruturado no repositório, o projeto contém os seguintes arquivos principais:

* `index.html`: A aplicação web principal contendo toda a interface, lógicas de Web Worker, CSS de tema e dicionário i18n.
* `minifier.py`: Script auxiliar em Python para minificação via linha de comando/backend (conforme sua estrutura local).
* `exemplo.js`: Arquivo de exemplo utilizado para realizar testes de ofuscação e compressão.

### 🚀 Como Usar

#### Interface Web Local
1. Dê um clique duplo no arquivo `index.html` para abri-lo em qualquer navegador moderno (Chrome, Edge, Firefox, Safari).
2. Arraste e solte um arquivo (ex: `exemplo.js`) sobre a área pontilhada, ou simplesmente cole seu código na caixa de texto.
3. Clique em **Minificar Código**.
4. Faça o download do arquivo otimizado (ex: `exemplo.min.js`).

#### Página Publica
Acesse a seguinte página: https://jluckmay.github.io/simple-minifier/

### 🛠️ Tecnologias Utilizadas

* **HTML5 / CSS3:** Estrutura semântica e variáveis CSS (`:root`) para temas dinâmicos.
* **Vanilla JavaScript:** Sem dependências pesadas de framework.
* **Web Workers:** Para processamento assíncrono em arquivos pesados (evita travamentos na interface).
* **Terser (via CDN):** Para construção de AST e ofuscação profunda de JavaScript.