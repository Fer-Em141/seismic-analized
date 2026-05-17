import pandas as pd
import matplotlib.pyplot as plt

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"


df = pd.read_csv(url)

print(df.head())
print(df[["mag", "depth"]].describe())

plt.figure(figsize=(10,6))
plt.hist(df["mag"].dropna(), bins=30)
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.title("Earthquake Magnitude Distribution")
plt.savefig("../figures/magnitude_distribution.png")
plt.show()

#Agregado

plt.figure(figsize=(10, 6))
plt.scatter(
    df["depth"],
    df["mag"],
    c=df["depth"],
    cmap="viridis",
    alpha=0.5
)

plt.xlabel("Depth (km)")
plt.ylabel("Magnitude")
plt.title("Depth vs Magnitude of Earthquakes")

plt.xlim(0, df["depth"].quantile(0.99))
plt.ylim(df["mag"].quantile(0.01), df["mag"].quantile(0.99))

plt.tight_layout()
plt.savefig("../figures/depth_vs_magnitude.png", dpi=300)
plt.show()
