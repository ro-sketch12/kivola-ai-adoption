import unittest

from src.roadmap_pipeline import build_demo_input, build_roadmap, detect_use_cases, rank_use_cases


class RoadmapPipelineTest(unittest.TestCase):
    def test_builds_public_safe_demo_roadmap(self):
        roadmap = build_roadmap(build_demo_input())

        self.assertEqual(roadmap["company"], "Max Mustermann")
        self.assertTrue(roadmap["source"]["public_safe"])
        self.assertTrue(roadmap["review_gate"]["required"])
        self.assertGreaterEqual(len(roadmap["use_cases"]), 2)
        self.assertEqual(roadmap["pipeline"][0], "Kundengespräch")

    def test_detects_offer_and_content_context(self):
        cases = detect_use_cases(
            "Im Büro dauern Angebote lange. Longform Video soll zu Clips werden."
        )
        names = [case.name for case in cases]

        self.assertIn("Büro- und Angebotsvorbereitung strukturieren", names)
        self.assertIn("Content aus Longform-Material ableiten", names)

    def test_ranking_prefers_high_impact_low_effort_cases(self):
        ranked = rank_use_cases(
            detect_use_cases("Angebote und wiederkehrende Email Antworten kosten Zeit.")
        )

        self.assertEqual(ranked[0]["decision"], "starten")
        self.assertIn("score", ranked[0])

    def test_requires_transcript(self):
        with self.assertRaises(ValueError):
            build_roadmap({"company": "Max Mustermann"})


if __name__ == "__main__":
    unittest.main()

