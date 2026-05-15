# Kivola AI-Fahrplan Demo

Status: public-facing demo artifact  
Datenstand: 2026-05-13  
Datenbasis: synthetischer Beispielkunde, keine echten Kundendaten

## Ziel

Zeigen, wie Kivola aus einem Discovery-Gespräch einen umsetzbaren AI-Fahrplan macht:

1. Problem und Prozess aufnehmen.
2. Use Cases strukturiert bewerten.
3. Zeitersparnis als Annahme formulieren, nicht als Garantie.
4. Tool-Stack und Pilotplan vorschlagen.
5. Handoff so schreiben, dass ein kleines Team damit starten kann.

## Demo-Kunde

Name: Max Handwerk  
Team: 9 Personen  
Situation: Angebote, Baustellennotizen und Rückfragen laufen über Telefon, Fotos, Messenger und E-Mail.  
Ziel: weniger Nacharbeit zwischen Vor-Ort-Termin, Büro und Angebot.

Alle Angaben sind erfunden. Der Demo-Kunde dient nur dazu, Methodik, Priorisierung und Handoff zu zeigen.

## Discovery-Auszug

| Feld | Demo-Antwort |
| --- | --- |
| Hauptprozess | Vor-Ort-Termin -> Fotos/Notizen -> Angebot -> Rückfragen -> Auftrag |
| Schmerzpunkt | Informationen sind verteilt, Angebotsentwurf startet oft zu spät |
| Datenlage | Fotos, Freitextnotizen, alte Angebote, Materialpositionen |
| Risiko | falsche Annahmen aus unvollständigen Fotos oder fehlenden Raumdaten |
| Erfolgskriterium | Angebotsentwurf schneller erstellen, aber final weiter menschlich prüfen |

## Use-Case-Priorisierung

| Use Case | Nutzen | Aufwand | Risiko | Priorität |
| --- | ---: | ---: | ---: | --- |
| Foto- und Notizbriefing in Angebotsentwurf umwandeln | hoch | mittel | mittel | Pilot 1 |
| Sprachnotizen in Baustellenprotokoll strukturieren | mittel | niedrig | niedrig | Pilot 2 |
| E-Mail-Rückfragen automatisch vorsortieren | mittel | niedrig | mittel | Backlog |
| Vollautomatische Preisentscheidung | unklar | hoch | hoch | nicht starten |

## Zeitersparnis-Logik

Kivola rechnet bewusst mit Annahmen und markiert unsichere Felder.

| Annahme | Demo-Wert | Kommentar |
| --- | ---: | --- |
| Angebote pro Woche | 8 | vom Betrieb zu messen |
| manuelle Vorstrukturierung je Angebot | 18 min | Startwert aus Discovery |
| realistische Entlastung im Pilot | 30-45% | kein Vollautomations-Claim |
| Prüfzeit nach AI-Entwurf | 6-10 min | Pflicht, weil Fachwissen wichtig bleibt |

Ergebnis im Demo-Fahrplan: Der Pilot ist sinnvoll, wenn die Vorstrukturierung schneller wird und die fachliche Prüfung nicht länger dauert als vorher.

## Tool-Auswahl

| Baustein | Zweck | Public-facing Auswahlkriterium |
| --- | --- | --- |
| Eingabeformular | strukturierter Startpunkt für Auftrag, Fotos, Notizen | wenig Reibung im Alltag |
| LLM-Schicht | Text aus Notizen/Fotos in Entwurf strukturieren | menschliche Prüfung bleibt Pflicht |
| Angebotsvorlage | einheitlicher Output für Büro und Kunde | klare Felder statt Fließtext |
| Audit-Felder | Annahmen, fehlende Daten, Warnhinweise | keine stillen Schätzungen |

## 4-Wochen-Pilot

| Woche | Fokus | Output |
| --- | --- | --- |
| 1 | echte Beispielabläufe anonymisiert aufnehmen | 5 Beispielaufträge, Feldliste, Fehlerfälle |
| 2 | Demo-Workflow mit Fake- oder anonymisierten Daten bauen | erster Angebotsentwurf mit Warnfeldern |
| 3 | Pilot mit 5-10 nichtkritischen Fällen testen | Zeitmessung, Korrekturquote, Nutzerfeedback |
| 4 | Go/No-Go und Handoff | Entscheidung, Limit-Liste, nächste Automatisierung |

## Anonymisierter Pilot-Kontext

### Content Creator

Ausgangslage: Lange Videos mussten manuell zu kurzen Clips verarbeitet werden.  
Umsetzung: Tool-Setup für automatisches Short-Form-Clipping, Workflow-Erklärung, Übergabe für wiederholbare Nutzung.  
Messung: Reichweiten- und Zeitersparnis-Feedback zählt öffentlich erst als harter Beleg, wenn Name, Video oder Messwerte freigegeben sind.  
Public-Grenze: Kein Accountname, keine Analytics-Screenshots, keine Umsatz- oder Reichweitendaten ohne Freigabe.

### Handwerksbetrieb

Ausgangslage: Interesse an AI im Alltag, aber keine klare Priorisierung.  
Umsetzung: Use-Case-Fahrplan, Pilotoptionen, Risiken und erste Tool-Auswahl.  
Messung: Pilotfälle, Zeitmessung und Korrekturquote müssen vor einem harten Impact-Claim erhoben und freigegeben werden.  
Public-Grenze: Keine echten Angebote, Fotos, Namen, Preise, Kontaktdaten oder internen Abläufe.

## Was dieser Case belegt

- Robert kann aus einem unscharfen Kundengespräch einen klaren Umsetzungsplan bauen.
- Er denkt in Prozess, Risiko, Pilot und Handoff statt in reiner Tool-Liste.
- Er trennt Annahmen, Messwerte und harte Claims.
- Private Kundendaten bleiben aus dem public Proof heraus.
