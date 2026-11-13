import unittest
from src.energia import monthly_consumption, analyze, EnergyScenario
from src.assistente import EnergyAssistant

class EnergyTests(unittest.TestCase):
    def test_consumption(self):
        self.assertAlmostEqual(monthly_consumption(60, 5, 5, 30), 45.0)

    def test_led_savings(self):
        result = analyze(EnergyScenario())
        self.assertAlmostEqual(result["led_kwh"], 6.75)
        self.assertAlmostEqual(result["saved_kwh"], 38.25)

    def test_solar_estimate(self):
        result = analyze(EnergyScenario())
        self.assertAlmostEqual(result["solar_generation"], 54.0)
        self.assertAlmostEqual(result["solar_offset"], 45.0)

    def test_assistant_answer(self):
        self.assertIn("38.25", EnergyAssistant().answer("Como economizar com LED?"))

    def test_negative_values_rejected(self):
        with self.assertRaises(ValueError):
            monthly_consumption(-60, 5, 5, 30)

if __name__ == "__main__":
    unittest.main()
