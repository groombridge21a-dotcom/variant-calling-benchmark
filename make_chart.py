import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
labels = ["Precision", "Recall", "F1"]
a = [96.2, 50.2, 66.0]
b = [99.9, 72.9, 84.3]
x = list(range(3))
w = 0.38
fig, ax = plt.subplots(figsize=(7, 4.5))
r1 = ax.bar([i - w/2 for i in x], a, w, label="~4.6x coverage")
r2 = ax.bar([i + w/2 for i in x], b, w, label="~9x coverage")
ax.bar_label(r1, fmt="%.1f")
ax.bar_label(r2, fmt="%.1f")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(0, 110)
ax.set_ylabel("Percent")
ax.set_title("SNP calling accuracy, simulated chr20 (bcftools)")
ax.legend()
fig.tight_layout()
fig.savefig("figures/coverage_benchmark.png", dpi=200)
