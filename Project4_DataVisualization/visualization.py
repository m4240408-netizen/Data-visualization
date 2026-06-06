from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Resolve paths relative to this script so it works from any working directory
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data.CSV"
chart_dir = base_dir / "charts"

if not csv_path.exists():
	raise FileNotFoundError(f"Data file not found: {csv_path}")

df = pd.read_csv(csv_path)

if df.empty:
	raise ValueError(f"Data file is empty: {csv_path}")

if 'Gender' not in df.columns:
	raise ValueError(f"Expected column 'Gender' not found in data file: {csv_path}")

print(df.head())

# Example Chart 1
plt.figure(figsize=(8,5))
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
chart_dir.mkdir(parents=True, exist_ok=True)
plt.savefig(chart_dir / "gender_distribution.png")
plt.show()