# Apple Inc. Financial Analysis (AAPL)

![Apple financial analysis project cover](assets/recruiter/cover.png)

An inspectable financial-accounting case study built from Apple Inc.'s 2023 and 2024 annual filings. The repository brings source reports, a retained ratio dataset, Python visualisations, and written deliverables together so the evidence and interpretation can be reviewed in one place.

> The repository URL contains the legacy ticker typo `APPL`; Apple's correct ticker is `AAPL`. Renaming the repository is tracked separately because it changes the public URL.

## Analysis scope

The project compares Apple's 2024 financial performance with 2023 across four areas:

- **Profitability** — gross, operating and net margins; return on assets; return on equity
- **Liquidity** — current, quick and cash ratios
- **Operating efficiency** — asset turnover, inventory turnover, days inventory outstanding, receivables turnover and days sales outstanding
- **Capital structure** — debt-to-equity, debt-to-assets and equity ratios

The source filings are retained in HTML and PDF formats. Calculated values are stored in [`apple_financial_ratios.csv`](apple_financial_ratios.csv), while the reports explain the accounting interpretation and business implications.

## Key findings from the retained calculations

| Metric | 2024 | 2023 | Movement |
|---|---:|---:|---:|
| Gross profit margin | 46.21% | 44.13% | +2.08 percentage points |
| Operating profit margin | 31.51% | 29.82% | +1.69 percentage points |
| Net profit margin | 23.97% | 25.31% | -1.33 percentage points |
| Return on assets | 25.68% | 27.51% | -1.83 percentage points |
| Return on equity | 164.59% | 156.08% | +8.52 percentage points |
| Current ratio | 0.87 | 0.99 | -0.12 |
| Inventory turnover | 53.67× | 60.54× | -6.87× |
| Days sales outstanding | 31.19 days | 28.10 days | +3.09 days |
| Debt-to-equity | 1.70 | 1.69 | broadly stable |
| Debt-to-assets | 0.26 | 0.30 | improved by 0.03 |

The analysis identifies stronger gross and operating profitability alongside weaker short-term liquidity and slower inventory and receivables efficiency. Apple's reported operating cash flow of approximately $118.3 billion is discussed as an important counterbalance when interpreting the liquidity ratios.

## Repository guide

### Reader-first documents

- [`Executive_Summary.md`](Executive_Summary.md) — headline findings and recommendations
- [`Apple_Financial_Analysis_Report_Updated.md`](Apple_Financial_Analysis_Report_Updated.md) — editable full report
- `Apple_Financial_Analysis_Report.docx` — Word deliverable
- [`report/financial_accounting_report.pdf`](report/financial_accounting_report.pdf) — LaTeX/PDF report
- [`FINANCIAL_STATEMENTS_GUIDE.md`](FINANCIAL_STATEMENTS_GUIDE.md) — supporting accounting guidance
- `Assignment.pdf` — original assignment context

### Evidence and calculations

- Apple 2023 and 2024 10-K filings in HTML and PDF form
- [`apple_financial_ratios.csv`](apple_financial_ratios.csv) — retained ratios and year-over-year differences
- [`industry_benchmarks.md`](industry_benchmarks.md) — external comparison material used by the report
- [`report/references.bib`](report/references.bib) — bibliography for the LaTeX version

### Visual outputs

The repository includes charts for profitability, liquidity, operational efficiency, gearing, benchmark comparisons, working capital, and an integrated summary dashboard. Root-level PNG files support the Markdown and Word workflow; matching copies under `report/figures/` are used by the LaTeX report.

## Reproducing and validating the visualisations

Create an isolated Python environment and install the declared dependencies:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Regenerate the charts from the retained ratio CSV:

```bash
python create_visualizations.py
python create_additional_visualizations.py
```

Run the dataset-integrity checks with:

```bash
python -m unittest discover -s tests -v
```

The automated checks verify that:

- the required ratio columns and metric names are present;
- metric names are unique;
- all retained values are finite numbers;
- every `Change` value equals `2024 - 2023`;
- both chart scripts compile and execute in a headless environment.

GitHub Actions repeats these checks and regenerates all charts on each pull request.

## Reproducibility boundary

The chart layer is reproducible from `apple_financial_ratios.csv`, and the CSV is automatically checked for structural and arithmetic consistency. The repository does **not** currently include a calculation script or linked workbook that rebuilds every ratio directly from raw filing line items. The retained filings allow manual source review, but full source-to-ratio automation would require a separate extraction and calculation pipeline.

## Methodology and interpretation boundaries

- Ratio movements are descriptive; they do not by themselves establish causation.
- Apple's unusually high return on equity is affected by its equity base and share-repurchase programme, so it should not be interpreted as a standalone operating-performance measure.
- `create_additional_visualizations.py` contains manually entered external benchmark values. Automation confirms that the script runs, not that those benchmarks remain current or methodologically comparable.
- The additional year-over-year chart uses positive and negative numeric movement; a positive number is not automatically an economic improvement for every ratio.
- External benchmarks should be checked against their original sources before academic, professional, or investment use.
- Strategic observations and recommendations are assignment interpretations, not investment advice.

## Portfolio value

This case study demonstrates:

- financial-statement interpretation and ratio analysis;
- retained evidence and calculation-data review;
- year-over-year performance comparison;
- Python-based financial visualisation;
- automated data-integrity validation;
- communication through executive, Markdown, Word, LaTeX, and PDF deliverables;
- awareness of the limitations behind ratios and benchmark comparisons.

## Project context

This repository was prepared as a financial-analysis assignment and reflects the 2023–2024 reporting period included in the project. It is an analytical case study rather than a live equity-research model, valuation model, or investment recommendation.