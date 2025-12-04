import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Sample DataFrame matching the provided data
data = {
    'a': [2, 4, 8, 5, 7, 6],
    'b': [4, 2, 3, 4, 2, 6],
    'c': [6, 4, 7, 4, 7, 8],
    'd': [8, 2, 6, 4, 8, 6],
    'e': [10, 2, 4, 3, 3, 2],
}

df = pd.DataFrame(data)
# Optional: label the rows 1..n for clarity
df.index = [f"R{i+1}" for i in range(len(df))]

# Create grouped bar plot
ax = df.plot(kind='bar', figsize=(10,6))
ax.set_xlabel('Sample Row')
ax.set_ylabel('Value')
ax.set_title('Grouped Bar Plot of Sample Data')
ax.legend(title='Series')
plt.tight_layout()

# Save plot to workspace
out_path = 'myenv/bar_plot.png'
plt.savefig(out_path, dpi=150)
print(f"Saved plot to {out_path}")
