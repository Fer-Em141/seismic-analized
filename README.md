---

# **Seismic Analized**

An analytical project focused on exploring global earthquake activity using real-time data from the USGS Earthquake API.
The repository includes Python scripts for data ingestion, cleaning, visualization, and exploratory analysis.

---

## **Features**

* Fetches live earthquake data from the USGS feed (`all_month.csv`).
* Cleans and processes the dataset using **pandas**.
* Generates multiple visualizations using **matplotlib**:
* Magnitude distribution histogram
 - Depth vs. magnitude scatter plot
 - Organized project structure following a lightweight data-science workflow:

```
seismic-analized/
├── data/
├── figures/
├── notebook/
├── reports/
├── src/
├── venv/
└── README.md
```

---

## **How to Run the Project**

### **1. Clone the repository**

```bash
git clone https://github.com/Fer-Em141/seismic-analized.git
cd seismic-analized
```

### **2. Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate   # Linux
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run analysis scripts**

Inside the `src/` folder:

```bash
python3 main.py
```

This will:

* Fetch fresh data
* Print summary statistics
* Generate visualizations inside the **figures/** folder

Generated plots example:

* `figures/magnitude_distribution.png`
* `figures/depth_vs_magnitude.png`

---

## **Data Source**

US Geological Survey (USGS) – Earthquake Hazards Program
[https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv)

---

## Author
**Emilio (Fer-Em141)**  
Python & Data Analysis Enthusiast

---
