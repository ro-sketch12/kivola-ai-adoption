# Kivola Guardrails Checklist

Status: public-facing summary  
Datenstand: 2026-05-13  
Quelle: private Kivola-Repo-Struktur, zusammengefasst ohne Codeauszug mit privaten Daten

## Public-facing Substanz

Das private Kivola-Repo enthält ein System für strukturierte AI-Fahrpläne:

- Python-DOCX-Reportgenerator
- typisiertes Datenmodell
- ROI- und Zeitersparnis-Hilfslogik
- Validierungs- und Qualitätschecks
- Tests für ROI, Parsing, Sanitizing und Anti-Hallucination-Fälle
- CI-Matrix für Python-Versionen

## Guardrail-Prinzipien

| Bereich | Regel | Warum das wichtig ist |
| --- | --- | --- |
| Eingabedaten | Pflichtfelder werden geprüft und fehlende Werte markiert | keine stillen Annahmen |
| ROI | Unsichere Werte werden als Annahme geführt | keine erfundenen Impact-Zahlen |
| Textausgabe | Texte werden bereinigt und strukturiert | kein Rohdaten-Dump |
| Use Cases | Priorisierung trennt Nutzen, Aufwand und Risiko | Pilot startet mit realistischem Scope |
| Compliance | Risiken werden benannt, nicht wegformuliert | kein harter Rechtsclaim ohne Nachweis |
| Handoff | Pilotplan enthält nächste Schritte, Messung und Grenzen | Umsetzung statt Beratungsfloskel |

## Public/Private-Grenze

Öffentlich erlaubt:

- synthetische Demo-Fahrpläne
- anonymisierte Prozessdiagramme
- Methodik und Guardrails
- Test- und CI-Existenz als Beschreibung
- freigegebene Testimonials

Privat bleibt:

- echte Kundennamen
- reale Rohberichte
- echte Angebote, Fotos, Preise, Kontakte
- private Prompts und interne Strategien
- Analytics, Logs, CRM- oder Pipeline-Daten
- konkrete Finanzdaten ohne explizite Freigabe

## Interview-Demo

Der sichere Demo-Pfad:

1. Synthetischen Demo-Kunden zeigen.
2. Discovery-Felder und fehlende Daten markieren.
3. Priorisierung und Pilotplan erklären.
4. Annahmen vs. Messwerte trennen.
5. Public/Private-Grenze zeigen.

