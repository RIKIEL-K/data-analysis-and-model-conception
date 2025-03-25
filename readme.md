# Beans & Pods Inc - Sales Analysis Dashboard

This project is an interactive data analysis dashboard for **Beans & Pods Inc**, built using **Streamlit**. The dashboard provides insights into coffee sales data, including averages, totals, correlations, and distributions of sales by region, channel, and product type.

## Features

### 1. Data Exploration
- Display sample rows from the dataset using a slider to select the number of rows.
- Interactive form to view data samples.

### 2. Sales Averages
- Calculate and display average sales:
  - By **Region** (North, Center, South).
  - By **Channel** (Online, Store).
- Visualize averages using bar charts.

### 3. Total Sales
- Calculate and display total sales:
  - By **Region**.
  - By **Channel**.
- Generate reports with key insights:
  - Highlight regions or channels with the highest and lowest sales.
  - Provide conclusions based on sales data.

### 4. Product Sales Distribution
- Visualize the distribution of sales for individual coffee products (e.g., Robusta, Arabica, Espresso, etc.) using histograms.

### 5. Correlation Analysis (in `pages/directives.py`)
- Analyze correlations between:
  - Coffee types.
  - Sales channels and coffee types.
  - Regions and sales channels.
- Visualize correlations using heatmaps and scatter plots.

### 6. Conclusions and Recommendations (in `pages/conclusions.py`)
- Summarize key findings from the analysis.
- Provide actionable recommendations for marketing and sales strategies.
- Suggest additional data to collect for deeper insights.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the streamlit app:
   ```bash
   streamlit run Analyse.py

This documentation provides a clear overview of your project, its features, and how to use it. Let me know if you'd like to add or modify anything!