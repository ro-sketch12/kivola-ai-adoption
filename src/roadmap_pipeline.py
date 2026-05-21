from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable


@dataclass(frozen=True)
class UseCase:
    name: str
    evidence: str
    impact: int
    effort: int
    risk: int
    first_test: str


def build_roadmap(input_data: dict) -> dict:
    transcript = str(input_data.get("transcript", "")).strip()
    if not transcript:
        raise ValueError("transcript is required")

    company = input_data.get("company", "Max Mustermann")
    use_cases = rank_use_cases(detect_use_cases(transcript))

    return {
        "company": company,
        "source": {
            "transcript": "anonymized-demo",
            "public_safe": True,
        },
        "pipeline": [
            "Kundengespräch",
            "Transkript",
            "Agenten-Analyse",
            "Fahrplan-Entwurf",
            "Review durch Robert",
            "Testlauf und Übergabe",
        ],
        "recommended_first_test": use_cases[0]["name"] if use_cases else "Arbeitsablauf priorisieren",
        "use_cases": use_cases,
        "review_gate": {
            "required": True,
            "checks": [
                "Passt der Anwendungsfall zum Gespräch?",
                "Sind Annahmen und belegte Aussagen getrennt?",
                "Ist der erste Test klein genug?",
                "Bleiben Kundendaten aus öffentlichen Unterlagen heraus?",
            ],
        },
    }


def detect_use_cases(transcript: str) -> list[UseCase]:
    text = transcript.lower()
    cases: list[UseCase] = []

    if any(word in text for word in ["angebot", "rechnung", "büro", "administration"]):
        cases.append(
            UseCase(
                name="Büro- und Angebotsvorbereitung strukturieren",
                evidence="Im Gespräch wurden wiederkehrende Büro- oder Angebotsaufgaben genannt.",
                impact=4,
                effort=2,
                risk=2,
                first_test="Eine vorhandene Vorlage mit Demo-Daten in einen prüfbaren Entwurf überführen.",
            )
        )

    if any(word in text for word in ["video", "content", "clip", "shorts", "kanal"]):
        cases.append(
            UseCase(
                name="Content aus Longform-Material ableiten",
                evidence="Im Gespräch wurde Content-Wiederverwertung oder zusätzlicher Kanal erwähnt.",
                impact=3,
                effort=2,
                risk=1,
                first_test="Ein Longform-Beispiel in drei Clip-Briefs und Veröffentlichungsnotizen übersetzen.",
            )
        )

    if any(word in text for word in ["e-mail", "email", "kundenanfrage", "antwort"]):
        cases.append(
            UseCase(
                name="Kundenkommunikation vorbereiten",
                evidence="Im Gespräch wurden wiederkehrende Antworten oder Kundenanfragen genannt.",
                impact=3,
                effort=1,
                risk=2,
                first_test="Drei Antwortvorlagen mit Freigabe-Schritt vorbereiten.",
            )
        )

    if not cases:
        cases.append(
            UseCase(
                name="Arbeitsablauf priorisieren",
                evidence="Das Gespräch enthält noch keinen eindeutigen Automationskandidaten.",
                impact=2,
                effort=1,
                risk=1,
                first_test="Ablaufkarte mit Aufgaben, Häufigkeit und manuellem Aufwand erstellen.",
            )
        )

    return cases


def rank_use_cases(use_cases: Iterable[UseCase]) -> list[dict]:
    ranked = []
    for case in use_cases:
        score = round((case.impact * 2 - case.effort - case.risk) / 5, 2)
        row = asdict(case)
        row["score"] = score
        row["decision"] = "starten" if score >= 0.6 else "erst klären"
        ranked.append(row)
    return sorted(ranked, key=lambda row: row["score"], reverse=True)


def build_demo_input() -> dict:
    return {
        "company": "Max Mustermann",
        "transcript": (
            "Wir verlieren im Büro Zeit mit Angeboten und wiederkehrenden E-Mail-Antworten. "
            "Außerdem gibt es Longform-Content, aus dem kurze Clips für einen weiteren Kanal "
            "entstehen könnten. Wichtig ist, dass alles kontrolliert wird."
        ),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(build_roadmap(build_demo_input()), ensure_ascii=False, indent=2))

