import csv
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RATIO_FILE = ROOT / "apple_financial_ratios.csv"
REQUIRED_COLUMNS = {"Ratio Type", "2024", "2023", "Change"}
REQUIRED_RATIOS = {
    "Gross Profit Margin (%)",
    "Operating Profit Margin (%)",
    "Net Profit Margin (%)",
    "Return on Assets (ROA) (%)",
    "Return on Equity (ROE) (%)",
    "Current Ratio",
    "Quick Ratio",
    "Cash Ratio",
    "Asset Turnover (times)",
    "Inventory Turnover (times)",
    "Days Inventory Outstanding",
    "Accounts Receivable Turnover (times)",
    "Days Sales Outstanding",
    "Debt to Equity Ratio",
    "Debt to Assets Ratio",
    "Equity Ratio",
}


class RatioDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with RATIO_FILE.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            cls.fieldnames = set(reader.fieldnames or [])
            cls.rows = list(reader)

    def test_required_columns_are_present(self) -> None:
        self.assertTrue(
            REQUIRED_COLUMNS.issubset(self.fieldnames),
            f"Missing columns: {sorted(REQUIRED_COLUMNS - self.fieldnames)}",
        )

    def test_ratio_names_are_present_and_unique(self) -> None:
        names = [row["Ratio Type"].strip() for row in self.rows]
        self.assertEqual(len(names), len(set(names)), "Ratio names must be unique")
        self.assertTrue(
            REQUIRED_RATIOS.issubset(set(names)),
            f"Missing ratios: {sorted(REQUIRED_RATIOS - set(names))}",
        )

    def test_values_are_finite_numbers(self) -> None:
        for row in self.rows:
            for column in ("2024", "2023", "Change"):
                with self.subTest(ratio=row["Ratio Type"], column=column):
                    value = float(row[column])
                    self.assertTrue(math.isfinite(value))

    def test_change_matches_year_over_year_difference(self) -> None:
        for row in self.rows:
            with self.subTest(ratio=row["Ratio Type"]):
                expected = float(row["2024"]) - float(row["2023"])
                self.assertAlmostEqual(float(row["Change"]), expected, places=10)


if __name__ == "__main__":
    unittest.main()
