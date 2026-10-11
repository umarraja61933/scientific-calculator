import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Scientific Calculator - Amna Hafeez",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            max-width: 900px;
            padding: 1rem 0.6rem 1rem;
        }
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 12% 18%, rgba(236, 72, 153, 0.38), transparent 28%),
                radial-gradient(circle at 88% 78%, rgba(34, 211, 238, 0.34), transparent 30%),
                linear-gradient(125deg, #07152f, #102b58, #0b3150, #35102f);
            background-size: 180% 180%;
            animation: gradientAnimation 18s ease infinite;
            min-height: 100vh;
        }
        [data-testid="stHeader"] {
            background: transparent;
        }
        [data-testid="stMain"] {
            background: transparent;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

calculator_html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* { box-sizing: border-box; }

html, body {
    margin: 0;
    padding: 0;
    background: transparent;
    color: #f8fafc;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

body {
    padding: 5px;
}

/* Main calculator card */
.calculator {
    position: relative;
    max-width: 600px;
    margin: 0 auto;
    padding: 22px 24px 18px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 26px;
    background: linear-gradient(145deg, rgba(10, 31, 64, 0.97), rgba(12, 20, 48, 0.98));
    backdrop-filter: blur(25px);
    box-shadow: 
        0 30px 60px -15px rgba(3, 5, 25, 0.72),
        0 0 42px rgba(34, 211, 238, 0.25),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
    overflow: hidden;
    isolation: isolate;
    animation: cardFloatIn 0.75s ease-out both;
}
@keyframes cardFloatIn {
    from { opacity: 0; transform: translateY(12px) scale(0.99); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.calculator::before {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    top: -120px;
    right: -60px;
    border-radius: 50%;
    background: rgba(236, 72, 153, 0.34);
    filter: blur(50px);
    pointer-events: none;
}

.calculator::after {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    bottom: -120px;
    left: -60px;
    border-radius: 50%;
    background: rgba(56, 189, 248, 0.28);
    filter: blur(50px);
    pointer-events: none;
}

/* Header */
.header {
    position: relative;
    z-index: 1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 14px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.brand-icon {
    display: grid;
    place-items: center;
    width: 46px;
    height: 46px;
    border: 1px solid rgba(103, 232, 249, 0.72);
    border-radius: 13px;
    background: linear-gradient(135deg, #22d3ee, #ec4899);
    color: #ffffff;
    font-size: 24px;
    font-weight: 800;
    box-shadow: 0 4px 20px rgba(34, 211, 238, 0.42);
}

.brand-copy h1 {
    margin: 0 0 2px;
    font-size: 20px;
    line-height: 1.2;
    letter-spacing: -.3px;
    color: #f8fafc;
    font-weight: 800;
}

.subtitle {
    color: #67e8f9;
    font-size: 14.5px;
    letter-spacing: .4px;
    font-weight: 700;
    margin-top: 3px;
}

.mode {
    border: 1px solid rgba(103, 232, 249, 0.55);
    background: rgba(9, 35, 72, 0.94);
    color: #67e8f9;
    padding: 8px 14px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .5px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

.mode:hover {
    border-color: rgba(103, 232, 249, 0.95);
    background: rgba(236, 72, 153, 0.25);
    transform: translateY(-1px);
}

/* Display */
.display {
    position: relative;
    z-index: 1;
    background: linear-gradient(145deg, #06172d, #0b2948 58%, #102b48);
    border: 1px solid rgba(103, 232, 249, 0.38);
    border-radius: 16px;
    padding: 12px 16px 10px;
    margin-bottom: 14px;
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.8), 0 4px 20px rgba(0,0,0,0.4);
}

.display::before {
    content: "EXPRESSION";
    position: absolute;
    top: 6px;
    left: 14px;
    color: #f9a8d4;
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

#expression {
    width: 100%;
    min-height: 38px;
    border: none;
    outline: none;
    background: transparent;
    color: #f1f5f9;
    font-size: 23px;
    text-align: right;
    padding: 12px 0 2px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
    caret-color: #67e8f9;
}

#expression::placeholder {
    color: #64748b;
}

.result-label {
    text-align: right;
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #f9a8d4;
    margin-top: 4px;
}

#result {
    min-height: 32px;
    text-align: right;
    font-size: 27px;
    line-height: 1.15;
    font-weight: 800;
    letter-spacing: -.4px;
    color: #67e8f9;
    overflow-wrap: anywhere;
    padding-top: 2px;
    text-shadow: 0 0 20px rgba(236, 72, 153, 0.48);
}

/* Section labels */
.section-label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 9px;
    font-weight: 800;
    color: #e0e7ff;
    letter-spacing: 1.5px;
    margin: 12px 2px 8px;
}

.section-label::before {
    content: "";
    width: 3.5px;
    height: 12px;
    border-radius: 4px;
    background: linear-gradient(#ec4899, #22d3ee);
}

/* Buttons */
.buttons {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 8px;
}

button.key {
    position: relative;
    min-width: 0;
    min-height: 44px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 11px;
    background: linear-gradient(145deg, rgba(13, 54, 91, 0.88), rgba(8, 28, 55, 0.97));
    color: #f1f5f9;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    user-select: none;
    box-shadow: 0 4px 8px -1px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: all 0.15s ease;
}

button.key:hover {
    transform: translateY(-2px);
    border-color: rgba(103, 232, 249, 0.72);
    background: linear-gradient(145deg, rgba(14, 116, 144, 0.84), rgba(30, 41, 78, 0.98));
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4), 0 0 14px rgba(103, 232, 249, 0.28);
}

button.key:active {
    transform: translateY(1px) scale(0.97);
}

button.function {
    background: linear-gradient(145deg, rgba(190, 24, 93, 0.32), rgba(8, 29, 56, 0.97));
    border-color: rgba(236, 72, 153, 0.48);
    color: #67e8f9;
    font-size: 14px;
    font-weight: 750;
}

button.function:hover {
    border-color: rgba(249, 168, 212, 0.85);
    background: linear-gradient(145deg, rgba(236, 72, 153, 0.58), rgba(10, 39, 70, 0.98));
}

button.operator {
    background: linear-gradient(145deg, rgba(8, 145, 178, 0.35), rgba(8, 29, 56, 0.97));
    border-color: rgba(103, 232, 249, 0.48);
    color: #67e8f9;
    font-size: 18px;
    font-weight: 750;
}

button.operator:hover {
    border-color: rgba(56, 189, 248, 0.8);
    background: linear-gradient(145deg, rgba(8, 145, 178, 0.62), rgba(10, 39, 70, 0.98));
}

button.danger {
    background: linear-gradient(145deg, rgba(190, 24, 93, 0.45), rgba(30, 22, 58, 0.96));
    border-color: rgba(251, 113, 133, 0.55);
    color: #fda4af;
    font-weight: 750;
}

button.danger:hover {
    border-color: rgba(251, 113, 133, 0.8);
    background: linear-gradient(145deg, rgba(225, 29, 72, 0.72), rgba(45, 27, 67, 0.98));
}

button.equal {
    background: linear-gradient(135deg, #ec4899, #0891b2);
    color: white;
    border-color: rgba(249, 168, 212, 0.85);
    font-size: 21px;
    font-weight: 800;
    box-shadow: 0 4px 18px rgba(236, 72, 153, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.35);
}

button.equal:hover {
    background: linear-gradient(135deg, #f472b6, #06b6d4);
    border-color: rgba(224, 231, 255, 1);
    box-shadow: 0 6px 20px rgba(236, 72, 153, 0.58), 0 0 18px rgba(34, 211, 238, 0.38);
}

/* Footer hints */
.footer-bar {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 14px;
}

.hint {
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 999px;
    background: rgba(9, 39, 70, 0.84);
    color: #e0e7ff;
    padding: 4px 10px;
    font-size: 8.5px;
}

.hint strong {
    color: #67e8f9;
}

/* Responsive adjustments */
@media (max-width: 520px) {
    .calculator {
        padding: 14px 12px 12px;
        border-radius: 18px;
    }
    .brand-copy h1 {
        font-size: 16px;
    }
    .buttons {
        gap: 6px;
    }
    button.key {
        min-height: 40px;
        font-size: 13px;
    }
    .footer-bar {
        display: none;
    }
}
</style>
</head>

<body>
<div class="calculator">
    <div class="header">
        <div class="brand">
            <div class="brand-icon">∑</div>
            <div class="brand-copy">
                <h1>Scientific Calculator</h1>
                <div class="subtitle">Design By: Amna Hafeez</div>
            </div>
        </div>
        <button class="mode" id="mode" type="button" title="Degrees mode">DEG</button>
    </div>

    <div class="display">
        <input id="expression" type="text"
            placeholder="Type formula or use buttons..."
            autocomplete="off" autocapitalize="off"
            spellcheck="false" aria-label="Calculator expression">
        <div class="result-label">RESULT</div>
        <div id="result" aria-live="polite">0</div>
    </div>

    <div class="section-label">SCIENTIFIC FUNCTIONS</div>
    <div class="buttons">
        <button class="key function" data-insert="sin(">sin</button>
        <button class="key function" data-insert="cos(">cos</button>
        <button class="key function" data-insert="tan(">tan</button>
        <button class="key function" data-insert="asin(">sin⁻¹</button>
        <button class="key function" data-insert="acos(">cos⁻¹</button>

        <button class="key function" data-insert="atan(">tan⁻¹</button>
        <button class="key function" data-insert="log(">log</button>
        <button class="key function" data-insert="ln(">ln</button>
        <button class="key function" data-insert="sqrt(">√</button>
        <button class="key function" data-insert="abs(">abs</button>

        <button class="key function" data-insert="^2">x²</button>
        <button class="key function" data-insert="^">xʸ</button>
        <button class="key function" data-insert="!">x!</button>
        <button class="key function" data-insert="pi">π</button>
        <button class="key function" data-insert="e">e</button>
    </div>

    <div class="section-label">BASIC OPERATIONS</div>
    <div class="buttons">
        <button class="key danger" data-action="clear">AC</button>
        <button class="key danger" data-action="delete">DEL</button>
        <button class="key operator" data-insert="(">(</button>
        <button class="key operator" data-insert=")">)</button>
        <button class="key operator" data-insert="%">%</button>

        <button class="key" data-insert="7">7</button>
        <button class="key" data-insert="8">8</button>
        <button class="key" data-insert="9">9</button>
        <button class="key operator" data-insert="/">÷</button>
        <button class="key operator" data-insert="*">×</button>

        <button class="key" data-insert="4">4</button>
        <button class="key" data-insert="5">5</button>
        <button class="key" data-insert="6">6</button>
        <button class="key operator" data-insert="-">−</button>
        <button class="key operator" data-insert="+">+</button>

        <button class="key" data-insert="1">1</button>
        <button class="key" data-insert="2">2</button>
        <button class="key" data-insert="3">3</button>
        <button class="key" data-insert="0">0</button>
        <button class="key" data-insert=".">.</button>

        <button class="key function" data-insert="e+">EXP</button>
        <button class="key function" data-action="sign">±</button>
        <button class="key function" data-action="square-root">√x</button>
        <button class="key equal" data-action="calculate" style="grid-column: span 2;">=</button>
    </div>

    <div class="footer-bar">
        <div class="hint"><strong>Enter</strong> Calculate</div>
        <div class="hint"><strong>Backspace</strong> Delete</div>
        <div class="hint"><strong>Esc</strong> Clear All</div>
        <div class="hint"><strong>Brackets Required</strong> for Functions</div>
    </div>
</div>

<script>
const input = document.getElementById("expression");
const output = document.getElementById("result");
const modeButton = document.getElementById("mode");

let degreeMode = true;
let lastAnswer = 0;

input.focus();

function insertAtCursor(text) {
    const start = input.selectionStart ?? input.value.length;
    const end = input.selectionEnd ?? input.value.length;
    const old = input.value;

    input.value = old.slice(0, start) + text + old.slice(end);
    input.focus();

    const pos = start + text.length;
    input.setSelectionRange(pos, pos);
    output.textContent = "Ready";
}

function clearAll() {
    input.value = "";
    output.textContent = "0";
    input.focus();
}

function factorial(n) {
    if (!Number.isInteger(n) || n < 0 || n > 170) {
        throw Error("Factorial needs an integer from 0 to 170.");
    }
    let answer = 1;
    for (let i = 2; i <= n; i++) answer *= i;
    return answer;
}

// Balance missing closing parentheses automatically
function balanceParentheses(expr) {
    let openCount = (expr.match(/\(/g) || []).length;
    let closeCount = (expr.match(/\)/g) || []).length;
    if (openCount > closeCount) {
        expr += ')'.repeat(openCount - closeCount);
    }
    return expr;
}

function calculate() {
    try {
        let expr = input.value.trim();
        if (!expr) {
            output.textContent = "Enter an expression";
            return;
        }

        expr = balanceParentheses(expr);

        // Convert display symbols to JS operators
        expr = expr.replace(/×/g, "*")
                   .replace(/÷/g, "/")
                   .replace(/π/g, "pi")
                   .replace(/−/g, "-")
                   .replace(/\^/g, "**");

        // Support postfix factorial
        for (let i = 0; i < 10 && /!/.test(expr); i++) {
            const before = expr;
            expr = expr.replace(/(\b\d+(?:\.\d+)?|\([^()]*\))!/g, "factorial($1)");
            if (before === expr) break;
        }

        if (expr.includes("!")) {
            throw Error("Use factorial on a number or bracketed value.");
        }

        const names = {
            sin: "sin", cos: "cos", tan: "tan",
            asin: "asin", acos: "acos", atan: "atan",
            log: "log", ln: "ln", sqrt: "sqrt", abs: "abs",
            pi: "pi", e: "e", factorial: "factorial"
        };

        const identifiers = expr.match(/[A-Za-z_]+/g) || [];
        for (const name of identifiers) {
            if (!(name in names)) throw Error("Unknown function or symbol: " + name);
        }

        // Percentage conversion
        expr = expr.replace(/(\d+(?:\.\d+)?|\([^()]*\))%/g, "($1/100)");

        // Implicit multiplication
        expr = expr.replace(/(\d|\))\s*(pi\b|e\b|sin\b|cos\b|tan\b|asin\b|acos\b|atan\b|log\b|ln\b|sqrt\b|abs\b|\()/g, "$1*$2");
        expr = expr.replace(/(pi\b|e\b|\))\s*(\d|\()/g, "$1*$2");

        if (!/^[0-9A-Za-z_+\-*/().,\s]*$/.test(expr)) {
            throw Error("Expression contains unsupported characters.");
        }

        const sin = x => Math.sin(degreeMode ? x * Math.PI / 180 : x);
        const cos = x => Math.cos(degreeMode ? x * Math.PI / 180 : x);
        const tan = x => {
            const angle = degreeMode ? x * Math.PI / 180 : x;
            if (Math.abs(Math.cos(angle)) < 1e-12) {
                throw Error("tan is undefined at this angle.");
            }
            return Math.tan(angle);
        };
        const asin = x => {
            const v = Math.asin(x);
            return degreeMode ? v * 180 / Math.PI : v;
        };
        const acos = x => {
            const v = Math.acos(x);
            return degreeMode ? v * 180 / Math.PI : v;
        };
        const atan = x => {
            const v = Math.atan(x);
            return degreeMode ? v * 180 / Math.PI : v;
        };
        const log = x => Math.log10(x);
        const ln = x => Math.log(x);
        const sqrt = x => Math.sqrt(x);
        const abs = x => Math.abs(x);
        const pi = Math.PI;
        const e = Math.E;

        const result = Function(
            "sin", "cos", "tan", "asin", "acos", "atan",
            "log", "ln", "sqrt", "abs", "pi", "e", "factorial",
            '"use strict"; return (' + expr + ');'
        )(sin, cos, tan, asin, acos, atan, log, ln, sqrt, abs, pi, e, factorial);

        if (typeof result !== "number" || !Number.isFinite(result)) {
            throw Error("Result is undefined or outside supported range.");
        }

        lastAnswer = result;
        output.textContent = Number(result.toPrecision(12)).toString();
    } catch (error) {
        output.textContent = error.message || "Invalid expression";
    }
}

// Button Click Handlers
document.querySelectorAll("[data-insert]").forEach(button => {
    button.addEventListener("click", () => insertAtCursor(button.dataset.insert));
});

document.querySelectorAll("[data-action]").forEach(button => {
    button.addEventListener("click", () => {
        const action = button.dataset.action;

        if (action === "clear") clearAll();
        if (action === "delete") {
            const start = input.selectionStart ?? input.value.length;
            const end = input.selectionEnd ?? input.value.length;

            if (start !== end) {
                input.setRangeText("", start, end, "start");
            } else if (start > 0) {
                input.setRangeText("", start - 1, start, "start");
            }
            input.focus();
            output.textContent = "Ready";
        }
        if (action === "calculate") calculate();
        if (action === "sign") {
            if (input.value.trim()) {
                insertAtCursor("*(-1)");
            } else {
                insertAtCursor("-");
            }
        }
        if (action === "square-root") insertAtCursor("sqrt(");
    });
});

modeButton.addEventListener("click", () => {
    degreeMode = !degreeMode;
    modeButton.textContent = degreeMode ? "DEG" : "RAD";
    modeButton.title = degreeMode ? "Degrees mode" : "Radians mode";
});

// Full keyboard navigation support including Backspace
input.addEventListener("keydown", event => {
    if (event.key === "Enter" || event.key === "=") {
        event.preventDefault();
        calculate();
    } else if (event.key === "Escape") {
        event.preventDefault();
        clearAll();
    } else if (event.key === "Backspace") {
        output.textContent = "Ready";
    }
});

input.addEventListener("input", () => {
    output.textContent = "Press Enter to calculate";
});
</script>
</body>
</html>
"""

components.html(calculator_html, height=710, scrolling=False)