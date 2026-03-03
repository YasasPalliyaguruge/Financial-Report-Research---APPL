"""
Apple Financial Analysis Visualizations
Creates comprehensive charts for Apple's financial ratios (2023 vs 2024)
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

# Read the data
df = pd.read_csv("apple_financial_ratios.csv")

# Create figure settings
fig_dpi = 300
fig_size = (12, 8)


def add_data_labels(ax, bars, format_str="{:.2f}", offset=0.01):
    """Add data labels on top of bars"""
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + offset,
            format_str.format(height),
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )


# 1. Profitability Comparison Chart
print("Creating Profitability Comparison Chart...")
fig1, ax1 = plt.subplots(figsize=fig_size, dpi=fig_dpi)

profitability_data = df[
    df["Ratio Type"].isin(
        [
            "Gross Profit Margin (%)",
            "Operating Profit Margin (%)",
            "Net Profit Margin (%)",
            "Return on Assets (ROA) (%)",
            "Return on Equity (ROE) (%)",
        ]
    )
]

x = np.arange(len(profitability_data))
width = 0.35

bars1 = ax1.bar(
    x - width / 2,
    profitability_data["2024"],
    width,
    label="2024",
    color=APPLE_BLUE,
    alpha=0.8,
)
bars2 = ax1.bar(
    x + width / 2,
    profitability_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)

ax1.set_xlabel("Profitability Metrics", fontsize=12, fontweight="bold")
ax1.set_ylabel("Percentage (%)", fontsize=12, fontweight="bold")
ax1.set_title(
    "Apple Inc. - Profitability Ratios Comparison (2023 vs 2024)",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
ax1.set_xticks(x)
ax1.set_xticklabels(
    [label.replace(" (%)", "") for label in profitability_data["Ratio Type"]],
    rotation=45,
    ha="right",
)
ax1.legend(loc="upper right", frameon=True, shadow=True)
ax1.grid(axis="y", alpha=0.3, linestyle="--")

add_data_labels(ax1, bars1, "{:.2f}", 1)
add_data_labels(ax1, bars2, "{:.2f}", 1)

plt.tight_layout()
plt.savefig("profitability_comparison.png", dpi=fig_dpi, bbox_inches="tight")
plt.close()
print("[OK] Saved: profitability_comparison.png")


# 2. Liquidity Ratios Chart
print("Creating Liquidity Ratios Chart...")
fig2, ax2 = plt.subplots(figsize=fig_size, dpi=fig_dpi)

liquidity_data = df[
    df["Ratio Type"].isin(["Current Ratio", "Quick Ratio", "Cash Ratio"])
]

x = np.arange(len(liquidity_data))
width = 0.35

bars1 = ax2.bar(
    x - width / 2,
    liquidity_data["2024"],
    width,
    label="2024",
    color=APPLE_LIGHT_BLUE,
    alpha=0.8,
)
bars2 = ax2.bar(
    x + width / 2,
    liquidity_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)

ax2.set_xlabel("Liquidity Metrics", fontsize=12, fontweight="bold")
ax2.set_ylabel("Ratio Value", fontsize=12, fontweight="bold")
ax2.set_title(
    "Apple Inc. - Liquidity Ratios Comparison (2023 vs 2024)",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
ax2.set_xticks(x)
ax2.set_xticklabels(liquidity_data["Ratio Type"])
ax2.legend(loc="upper right", frameon=True, shadow=True)
ax2.grid(axis="y", alpha=0.3, linestyle="--")
ax2.axhline(y=1.0, color="red", linestyle="--", alpha=0.5, label="Benchmark (1.0)")

add_data_labels(ax2, bars1, "{:.3f}", 0.02)
add_data_labels(ax2, bars2, "{:.3f}", 0.02)

plt.tight_layout()
plt.savefig("liquidity_ratios.png", dpi=fig_dpi, bbox_inches="tight")
plt.close()
print("[OK] Saved: liquidity_ratios.png")


# 3. Efficiency Metrics Chart
print("Creating Efficiency Metrics Chart...")
fig3, ax3 = plt.subplots(figsize=fig_size, dpi=fig_dpi)

efficiency_data = df[
    df["Ratio Type"].isin(
        [
            "Asset Turnover (times)",
            "Inventory Turnover (times)",
            "Accounts Receivable Turnover (times)",
            "Days Inventory Outstanding",
            "Days Sales Outstanding",
        ]
    )
]

x = np.arange(len(efficiency_data))
width = 0.35

bars1 = ax3.bar(
    x - width / 2,
    efficiency_data["2024"],
    width,
    label="2024",
    color=APPLE_DARK_BLUE,
    alpha=0.8,
)
bars2 = ax3.bar(
    x + width / 2,
    efficiency_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)

ax3.set_xlabel("Efficiency Metrics", fontsize=12, fontweight="bold")
ax3.set_ylabel("Value", fontsize=12, fontweight="bold")
ax3.set_title(
    "Apple Inc. - Efficiency Metrics Comparison (2023 vs 2024)",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
ax3.set_xticks(x)
ax3.set_xticklabels(
    [label.replace(" (times)", "") for label in efficiency_data["Ratio Type"]],
    rotation=45,
    ha="right",
)
ax3.legend(loc="upper right", frameon=True, shadow=True)
ax3.grid(axis="y", alpha=0.3, linestyle="--")

add_data_labels(ax3, bars1, "{:.2f}", 0.5)
add_data_labels(ax3, bars2, "{:.2f}", 0.5)

plt.tight_layout()
plt.savefig("efficiency_metrics.png", dpi=fig_dpi, bbox_inches="tight")
plt.close()
print("[OK] Saved: efficiency_metrics.png")


# 4. Gearing/Capital Structure Chart
print("Creating Gearing/Capital Structure Chart...")
fig4, ax4 = plt.subplots(figsize=fig_size, dpi=fig_dpi)

gearing_data = df[
    df["Ratio Type"].isin(
        ["Debt to Equity Ratio", "Debt to Assets Ratio", "Equity Ratio"]
    )
]

x = np.arange(len(gearing_data))
width = 0.35

bars1 = ax4.bar(
    x - width / 2,
    gearing_data["2024"],
    width,
    label="2024",
    color=APPLE_BLUE,
    alpha=0.8,
)
bars2 = ax4.bar(
    x + width / 2,
    gearing_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)

ax4.set_xlabel("Capital Structure Metrics", fontsize=12, fontweight="bold")
ax4.set_ylabel("Ratio Value", fontsize=12, fontweight="bold")
ax4.set_title(
    "Apple Inc. - Gearing & Capital Structure Comparison (2023 vs 2024)",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
ax4.set_xticks(x)
ax4.set_xticklabels(gearing_data["Ratio Type"])
ax4.legend(loc="upper right", frameon=True, shadow=True)
ax4.grid(axis="y", alpha=0.3, linestyle="--")

add_data_labels(ax4, bars1, "{:.3f}", 0.02)
add_data_labels(ax4, bars2, "{:.3f}", 0.02)

plt.tight_layout()
plt.savefig("gearing_ratios.png", dpi=fig_dpi, bbox_inches="tight")
plt.close()
print("[OK] Saved: gearing_ratios.png")


# 5. Comprehensive Dashboard
print("Creating Comprehensive Dashboard...")
fig5 = plt.figure(figsize=(20, 16), dpi=fig_dpi)
fig5.suptitle(
    "Apple Inc. - Comprehensive Financial Analysis Dashboard (2023 vs 2024)",
    fontsize=18,
    fontweight="bold",
    y=0.995,
)

# Create 2x2 grid of subplots
gs = fig5.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# Subplot 1: Profitability
ax5a = fig5.add_subplot(gs[0, 0])
x = np.arange(len(profitability_data))
width = 0.35
bars1 = ax5a.bar(
    x - width / 2,
    profitability_data["2024"],
    width,
    label="2024",
    color=APPLE_BLUE,
    alpha=0.8,
)
bars2 = ax5a.bar(
    x + width / 2,
    profitability_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)
ax5a.set_xlabel("Profitability Metrics", fontsize=10, fontweight="bold")
ax5a.set_ylabel("Percentage (%)", fontsize=10, fontweight="bold")
ax5a.set_title("Profitability Ratios", fontsize=12, fontweight="bold")
ax5a.set_xticks(x)
ax5a.set_xticklabels(
    [label.replace(" (%)", "") for label in profitability_data["Ratio Type"]],
    rotation=45,
    ha="right",
    fontsize=8,
)
ax5a.legend(loc="upper right", fontsize=8)
ax5a.grid(axis="y", alpha=0.3, linestyle="--")

# Subplot 2: Liquidity
ax5b = fig5.add_subplot(gs[0, 1])
x = np.arange(len(liquidity_data))
bars1 = ax5b.bar(
    x - width / 2,
    liquidity_data["2024"],
    width,
    label="2024",
    color=APPLE_LIGHT_BLUE,
    alpha=0.8,
)
bars2 = ax5b.bar(
    x + width / 2,
    liquidity_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)
ax5b.set_xlabel("Liquidity Metrics", fontsize=10, fontweight="bold")
ax5b.set_ylabel("Ratio Value", fontsize=10, fontweight="bold")
ax5b.set_title("Liquidity Ratios", fontsize=12, fontweight="bold")
ax5b.set_xticks(x)
ax5b.set_xticklabels(liquidity_data["Ratio Type"])
ax5b.legend(loc="upper right", fontsize=8)
ax5b.grid(axis="y", alpha=0.3, linestyle="--")
ax5b.axhline(y=1.0, color="red", linestyle="--", alpha=0.5)

# Subplot 3: Efficiency
ax5c = fig5.add_subplot(gs[1, 0])
x = np.arange(len(efficiency_data))
bars1 = ax5c.bar(
    x - width / 2,
    efficiency_data["2024"],
    width,
    label="2024",
    color=APPLE_DARK_BLUE,
    alpha=0.8,
)
bars2 = ax5c.bar(
    x + width / 2,
    efficiency_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)
ax5c.set_xlabel("Efficiency Metrics", fontsize=10, fontweight="bold")
ax5c.set_ylabel("Value", fontsize=10, fontweight="bold")
ax5c.set_title("Efficiency Metrics", fontsize=12, fontweight="bold")
ax5c.set_xticks(x)
ax5c.set_xticklabels(
    [label.replace(" (times)", "") for label in efficiency_data["Ratio Type"]],
    rotation=45,
    ha="right",
    fontsize=8,
)
ax5c.legend(loc="upper right", fontsize=8)
ax5c.grid(axis="y", alpha=0.3, linestyle="--")

# Subplot 4: Gearing
ax5d = fig5.add_subplot(gs[1, 1])
x = np.arange(len(gearing_data))
bars1 = ax5d.bar(
    x - width / 2,
    gearing_data["2024"],
    width,
    label="2024",
    color=APPLE_BLUE,
    alpha=0.8,
)
bars2 = ax5d.bar(
    x + width / 2,
    gearing_data["2023"],
    width,
    label="2023",
    color=APPLE_GRAY,
    alpha=0.8,
)
ax5d.set_xlabel("Capital Structure Metrics", fontsize=10, fontweight="bold")
ax5d.set_ylabel("Ratio Value", fontsize=10, fontweight="bold")
ax5d.set_title("Gearing & Capital Structure", fontsize=12, fontweight="bold")
ax5d.set_xticks(x)
ax5d.set_xticklabels(gearing_data["Ratio Type"])
ax5d.legend(loc="upper right", fontsize=8)
ax5d.grid(axis="y", alpha=0.3, linestyle="--")

plt.savefig("comprehensive_dashboard.png", dpi=fig_dpi, bbox_inches="tight")
plt.close()
print("[OK] Saved: comprehensive_dashboard.png")

print("\n" + "=" * 60)
print("All visualizations created successfully!")
print("=" * 60)
print("Files generated:")
print("  1. profitability_comparison.png")
print("  2. liquidity_ratios.png")
print("  3. efficiency_metrics.png")
print("  4. gearing_ratios.png")
print("  5. comprehensive_dashboard.png")
print("=" * 60)
