OUTPUT = "info-card.svg"

lines = [
    ("USER", "Aman Kumar Ranjan"),
    ("ROLE", "CSE / Data Science"),
    ("FOCUS", "AI / ML / DL / RAG"),
    ("LANG", "Python • Java • JavaScript"),
    ("ML", "Scikit-learn • TensorFlow"),
    ("DL", "LSTM • GRU • Transformers"),
    ("DATA", "Pandas • NumPy • Matplotlib"),
    ("WEB", "MERN • PWA"),
    ("PROJECTS", "Digital Twin • RAG • Forecasting"),
]

width = 500
line_height = 34
height = 100 + len(lines) * line_height

svg = [
    f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect
width="100%"
height="100%"
rx="14"
fill="#0d1117"
stroke="#30363d"/>

<text
x="25"
y="35"
fill="#58a6ff"
font-family="monospace"
font-size="18"
font-weight="bold">
aman@github:~$
</text>

<text
x="25"
y="62"
fill="#8b949e"
font-family="monospace"
font-size="13">
./whoami
</text>

<style>
.line {{
    animation: fade 0.5s ease-out forwards;
    opacity: 0;
}}

@keyframes fade {{
    from {{
        opacity: 0;
        transform: translateX(-10px);
    }}

    to {{
        opacity: 1;
        transform: translateX(0);
    }}
}}
</style>'''
]

for i, (key, value) in enumerate(lines):

    y = 95 + i * line_height
    delay = i * 0.12

    svg.append(
        f'''<text
class="line"
x="25"
y="{y}"
fill="#79c0ff"
font-family="monospace"
font-size="13"
style="animation-delay:{delay}s">
{key}
</text>'''
    )

    svg.append(
        f'''<text
class="line"
x="145"
y="{y}"
fill="#c9d1d9"
font-family="monospace"
font-size="13"
style="animation-delay:{delay}s">
{value}
</text>'''
    )

svg.append("</svg>")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Created {OUTPUT}")