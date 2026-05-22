# Kivola · KI-Adoption aus Kundengespräch

Kivola zeigt, wie aus einem Kundengespräch ein KI-Fahrplan entsteht: Gespräch verstehen, Transkript strukturieren, Arbeitsabläufe analysieren, Tool-/API-Lösung auswählen, Testlauf planen und verständlich übergeben.

Der Kern ist kundennahe Umsetzung. Nicht “mehr Tools”, sondern: Was sollte dieses Unternehmen zuerst testen, warum genau dort und wie wird das Ergebnis kontrolliert?

## 60-Sekunden-Überblick

| Frage | Antwort |
| --- | --- |
| Problem | Kleine Unternehmen wissen oft nicht, wo KI im Alltag zuerst sinnvoll ist. |
| Lösung | Ein phasenbasierter KI-Fahrplan aus Gespräch, Transkript, Recherche, Priorisierung, Review und Übergabe. |
| KI-Rolle | KI-Agenten strukturieren Recherche, Analyse, Toolauswahl und Dokumententwurf. |
| Roberts Rolle | Gesprächslogik, Analyseablauf, Review, anonymisierte Arbeitsprobe und Übergabeform entwickelt. |
| Öffentliche Arbeitsprobe | Anonymisierter Max-Mustermann-Fahrplan als PDF im Portfolio. |
| Öffentliche Grenze | Keine Rohtranskripte, Kundennamen, internen Notizen oder vollständigen Prompts. |

## Architektur

Siehe [docs/architecture.md](./docs/architecture.md).

## Workflow

Siehe [docs/workflow.md](./docs/workflow.md).

## Schneller Einstieg

Siehe [docs/quick-review.md](./docs/quick-review.md) für den schnellen Überblick.

## Ausführbarer Code-Auszug

Dieses Repo enthält keinen vollständigen Kunden- oder Agenten-Workflow. Der Code-Auszug zeigt reduziert und ausführbar, wie Gesprächsmaterial in priorisierte Anwendungsfälle und einen prüfbaren Fahrplan überführt werden kann:

- `src/roadmap_pipeline.py`: deterministische Demo-Pipeline für Use-Case-Erkennung, Priorisierung, Fahrplan und Review-Gate
- `tests/test_roadmap_pipeline.py`: Tests für Priorisierung, Fahrplanstruktur und anonymisierte Demo-Daten

Lokal prüfen:

```bash
python3 -m unittest discover -s tests
python3 scripts/check_public_content.py
```

Der Code arbeitet nur mit Max-Mustermann-Demo-Daten. Nicht enthalten sind Rohtranskripte, Kundennamen, interne Notizen, vollständige Prompts oder externe API-Aufrufe.

## Was öffentlich prüfbar ist

- Fahrplan-Logik
- Analysephasen
- Review-/Handover-Rolle
- reduzierter, ausführbarer Code-Auszug für Priorisierung und Fahrplanstruktur
- anonymisierte PDF-Arbeitsprobe
- Public/Private-Grenze

## Was bewusst nicht öffentlich ist

- Originaltranskripte
- echte Kundennamen und Kontakte
- interne Notizen
- vollständige Rohprompts
- nicht geprüfte Preis-/ROI-/Förderversprechen

## Tech/Tools

Python, python-docx, strukturierte JSON-Daten, Recherche- und Scraping-Workflows, Dokumentgenerierung, manuelle Review- und Übergabelogik.

## Portfolio-Link

Der anonymisierte Original-Fahrplan wird über das Portfolio verlinkt, nicht als schweres PDF in dieses Repo gelegt.
