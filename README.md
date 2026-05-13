# Pricing Strategy Analysis 📈

*Data‑driven pricing & revenue optimization pipeline*  

A **complete end‑to‑end analytics solution** that cleans raw retail data, merges multiple sources, computes price elasticity, simulates optimal price changes, analyzes competitors, segments customers, forecasts sales, and persists results to a SQL Server database.

---

## 🔥 Why This Project Stands Out

- **Full‑stack data workflow** (ingestion → transformation → analytics → storage)  
- **Business impact:** Identifies revenue‑lifting price adjustments and forecasts demand trends.  
- **Scalable & reproducible:** Modular Python package (`src/`) with clear separation of concerns.  
- **Ready for production:** SQL Server upload, CSV export, and a CLI‑style `main.py` driver.  

*Ideal for roles in Data Engineering, Pricing Analytics, Business Intelligence, or any data‑science‑focused position.*

---

## 🗂️ Repository Structure

```text
pricing-strategy-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── config.py
├── Pricing_Strategy_Analysis.pbix
│
├── data/
│   │
│   ├── raw/
│   │   ├── retail_price_optimization.csv
│   │   ├── superstore.csv
│   │   └── product_retail_price_survey.csv
│   │
│   └── processed/
│       ├── merged_dataset.csv
│       ├── elasticity_output.csv
│       ├── optimized_output.csv
│       ├── competitor_analysis.csv
│       ├── customer_segments.csv
│       ├── sales_forecast.csv
│       ├── retail_summary.csv
│       └── survey_summary.csv
│
├── notebooks/
│   │
│   ├── 01_Data_Loading_and_Preprocessing.ipynb
│   ├── 02_Data_Merging_and_Feature_Engineering.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Pricing_Elasticity_Analysis.ipynb
│   ├── 05_Revenue_Optimization.ipynb
│   ├── 06_Competitor_Analysis.ipynb
│   ├── 07_Customer_Segmentation.ipynb
│   ├── 08_Sales_Forecasting.ipynb
│   └── 09_PowerBI_Data_Validation.ipynb
│
├── sql/
│   │
│   ├── create_database.sql
│   ├── create_tables.sql
│   ├── views.sql
│   ├── stored_procedures.sql
│   └── analytical_queries.sql
│
├── src/
│   │
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── merge_datasets.py
│   ├── elasticity.py
│   ├── optimization.py
│   ├── competitor_analysis.py
│   ├── customer_segmentation.py
│   ├── forecasting.py
│   ├── database.py
│   └── utils.py
│
├── visuals/
│   │
│   ├── charts/
│   │   ├── revenue_by_category.png
│   │   ├── profit_by_region.png
│   │   ├── discount_vs_revenue.png
│   │   ├── price_vs_units_sold.png
│   │   ├── monthly_revenue_trend.png
│   │   ├── top_10_products.png
│   │   ├── competitor_price_gap.png
│   │   ├── customer_segments.png
│   │   ├── elasticity_analysis.png
│   │   └── forecasting_trend.png
│   │
│   ├── powerbi_dashboard/
│   │   ├── executive_summary.png
│   │   ├── pricing_strategy_dashboard.png
│   │   ├── customer_market_dashboard.png
│   │   └── forecasting_optimization_dashboard.png
│   │
│   └── architecture/
│       ├── project_architecture.png
│       └── data_pipeline_flow.png
│
├── reports/
│   │
│   ├── Pricing_Strategy_Analysis_Report.docx
│   ├── Executive_Summary.pdf
│   └── Project_Presentation.pptx
│
├── dashboard_assets/
│   │
│   ├── icons/
│   ├── themes/
│   │   └── pricing_strategy_theme.json
│   │
│   └── templates/
│       └── dashboard_wireframe.png
│
└── docs/
    │
    ├── business_problem_statement.md
    ├── project_workflow.md
    ├── kpi_definitions.md
    ├── dashboard_documentation.md
    └── deployment_guide.md
```

---

## 📐 Project Architecture & Workflow

### Project Architecture
![Project Architecture](visuals/architecture/Project%20Architecture%20-%20visual%20selection.png)

### Data Pipeline Flow
![Data Pipeline Flow](visuals/architecture/Data%20Pipeline%20Flow%20-%20visual%20selection.png)


---

## 🚀 Quick Start

### Prerequisites

```bash
python >=3.9
pip install -r requirements.txt
```

### Run the Pipeline

```bash
python main.py
```

The script will:

1. Load raw CSVs.  
2. Clean and standardise column names.  
3. Merge datasets into a single DataFrame.  
4. Compute elasticity, optimise pricing, run competitor gap analysis, segment customers, and forecast sales.  
5. Save all intermediate results to `data/processed/`.  
6. Upload the merged dataset to SQL Server (`sales_data` table).

---

## 📊 Core Outputs (saved under `data/processed/`)

| Output File | Description |
|-------------|-------------|
| `merged_dataset.csv` | Unified dataset after cleaning & merging |
| `elasticity_output.csv` | Elasticity scores per product / SKU |
| `optimized_output.csv` | Revenue projection under simulated price changes |
| `competitor_analysis.csv` | Gap analysis vs. key competitors |
| `customer_segments.csv` | K‑means cluster labels for each customer |
| `sales_forecast.csv` *(optional)* | 30‑day sales forecast using linear regression |

---

## 🛠️ Modules Overview  

| Module | Purpose | Key Functions |
|--------|---------|----------------|
| **preprocessing.py** | Clean raw CSVs | `clean_retail_price_data`, `clean_superstore_data`, `clean_price_survey_data` |
| **merge_datasets.py** | Combine all sources | `merge_datasets` |
| **elasticity.py** | Compute price elasticity | `calculate_elasticity` |
| **optimization.py** | Simulate price changes | `simulate_price_change` |
| **competitor_analysis.py** | Identify competitive gaps | `competitor_gap_analysis` |
| **customer_segmentation.py** | K‑means clustering of customers | `customer_segmentation` |
| **forecasting.py** | 30‑day sales forecast | `sales_forecast` |
| **database.py** | Upload DataFrame to SQL Server | `upload_dataframe` |
| **utils.py** | Helper utilities | `save_csv` |

---

## 📈 Business Value

- **Revenue lift:** Simulation shows optimal price increase of *X %* yields *Y %* revenue boost while preserving margin.  
- **Strategic insights:** Elasticity identifies price‑sensitive products, enabling targeted promotions.  
- **Competitive edge:** Gap analysis surfaces under‑priced vs. over‑priced items relative to key rivals.  
- **Customer focus:** Segmentation enables personalized pricing & marketing campaigns.  
- **Future‑ready:** Forecasting prepares inventory and staffing plans based on demand projections.

---

## 📊 Key Analytical Insights

### Revenue & Profitability
<p align="center">
  <img src="visuals/charts/revenue_by_category.png" width="45%" />
  <img src="visuals/charts/profit_by_region.png" width="45%" />
</p>

### Pricing Dynamics
<p align="center">
  <img src="visuals/charts/price_vs_units_sold.png" width="45%" />
  <img src="visuals/charts/discount_vs_revenue.png" width="45%" />
</p>

### Market & Customer Analysis
<p align="center">
  <img src="visuals/charts/competitor_price_gap.png" width="45%" />
  <img src="visuals/charts/customer_segments.png" width="45%" />
</p>

### Trends
![Monthly Revenue Trend](visuals/charts/monthly_revenue_trend.png)

---

## 📂 Data Sources

| Source | Description | Sample Columns |
|--------|-------------|----------------|
| `retail_price_optimization.csv` | Raw retail pricing data | `product_id`, `price`, `sales`, `profit` |
| `superstore.csv` | Transactional data (Latin‑1 encoded) | `order_id`, `order_date`, `customer_id`, `sales` |
| `retail_price_survey.csv` | Survey‑based price perception | `product_id`, `price_sensitivity`, `brand_preference` |

---

## 🧹 Lint & Code Quality

- **PEP‑8 compliant** (flake8).  
- Unused imports removed (`numpy` in `preprocessing.py`).  
- `.gitignore` now excludes **`.ipynb_checkpoints`**, `__pycache__`, and SQL Server DB files.

---

## 📦 Installation (Optional Docker)

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```

Build & run:

```bash
docker build -t pricing-analysis .
docker run --rm pricing-analysis
```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

---

## ✉️ Contact

**Aniket Tayade** – Data Analyst / Pricing Specialist  
📧 [E-Mail] tayadeanni@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/aniket-g-tayade/)

---
