import os
import shutil

def assemble_html():
    css_content = """
@page {
  size: A4;
  margin: 18mm 15mm 20mm 15mm;
  @bottom-right {
    content: counter(page);
    font-family: 'Times New Roman', Times, serif;
    font-size: 10pt;
    color: #475569;
  }
}

body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 11pt;
  line-height: 1.55;
  color: #1e293b;
  background-color: #ffffff;
  margin: 0;
  padding: 0;
}

.cover-page {
  page-break-after: always;
  height: 90vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  border: 3px double #1e3a8a;
  padding: 40px;
  box-sizing: border-box;
}

.cover-institution {
  font-size: 14pt;
  font-weight: bold;
  letter-spacing: 1.5px;
  color: #1e3a8a;
  text-transform: uppercase;
  margin-bottom: 30px;
}

.cover-title {
  font-size: 28pt;
  font-weight: bold;
  color: #0f172a;
  margin: 20px 0;
  line-height: 1.2;
}

.cover-subtitle {
  font-size: 15pt;
  color: #334155;
  margin-bottom: 40px;
  max-width: 650px;
  line-height: 1.4;
}

.cover-divider {
  width: 120px;
  height: 3px;
  background-color: #2563eb;
  margin: 20px auto 40px auto;
}

.cover-details {
  font-size: 12pt;
  color: #475569;
  margin-top: 30px;
  line-height: 1.8;
}

.toc-page {
  page-break-after: always;
  padding: 20px 10px;
}

.toc-title {
  font-size: 20pt;
  font-weight: bold;
  text-align: center;
  color: #0f172a;
  border-bottom: 2px solid #0f172a;
  padding-bottom: 10px;
  margin-bottom: 25px;
}

.toc-list {
  list-style: none;
  padding: 0;
}

.toc-item {
  margin: 12px 0;
  font-size: 12pt;
}

.toc-item a {
  text-decoration: none;
  color: #1e3a8a;
  display: flex;
  justify-content: space-between;
}

.chapter {
  page-break-before: always;
  margin-top: 10px;
}

.chapter-header {
  border-bottom: 2px solid #1e3a8a;
  padding-bottom: 12px;
  margin-bottom: 24px;
}

.chapter-number {
  font-size: 12pt;
  font-weight: bold;
  letter-spacing: 2px;
  color: #2563eb;
  text-transform: uppercase;
}

.chapter-title {
  font-size: 21pt;
  font-weight: bold;
  color: #0f172a;
  margin: 6px 0 0 0;
}

h2 {
  font-size: 14pt;
  font-weight: bold;
  color: #1e3a8a;
  border-bottom: 1px solid #cbd5e1;
  padding-bottom: 5px;
  margin-top: 25px;
  margin-bottom: 12px;
  page-break-after: avoid;
}

h3 {
  font-size: 12pt;
  font-weight: bold;
  color: #334155;
  margin-top: 18px;
  margin-bottom: 8px;
  page-break-after: avoid;
}

p {
  margin: 8px 0;
  text-align: justify;
}

.abstract-box {
  background-color: #f8fafc;
  border-left: 4px solid #2563eb;
  padding: 12px 16px;
  margin: 15px 0 20px 0;
  font-size: 10.5pt;
  color: #334155;
}

.definition-box {
  background-color: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-left: 4px solid #16a34a;
  padding: 12px 16px;
  margin: 15px 0;
  border-radius: 4px;
  page-break-inside: avoid;
}

.definition-title {
  font-weight: bold;
  color: #15803d;
  font-size: 11.5pt;
  margin-bottom: 6px;
}

.theorem-box {
  background-color: #eff6ff;
  border: 1px solid #bfdbfe;
  border-left: 4px solid #2563eb;
  padding: 12px 16px;
  margin: 15px 0;
  border-radius: 4px;
  page-break-inside: avoid;
}

.theorem-title {
  font-weight: bold;
  color: #1d4ed8;
  font-size: 11.5pt;
  margin-bottom: 6px;
}

.method-box {
  background-color: #fffbeb;
  border: 1px solid #fde68a;
  border-left: 4px solid #d97706;
  padding: 12px 16px;
  margin: 15px 0;
  border-radius: 4px;
  page-break-inside: avoid;
}

.method-title {
  font-weight: bold;
  color: #b45309;
  font-size: 11.5pt;
  margin-bottom: 6px;
}

.zoom-box {
  background-color: #faf5ff;
  border: 1px solid #e9d5ff;
  border-left: 4px solid #9333ea;
  padding: 12px 16px;
  margin: 15px 0;
  border-radius: 4px;
  page-break-inside: avoid;
}

.zoom-title {
  font-weight: bold;
  color: #7e22ce;
  font-size: 11.5pt;
  margin-bottom: 6px;
}

.tip-box {
  background-color: #fdf2f8;
  border: 1px solid #fbcfe8;
  border-left: 4px solid #db2777;
  padding: 12px 16px;
  margin: 15px 0;
  border-radius: 4px;
  page-break-inside: avoid;
}

.tip-title {
  font-weight: bold;
  color: #be185d;
  font-size: 11.5pt;
  margin-bottom: 6px;
}

.exercise-card {
  background-color: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 20px 0;
  page-break-inside: avoid;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.exercise-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
  border-bottom: 1px dashed #cbd5e1;
  padding-bottom: 6px;
}

.exercise-badge {
  background-color: #1e3a8a;
  color: #ffffff;
  font-weight: bold;
  font-size: 9.5pt;
  padding: 3px 8px;
  border-radius: 4px;
}

.exercise-title {
  font-weight: bold;
  font-size: 12pt;
  color: #0f172a;
}

.exercise-statement {
  background-color: #f8fafc;
  padding: 10px 14px;
  border-radius: 4px;
  font-style: italic;
  margin-bottom: 12px;
}

.solution-box {
  border-top: 1px solid #e2e8f0;
  padding-top: 10px;
}

.solution-title {
  font-weight: bold;
  color: #047857;
  margin-bottom: 8px;
  font-size: 11pt;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  margin: 15px 0;
  font-size: 10.5pt;
  page-break-inside: avoid;
}

.data-table th, .data-table td {
  border: 1px solid #cbd5e1;
  padding: 8px 10px;
  text-align: left;
}

.data-table th {
  background-color: #f1f5f9;
  font-weight: bold;
  color: #0f172a;
}

.figure-container {
  text-align: center;
  margin: 20px auto;
  page-break-inside: avoid;
}

.svg-fig {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}

.figure-caption {
  font-size: 10pt;
  font-style: italic;
  color: #475569;
  margin-top: 8px;
}
"""

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Électromagnétisme Expliqué - Traité Pédagogique Complet</title>
  <style>{css_content}</style>
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      svg: {{
        fontCache: 'global'
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>

  <!-- PAGE DE COUVERTURE -->
  <div class="cover-page">
    <div class="cover-institution">UNIVERSITÉ JOSEPH KI-ZERBO • IBAM MIAGE 2</div>
    <div class="cover-title">ÉLECTROMAGNÉTISME EXPLIQUÉ</div>
    <div class="cover-subtitle">Traité Didactique d'Électrostatique, Magnétostatique, Équations de Maxwell & Télécommunications : Théorie Rigoureuse, Représentations 3D et Corrigés Intégraux Détaillés</div>
    <div class="cover-divider"></div>
    <div class="cover-details">
      <strong>Auteur de référence :</strong> Prof. Marcel Bawindsom KÉBRÉ<br>
      <strong>Édition Pédagogique Augmentée :</strong> Avec Zooms Méthodologiques, Guides de Symétrie/Antisymétrie & Résolutions Pas à Pas<br>
      <strong>Contenu :</strong> Cours Fondations & Chapitres 1 à 5 • 10 Exercices de Calcul Vectoriel • 17 Exercices de Fin de Chapitre • 8 Travaux Dirigés Complets
    </div>
  </div>

  <!-- TABLE DES MATIÈRES -->
  <div class="toc-page">
    <div class="toc-title">Table des Matières</div>
    <ul class="toc-list">
      <li class="toc-item"><strong>Chapitre 0 : Fondations Mathématiques – Repères 3D & Calcul Vectoriel</strong></li>
      <li class="toc-item"><strong>Chapitre 1 : Charge Électrique, Loi de Coulomb et Champ Électrostatique</strong></li>
      <li class="toc-item"><strong>Chapitre 2 : Flux Électrostatique, Théorème de Gauss & Équations Locales</strong></li>
      <li class="toc-item"><strong>Chapitre 3 : Potentiel et Énergie Électrostatiques</strong></li>
      <li class="toc-item"><strong>Chapitre 4 : Magnétostatique – Courants, Loi de Biot-Savart & Théorème d'Ampère</strong></li>
      <li class="toc-item"><strong>Chapitre 5 : Équations de Maxwell, Ondes Électromagnétiques et Antennes</strong></li>
      <li class="toc-item"><strong>Corrigés Détaillés I : Les 10 Exercices de Calcul Vectoriel (Stokes, Flux, Rotationnel)</strong></li>
      <li class="toc-item"><strong>Corrigés Détaillés II : Les 17 Exercices de Fin de Chapitre du Cours IBAM</strong></li>
      <li class="toc-item"><strong>Corrigés Détaillés III : Les 8 Travaux Dirigés Complets (TD 1 à TD 8)</strong></li>
    </ul>
  </div>
"""

    # Read each chapter html
    files = [
        "src_book/ch0_fondations.html",
        "src_book/ch1_cours.html",
        "src_book/ch2_cours.html",
        "src_book/ch3_cours.html",
        "src_book/ch4_cours.html",
        "src_book/ch5_cours.html",
        "src_book/corr_calcul_vectoriel.html",
        "src_book/corr_chapitres.html",
        "src_book/corr_td.html"
    ]

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            html += f"\n<!-- SECTION: {fpath} -->\n" + f.read()

    html += """
</body>
</html>
"""

    with open("src_book/electromagnetisme_explique.html", "w", encoding="utf-8") as out:
        out.write(html)

    print("HTML assembly complete: src_book/electromagnetisme_explique.html")

if __name__ == "__main__":
    assemble_html()
