# 📊 E-commerce Sales ETL & Dashboard

## Project Overview
This project demonstrates an end-to-end data engineering and analytics pipeline using real-world e-commerce data.

The workflow includes:
- Extracting raw data from CSV
- Transforming and cleaning data using Python (Pandas)
- Loading data into PostgreSQL
- Performing SQL analysis
- Visualizing insights with Tableau

---

## Tech Stack
- Python (Pandas)
- PostgreSQL
- Tableau
- Git & GitHub

---

## ETL Pipeline

### Extract
- Loaded dataset from CSV file
- Used Pandas for data ingestion

###Transform
- Handled missing values
- Removed invalid records (negative quantity, zero price)
- Converted data types (date, numeric)
- Removed duplicates
- Created new feature: Revenue = Quantity × Price

### Load
- Inserted cleaned data into PostgreSQL database
- Optimized data loading using efficient methods

---

## Dashboard Insights

The Tableau dashboard provides:

- Total Revenue
- Revenue by Country
- Revenue Over Time
- Top 5 Products
- Orders by Country

---

## Key Insights

- United Kingdom generates the highest revenue
- A small number of products drive a large portion of sales
- Sales trends vary over time, showing peak periods
- Customer purchasing behavior differs by country

---

## 📁 Project Structure
```
   ecommerce_etl/
   ├── etl/
   │ ├── extract.py
   │ ├── transform.py
   │ ├── load.py
   │ └── init.py
   ├── config.py
   ├── db.py
   ├── main.py
   ├── .env (excluded)
   ├── requirements.txt
   └── data.csv (excluded)
```
---

##  How to Run
1. Clone the repository
```
 git clone https://github.com/your-username/ecommerce-etl-dashboard.git
 cd ecommerce-etl-dashboard
```
3. Create virtual environment
```
 python -m venv venv
 venv\Scripts\activate
```
3. Install dependencies
```
 pip install -r requirements.txt
```
4. Set environment variables Create `.env` file:
```
DB_PASSWORD=your_password
```
6. Run ETL pipeline
```
python main.py
```
 
---
### Dashboard Preview
This dashboard shows key insights from e-commerce sales data, including revenue trends, top products, and country performance.
<img width="1707" height="854" alt="Screenshot 2026-03-26 221816" src="https://github.com/user-attachments/assets/a04b68ce-0f3e-4f53-a73f-852e7a49702c" />

---

## Future Improvements

- Use PostgreSQL COPY for faster data loading
- Add Airflow for pipeline scheduling
- Deploy dashboard to cloud
- Handle larger datasets (scalability)

---


## Author
- Phon Seaklang


