"""
Apple Financial Analysis - Additional Visualizations
Creates: 1) Apple vs Industry Benchmark Comparison
        2) Year-over-Year Change Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set style (Apple-inspired)
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['font.size'] = 10

# Apple-inspired colors
APPLE_BLUE = "#007AFF"
APPLE_GRAY = "#8E8E93"
APPLE_LIGHT_BLUE = "#5AC8FA"
APPLE_DARK_BLUE = "#0055D4"
APPLE_GREEN = "#34C759"
APPLE_RED = "#FF3B30"
APPLE_ORANGE = "#FF9500"
APPLE_PURPLE = "#AF52DE"

# Read the data
df = pd.read_csv("apple_financial_ratios.csv")

# Industry benchmark data (from industry_benchmarks.md)
industry_benchmarks = {
    "Gross Profit Margin (%)": {"apple_2024": 46.21, "benchmark": 50.0, "benchmark_label": "Tech Sector (40-60%)"},
    "Operating Profit Margin (%)": {"apple_2024": 31.51, "benchmark": 28.8, "benchmark_label": "Semiconductor (28.8%)"},
    "Return on Equity (ROE) (%)": {"apple_2024": 164.59, "benchmark": 27.8, "benchmark_label": "Tech Sector Record High"},
    "Current Ratio": {"apple_2024": 0.87, "benchmark": 2.12, "benchmark_label": "Tech Sector Average"},
    "Quick Ratio": {"apple_2024": 0.56, "benchmark": 2.12, "benchmark_label": "Tech Sector Average"},
    "Inventory Turnover (times)": {"apple_2024": 53.67, "benchmark": 7.84, "benchmark_label": "Tech Sector Average"},
    "Days Sales Outstanding": {"apple_2024": 31.19, "benchmark": 34.0, "benchmark_label": "Tech & Professional Services"},
    "Debt to Equity Ratio": {"apple_2024": 1.70, "benchmark": 1.1, "benchmark_label": "Tech Hardware Average"},
}

# Create figure settings
fig_dpi = 300
fig_size = (14, 10)


# =============================================================================
# VISUALIZATION 1: Apple vs Industry Benchmark Comparison
# =============================================================================
print("Creating Apple vs Industry Benchmark Comparison Chart...")

# Prepare data for benchmark comparison
metrics = list(industry_benchmarks.keys())
apple_values = [industry_benchmarks[m]["apple_2024"] for m in metrics]
benchmark_values = [industry_benchmarks[m]["benchmark"] for m in metrics]

# Create horizontal bar chart
fig1, ax1 = plt.subplots(figsize=fig_size, dpi=fig_dpi)

y_pos = np.arange(len(metrics))
height = 0.35

# Create bars
bars1 = ax1.barh(y_pos - height/2, apple_values, height, label='Apple (2024)',
                  color=APPLE_BLUE, alpha=0.85)
bars2 = ax1.barh(y_pos + height/2, benchmark_values, height, label='Industry Benchmark',
                  color=APPLE_GRAY, alpha=0.7)

# Customize the chart
ax1.set_ylabel('Financial Metrics', fontsize=12, fontweight='bold')
ax1.set_xlabel('Value', fontsize=12, fontweight='bold')
ax1.set_title('Apple Inc. vs Technology Industry Benchmarks (2024)',
              fontsize=16, fontweight='bold', pad=20)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(metrics, fontsize=10)
ax1.legend(loc='upper right', frameon=True, shadow=True, fontsize=11)
ax1.grid(axis='x', alpha=0.3, linestyle='--')

# Add value labels on bars
for bar in bars1:
    width = bar.get_width()
    ax1.text(width + max(apple_values) * 0.01, bar.get_y() + bar.get_height()/2,
            f'{width:.2f}', ha='left', va='center', fontsize=8, fontweight='bold', color=APPLE_BLUE)

for bar in bars2:
    width = bar.get_width()
    ax1.text(width + max(benchmark_values) * 0.01, bar.get_y() + bar.get_height()/2,
            f'{width:.2f}', ha='left', va='center', fontsize=8, fontweight='bold', color=APPLE_GRAY)

# Add performance annotations
performance_text = "Key Insights:\n• Apple's ROE (164.59%) is 6x tech sector record\n• Inventory turnover (53.67x) is 6.8x industry avg\n• Liquidity ratios below sector (strategic choice)"
ax1.text(0.98, 0.02, performance_text, transform=ax1.transAxes,
         fontsize=9, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig("apple_vs_industry_benchmark.png", dpi=fig_dpi, bbox_inches='tight')
plt.close()
print("[OK] Saved: apple_vs_industry_benchmark.png")


# =============================================================================
# VISUALIZATION 2: Year-over-Year Change Analysis (Diverging Bar Chart)
# =============================================================================
print("Creating Year-over-Year Change Analysis Chart...")

# Get all ratios with their changes
change_data = df.copy()
change_data['Abs_Change'] = change_data['Change'].abs()

# Sort by absolute change for better visualization
change_data = change_data.sort_values('Abs_Change', ascending=True)

# Create diverging bar chart
fig2, ax2 = plt.subplots(figsize=(fig_size[0], 14), dpi=fig_dpi)

# Prepare data
ratios = change_data['Ratio Type'].values
changes = change_data['Change'].values

# Create color array based on positive/negative change
colors = [APPLE_GREEN if x >= 0 else APPLE_RED for x in changes]

# Create horizontal bar chart
bars = ax2.barh(ratios, changes, color=colors, alpha=0.75, edgecolor='black', linewidth=0.5)

# Add vertical line at x=0
ax2.axvline(x=0, color='black', linestyle='-', linewidth=0.8)

# Customize the chart
ax2.set_xlabel('Year-over-Year Change', fontsize=12, fontweight='bold')
ax2.set_title('Apple Inc. - Financial Ratios Year-over-Year Change (2023 → 2024)',
              fontsize=16, fontweight='bold', pad=20)
ax2.grid(axis='x', alpha=0.3, linestyle='--')

# Add value labels on bars
for bar, change in zip(bars, changes):
    width = bar.get_width()
    label_x = width + 0.05 if width >= 0 else width - 0.05
    ax2.text(label_x, bar.get_y() + bar.get_height()/2,
            f'{change:+.2f}', ha='left' if width >= 0 else 'right',
            va='center', fontsize=9, fontweight='bold')

# Format x-axis to show percentage/decimal clearly
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:+.1f}' if x != 0 else '0'))

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=APPLE_GREEN, edgecolor='black', label='Improvement (+)'),
    Patch(facecolor=APPLE_RED, edgecolor='black', label='Decline (-)')
]
ax2.legend(handles=legend_elements, loc='upper right', frameon=True, shadow=True, fontsize=11)

# Add summary statistics
positive_changes = sum(changes > 0)
negative_changes = sum(changes < 0)
summary_text = f"Summary: {positive_changes} Improvements | {negative_changes} Declines"
ax2.text(0.5, 0.98, summary_text, transform=ax2.transAxes,
         fontsize=11, verticalalignment='top', horizontalalignment='center',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

plt.tight_layout()
plt.savefig("yoy_change_analysis.png", dpi=fig_dpi, bbox_inches='tight')
plt.close()
print("[OK] Saved: yoy_change_analysis.png")


# =============================================================================
# VISUALIZATION 3: Working Capital Composition (Stacked Bar Chart)
# =============================================================================
print("Creating Working Capital Composition Chart...")

# Working capital data from verified SEC 10-K
working_capital_2024 = {
    "Cash and Cash Equivalents": 29.943,
    "Marketable Securities": 35.228,
    "Accounts Receivable": 33.410,
    "Inventories": 7.286,
    "Other Current Assets": 47.120  # Vendor non-trade receivables + other
}

working_capital_2023 = {
    "Cash and Cash Equivalents": 29.965,
    "Marketable Securities": 31.590,
    "Accounts Receivable": 29.508,
    "Inventories": 6.331,
    "Other Current Assets": 46.171
}

current_liabilities_2024 = 176.392
current_liabilities_2023 = 145.308

fig3, ax3 = plt.subplots(figsize=fig_size, dpi=fig_dpi)

years = ['2023', '2024']
x_pos = np.arange(len(years))
width = 0.35

# Prepare stacked data
assets_2023 = [working_capital_2023[k] for k in working_capital_2023]
assets_2024 = [working_capital_2024[k] for k in working_capital_2024]
categories = list(working_capital_2024.keys())
colors_wc = [APPLE_BLUE, APPLE_LIGHT_BLUE, APPLE_DARK_BLUE, APPLE_GREEN, APPLE_PURPLE]

# Create stacked bars
bottom_2023 = np.zeros(len(years))
bottom_2024 = np.zeros(len(years))

for i, category in enumerate(categories):
    values_2023 = working_capital_2023[category]
    values_2024 = working_capital_2024[category]

    ax3.bar('2023', values_2023, bottom=bottom_2023[0], width=width,
            label=category if i == 0 else "", color=colors_wc[i], alpha=0.85, edgecolor='white')
    bottom_2023[0] += values_2023

    ax3.bar('2024', values_2024, bottom=bottom_2024[0], width=width,
            label=category if i == 0 else "", color=colors_wc[i], alpha=0.85, edgecolor='white')
    bottom_2024[0] += values_2024

# Add current liabilities as comparison line
ax3.plot(['2023', '2024'], [current_liabilities_2023, current_liabilities_2024],
         marker='o', markersize=10, linewidth=2.5, color=APPLE_RED,
         label='Current Liabilities', linestyle='--')

# Customize the chart
ax3.set_ylabel('Amount (Billions USD)', fontsize=12, fontweight='bold')
ax3.set_title('Apple Inc. - Working Capital Composition (2023 vs 2024)',
              fontsize=16, fontweight='bold', pad=20)
ax3.legend(loc='upper left', frameon=True, shadow=True, fontsize=10, ncol=2)
ax3.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels for total current assets
total_ca_2024 = sum(working_capital_2024.values())
total_ca_2023 = sum(working_capital_2023.values())
ax3.text('2023', total_ca_2023 + 10, f'Total CA:\n${total_ca_2023:.1f}B',
         ha='center', va='bottom', fontsize=9, fontweight='bold', color=APPLE_BLUE)
ax3.text('2024', total_ca_2024 + 10, f'Total CA:\n${total_ca_2024:.1f}B',
         ha='center', va='bottom', fontsize=9, fontweight='bold', color=APPLE_BLUE)

# Add current ratio annotations
cr_2023 = total_ca_2023 / current_liabilities_2023
cr_2024 = total_ca_2024 / current_liabilities_2024
ax3.text('2023', current_liabilities_2023 - 15, f'CL: ${current_liabilities_2023:.1f}B\nCR: {cr_2023:.2f}',
         ha='center', va='top', fontsize=8, color=APPLE_RED)
ax3.text('2024', current_liabilities_2024 - 20, f'CL: ${current_liabilities_2024:.1f}B\nCR: {cr_2024:.2f}',
         ha='center', va='top', fontsize=8, color=APPLE_RED)

# Add analysis note
analysis_text = "Note: Current Ratio < 1.0 reflects strategic working capital management\nbacked by strong operating cash flow ($118.3B in 2024)"
ax3.text(0.5, 0.02, analysis_text, transform=ax3.transAxes,
         fontsize=8, verticalalignment='bottom', horizontalalignment='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

plt.tight_layout()
plt.savefig("working_capital_composition.png", dpi=fig_dpi, bbox_inches='tight')
plt.close()
print("[OK] Saved: working_capital_composition.png")


print("\n" + "=" * 70)
print("ADDITIONAL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("=" * 70)
print("Files generated:")
print("  6. apple_vs_industry_benchmark.png     (Apple vs Industry Comparison)")
print("  7. yoy_change_analysis.png              (Year-over-Year Change Analysis)")
print("  8. working_capital_composition.png      (Working Capital Breakdown)")
print("=" * 70)
print("Total visualizations now available: 8")
print("=" * 70)
