# NeuroLin · Simulador de neuronas para Modelos Lineales

Simulador interactivo que lleva la regresión lineal hasta la neurona artificial: cómo una neurona **predice**, **decide** y **aprende**.

Proyecto de **Jeferson Beltran**, estudiante de Economía · Modelos Lineales (2018622) · 2026-II · Universidad Nacional de Colombia.

## Módulos
0. Introducción: anatomía de la neurona y redes neuronales (qué partes forman la conexión y cómo se refuerza al aprender)
1. De la neurona biológica a la artificial (Cap. 8.4)
2. Una neurona que predice: regresión lineal (Cap. 1 y 2)
3. Una neurona que decide: clasificación (Cap. 7 y 4.1)
4. Cómo aprende: pérdida y descenso de gradiente (Cap. 1.2 y 8.4)
5. Aprender sin memorizar: validación, Ridge y LASSO (Cap. 4)

Incluye ficha de teoría con fórmulas, tutorial guiado, desafío y cuestionario.

## Contenido del repositorio
| Archivo | Descripción |
|---|---|
| `index.html` | Código fuente del simulador (se usa con servidor local o GitHub Pages) |
| `NeuroLin.html` | Versión descargable en un solo archivo (Nachito embebido); solo necesita internet para Plotly y KaTeX |
| `NeuroLin_Fundamentos_Teoricos_y_Practicos.docx` | Documento de fundamentos teóricos y prácticos |
| `assets/nachito.jpeg` | Mascota Nachito |
| `tools/build.py` | Regenera `NeuroLin.html` desde `index.html` (`python tools/build.py`) |

## Uso
Es un sitio estático (HTML + JavaScript, sin compilación). Requiere internet para cargar Plotly y KaTeX desde CDN.

```powershell
python -m http.server 8000
```
Abrir `http://localhost:8000/`. Las rutas usan hash (`#/m/neurona`), por lo que funciona en GitHub Pages sin configuración extra.

## Créditos
Gráficas: Plotly.js · Fórmulas: KaTeX · Mascota: Nachito, Universidad Nacional de Colombia.
