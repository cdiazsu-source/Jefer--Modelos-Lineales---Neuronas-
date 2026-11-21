"""Genera NeuroLin.html (archivo único, con Nachito embebido) a partir de index.html.
Uso: python tools/build.py
"""
import base64, os

src = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(src, "index.html"), encoding="utf-8").read()
b64 = base64.b64encode(open(os.path.join(src, "assets", "nachito.jpeg"), "rb").read()).decode()
n_before = html.count("assets/nachito.jpeg")
# estáticos del HTML -> se rellenan por script
html = html.replace('<link rel="icon" type="image/jpeg" href="assets/nachito.jpeg">', '<link rel="icon" type="image/jpeg" data-nach>')
html = html.replace('<span class="av sm"><img src="assets/nachito.jpeg" alt="Nachito, mascota de la Universidad Nacional de Colombia"></span>NeuroLin', '<span class="av sm"><img data-nach alt="Nachito, mascota de la Universidad Nacional de Colombia"></span>NeuroLin')
# dentro de plantillas JS -> ${NACH}
html = html.replace('src="assets/nachito.jpeg"', 'src="${NACH}"')
assert "assets/nachito.jpeg" not in html, "quedan referencias"
init = "const NACH='data:image/jpeg;base64," + b64 + "';\ndocument.querySelectorAll('[data-nach]').forEach(e=>{e.tagName==='LINK'?e.href=NACH:e.src=NACH});\n"
html = html.replace("'use strict';\n", "'use strict';\n" + init, 1)
assert "const NACH=" in html
open(os.path.join(src, "NeuroLin.html"), "w", encoding="utf-8", newline="\n").write(html)
print("refs originales:", n_before, "| tamaño KB:", round(len(html.encode()) / 1024))
