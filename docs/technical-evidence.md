# Kivola Technical Evidence

Status: public-facing source-inspection summary  
Datenstand: 2026-05-13  
Quelle: private Kivola-Repo-Struktur, keine Rohdaten und keine Kundendaten

## Warum dieses Blatt existiert

Der Kivola-Case soll nicht nur behaupten, dass es ein System gibt. Dieses Blatt zeigt auf hoher Ebene, welche Bausteine im privaten Repo geprüft wurden, ohne Code, Kundendaten oder interne Details offenzulegen.

## Geprüfte Bausteine

| Bereich | Evidence | Was es zeigt |
| --- | --- | --- |
| Report-Generator | `ki-analyse-agent/generate_analyse.py` | Fahrplan wird aus strukturierten Eingaben als Dokument erzeugt |
| Datenmodell | `ki-analyse-agent/data_model.py` | Eingaben sind typisiert und validiert |
| Zeit-/ROI-Logik | `ki-analyse-agent/roi_calculator.py` | Annahmen, Summen und fehlende Daten werden getrennt behandelt |
| Tests | `ki-analyse-agent/tests/test_roi.py` | Tests für Parsing, Annahmen, Sanitizing und Guardrail-Fälle |
| CI | `.github/workflows/ci.yml` | Lint/Test-Lauf über mehrere Python-Versionen vorgesehen |
| Demo-Input | `ki-analyse-agent/example-input.json` | nur als internes Seed-Beispiel genutzt, nicht public gezeigt |

## Was öffentlich gezeigt wird

- synthetischer Fahrplan
- Guardrails und Prozessdiagramm
- Beschreibung der geprüften Bausteine
- Video-Script für eine sichere Demo

## Was bewusst nicht gezeigt wird

- private Repo-URL oder Rohdateien
- echte Kunden, Kontakte, Preise, Reports oder Screenshots
- private Prompts, Logs, CRM-Daten oder Analytics
- Testausgaben mit lokalen Pfaden oder internen Details

## Interview-Hinweis

Falls ein technischer Reviewer mehr Tiefe braucht, kann Robert in einem privaten Screen-Share die Struktur zeigen. Für die öffentliche Bewerbung reicht diese Zusammenfassung plus synthetische Demo.
